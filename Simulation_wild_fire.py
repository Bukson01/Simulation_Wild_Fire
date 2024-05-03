import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# Initial forest settings:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# Pause length between simulation steps:
PAUSE_LENGTH = 0.5

def main():
    """Main function to run the forest fire simulation."""
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)
        nextForest = {'width': forest['width'], 'height': forest['height']}

        # Run a single simulation step:
        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue

                if forest[(x, y)] == TREE:
                    handleTree(nextForest, x, y)
                elif forest[(x, y)] == FIRE:
                    handleFire(nextForest, x, y)
                else:
                    handleEmptySpace(nextForest, x, y)

        forest = nextForest
        time.sleep(PAUSE_LENGTH)

def createNewForest():
    """Create a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest

def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')

def handleTree(nextForest, x, y):
    """Handle tree behavior during simulation step."""
    if random.random() <= GROW_CHANCE:
        nextForest[(x, y)] = TREE

def handleFire(nextForest, x, y):
    """Handle fire behavior during simulation step."""
    for ix in range(-1, 2):
        for iy in range(-1, 2):
            if forest.get((x + ix, y + iy)) == TREE:
                nextForest[(x + ix, y + iy)] = FIRE
    nextForest[(x, y)] = EMPTY

def handleEmptySpace(nextForest, x, y):
    """Handle empty space behavior during simulation step."""
    if random.random() <= GROW_CHANCE:
        nextForest[(x, y)] = TREE

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

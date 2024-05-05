import random
import sys
import time
from bext import goto, clear, fg

class ForestFireSimulator:
    def __init__(self, width, height, tree_density, grow_chance, fire_chance, pause_length):
        # Initialize the parameters of the simulation.
        self.WIDTH = width
        self.HEIGHT = height
        self.TREE = 'A'  # Representation of a tree in the forest.
        self.FIRE = 'W'  # Representation of a burning tree in the forest.
        self.EMPTY = ' '  # Representation of an empty space in the forest.
        self.INITIAL_TREE_DENSITY = tree_density  # Initial density of trees in the forest.
        self.GROW_CHANCE = grow_chance  # Probability of a tree growing in an empty space.
        self.FIRE_CHANCE = fire_chance  # Probability of a tree catching fire.
        self.PAUSE_LENGTH = pause_length  # Duration between each simulation step.
        # Create the initial forest.
        self.forest = self._create_new_forest()

    def _create_new_forest(self):
        """Create a new forest data structure."""
        # Use a dictionary comprehension to create the forest with initial tree density.
        forest = {(x, y): self.TREE if random.random() <= self.INITIAL_TREE_DENSITY else self.EMPTY
                  for x in range(self.WIDTH) for y in range(self.HEIGHT)}
        return forest

    def _next_forest_state(self):
        """Calculate the next state of the forest."""
        # Calculate the state of each cell in the forest based on the current state.
        next_forest = {}
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if (x, y) in next_forest:
                    continue

                if self.forest[(x, y)] == self.EMPTY and random.random() <= self.GROW_CHANCE:
                    next_forest[(x, y)] = self.TREE
                elif self.forest[(x, y)] == self.TREE and random.random() <= self.FIRE_CHANCE:
                    next_forest[(x, y)] = self.FIRE
                elif self.forest[(x, y)] == self.FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if self.forest.get((x + ix, y + iy)) == self.TREE:
                                next_forest[(x + ix, y + iy)] = self.FIRE
                    next_forest[(x, y)] = self.EMPTY
                else:
                    next_forest[(x, y)] = self.forest[(x, y)]
        return next_forest

    def display_forest(self):
        """Display the forest data structure on the screen."""
        goto(0, 0)
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                if self.forest[(x, y)] == self.TREE:
                    fg('green')  # Set the foreground color to green for trees.
                    print(self.TREE, end='')  # Print the tree character.
                elif self.forest[(x, y)] == self.FIRE:
                    fg('red')  # Set the foreground color to red for burning trees.
                    print(self.FIRE, end='')  # Print the burning tree character.
                elif self.forest[(x, y)] == self.EMPTY:
                    print(self.EMPTY, end='')  # Print the empty space character.
            print()
        fg('reset')  # Reset the foreground color to default.
        print(f'Grow chance: {self.GROW_CHANCE * 100}%  ', end='')
        print(f'Lightning chance: {self.FIRE_CHANCE * 100}%  ', end='')
        print('Press Ctrl-C to quit.')

    def simulate(self):
        """Run the forest fire simulation."""
        clear()  # Clear the terminal screen.
        try:
            while True:  # Main simulation loop.
                self.display_forest()  # Display the current state of the forest.
                self.forest = self._next_forest_state()  # Calculate the next state of the forest.
                time.sleep(self.PAUSE_LENGTH)  # Pause for a specified duration.
        except KeyboardInterrupt:
            sys.exit()  # Exit the program when Ctrl-C is pressed.

if __name__ == '__main__':
    # Initialize and run the simulation.
    simulator = ForestFireSimulator(
        width=79,
        height=22,
        tree_density=0.20,
        grow_chance=0.01,
        fire_chance=0.01,
        pause_length=0.5
    )
    simulator.simulate()

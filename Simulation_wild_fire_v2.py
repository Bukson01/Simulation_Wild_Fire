import random
import sys
import time
from bext import goto, clear, fg

class Tree:
    """Class to represent a tree in the forest."""
    def __init__(self, name, catch_fire_chance):
        self.name = name  # Name of the tree type.
        self.catch_fire_chance = catch_fire_chance  # Probability of the tree catching fire.

class ForestFireSimulator:
    def __init__(self, width, height, tree_types, river_density, lake_density, grow_chance, fire_chance, pause_length):
        # Initialize the parameters of the simulation.
        self.WIDTH = width
        self.HEIGHT = height
        self.tree_types = tree_types  # List of Tree objects representing different tree types.
        self.river_density = river_density  # Density of rivers in the forest.
        self.lake_density = lake_density  # Density of lakes in the forest.
        self.grow_chance = grow_chance  # Probability of a tree growing in an empty space.
        self.fire_chance = fire_chance  # Probability of a tree catching fire.
        self.pause_length = pause_length  # Duration between each simulation step.
        # Create the initial forest.
        self.forest = self._create_new_forest()

    def _create_new_forest(self):
        """Create a new forest data structure."""
        # Use a dictionary comprehension to create the forest with initial tree density.
        forest = {(x, y): None for x in range(self.WIDTH) for y in range(self.HEIGHT)}
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if random.random() <= self.river_density:
                    forest[(x, y)] = 'River'  # Add a river at this location.
                elif random.random() <= self.lake_density:
                    forest[(x, y)] = 'Lake'  # Add a lake at this location.
                elif random.random() <= self.grow_chance:
                    # Randomly select a tree type and add it to the forest.
                    tree_type = random.choice(self.tree_types)
                    forest[(x, y)] = tree_type
        return forest

    def _next_forest_state(self):
        """Calculate the next state of the forest."""
        # Calculate the state of each cell in the forest based on the current state.
        next_forest = {}
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if (x, y) in next_forest:
                    continue

                if self.forest[(x, y)] is None and random.random() <= self.grow_chance:
                    # Randomly select a tree type and grow it in this empty space.
                    tree_type = random.choice(self.tree_types)
                    next_forest[(x, y)] = tree_type
                elif isinstance(self.forest[(x, y)], Tree) and random.random() <= self.fire_chance:
                    # Check neighboring cells and set them on fire if applicable.
                    next_forest[(x, y)] = 'Burning'  # Tree is now burning.
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if self.forest.get((x + ix, y + iy)) == Tree:
                                if random.random() <= self.forest[(x + ix, y + iy)].catch_fire_chance:
                                    next_forest[(x + ix, y + iy)] = 'Burning'  # Neighbor tree catches fire.
                elif self.forest[(x, y)] == 'Burning':
                    # Tree is currently burning. It takes multiple steps to burn down completely.
                    # Reduce the burning intensity with each step.
                    if random.random() <= 0.5:  # Adjust burning intensity here.
                        next_forest[(x, y)] = None  # Tree has burned down completely.
                    else:
                        next_forest[(x, y)] = 'Burning'  # Tree is still burning.
                else:
                    next_forest[(x, y)] = self.forest[(x, y)]  # Copy the existing object.
        return next_forest

    def display_forest(self):
        """Display the forest data structure on the screen."""
        clear()  # Clear the terminal screen.
        goto(0, 0)
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                cell = self.forest[(x, y)]
                if cell is None:
                    print(' ', end='')  # Print an empty space.
                elif cell == 'River':
                    fg('blue')  # Set the foreground color to blue for rivers.
                    print('R', end='')  # Print a river character.
                elif cell == 'Lake':
                    fg('blue')  # Set the foreground color to blue for lakes.
                    print('L', end='')  # Print a lake character.
                elif isinstance(cell, Tree):
                    fg('green')  # Set the foreground color to green for trees.
                    print(cell.name[0], end='')  # Print the first letter of the tree type.
                elif cell == 'Burning':
                    fg('red')  # Set the foreground color to red for burning trees.
                    print('B', end='')  # Print a burning tree character.
            print()
        fg('reset')  # Reset the foreground color to default.
        print(f'Grow chance: {self.grow_chance * 100}%  ', end='')
        print(f'Fire chance: {self.fire_chance * 100}%  ', end='')
        print('Press Ctrl-C to quit.')

    def simulate(self):
        """Run the forest fire simulation."""
        try:
            while True:  # Main simulation loop.
                self.display_forest()  # Display the current state of the forest.
                self.forest = self._next_forest_state()  # Calculate the next state of the forest.
                time.sleep(self.pause_length)  # Pause for a specified duration.
        except KeyboardInterrupt:
            sys.exit()  # Exit the program when Ctrl-C is pressed.

if __name__ == '__main__':
    # Define the parameters for the simulation.
    tree_types = [Tree('Pine', 0.02), Tree('Oak', 0.01)]  # Example tree types with different fire catching chances.
    simulator = ForestFireSimulator(
        width=50,
        height=20,
        tree_types=tree_types,
        river_density=0.05,
        lake_density=0.03,
        grow_chance=0.02,
        fire_chance=0.01,
        pause_length=0.1
    )
    simulator.simulate()

## Forest Fire Simulation 
# Forest Fire Simulation

This forest fire simulation program is an improvement based on the code provided in the "Big Book of Small Python Programming" by Al Sweigart. It simulates the spread of wildfires in a forest environment and incorporates several advanced features to enhance realism and customization.

# Description

The simulation creates a virtual forest environment where trees can catch fire and spread flames to neighboring trees. The program models the growth of trees, the occurrence of lightning strikes, and the spread of fire. The user can observe how the fire spreads over time and monitor the state of the forest.

# Features

- **Randomly Created Lakes and Rivers**: Lakes and rivers are added to the forest as fire breaks, preventing flames from crossing them.
  
- **Chance of Tree Ignition**: Each tree has a percentage chance of catching fire from its neighboring trees, adding randomness to the simulation.

- **Different Types of Trees**: Various types of trees are introduced, each with different chances of catching fire. This feature allows users to customize the forest environment.

- **Multiple States of Burning Trees**: Trees can have different burning states, requiring multiple simulation steps for a tree to burn down completely. This feature adds complexity to the simulation and mimics real-world scenarios.

## Acknowledgement

This program is an enhancement and modification of the forest fire simulation code provided in the "Big Book of Small Python Programming" by Al Sweigart. The original code served as the foundation for implementing advanced features and improving the simulation's realism and flexibility.

# Usage

To run the simulation, simply execute the Python script `forest_fire_simulation.py`. The program will display the forest environment and simulate the spread of fire over time. Press `Ctrl-C` to stop the simulation.

# Dependencies

This program requires the `bext` module for terminal-based graphics. You can install it using pip:

```
pip install Bext
```

# Credits

- Original code: "Big Book of Small Python Programming" by Al Sweigart
- Author: [Your Name]

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
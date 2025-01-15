
# Game of Life by Conway

## Description
The **Game of Life** is a cellular automaton devised by the mathematician John Conway. It is a zero-player game, meaning its evolution is determined by its initial state and does not require further input. Players can create an initial configuration and observe how it evolves over time according to a set of simple rules:

1. Any live cell with two or three live neighbors survives.
2. Any dead cell with exactly three live neighbors becomes a live cell.
3. All other live cells die in the next generation, and all other dead cells stay dead.

This project provides a Python implementation of Conway's Game of Life using the Pygame library for visualization.

---

## How to Run the Project

### Prerequisites
To run this project, you need:

1. Python installed on your system.
2. The following Python libraries installed:
   - numpy
   - pygame

### Running the Game
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python game_of_life.py
   ```

5. Once the game starts, you can:
   - Click with the left mouse button to set initial live cells.
   - Press the `SPACE` key to start or pause the simulation.
   - Close the window to exit the game.

---

## License
This project is released under the [MIT License](LICENSE). 



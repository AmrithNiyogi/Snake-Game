# Snake Game

A classic Snake Game implemented using Python's Turtle graphics library.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a simple Snake Game where the player controls a snake to eat food and grow longer. The game ends when the snake collides with the wall or itself.

## Features

- Custom snake and food designs.
- Real-time score tracking.
- Game over detection when the snake hits the wall or its own tail.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AmrithNiyogi/snake-game.git
    ```

2. Navigate to the project directory:
    ```sh
    cd snake-game
    ```

3. Ensure you have Python installed (preferably version 3.6 or above).

4. Install the required dependencies (if any)

## Usage

To start the game, run the following command:
```sh
python snake_game.py
```

## Controls

- **Up Arrow**: Move up
- **Down Arrow**: Move down
- **Left Arrow**: Move left
- **Right Arrow**: Move right

## Code Structure

- `snake_game.py`: The entry point for the game. Sets up the screen and starts the game loop.
- `snake.py`: Contains the `Snake` class which manages the snake's behavior and movement.
- `food.py`: Contains the `Food` class which manages the food's behavior and positioning.
- `scoreboard.py`: Contains the `Scoreboard` class which manages the score display and game over message.
- `food_design.py`: Contains the `FoodDesign` class which defines the custom shape for the food.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

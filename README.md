# Alien Invasion Game

Welcome to the Alien Invasion Game, a classic arcade-style game built using Python and the Pygame library. In this game, you control a spaceship and your mission is to defend Earth by shooting down waves of invading aliens. This README file will guide you through setting up and playing the game, as well as provide insights into the codebase.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Game Controls](#game-controls)
6. [Code Structure](#code-structure)
7. [Contributing](#contributing)

## Features

- Classic space shooter gameplay
- Multiple levels with increasing difficulty
- High score tracking
- Sound effects and music
- Smooth animations and responsive controls

## Requirements

- Python 3.7 or higher
- Pygame 2.0.0 or higher

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/alien-invasion.git
   cd alien-invasion
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the game, simply run the `alien_invasion.py` script:

```bash
python alien_invasion.py
```

## Game Controls

- **Arrow keys** - Move the spaceship left or right
- **Spacebar** - Fire bullets
- **Q** - Quit the game

## Code Structure

The project is organized into several modules for better maintainability:

- `alien_invasion.py`: The main script to run the game.
- `settings.py`: Contains game settings like screen size, ship speed, etc.
- `game_functions.py`: Tracks game statistics like score and high score.
- `button.py`: Handles button creation and functionality for the game's start screen.
- `ship.py`: Manages the player's spaceship.
- `bullet.py`: Manages the bullets fired by the spaceship.
- `alien.py`: Manages the alien enemies.
- `scoreboard.py`: Handles the display of the score, high score, and level.
- `game_functions.py`: Contains the main game functions such as event handling, updating the screen, and checking for collisions.

## Contributing

We welcome contributions to enhance the game! Here’s how you can contribute:

1. **Fork the repository.**
2. **Create a new branch:** `git checkout -b feature/your-feature-name`
3. **Commit your changes:** `git commit -m 'Add some feature'`
4. **Push to the branch:** `git push origin feature/your-feature-name`
5. **Open a pull request.**

Please make sure to update tests as appropriate.



---

Enjoy defending Earth from the alien invasion! If you have any questions or need further assistance, feel free to open an issue or contact us at [your-email@example.com](mailto:rhythmbhetwal77@gmail.com). Happy gaming!


# The Asteroid Game

A small, minimal remake of the classic Asteroids game written with Pygame.

This repository contains a simple game loop, player ship, asteroids that spawn and split, and basic shooting.

## Requirements

- Python 3.12 or newer
- [uv](https://github.com/astral-sh/uv) (for fast dependency management)
- pygame (installed via uv)

## Installation (Windows / PowerShell)

1. Install [uv](https://github.com/astral-sh/uv) if you don't have it:

   ```powershell
   pip install uv
   ```

2. Create and activate a virtual environment (recommended):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies using uv:

   ```powershell
   uv pip install -r pyproject.toml
   ```

   Or, if you want to install directly from the lock file (if present):

   ```powershell
   uv pip install -r uv.lock
   ```

4. Run the game:

   ```powershell
   python main.py
   ```

## Controls

- A — rotate left
- D — rotate right
- W — thrust (move forward)
- SPACE — shoot
- Close the window to quit

## Gameplay notes

- Asteroids spawn at the edges and move across the screen. When a shot collides with an asteroid it splits into smaller asteroids (until the minimum size).
- If the player collides with an asteroid the game prints "Game over!" and exits.

## Project structure

- `main.py` — game loop, groups, and wiring of sprite containers
- `player.py` — player ship implementation and input handling
- `asteroid.py` — asteroid behavior and splitting
- `asteroidfield.py` — asteroid spawn logic
- `shot.py` — projectile implementation
- `circleshape.py` — base sprite class for circular objects
- `constants.py` — numeric constants for screen size, speeds, radii, etc.

## Development

This is a small project intended for learning. Feel free to open issues or submit PRs to add features like scoring, sound effects, improved collision handling, or a UI.


# Health-Flask mini game

## Overview
A turn-based Flask game where, at the end of each turn, a random event happens to the player (e.g., losing health, money, flasks, or getting poisoned). During their turn, the player must choose an action (e.g., do nothing, drink a flask to regain health, use antidote, etc.). There is also a shop with limited inventory. The goal is to survive as many turns as possible.

## Status
This is a rough early version of a Flask game I built to practice Python and game design. As of 13-05-2025, it's fully functional but still messy due to being dropped mid-modularisation. The structure is expected to improve over time. Updates may have occurred since this date.

## Purpose
This was my first attempt at making a game, motivated by my goal of working in the gaming industry. I wanted hands-on experience with core backend processes like user input handling and testing, while also exploring gameplay mechanics such as balancing difficulty and tracking high scores. A key goal was also to improve my object-oriented programming (OOP) skills, which are essential in game development.

## Features
- Shop and Player classes define player actions and attributes
- Customisable starting stats (within a total limit)
- High scores are saved to a top 20 leaderboard and printed at game over
- `while` loops keep the player inside appropriate sections (game, shop)

## Future Plans
- Add integration tests
- Implement a main menu and allow users to save/load progress (player stats + turns survived)
- Add a narrative (e.g., the player is a sellsword preparing for battle each turn, with death screens, etc.)
- Introduce weapon and armor upgrades to turn it into a progression-style game
- Add more actions, items, and layers to enhance depth

## What I Learned
- How to use `while` loops to control game state (e.g., `while hp > 0:` to keep the game running)
- How to structure OOP code for game mechanics
- Use of functions like `getattr()` and `setattr()` for dynamic object attribute access

## How to Run

```bash
python3 main.py

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2023-08-18

### Added

- Introduced the `Tile` class to represent individual tiles with letters and values.
- Introduced the `BagTiles` class that simulates a bag of tiles for a word game.
- Added methods in `BagTiles` to extract and replace tiles in the bag.
- Added the tests for the `Tile` and `BagTiles` classes.
- Utilized the `unittest` library to ensure the correct functioning of the methods.
- Introduced the `Cell` class to represent individual cells on the game board.
- Added methods to the `Cell` class for adding letters, calculating letter and word values, and handling multipliers.
- Introduced the `Board` class to represent the game board and its grid of cells.
- Added tests for the `Cell` and `Board` classes in separate test files (`test_cell.py` and `test_board.py`).
- Introduced the `Player` class to represent players in the game.
- Created the `ScrabbleGame` class to manage the Scrabble game itself.
- Added the `player.py`, `scrabble.py`, `test_player.py`, and `test_scrabble.py` files to the project.
- Added to the Player Class the draw_tiles method, which allows a player to take new tiles from the bag and which takes as arguments the bag of tiles and the number of tiles to take.
- Added to the Player Class the exchange_tiles method, which allows a player to exchange tiles with the bag and which receives the bag of tiles and a list of tiles that the player wants to exchange as arguments.
- Added to the Player Class the calculate_score method, which calculates the player's score based on the cells in which letters have been placed and their values ​​multiplied by the board multipliers.
- Added the `place_tile` method to the `Board` class, which allows placing a tile on a specific cell if it's empty.
- Added the `validate_word` method to the `Board` class, which checks if a given word can be placed in a specific starting cell and direction without violating any rules.
- Added tests for the `Board` class in the `test_board.py` file.



### Changed

- Improved the `BagTiles` constructor by using a more organized structure for tile initialization.
- Refactored the `take` method in `BagTiles` to calculate the number of tiles taken more accurately.
- Enhanced the `put` method in `BagTiles` to directly extend the list of tiles.
- Improved the `BagTiles` constructor by using a more organized structure for tile initialization.
- Refactored the `take` method in `BagTiles` to calculate the number of tiles taken more accurately.
- Enhanced the `put` method in `BagTiles` to directly extend the list of tiles.


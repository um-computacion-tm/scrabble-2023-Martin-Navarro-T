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

### Changed

- Improved the `BagTiles` constructor by using a more organized structure for tile initialization.
- Refactored the `take` method in `BagTiles` to calculate the number of tiles taken more accurately.
- Enhanced the `put` method in `BagTiles` to directly extend the list of tiles.


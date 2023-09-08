# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] First Sprint (First 6/6 commits) - 2023-08-18 a 2023-08-29
## [0.0.2] Second Sprint (7/12 commits) - 2023-08-30 y 2023-09-06

"I have decided to divide the information that I am adding in different files to improve readability, organization and easier access to the data."

### Added

### main.py
# main.py
- Added the main entry point for the Scrabble game.
- Implemented a user-friendly interface for starting and playing the game.
- Prompts the user to input the number of players (2 to 4 players supported).
- Allows players to take turns entering words, positions, and orientations for placing tiles on the game board.
- Validates the input word, position, and orientation to determine if the move is valid.
- Cycles through player turns until the game is over.

Example usage:
1. Run `main.py` to start the Scrabble game.
2. Enter the number of players (2 to 4 players supported).
3. Players take turns inputting words, positions, and orientations to place tiles on the board.
4. The game validates each move and provides feedback on its validity.

This provides an interactive way for players to play the Scrabble game.

#### models.py
- Added the `Tile` class to represent individual tiles with letters and values.
- Added the `BagTiles` class to simulate a bag of tiles for a word game.
- Included the constructor for `BagTiles` to initialize the bag of tiles with the letter values.
- Added the `take` method to the `BagTiles` class, allowing the extraction of a specified number of tiles from the bag.
- Added the `put` method to the `BagTiles` class, which allows adding a list of tiles back to the bag.

#### board.py
- Added the `place_tile` method to the `Board` class, which allows placing a tile on a specific cell if it's empty.
- Added the `validate_word` method to the `Board` class, which checks if a given word can be placed in a specific starting cell and direction without violating any rules.

#### cell.py
- Added the `Cell` class to represent individual cells on the game board.
- Added the `add_letter` method to the `Cell` class, allowing the addition of letters to a cell.
- Added the `remove_letter` method to the `Cell` class, enabling the removal of letters from a cell.
- Added the `calculate_value` method to the `Cell` class for calculating the value of the cell, considering its letter, multiplier, and type.
-Added the `Calculate_value` class to handle the calculation of word values based on the cells on the game board.
-Added the `calculate_value` method to the `Cell` class for calculating the value of the cell, considering its letter, multiplier, and type.

#### player.py
- Added the `Player` class to represent players in the game.
- Added the `draw_tiles` method to the `Player` class, allowing a player to take new tiles from the bag and which takes as arguments the bag of tiles and the number of tiles to take.
- Added the `exchange_tiles` method to the `Player` class, which allows a player to exchange tiles with the bag and which receives the bag of tiles and a list of tiles that the player wants to exchange as arguments.
- Added the `view_tiles` method to the `Player` class, which returns a list of the tiles held by the player.
- Added the `view_score` method to the `Player` class, which returns the current score of the player.
- Added the `start_turn` method to the `Player` class to indicate the start of a player's turn.
- Added the `end_turn` method to the `Player` class to indicate the end of a player's turn.
- Added the `bag_tiles` parameter to the `__init__` method of the `Player` class, allowing the player to be associated with a bag of tiles for tile drawing and exchange. This parameter was not present in the previous implementation.

#### scrabble.py
- Added the `ScrabbleGame` class to manage the Scrabble game itself.
- Added the `playing` method to the `ScrabbleGame` class to indicate whether the game is currently being played.
- Added the `next_turn` method to the `ScrabbleGame` class, which handles the transition to the next player's turn and increments the current turn count.

#### test_models.py
- Added test cases for the `Tile` and `BagTiles` classes in the `TestTiles` and `TestBagTiles` test suites.
- Included test cases for the `test_tile`, `test_bag_tiles`, `test_take`, and `test_put` methods in the respective test suites.
- Used the `unittest.mock.patch` decorator to mock the `random.shuffle` function in the `test_bag_tiles` method of the `TestBagTiles` test suite.

#### test_board.py
- Added test cases for the `Board` class in the `TestBoard` test suite.
- Included test cases for the `test_init`, `test_place_tile`, and `test_validate_word` methods in the `TestBoard` test suite.

#### test_cell.py 
- Added test cases for the `Cell` class in the `TestCell` test suite.
- Included test cases for the `test_init`, `test_add_letter`, `test_cell_value`, `test_cell_multiplier_word`, `test_remove_letter`, and `test_inactive_cell` methods in the `TestCell` test suite.

#### test_player.py
- Added test cases for the `Player` class in the `TestPlayer` test suite.
- Included test cases for the `test_init`, `test_draw_tiles`, `test_exchange_tiles`, `test_view_tiles`, `test_view_score`, `test_start_end_turn`, and `calculate_score` methods in the `TestPlayer` test suite.
- Added a `MockBoard` class and a `MockCell` class to simulate game board and cell behavior in the tests.

#### test_scrabble.py
- Added test cases for the `ScrabbleGame` class in the `TestScrabbleGame` test suite.
- Included test cases for the `test_init`, `test_playing`, `test_next_turn`, `test_next_turn_when_game_is_starting`, `test_next_turn_when_player_is_not_the_first`, and `test_next_turn_when_player_is_last` methods in the `TestScrabbleGame` test suite.

### test_calculate_word_value.pu
- Added a test suite for calculating word values in the Scrabble game.
- Implemented test cases to validate the calculation of word values with various scenarios.
- Created tests for calculating word values with letter multipliers, word multipliers, and combinations of both.
- Added tests to handle cases with inactive cells and active cells.
- Ensured that the `Calculate_value` class is correctly imported and used in the test cases.
These test cases provide comprehensive coverage for calculating word values in the Scrabble game, ensuring accurate scoring and handling various gameplay scenarios.


### Changed
- Improved the `BagTiles` constructor by using a more organized structure for tile initialization.
- Refactored the `take` method in `BagTiles` to calculate the number of tiles taken more accurately.
- Enhanced the `put` method in `BagTiles` to directly extend the list of tiles.
- Improved the `BagTiles` constructor by using a more organized structure for tile initialization.
- Refactored the `take` method in `BagTiles` to calculate the number of tiles taken more accurately.
- Enhanced the `put` method in `BagTiles` to directly extend the list of tiles.
- In Scrabble.py, optimized player list initialization. The named Player class is now instantiated and added to the player list.
- In Scrabble.py, the logic for switching to the next turn was improved. Now ensures that turns flow correctly between players.





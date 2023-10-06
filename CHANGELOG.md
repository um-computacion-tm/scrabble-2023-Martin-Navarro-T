# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [0.0.23] - "Commit 23" - 2023/10/06

### Removed
- Removed the previous implementation of the `validate_word` method in `player.py`.
- Removed the tests for `validate_word`:
  - `test_validate_word_valid`
  - `test_validate_word_invalid`

### Fixed
- Fixed a bug that caused the number of tiles in the player's hand after the exchange to not match the expected number, resulting in the `test_exchange_tiles` test in `test_player.py` failing.

### Added
- `BagTiles` Class in `bagtiles.py`:
  - Added an `initial_tiles` method to ensure the tile bag contains the required initial tiles, aligning with game rules Simplified tile initialization within the constructor, improving code readability.
- New Test Cases in `test_player.py`:
  - `test_validate_rack_true`: Validates the `has_letters` method for confirming tile availability in the player's rack, returning `True` for valid words. 
  - `test_validate_rack_false`: Ensures the `has_letters` method correctly returns `False` for words with missing tiles. 
- New Test Case in `test_bagtiles.py`:
  - `test_initial_tiles`: Tests the functionality of the newly added `initial_tiles` method in the `BagTiles` class. #Added
  - `test_put_more_than_7_tiles`: Check the behavior of the put function when trying to put more than 7 tiles at a time, which should raise the ImpossibleToChangeMoreThan7 exception.
  - `test_put_bag_full`: Check the behavior of the put function when trying to put a token into a full bag, which should raise the BagFull exception.

### Changed
- Modified the `take` and `put` methods in `BagTiles` class.
- Updated the `take` method to handle cases where there are not enough tiles available in the bag.
- Updated the `put` method to check if adding tiles would exceed the maximum limit of 100 tiles in the bag.
- Updated the `exchange_tiles` method in the `Player` class in `player.py`.
- Refactored the `validate_word` method in the `Player` class in `player.py` to `has_letters`.
  - The `validate_word` method, which checked if a word can be formed using the player's rack, has been replaced with a more general method, `has_letters`.
  - The new method checks if a set of tiles can be formed using the player's rack letters, making the logic more versatile and reusable.
- Modified the `test_exchange_tiles` method in the `TestPlayer` class in `test_player.py`.
- Modified the `test_bag_tiles` method in the `TestBagTiles` class in `test_bagtiles.py`.
- Updated the test case in `test_bagtiles.py` to accommodate changes in the `BagTiles` class, including the addition of the `initial_tiles` method. 

## [0.0.22] - "Commit 22" - 2023/10/05

### Added
- New methods have been added to the `ScrabbleGame` class in `scrabble.py`:
  - `validate_word`: Validates whether a given word can be placed on the board at a specific location and orientation. It checks the word's validity against a dictionary and board placement rules.
  - `game_over`: Determines if the game has ended. Returns `True` when the tile bag is empty, indicating no more tiles are available for play.
- New tests have been added for the methods of the `ScrabbleGame` class in `test_scrabble_game.py`:
  - `test_validate_word`: Verifies that the `validate_word` method correctly validates a valid word for board placement.
  - `test_validate_word_false`: Ensures that the `validate_word` method returns `False` when attempting to validate an invalid word.
  - `test_game_over_true`: Confirms that the `game_over` method returns `True` when the tile bag is empty, indicating the end of the game.
  - `test_game_over_false`: Verifies that the `game_over` method returns `False` when there are still tiles available in the tile bag.

## [0.0.21] - "Commit 21" - 2023/10/03

### Changed
- The `__init__` method of the `BagTiles` class in `bagtiles.py` has been modified.
  - The constructor now generates the tiles based on the specified quantity and stores them in `self.tiles`. The order of the tiles has also been changed to match the game rules
- The `test_bag_tiles` test has been modified to reflect the changes in the constructor and verify its correct operation.

### Removed
- The `initial_tiles` method has been removed, as the constructor (`__init__`) now handles tile generation.
- Removed test `test_initial_tiles` which is no longer relevant due to changes in initialization.

## [0.0.20] - "Commit 20" - 2023/10/02

### Removed
- Import of `unicodedata` has been removed as it is no longer used in the code.
- Removed the `remove_accents` method from the `Dictionary` class.

### Changed
- The `Dictionary` class has been updated to improve code efficiency and simplicity.
- Class initialization now loads all dictionary words into `self.dictionary` instead of opening the file every time `Dictionary` is instantiated.
- Changed the `__init__` constructor of the `Dictionary` class to load all the dictionary words into a `self.dictionary` variable.
- Changed the `verify_word` method of the `Dictionary` class to check if a word exists in `self.dictionary`.

### Added
- New methods have been added to the `Player` class in `player.py`:
  - `set_tiles(self, tiles)`: Sets the player's tiles with a given tile list.
  - `get_tiles(self)`: Returns the player's current tiles.
- New tests have been added for the methods of the `Player` class in `test_player.py`:
  - `test_set_tiles(self)`: Test that verifies that the `set_tiles` method sets the letters correctly.
  - `test_get_tiles(self)`: Test that verifies that the `get_tiles` method returns the letters correctly.

## [0.0.19] - "Commit 19" - 2023/09/29

### Changed
- Replaced old dictionary loading logic with new one in `dictionary.py`.
- Improved handling of Unicode characters in the `remove_accents` method.
- The `Dictionary` class has been changed with new methods
- The `TestDictionary` class has been updated with the new tests.

### Removed
- The following methods have been removed from the `Dictionary` class in `dictionary.py`:
  - `__init__(self, file_path=None)`: The constructor that initialized the `Dictionary` instance.
  - `load_dictionary(self)`: The method that loaded the dictionary from a file.
  - `is_valid_word(self, word)`: The method that checked if a word was valid in the dictionary.
- The following tests in `TestDictionary` have been removed:
  - `test_is_valid_word_valid`
  - `test_is_valid_word_invalid`
  - `test_load_dictionary_file_not_found`

### Added
- Added `verify_word` method to verify words in the dictionary.
- Added `remove_accents` method for accent removal.
- Added the ability to load a dictionary from a file in `dictionary.py`.
- New tests have been added in `TestDictionary`:
  - `test_remove_accents`: Verifies that the `remove_accents` function correctly removes accents from a word.
  - `test_simple_verify`: Checks that the `verify_word` function returns `True` for an existing word in the dictionary.
  - `test_verify_false_word`: Checks that the `verify_word` function returns `False` for a word that does not exist in the dictionary.
  - `test_verify_word_with_accents`: Verify that the `verify_word` function handles words with accents correctly.
  - `test_verify_word_with_umlaut`: Verifies that the `verify_word` function handles words with umlauts correctly.

## [0.0.18] - "Dieciochoavo Commit" - 2023/09/25

### Added
- Added the `clear_cell` function to the `Board` class in `board.py`, which allows clearing a cell at a specific location by removing any tile or content present in that cell. The cell will be empty after calling this function.
- Added tests in `test_board.py` to validate the new `clear_cell` function:
   - `test_clear_cell_valid`: Verifies that the `clear_cell` function works correctly when clearing a cell containing a tile. After clearing, the cell should be empty.
   - `test_clear_cell_invalid`: Checks that the `clear_cell` function returns `False` when attempting to clear a cell outside the board's boundaries. The cell outside the boundaries should not be modified.

## [0.0.17] - "Diecisieteavo Commit" - 2023/09/22

### Added
- Added `pass_turn` method to allow the player to pass their turn. This method ends the player's current turn.
- Added `check_tile_in_hand(tile)` method to check if a specific tile is present in the player's hand. It verifies if the tile exists in the player's current set of tiles.
- Added `get_hand_size` method to retrieve the current size of the player's hand, i.e., the number of tiles the player holds.
- Added `get_score` method to calculate the player's score based on played tiles on the board. It calculates the score by summing the values of the played tiles, considering any multipliers.
- Added `validate_word(word)` method to validate if a given word can be formed with the tiles in the player's hand. It checks if all the letters required for the word are present in the player's hand.
- Added `MockCell` class to simulate game cells for testing purposes:
   - `__init__(self, value)`: Initializes a MockCell instance with a specified value.
   - `calculate_value(self)`: Simulates calculating the value of the cell, returning the specified value.
- Added tests for the new methods:
   - `test_pass_turn`: Verifies that the player can pass their turn successfully.
   - `test_check_tile_in_hand`: Tests if the method correctly identifies tiles present in the player's hand.
   - `test_get_hand_size`: Ensures that the method returns the correct number of tiles in the player's hand.
   - `test_get_score_no_played_cells`: Tests the calculation of the player's score when no cells have been played on the board.
   - `test_get_score_with_played_cells`: Tests the calculation of the player's score when cells with values have been played on the board.
   - `test_validate_word_valid`: Checks if the validate_word method correctly validates a valid word.
   - `test_validate_word_invalid`: Tests the validate_word method to confirm it correctly identifies an invalid word.

### Note
- There are two definitions of MockCell in the codebase. The first definition is within the MockBoard class, used to simulate the game board's cells. The second definition is outside the MockBoard class and is used in test cases to simulate cells played on the board for scoring calculations. The reason for having two MockCell definitions is to separate their roles: one for simulating the board and the other for simulating played cells.

## [0.0.16] - "Dieciseisavo Commit" - 2023/09/21

### Added
- Added the `validate_word_horizontal` method in `board.py` to validate words in horizontal orientation.
- Added `validate_word_vertical` method in `board.py` to validate words in vertical orientation.
- Added `is_empty` method in `board.py`to check if the board is empty.
- Added the `word_in_the_center` method in `board.py` to determine whether a word is placed in the center of the board.
- Added the `validate_word_place_board` method in `board.py` to validate if a word can be placed on the board.
- Added the following tests to validate the new methods:
   - `test_board_is_empty`: Check if the board is empty.
   - `test_board_is_not_empty`: Check if the board is not empty.
   - `test_place_word_empty_board_horizontal_fine`: Tests whether a word is correctly placed on an empty board in horizontal orientation.
   - `test_place_word_empty_board_vertical_fine`: Tests whether a word is correctly placed on an empty board in vertical orientation.
   - `test_place_word_empty_board_horizontal_wrong`: Checks that a word is not placed on an empty board in horizontal orientation.
   - `test_place_word_empty_board_vertical_wrong`: Checks that a word is not placed on an empty board in vertical orientation.
   - `test_place_word_no_empty_board_horizontal_fine`: Tests whether a word is correctly placed on a non-empty board in horizontal orientation.
   - `test_place_word_no_empty_board_vertical_fine`: Tests whether a word is correctly placed on a non-empty board in vertical orientation.
   - `test_place_word_no_empty_board_horizontal_wrong`: Checks that a word is not placed on a non-empty board in horizontal orientation.
   - `test_place_word_no_empty_board_vertical_wrong`: Checks that a word is not placed on a non-empty board in vertical orientation.

## [0.0.15] - "Quinceavo Commit" - 2023/09/20   

### Added
- Added the `validate_word_inside_board` method to the `Board` class in `board.py`, which allows checking if a word can fit completely inside the board at a specific location and orientation.
- Added the `validate_word_out_of_board` method to the `Board` class in `board.py`, which allows checking if a word would extend beyond the boundaries of the board from a given location and orientation.
- Added the following tests in `test_board.py`:
   - `test_word_inside_board`: Checks if the words fit inside the board.
   - `test_word_out_of_board`: Tests if words extend outside the board.
   - `test_word_inside_board_vertical`: Confirms that vertical words fit inside the board.

## [0.0.14] - "Catorceavo Commit" - 2023/09/14

### Added
- Added the ability to import classes from the `game` module in `main.py` to improve code organization.
- Implemented unit tests in main.py for the `valid_player_count` and `get_player_count` functions of the `Main` class in the `test_main.py` file.
- Integration tests were implemented in main.py to verify the interaction between the `Main` class and `ScrabbleGame` in the `test_main_integration.py` file.
- In `main.py` the `Main` class was implemented to handle the initial configuration and interaction with the game.
- Added the ability to import classes from the `game.scrabble` module in `main.py`.
- Added unit tests for the player configuration and validation functions of the `Main` class in the `test_main.py` file:
   - The `setUp` and `tearDown` methods were implemented to configure and reset the test environment respectively.
   - `test_valid_player_count`: Test the validation of the number of players.
   - `test_valid_player_count_error`: Test validation of the number of players when an invalid value is entered.
   - `test_player_count_input_valid`: Test the main game flow with a valid number of players.
   - `test_player_count_input_invalid_then_valid`: Test the game flow with an invalid number of players followed by a valid number of players.

## [0.0.13] - "Treceavo Commit" - 2023/09/13

### Fixed
- Refactoring of the code in the `main.py` file to follow CodeClimate recommendations.
- In `board.py`, the `validate_word` method was refactored to improve its structure and follow CodeClimate recommendations.
- Refactoring of the code in the `Calculate_value` class in `cell.py` following CodeClimate recommendations.
- Refactored the `calculate_word_value` method to improve readability and maintain code consistency.

### Added
- Added `calculate_cell_value` method in `Calculate_value` class to separate calculation logic from cells.
- Added `calculate_word_multiplier` method in `Calculate_value` class to calculate word multipliers.
- Added additional tests in `test_calculate_word_value.py` to validate the new methods and ensure they work correctly.
  - `test_calculate_word_multiplier_with_word_multiplier`: Check for correct calculation of word multipliers.
  - `test_calculate_word_multiplier_without_word_multiplier`: Check that word multipliers are not applied when not necessary.
  - `test_calculate_word_value`: Verifies that the word value calculation is accurate.
  - `test_calculate_cell_value_with_letter_multiplier`: Check for correct cell value calculation with letter multipliers.
  - `test_calculate_cell_value_without_multiplier`: Check cell value calculation without multipliers.
  - `test_calculate_cell_value_empty_cell`: Check the calculation of the value of an empty cell.

## [0.0.12] - "Doceavo Commit" - 2013/09/11

### Added
- Creation of the `dictionary.py` file to host the `Dictionary` class.
- Introduction of the `Dictionary` class in the `dictionary.py` file, designed to manage a word dictionary.
- In the `Dictionary` class, added a constructor that takes a dictionary file as a parameter (by default, "dictionary.txt").
- Inclusion of 'load_dictionary' method to load words from the dictionary file into a set (self.words).
- Implementation of the 'is_valid_word' method to check if a word is valid based on the content of the loaded dictionary.
- Created test file `test_dictionary.py` to test the functionality of the `Dictionary` class.
- Inclusion of test cases for each method of the `Dictionary` class in `test_dictionary.py`, including `load_dictionary` and `is_valid_word`.
- Verification that `load_dictionary` correctly loads the dictionary from the specified file.
- Check that `is_valid_word` returns `True` for valid words and `False` for invalid words based on the loaded dictionary.
- Handling of the `FileNotFoundError` exception to ensure proper behavior if the dictionary file is not found.

## [0.0.11] - "Onceavo Commit" - 2013/09/10

### Added
- Introducing the `joker` method within the `Tile` class. This method allows for the modification of a tile's letter when it is a wildcard ('*').
- Added the `NotAJoker` exception to the `Tile` class, which handles cases where the `joker` method is used on a non-wildcard tile.
- Introduced custom exceptions in the `BagTiles` class to handle specific scenarios:
  - `NoTilesAvailable`: Raised when attempting to take tiles from an empty bag.
  - `ImpossibleToChangeMoreThan7`: Raised when trying to put more than 7 tiles into the bag at once.
  - `BagFull`: Raised when attempting to put tiles into a bag that is already full (100 tiles).
- Expanded the test coverage within the `TestTile` suite to examine the behavior of the `joker` method.
  - `test_joker_with_valid_letter`: Ensures that the `joker` method correctly changes the letter of a wildcard tile to a valid letter ('A').
  - `test_joker_with_invalid_letter`: Verifies that attempting to use the `joker` method on a non-wildcard tile ('B') raises the `NotAJoker` exception.

### Changes
- Modified the `take` method in the `BagTiles` class to raise the `NoTilesAvailable` exception when attempting to take tiles from an empty bag.
- Adjusted the `put` method in the `BagTiles` class to raise the `ImpossibleToChangeMoreThan7` exception when trying to add more than 7 tiles at once and to raise the `BagFull` exception when attempting to put tiles into a bag that's already full (100 tiles).
- Updated the `test_take` method within the `TestBagTiles` test suite to include coverage for the `NoTilesAvailable` exception when taking tiles from an empty bag.
- Modified the `test_put` method within the `TestBagTiles` test suite to encompass the `ImpossibleToChangeMoreThan7` exception when attempting to add more than 7 tiles at once and the `BagFull` exception when trying to add tiles to a bag that's already full (100 tiles).

## [0.0.10] - "Decimo Commit" - 2013/09/09

### Changes
- I separated the functionality of the `models.py` file into two separate files, `tiles.py` and `board.py`, for better code organization.
- Split the `test_models.py` test cases into two separate files, `test_tiles.py` and `test_bagtiles.py`, to keep the tests clean and focused.
- All class methods were divided according to their class in the corresponding file.

### Added
- Introduced a `get_value_by_letter` method in the `Tile` class within `tiles.py`, which makes it easy to retrieve tile values ​​based on their letters.
- Implemented the `initial_tiles` method in the `Bagtiles` class inside `bagtiles.py`, which is responsible for setting the initial tile quantities according to the game rules.
- Created a set of test cases for the `Tile` class within the `TestTiles` test suite, ensuring accurate tile creation and attribute values.
- Expanded the `TestTiles` suite to include test cases for the `get_value_by_letter` method, validating proper letter-based value retrieval.
- Established the `TestBagTiles` test suite to host test cases for the `BagTiles` class.
- Added test cases within the `TestBagTiles` suite, covering methods like `test_bag_tiles`, `test_take`, and `test_put`.
- Used the `unittest.mock.patch` decorator to mock the `random.shuffle` function in the `test_bag_tiles` method of the `TestBagTiles` test suite.
- I included test cases for the `initial_tiles` method to ensure correct setting of initial tile quantities according to the game rules.

## [0.0.9] - "Noveno Commit" - 2013/09/08

### Added
- Added the `add_player_starting_position` method to the `Cell` class, This function allows you to assign the cell a starting position for a player in the game.
- Added tge `is_empty` method to the `Cell` class, This function checks if the cell is empty, that is, it does not contain any letters.
- Added the `has_letter` method to the `Cell` class, Allows you to check if the cell contains a specific letter.
- Added the `apply_word_multiplier` method to the `Cell` class, This function applies a word multiplier to the cell if its multiplier type is 'word'.
- Added the `apply_letter_multiplier` method to the `Cell` class, Applies a letter multiplier to the cell if its multiplier type is 'letter'.
- Included test cases for the `add_player_starting_position`, `is_empty`, `has_letter`, `apply_word_multiplier`, `apply_letter_multiplier`

## [0.0.8] - "Octavo Commit" - 2013/09/07

### Added
- Introduced the `Calculate_value` class, designed to manage the calculation of word values based on the cells on the game board.
- Implemented the `calculate_value` method within the `Cell` class, enabling the calculation of a cell's value by considering its letter, multiplier, and type attributes.
- Created the test suite `TestCalculateWordValue` to evaluate the calculation of word values within the `Scrabble game.
- Added a test case `test_simple` to validate the calculation of word values with simple letter values.
- Added a test case `test_with_letter_multiplier` to assess word value calculations considering letter multipliers.
- Added a test case `test_with_word_multiplier` to evaluate word value calculations incorporating word multipliers.
- Included a test case `test_with_letter_word_multiplier` to verify word value calculations with both letter and word multipliers.
- Added a test case `test_with_letter_word_multiplier_no_active` to ensure accurate handling of calculations when cells are inactive.
- Included a test case `test_with_letter_word_multiplier_active` to assess word value calculations with active cells.
These test cases offer extensive coverage for the calculation of word values in the Scrabble game, guaranteeing precise scoring and the handling of diverse gameplay situations.

- Created `main.py` as the main entry point for the Scrabble game.
- Added easy to use interface to start and play the game.
- Included a prompt to enter the number of players (supports 2 to 4 players).
- Enabled the ability for players to take turns entering words, positions, and orientations to place tiles on the game board.
- Implemented a validation of the entered word, position and orientation to determine if the movement is valid.
- Added a loop to alternate between players' turns until the game ends.
### Usage example main.py
1. Run `main.py` to start the Scrabble game.
2. Enter the number of players (supports 2 to 4 players).
3. Players take turns entering words, positions, and orientations to place tiles on the board.
4. The game validates each move and provides feedback on its validity.

## [0.0.7] - "Septimo Commit" - 2023/09/06

### Added 
- Added the `add_letter` method to the `Cell` class, allowing the addition of letters to a cell.
- Added the `remove_letter` method to the `Cell` class, enabling the removal of letters from a cell.
- Added the `calculate_value` method to the `Cell` class for calculating the value of the cell, considering its letter, multiplier, and type.
- Added test cases for the `Cell` class in the `TestCell` test suite.
- Included test cases for the`test_add_letter`, `test_cell_value`, `test_cell_multiplier_word`, `test_remove_letter`, and `test_inactive_cell` methods in the `TestCell` test suite.
- Added the `ScrabbleGame` class to manage the Scrabble game itself.
- Added the `playing` method to the `ScrabbleGame` class to indicate whether the game is currently being played.
- Added the `next_turn` method to the `ScrabbleGame` class, which handles the transition to the next player's turn and increments the current turn count.
- Added test cases for the `ScrabbleGame` class in the `TestScrabbleGame` test suite.
- Included test cases for the `test_playing`, `test_next_turn`, `test_next_turn_when_game_is_starting`, `test_next_turn_when_player_is_not_the_first`, and `test_next_turn_when_player_is_last` methods in the `TestScrabbleGame` test suite.
 
## [0.0.6] - "Sexto Commit" - 2023/08/29

### Added
- Added the `calculate_score` method to the `Player` class, allowing the calculation of a player's score based on placed letters and multipliers on the board.
- Added the `view_tiles` method to the `Player` class, which returns a list of the tiles held by the player.
- Added the `view_score` method to the `Player` class, which returns the current score of the player.
- Added the `start_turn` method to the `Player` class to indicate the start of a player's turn.
- Added the `end_turn` method to the `Player` class to indicate the end of a player's turn.
- Added tests for the `Player` class and the new methods in the `test_player.py` file.

- Added the `place_tile` method to the `Board` class, which facilitates placing a tile on a specific cell if it's empty.
- Added the `validate_word` method to the `Board` class, ensuring that a given word can be placed in a specific starting cell and direction without rule violations.
- Added test cases for the `Board` class in the `TestBoard` test suite.
- Included test cases for the `test_place_tile`, and `test_validate_word` methods in the `TestBoard` test suite.

## [0.0.5] - "Quinto Commit" - 2023/08/28

### Added
- Added the `place_tile` method to the `Board` class, which allows placing a tile on a specific cell if it's empty.
- Added the `validate_word` method to the `Board` class, which checks if a given word can be placed in a specific starting cell and direction without violating any rules.
- Added tests for the `Board` class in the `test_board.py` file.

## [0.0.4] - "Cuarto Commit" - 2023/08/28

### Added
- Added to the `Player` Class the `draw_tiles` method, which allows a player to take new tiles from the bag and which takes as arguments the bag of tiles and the number of tiles to take.
- Added to the `Player` Class the `exchange_tiles` method, which allows a player to exchange tiles with the bag and which receives the bag of tiles and a list of tiles that the player wants to exchange as arguments.
- Added to the `Player` Class the `calculate_score` method, which calculates the player's score based on the cells in which letters have been placed and their values ​​multiplied by the board multipliers.
- Added test cases for the `Player` class in the `TestPlayer` test suite.
- Included test cases for the `test_init`, `test_draw_tiles`, `test_exchange_tiles`, `test_view_tiles`, `test_view_score`, `test_start_end_turn`, and `calculate_score` methods in the `TestPlayer` test suite.
- Added a `MockBoard` class and a `MockCell` class to simulate game board and cell behavior in the tests.

## [0.0.3] - "Tercer Commit" - 2023/08/27

### Added
- Introduced the `Player` class to represent players in the game.
- Created the `ScrabbleGame` class to manage the Scrabble game itself.
- Added the `player.py`, `scrabble.py`, `test_player.py`, and `test_scrabble.py` files to the project.

### Changed
- Improved the `BagTiles` constructor by using a more organized structure for tile initialization.
- Refactored the `take` method in `BagTiles` to calculate the number of tiles taken more accurately.
- Enhanced the `put` method in `BagTiles` to directly extend the list of tiles.

## [0.0.2] - "Segundo Commit" - 2023/08/27

### Added
- Introduced the `Cell` class to represent individual cells on the game board.
- Added methods to the `Cell` class for adding letters, calculating letter and word values, and handling multipliers.
- Introduced the `Board` class to represent the game board and its grid of cells.
- Added tests for the `Board` class in `test_board.py`.
- Added test cases for the `Cell` class in the `TestCell` test suite.

### Changed
- Improved the `BagTiles` constructor by using a more organized structure for tile initialization.
- Refactored the `take` method in `BagTiles` to calculate the number of tiles taken more accurately.
- Enhanced the `put` method in `BagTiles` to directly extend the list of tiles.

## [0.0.1] - "Primer Commit" / "models.py" - 2023/08/18

### Added
- Introduced the `Tile` class to represent individual tiles with letters and values.
- Introduced the `BagTiles` class that simulates a bag of tiles for a word game.
- Added test cases for the `Tile` and `BagTiles` classes in the `TestTiles` and `TestBagTiles` test suites.
- Included test cases for the `test_tile`, `test_bag_tiles`, `test_take`, and `test_put` methods in the respective test suites.
- Used the `unittest.mock.patch` decorator to mock the `random.shuffle` function in the `test_bag_tiles` method of the `TestBagTiles` test suite.
- Utilized the `unittest` library to ensure the correct functioning of the methods.









 



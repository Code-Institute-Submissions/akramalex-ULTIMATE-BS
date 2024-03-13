from random import randint
import sys

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Sets the board size,
    the number of ships, the player's name
    and the board type(player board or computer board)
    Has methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        """
        Prints the current state of the board.
        Each cell of the board is represented by a character.
        '_' indicates an empty cell,
        'X' indicates a cell containing a ship, and
        '*' indicates a cell that has been guessed.
        """
        for row in self.board:
            print("  ".join(row))

    def guess(self, x, y):
        """
        Records a guess on the board and returns the result.
        Parameters:
        x: int - x-coordinate of the guess
        y: int - y-coordinate of the guess
        Returns:
        str - a string representing the result of the guess.
        """
        self.guesses.append((x, y))
        self.board[x][y] = "x"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        """
        adds a ship to the board at the specified coordinates
        if the number of ships on the board has reached the maximum limit.
        An error message if printed indicating the no more ships can be added.
        Otherwise, the ship is added to the board at the specified coordinates,
        and if the board type is "player",
        the corresponding cell on the player's
        board is marked with "@" to represent the ship
        """
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add anymore ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer,
    between  0 and size.
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
    Check if the coordinates (x, y) are valid for the given board.
    If the coordinate is valid return True; otherwise, return False.
    """
    if 0 <= x < board.size and 0 <= y < board.size:
        if (x, y) not in board.guesses:
            return True

    return False


def populate_board(board):
    """
    Populate the board with the ships in random positions.
    """

    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)
        if valid_coordinates(x, y, board) and (x, y) not in board.ships:
            board.add_ship(x, y)


def make_guess(board):
    """
    Prompt the player to make a guess and return the result.
    While true, the player enters a row number between 0 and 4,
    and column number between 0 and 4.
    If the values are not between 0 and 4 ,
    Print message "values must be between 0 and 4! please try again"
    If the number has been  guessed before,
    print message "You've already guessed those coordinates.
    please try again "
    Otherwise, return the player's guessed number and result
    """
    while True:
        try:
            x = int(input("Enter row number (0-4):\n"))
            y = int(input("Enter column number (0-4):\n"))

            if not (0 <= x < board.size and 0 <= y < board.size):
                print("Values must be between 0 and 4!. Please try again.")
            elif (x, y) in board.guesses:
                print("You can't guess the same coordinates twice!")
            else:
                result = board.guess(x, y)
                return x, y, result
        except ValueError:
            print("You must enter a number!")


def play_game(computer_board, player_board):
    """
    Play the battleship game.
    Print the player's board and computer's board
    Call function makes_guess
    to get the result
    and update the score as well
    """
    populate_board(computer_board)
    populate_board(player_board)

    while True:
        # Player's turn
        print(f"{player_board.name}'s board:")
        player_board.print_board()
        print("computer's board:")
        computer_board.print_board()

        print("Your turn:")
        x, y, result = make_guess(computer_board)
        if result == "Hit":
            print("Player guessed:", (x, y))
            print("player got a hit!")
            scores['player'] += 1
            if scores['player'] == player_board.num_ships:
                print("Congratulations! You've sunk all the computer's ships.")
                print("You Win!")
                new_game()
                return
        else:
            print("Player guessed:", (x, y))
            print("Player missed this time.")

        #  computer's turn (random guesses)
        while True:
            x = random_point(player_board.size)
            y = random_point(player_board.size)
            if (x, y) not in player_board.guesses:
                break
        result = player_board.guess(x, y)
        if result == "Hit":
            print("Computer guessed:", (x, y))
            print("Computer got a hit!")
            scores['computer'] += 1
            if scores["computer"] == player_board.num_ships:
                print("Oops! The computer has sunk all your ships. You lose!")
                new_game()
                return
        else:
            print("Computer guessed:", (x, y))
            print("Computer missed this time.")

        print("-" * 35)
        print("After this round, the scores are:")
        print(f"{player_board.name}: {scores['player']}."
              f" Computer: {scores['computer']}")
        print("-" * 35)

        # Ask the player to continue or quite
        choice = input("Enter any key to continue or 'n' to quit:\n")
        if choice.lower() == 'n':
            print("thank you")
            sys.exit()


def new_game():
    """
    Starts a new game. Sets the board and size and number of ships,
    resets the scores, and initializes the board.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome to ULTIMATE BATTLESHIPS!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)
    while True:
        player_name = input("Please enter your name: \n")
        if player_name.isalpha():
            print("-" * 35)
            print("Let's start the game,", player_name, "!")
            print("-" * 35)
            break

        else:
            print("Name cannot contain  numbers. please try again.")

    computer_board = Board(size, num_ships, "computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    try:
        play_game(computer_board, player_board)
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
        return


new_game()

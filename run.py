from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Sets board size,
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
        '_' indicates an empty cell.
        'X' indicates a cell containing a ship.
        '*' indicates a cell that has been guessed.
        """
        for row in self.board:
            print("  ".join(row))

    def guess(self, x, y):
        """
        Records a guess on the board and returns the result.
        x: int, x-coordinate of the guess
        y: int, y-coordinate of the guess
        Returns:
        str: "Hit" if the guess hits a ship, "Miss" otherwise.
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
        an error message if printed indicating the no more ships can be added.
        otherwise, the ship is added to the board at the specified coordinates,
        and if the board type is "player"
        the corresponding cell on the player's
        board is marked with "@" to represent the ship
        """
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add anymore ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

board = Board(5, 3, "player1", "player")
board.add_ship(1, 2)
board.print_board()
guess_result = board.guess(1, 2)
print("Guess result:", guess_result)
board.add_ship(3, 4)
board.add_ship(2, 3)
board.add_ship(4, 4)
board.print_board()




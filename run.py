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


board = Board(size=5, num_ships=3, name="player1," , type="player")
print("Board size:", board.size)
print("Number of ships:", board.num_ships)
print("Player name:", board.name)
print("Board type:", board.type)
print("Guesses:", board.guesses)
print("Ships:", board.ships)
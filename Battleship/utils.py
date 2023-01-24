class GameException:
    pass


class OutOfBoundsException(GameException):
    def __str__(self):
        return "This shot went out of bounds!"


class BadRandomShipsException(GameException):
    pass


class SquareShotTwiceException(GameException):
    def __str__(self):
        return "This square has already been shot!"


class Square:
    """
    Basic object of the game representing a board square.
    Defined by its coordinates.

    .x - square's horizontal coordinate.
    .y - square's vertical coordinate.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Square(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Square({self.x}, {self.y})"


class Ship:
    """
    The object to represent a ship.
    Defined by the coordinates of its bow, by its size and its course.

    .bow - coordinates of the topmost/leftmost ship's square.
    .course - either Square(1, 0) or Square(0, 1), representing ship's alignment.
    .decks - ship's length.
    .lives - ship's current amount of lives (number of decks not yet shot).
    """

    def __init__(self, bow: Square, course: Square = Square(0, 0), decks: int = 1):
        self.bow = bow
        self.course = course
        self.decks = decks
        self.lives = decks

    @property
    def get_squares(self):
        ship_squares = []
        next_square = self.bow
        for _ in range(self.decks):
            ship_squares.append(next_square)
            next_square += self.course
        return ship_squares

    def got_hit(self, shot):
        return shot in self.get_squares


class Board:
    """
    The object representing player's game board (a square grid).
    Defined by size and visibility.

    .size - the size of a grid.
    .is_hidden - the parameter to show if some parts of a board should be hidden in UI.
    .grid - the state of one's board.


    """

    def __init__(self, size: int = 6, gap: int = 10):
        self.size = size
        self.gap = gap
        self.human_grid = [[" "] * size for _ in range(size)]
        self.robot_grid = [[" "] * size for _ in range(size)]

        self.human_sunk = 0
        self.robot_sunk = 0

        self.busy = []
        self.ships = []

    # TBD: split into 2 functions
    def __str__(self):
        # OX coordinates line
        line = " " * 2
        for i in range(self.size):
            line += " " + chr(65 + i) + " " * 2
        field = line + " " * self.gap + line + "\n"

        # Upper outer grid line
        line = " \u256D"
        for i in range(self.size):
            line += "\u2508" * 3
            line += "\u252C" if i < self.size - 1 else "\u256E"
        field += line + " " * self.gap + line + "\n"

        for j in range(self.size):
            # Game cells line
            line = f"{j + 1}\u2502"
            for i in range(self.size):
                line += f" {self.human_grid[i][j]} \u2502"
            line += " " * self.gap
            line += f"{j + 1}\u2502"
            for i in range(self.size):
                line += f" {self.robot_grid[i][j]} \u2502"
            field += line + "\n"
            # Inner grid line
            if j < self.size - 1:
                line = " \u251C"
                for i in range(self.size):
                    line += "\u2508" * 3
                    line += "\u253C" if i < self.size - 1 else "\u2524"
            # Lower outer grid line
            else:
                line = " \u2570"
                for i in range(self.size):
                    line += "\u2508" * 3
                    line += "\u2534" if i < self.size - 1 else "\u256F"
            field += line + " " * self.gap + line + "\n"
        # Description line
        field += " " * 7 + "Your ships" + " " * (self.size * 4 - 15) + " " * self.gap
        field += " " * 7 + "Shoot here" + " " * (self.size * 4 - 15) + "\n"
        return field


temp_ship = Ship(Square(2, 3), Square(1, 0), 3)
print(*temp_ship.get_squares)
a = Square(2, 2)
b = Square(1, 1)
print(a + b)
print(chr(0x256D))
s = '123'
s = s + "a" + s * 2
print(s)
bb = Board()
print(bb)

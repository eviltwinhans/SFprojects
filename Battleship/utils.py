from random import randint
from secrets import choice
from time import sleep


class GameException(BaseException):
    pass


class OutOfBoundsException(GameException):
    def __str__(self):
        return "This shot went out of bounds!"


class BadRandomShipsException(GameException):
    pass


class CellShotTwiceException(GameException):
    def __str__(self):
        return "This square has already been shot!"


class Cell:
    """
    Basic object of the game representing a grid cell.
    Defined by its coordinates.

    .x (int): Cell's horizontal coordinate
    .y (int): Cell's vertical coordinate
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Cell(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    def to_ui_basis(self):
        ui_x = chr(65 + self.x)
        ui_y = str(self.y + 1)
        return ui_x + ui_y


class Ship:
    """
    The object to represent a ship.
    Defined by the coordinates of its bow, by its size and its course.

    .bow (Cell):    The coordinates of the topmost/leftmost ship's cell
    .course (Cell): Either Cell(1, 0) or Cell(0, 1), representing ship's alignment
    .decks (int):   Ship's length (the number of its cells)
    .lives (int):   Ship's current amount of lives (number of decks/cells not yet shot)
    """
    def __init__(self, bow: Cell, course=Cell(1, 0), decks=1):
        self.bow = bow
        self.course = course
        self.decks = decks
        self.lives = decks

    @property
    def get_cells(self):
        ship_cells = []
        next_cell = self.bow
        for _ in range(self.decks):
            ship_cells.append(next_cell)
            next_cell += self.course
        return ship_cells

    def got_hit(self, cell: Cell):
        return cell in self.get_cells


class Grid:
    """
    The object representing a player's grid.
    Defined by size and values.

    .size (int):              The size of a grid
    .values (list(list(str)): Values assigned to grid cells
    .busy (list(Cell)):       The list of cells already used during ship initiations or during the game
    .ships (list(Ship)):      The list of Ship instances initiated within the grid
    .victory_count (int):     The number of opponent ships sunk
    """
    def __init__(self, size):
        self.size = size
        self.values = [[" "] * size for _ in range(size)]

        self.busy = []
        self.ships = []
        self.victory_count = 0

    def hidden(self, fog: str = " "):
        fog_of_war = Grid(self.size)
        for i in range(self.size):
            for j in range(self.size):
                fog_of_war.values[i][j] = fog if self.values[i][j] in [" ", "\u2588"] else self.values[i][j]
        return fog_of_war

    def out(self, cell: Cell):
        return not ((0 <= cell.x < self.size) and (0 <= cell.y < self.size))

    def contour(self, ship, show=False):
        basic_shifts = [Cell(0, 0), Cell(1, 0), Cell(1, 1),
                        Cell(0, 1), Cell(-1, 1), Cell(-1, 0),
                        Cell(-1, -1), Cell(0, -1), Cell(1, -1)
                        ]
        for cell in ship.get_cells:
            for shift in basic_shifts:
                next_cell = cell + shift
                if not self.out(next_cell) and next_cell not in self.busy:
                    self.busy.append(next_cell)
                    if show:
                        self.values[next_cell.x][next_cell.y] = "."

    def add_ship(self, ship):
        for cell in ship.get_cells:
            if self.out(cell) or cell in self.busy:
                raise BadRandomShipsException
        for cell in ship.get_cells:
            self.values[cell.x][cell.y] = "\u2588"
            self.busy.append(cell)
        self.ships.append(ship)
        self.contour(ship)

    def shoot(self, shot: Cell):
        if self.out(shot):
            raise OutOfBoundsException
        if shot in self.busy:
            raise CellShotTwiceException

        self.busy.append(shot)
        for ship in self.ships:
            if ship.got_hit(shot):
                ship.lives -= 1
                self.values[shot.x][shot.y] = "X"
                if ship.lives == 0:
                    self.victory_count += 1
                    print("The ship is DESTROYED! Keep on!\n")
                    sleep(1)
                    self.contour(ship, show=True)
                else:
                    print("It's a HIT! Keep on!\n")
                    sleep(1)
                return True

        self.values[shot.x][shot.y] = "o"
        print("It's a MISS!\n")
        sleep(1)
        return False

    def clear_busy(self):
        self.busy = []


class Player:
    """
    Represents a general player.
    Defined by its own grid and the grid of their opponent.

    .your_grid (Grid):      The player's grid
    .opponents_grid (Grid): The grid of player's opponent
    """
    def __init__(self, your_grid, opponents_grid):
        self.your_grid = your_grid
        self.opponents_grid = opponents_grid

    def request_shot(self):
        raise NotImplementedError

    def move(self):
        while True:
            try:
                target = self.request_shot()
                repeat = self.opponents_grid.shoot(target)
                return repeat
            except GameException as e:
                print(e)


class RobotPlayer(Player):
    """
    Represents an AI player.
    """
    def request_shot(self):
        shot = Cell(randint(0, self.opponents_grid.size - 1), randint(0, self.opponents_grid.size - 1))
        print(f"Your opponent's move: {shot.to_ui_basis()}")
        return shot


class HumanPlayer(Player):
    """
    Represents a human player.
    """
    def request_shot(self):
        while True:
            shot_ui = list(input("Where to shoot? Please specify the coordinates: ").upper())
            if len(shot_ui) != 2:
                print("Incorrect move. Correct format: a letter, then a number. E.g. A1 or B3.")
                continue
            x_ui, y_ui = shot_ui
            if not (x_ui.isalpha() and 65 <= ord(x_ui) < 65 + self.opponents_grid.size
                    and y_ui.isdigit() and 1 <= int(y_ui) < 1 + self.opponents_grid.size):
                print("Incorrect move. Correct format: a letter, then a number. E.g. A1 or B3.")
                continue
            return Cell(ord(x_ui) - 65, int(y_ui) - 1)


class Game:
    """
    Represents one game of Battleship.
    Defined by a game schema (the list of ship's lengths), grid size, and number of spaces between two grids.

    .size (int):          The grid size for this game
    .gap (int):           The number of spaces between two grids
    .human_grid (Grid):   The state of human player's grid
    .robot_grid (Grid):   The state of AI player's grid
    .schema (list(int)):  The list of ship's lengths for the game
    .human (HumanPlayer): The field to store a HumanPlayer instance for the game
    .robot (RobotPlayer): The field to store a RobotPlayer instance for the game
    """
    def __init__(self, schema=[3, 2, 2, 1, 1, 1, 1], size=6, gap=10):
        self.schema = schema
        self.size = size
        self.gap = gap
        self.human_grid = self.create_grid()
        self.robot_grid = self.create_grid()

        self.human = HumanPlayer(self.human_grid, self.robot_grid)
        self.robot = RobotPlayer(self.robot_grid, self.human_grid)

    # TBD: separate line formation into a separate method
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
                line += f" {self.human_grid.values[i][j]} \u2502"
            line += " " * self.gap
            line += f"{j + 1}\u2502"
            for i in range(self.size):
                line += f" {self.robot_grid.hidden().values[i][j]} \u2502"
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

    def try_grid(self):
        game_schema = self.schema
        grid = Grid(self.size)
        attempts = 0
        for ship_length in game_schema:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Cell(randint(0, self.size - 1), randint(0, self.size - 1)),
                            choice([Cell(1, 0), Cell(0, 1)]), ship_length)
                try:
                    grid.add_ship(ship)
                    break
                except BadRandomShipsException:
                    pass
        grid.clear_busy()
        return grid

    def create_grid(self):
        grid = None
        while grid is None:
            grid = self.try_grid()
        return grid

    @staticmethod
    def greet():
        print()
        print("╭++++++++++++++++++++++++++++++++++++╮")
        print("│                                    │")
        print("│       Welcome to the game of       │")
        print("│            BATTLESHIP!             │")
        print("│                                    │")
        print("├++++++++++++++++++++++++++++++++++++┤")
        print("│ Please read the game designations: │")
        print("│                                    │")
        print("│ █ - Your ship's deck, undamaged    │")
        print("│ X - Ship's deck, destroyed         │")
        print("│ o - The shot missed                │")
        print("│ . - A cell near destroyed ship     │")
        print("│                                    │")
        print("╰++++++++++++++++++++++++++++++++++++╯")
        print()

    def main_cycle(self):
        Game.greet()
        turn = 0
        while True:
            print(self)
            if turn % 2 == 0:
                print("It's your turn!")
                repeater = self.human.move()
            else:
                print("Now it's computer's turn!")
                repeater = self.robot.move()
            if repeater:
                turn -= 1
            if self.robot.your_grid.victory_count == len(self.schema):
                print("All opponent's ships are destroyed! You won!\n")
                print(self)
                break
            if self.human.your_grid.victory_count == len(self.schema):
                print("All your ships are destroyed! Robo-player won!\n")
                print(self)
                break
            turn += 1

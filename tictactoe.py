def print_state(state):
    """Output the state of the game board to the console.

    Args:
        state (dict): Current state of the game board

    Returns:
        None
    """
    print(" \u256D\u2508\u2508\u2508\u252C\u2508\u2508\u2508\u252C\u2508\u2508\u2508\u256E")
    print("3\u2502 " + state['a3'] + " \u2502 " + state['b3'] + " \u2502 " + state['c3'] + " \u2502")
    print(" \u251C\u2508\u2508\u2508\u253C\u2508\u2508\u2508\u253C\u2508\u2508\u2508\u2524")
    print("2\u2502 " + state['a2'] + " \u2502 " + state['b2'] + " \u2502 " + state['c2'] + " \u2502")
    print(" \u251C\u2508\u2508\u2508\u253C\u2508\u2508\u2508\u253C\u2508\u2508\u2508\u2524")
    print("1\u2502 " + state['a1'] + " \u2502 " + state['b1'] + " \u2502 " + state['c1'] + " \u2502")
    print(" \u2570\u2508\u2508\u2508\u2534\u2508\u2508\u2508\u2534\u2508\u2508\u2508\u256F")
    print("   a   b   c  \n")


def game_init(message="Hey-hey! Let's play Tic-Tac-Toe!"):
    """Output a greeting to the players to the console,
    initialize an empty game board, return it and output to the console.

    Args:
        message (str): Greeting displayed at the beginning of the game

    Returns:
        state (dict): Initial state of the game board
    """
    print("\n" + "±" * len(message))
    print(message)
    print("±" * len(message) + "\n")
    state = {'a3': ' ', 'b3': ' ', 'c3': ' ',
             'a2': ' ', 'b2': ' ', 'c2': ' ',
             'a1': ' ', 'b1': ' ', 'c1': ' '
             }
    print_state(state)
    return state


def request_next_move(state, turn):
    """Request the coordinates of the next move.
    If the correct coordinates are not entered MAX_ATTEMPTS times in a row,
    then the corresponding flag (emergency_exit) changes the value to True.

    Args:
        state (dict): Current state of the game board
        turn (int): Sequence number of the current turn

    Returns:
        move (str): Coordinates of the next move
    """
    global emergency_exit
    translation = {39: None}  # To output the list of possible moves with no quotation marks.
    try_count = 0
    possible_moves = [k for k, v in state.items() if v == " "]
    next_move_message = f"It's your turn, Player {turn % 2 + 1}!\n" \
                        + "Your possible moves are " \
                        + str(possible_moves).translate(translation) \
                        + "\nMake your move: "
    while not emergency_exit:
        move = input(next_move_message).lower()
        if move in possible_moves:
            return move
        else:
            try_count += 1
            if try_count >= MAX_ATTEMPTS:
                emergency_exit = True
            else:
                print(f"Your move to _{move}_ is impossible.")
                next_move_message = "Your possible moves are " \
                                    + str(possible_moves).translate(translation) \
                                    + ".\nChoose wisely: "


def got_winner(state):
    """Check whether one of the horizontals, verticals or diagonals of the game board is occupied by one player.

    Args:
        state (dict): Current state of the game board

    Returns:
        _ (bool): Is it true that the winner is determined
    """
    if state['a1'] == state['a2'] == state['a3'] != " " \
            or state['b1'] == state['b2'] == state['b3'] != " " \
            or state['c1'] == state['c2'] == state['c3'] != " " \
            or state['a1'] == state['b1'] == state['c1'] != " " \
            or state['a2'] == state['b2'] == state['c2'] != " " \
            or state['a3'] == state['b3'] == state['c3'] != " " \
            or state['a1'] == state['b2'] == state['c3'] != " " \
            or state['a3'] == state['b2'] == state['c1'] != " ":
        return True
    else:
        return False


# The main cycle of the game.
MAX_ATTEMPTS = 5
greeting = "Hey-hey! Let's play Tic-Tac-Toe!"

while True:
    emergency_exit = False
    game_state = game_init(greeting)
    current_turn = 0

    while not got_winner(game_state) and not emergency_exit and current_turn <= 8:
        next_move = request_next_move(game_state, current_turn)
        if emergency_exit:
            break
        game_state[next_move] = 'O' if current_turn % 2 else 'X'  # Add X or O to dict, depending on the turn number.
        print_state(game_state)
        current_turn += 1

    if got_winner(game_state):
        print("\u2605" * 35)
        print(f"Congratulations, Player {(current_turn - 1) % 2 + 1}! You won!")
        print("\u2605" * 35)
    elif current_turn == 9:
        print("\u2690" * 23)
        print("It's a tie, my dudes!\nLet's try another time!")
        print("\u2690" * 23)
    else:
        # This code block is executed if and only if emergency_exit == True.
        print("\n" + "\u2620" * 46)
        print("Too many unsuccessful attempts to make a move.\nLet's try another time!")
        print("\u2620" * 46)
        break  # If game ends with emergency_exit, players are not invited to try again.

    if input("\nWould you like to try again? (yes/no): ").lower() not in ['yes', 'y', 'yeah']:
        break
    else:
        greeting = "Let's play another game of Tic-Tac-Toe!"

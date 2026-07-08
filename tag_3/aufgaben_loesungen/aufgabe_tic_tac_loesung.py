"""
Tic Tac Toe
"""

X = "X"
O = "O"
_ = None

type Matrix = list[list[str | None]]


def player(board: Matrix) -> str:
    """Returns player who has the next turn on board.

    if actions count is odd, next player is O, because X player started
    the game. Uses function actions() to get the number of available actions.

    count_ = 0 => X
    count_ = 1 => O
    count_ = 2 => X
    ...
    count_ = 9 => O

    Args:
        Board

    Returns:
        (str): next player
    """
    occupied = len(board) ** 2 - len(actions(board))
    if occupied % 2:
        return O
    return X


def actions(board: Matrix) -> set:
    """Returns set of all possible actions.

    Args:
        Board

    Returns:
        (set): tuple with all available actions on the board.
    """
    length = range(len(board))
    return {(i, j) for i in length for j in length if not board[i][j]}


def check_row(board: Matrix) -> str | None:
    """Check for same color in a row.

    Args:
        board: the game board
    Returns:
        str: Winner color or None
    """
    for row in board:
        # eg. set([X, X, X]) => {X} => len({X}) = 1
        if row[0] and len(set(row)) == 1:
            return row[0]
    return None


def check_vertical(board: Matrix) -> str | None:
    """Check for same color in a column.

    Transpose matrix and return X, O or None if no winner vertical

    Args:
        board: the game board
    Returns:
        str: Winner color or None
    """
    m = [list(row) for row in zip(*board)]
    return check_row(m)


def check_diagonal(board: Matrix) -> str | None:
    """Check for same color diagonal.

    Args:
        board: the game board

    Returns:
        Winner color or None
    """
    left_right_diag = [row[i] for i, row in enumerate(board)]
    right_left_diag = [row[-i - 1] for i, row in enumerate(board)]
    return check_row([left_right_diag, right_left_diag])


def check_board_full(board: Matrix) -> bool:
    """Check if Board is full and no actions left to play."""
    return not bool(actions(board))


def winner(board: Matrix) -> str | None:
    """Returns the winner of the game, if there is any."""
    return check_diagonal(board) or check_vertical(board) or check_row(board)


def terminal(board: Matrix) -> bool:
    """Returns True if game is over, False otherwise."""
    if winner(board):
        return True

    return check_board_full(board)


def test() -> None:
    board_1: Matrix = [
        [X, X, X],
        [O, O, _],
        [_, _, _],
    ]

    board_2: Matrix = [
        [X, O, X],
        [X, O, _],
        [_, O, _],
    ]

    board_3: Matrix = [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ]

    board_4: Matrix = [
        [X, O, X],
        [_, X, O],
        [_, _, O],
    ]

    tests = [
        {
            "board": board_1,
            "player": O,
            "actions": {(1, 2), (2, 0), (2, 1), (2, 2)},
            "winner": X,
            "terminal": True,
        },
        {
            "board": board_2,
            "player": X,
            "actions": {(1, 2), (2, 0), (2, 2)},
            "winner": O,
            "terminal": True,
        },
        {
            "board": board_3,
            "player": X,
            "actions": {
                (0, 0),
                (0, 1),
                (0, 2),
                (1, 0),
                (1, 1),
                (1, 2),
                (2, 0),
                (2, 1),
                (2, 2),
            },
            "winner": None,
            "terminal": False,
        },
        {
            "board": board_4,
            "player": X,
            "actions": {(1, 0), (2, 0), (2, 1)},
            "winner": None,
            "terminal": False,
        },
    ]

    for index, case in enumerate(tests, start=1):
        board = case["board"]

        assert player(board) == case["player"], f"board_{index}: player"
        assert actions(board) == case["actions"], f"board_{index}: actions"
        assert winner(board) == case["winner"], f"board_{index}: winner"
        assert terminal(board) == case["terminal"], f"board_{index}: terminal"

    print("Alle Tests erfolgreich.")


test()

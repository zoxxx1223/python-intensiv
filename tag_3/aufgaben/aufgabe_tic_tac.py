"""
(SCHWER)

Thema: Tic-Tac-Toe

Gegeben ist ein gültiges 3x3-Spielfeld. Ein Feld enthält entweder
X, O oder _ (leeres Feld). Spieler X beginnt immer.

Beispiel:

board = [
    [X, X, O],
    [O, _, X],
    [O, X, _]
]

Implementiere die folgenden Funktionen. Verwende Type-Hints,
Rückgabewerte und Docstrings.

Prüfe deine Implementierung mit den bereitgestellten Tests.
Kommentiere dazu die Zeile test() am Ende der Datei aus.

------------------------------------------------------------
1) player(board)

Gib den Spieler zurück, der als Nächstes am Zug ist.
Es bietet sich an, die Funktion actions() (siehe 2.) zu verwenden,
um die Anzahl der freien Felder zu zählen.

Beispiel:

board = [
    [X, O, _],
    [_, _, _],
    [_, _, _]
]

Ergebnis:
X

------------------------------------------------------------
2) actions(board)

Gib alle freien Felder als Set von Tupeln (Zeile, Spalte) zurück.

Beispiel:

board = [
    [X, X, O],
    [O, _, _],
    [O, X, _]
]

Ergebnis:
{(1, 1), (1, 2), (2, 2)}

------------------------------------------------------------
3) winner(board)

Gib den Gewinner zurück.

Ein Spieler gewinnt, wenn drei gleiche Symbole horizontal,
vertikal oder diagonal in einer Reihe liegen.

Rückgabe:
X, O oder None

------------------------------------------------------------
4) terminal(board)

Gib True zurück, wenn das Spiel beendet ist.

Das Spiel ist beendet, wenn
- winner(board) einen Gewinner liefert oder
- keine freien Felder (_) mehr vorhanden sind (zero actions).

Andernfalls gib False zurück.
"""

X = "X"
O = "O"
_ = None

type Matrix = list[list[str | None]]


def player(board: Matrix) -> str:
    """Returns player who has the next turn on board.

    if actions count is odd, next player is O, because X player started
    the game.

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


def actions(board: Matrix) -> set:
    """Returns set of all possible actions.

    Args:
        Board

    Returns:
        (set): tuple with all available actions on the board.
               Empty if no more actions available.
    """


def winner(board: Matrix) -> str | None:
    """Returns the winner of the game, if any."""


def terminal(board: Matrix) -> bool:
    """Returns True if game is over, False otherwise."""


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

    test_boards = [
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

    for index, case in enumerate(test_boards, start=1):
        board = case["board"]

        assert player(board) == case["player"], f"board_{index}: player"
        assert actions(board) == case["actions"], f"board_{index}: actions"
        assert winner(board) == case["winner"], f"board_{index}: winner"
        assert terminal(board) == case["terminal"], f"board_{index}: terminal"

    print("Alle Tests erfolgreich.")


if __name__ == "__main__":
    print("Tic-Tac-Toe Tests")
    # test()

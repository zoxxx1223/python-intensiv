GRID_SIZE = 50
BOARD_SIZE = 200

GROUND = [
    [1, 1, 1, 1],
    [1, 3, 1, 2],
    [1, 0, 3, 1],
    [2, 1, 1, 0],
]

SURFACE = [
    "Fels",
    "Wiese",
    "Wasser",
    "Schlamm",
    "Wüste",
]

while True:
    command = input("Bitte x und y eingeben: ").split()

    if command[0].lower() == "exit":
        print("Programm beendet.")
        break

    x, y = map(int, command)

    if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
        print("Player befindet sich außerhalb des Spielfelds.")
    else:
        x_grid = x // GRID_SIZE
        y_grid = y // GRID_SIZE
        surface = SURFACE[GROUND[y_grid][x_grid]]

        print(f"Rasterfeld: ({x_grid}, {y_grid})")
        print(f"Bodenart: {surface}")
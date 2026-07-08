# Aufgabe: data.txt einlesen (mit pathlib.Path)
# über die Zeilen iterieren und die Werte aufsplitten.
# nach int konvertieren und addieren. Es soll eine values-Liste
# erezugt werden, bei der jedes Element die Summe einer Zeile ist (append)

# values = [6, 9, 101, 28]

from pathlib import Path

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "data.txt", encoding="utf-8") as f:
    x = [sum(map(int, line.split(","))) for line in f]

print(x)

# list(map(int, ["20", "3"]))

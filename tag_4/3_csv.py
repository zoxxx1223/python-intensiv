"""
CSV einlesen und schreiben mit dem csv-Modul

reader => ein listensbasierter Reader (Liste)
DictReader => liest alles in ein Dict (CSV-Header wird benötigt)
writer => schreibt Liste von Listen
DictWriter => schreibt Dicts in eine Datei
"""

from pathlib import Path
import csv

DATA_DIR = Path(__file__).parent


def write_items(filename: str, items: list[dict]) -> None:
    """SChreibt modifizierte Items in CSV-Datei."""
    with open(DATA_DIR / filename, mode="w", encoding="utf-8", newline="") as f:
        # fieldnames sind die Keys, die von DictWriter erwartet werden
        # fieldnames=["id", "type"] wenn man nur eine Sub-Menge schreiben will
        writer = csv.DictWriter(f, fieldnames=items[0].keys())
        writer.writeheader()  # Schreibt den Header in die CSV DAtei
        writer.writerows(items)


def read_items(filename: str) -> list[dict]:
    """Lese die items-CSV Datei ein"""
    items = []
    with open(DATA_DIR / filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)

    return items


items: list[dict] = read_items(filename="items.csv")
print(items)
write_items(filename="items_modified.csv", items=items)

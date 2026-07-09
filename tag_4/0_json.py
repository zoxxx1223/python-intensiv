"""
Das json-Modul in Python


Python                  JSON
-----------------------------------------
dict                =>  object
list, tuple         =>  array
str                 =>  string
int, float          =>  number
True                =>  true
False               =>  false
None                =>  null

dump => in Datei speichern
dumps => Json-String erzeugen
load => Json-Datei laden
loads => Json-String laden
"""

import json
from pathlib import Path

data = {
    "president": {
        "name": "Zaphod Beeblebröx",
        "species": "Betelgeusian",
    },
}


def save_data(data: dict) -> None:
    """Schreibe data in eine Json-Datei."""
    with open(Path(__file__).parent / "data.json", mode="w", encoding="utf-8") as f:
        # ensure_ascii => False, damit Umlaute in die DAtei geschrieben werden
        # indent=2 => schönere Einrücking in der Ausgabedatei
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data(filename: str) -> dict:
    with open(Path(__file__).parent / "data.json", mode="r", encoding="utf-8") as f:
        return json.load(f)


json_string = json.dumps(data)
print("Dict:", data)
print("*" * 40)
# doppelte Anführungszeichen in den Strings verraten den JSON-String
print("JSON:", json_string)

# 3.) Python Objekt als JSON speichern
save_data(data=data)
data = load_data(filename="data.json")
print(data)

# 4.) einen JSON-String mit loadS einlesen
print(json.loads(json_string))

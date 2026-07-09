"""
Hauptprogramm
"""

import sys
from pathlib import Path

import requests

import jsonlib

# import numpy as np
# from jsonlib import save_data, load_data

print("Modul-Suchpfad:", sys.path)
for module in sys.modules:
    print("=>", module)

# via sys.modules kann man alle Module sehen, die aktuell
# geladen sind
print(sys.modules["enum"].IntEnum)
print("Hier liegt die python exe:", sys.executable)


def main():
    print("ich bin main")
    jsonlib.save_data({"a": 3})
    jsonlib.load_data("data.json")


main()

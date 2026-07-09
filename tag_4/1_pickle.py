"""
Das pickle MOdul (Python Objekte dauerhaft serialisieren).
Ist nur in der Pythonwelt verfügbar.


dump => in Datei speichern
dumps => Pickle-String erzeugen
load => Pickle-Datei laden
loads => Pickle-String laden

Pickle solte ausschließlich von sicheren Quellen verwendet werden,
da beim Unpicklen eine potentiell unsichere Aktion ausgeführt werden kann.
"""

import pickle
from pathlib import Path


data = {
    "president": {
        "name": "Zaphod Beeblebröx",
        "species": "Betelgeusian",
        "weapons": {"knife"},
    },
}
print(pickle.dumps(data))

# muss binär geöffnet werden
with open(Path(__file__).parent / "pickletest.pk", mode="wb") as f:
    pickle.dump(data, f)

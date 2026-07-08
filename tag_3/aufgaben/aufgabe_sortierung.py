# 1. Sortiere nach Einwohner (LEICHT)
lst = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]


# 2. Sortiere nach Bundesstaaten (Alabama, California...) LEICHT
states = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]


# 3. Sortiere absteigend (LEICHT)
lst = [500, 1000, 400, 40000, 999, 2, 0.5, 17]


# 4a) Sortiere nach Vornamen(MITTEL)
# 4b) Sortiere nach id (beachte dabei nur Digits, zb. 42ai => 42)
# Richtige Reihenfolge: 42, 123, 233
people = [
    {
        "first": "Arthur",
        "last": "Dent",
        "id": "1d23s",
    },
    {
        "first": "Zaphod",
        "last": "Beeblebrox",
        "id": "42ai",
    },
    {
        "first": "Ford",
        "last": "Perfect",
        "id": "233",
    },
]

# 5. Sortiere nach Punkten (aufsteigend) LEICHT
player = {"peter": 100, "klaus": 34, "wizz": 222, "angela": 23, "sabine": 400}

# 6 Gegebene eine Liste mit Personen und deren Verkäufen. MITTEL
# Der Verkaufserlös errechnet sich durch die letzten beiden Positionen,
# z.b. 46 x 18.67 für John Miller. Sortiere nach Verkaufserlös
umsaetze = [
    ("John", "Miller", 46, 18.67),
    ("Randy", "Steiner", 48, 27.99),
    ("Tina", "Baker", 53, 27.23),
    ("Andrea", "Baker", 40, 31.75),
    ("Eve", "Turner", 44, 18.99),
    ("Henry", "James", 50, 23.56),
]


# 7. Sortiere aufsteigend nach max-Wert der Liste. MITTEL
stox = [
    ["a", [22, 25, 14, 23]],
    ["b", [122, 25, 14, 233]],
    ["c", [422, 25, 14, 33]],
    ["d", [22, 1025, 14, 33]],
    ["e", [2, 5, 4, 3]],
]


"""
8. Sortiere die Liste nach dem Modulnamen (SCHWER)

Es soll nur der Modulname für die Sortierung verwendet werden.
Versionsangaben und Umgebungsbedingungen sollen ignoriert
werden.

Beispiele:

pytest==5.2                     -> pytest
pytest-cov                      -> pytest-cov
waldo-parillo;sys_platform=='win32'     -> waldo-parillo

Falsch:

[
    "pre-commit",
    "pytest-cov",
    "pytest==5.2",
    "waldo-parillo;sys_platform=='win32'",
]

Richtig:

[
    "pre-commit",
    "pytest==5.2",
    "pytest-cov",
    "waldo-parillo;sys_platform=='win32'",
]

Verwende eine eigene Sortierfunktion als key und keine
Lambda-Funktion.
"""

modules = [
    "waldo-parillo;sys_platform=='win32'",
    "pytest==5.2",
    "pytest-cov",
    "pre-commit",
]

"""
9. Sortiere die Dateigrößen (SCHWER)

Die Größen liegen als Strings vor und sollen nach ihrer
tatsächlichen Größe sortiert werden. Die Trennung mit Leerzeichen
zwischen Wert und Einheit ist garantiert.

Unterstützte Einheiten:

B (1)
KB (1024)
MB (1024**2)
GB (1024**3)

Beispiele:
1G B
800 B
2 MB
15 KB

=> nach Sortierung

800 B
15 KB
2 MB
1 GB

Die Sortierung soll aufsteigend erfolgen.

Verwende eine eigene Sortierfunktion als key und keine
Lambda-Funktion.
"""
sizes = [
    "15 KB",
    "2 MB",
    "800 B",
    "120 KB",
    "1 GB",
    "900 MB",
    "42 B",
]

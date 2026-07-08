"""
Bei der Übergabe von veränderlichen Datentypen wird die Referenz
übergeben und nicht der Wert

values = werte # hier wird Referenz kopiert
Seiteneffekt: Funktionen verändern die globale Umgebung.
Besser Funktionen ohne Seiteneffekte
"""


def get_list(values: list[int]) -> None:
    values.append(42)


werte = [1, 2, 3]
get_list(werte)  # es wird nur die Referenz übergeben
print("Werte:", werte)


# AUFGABE: globales player_stat Dict verändern

player_stat = {
    "bilbo": {
        "life": 100,
        "power": 29,
        "weapons": {"knife", "stick"},
    },
    "gollum": {
        "life": 120,
        "power": 29,
        "weapons": set(),
    },
}


# Funktion schreiben add_player_life_points
# soll die parameter Spielername und Lifepoints haben
# und die Lebenspunkte auf die bestehenden lebenspunkte hinzurechnen
def add_player_life_points(player: str, points: int) -> None:
    player_stat[player]["life"] += points

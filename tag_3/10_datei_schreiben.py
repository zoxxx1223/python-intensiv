"""
Datei schreiben: mode: w
An Datei anhängen: mode: a

=> wenn die Datei nicht existiert, wird die Datei angelegt.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent

data = [
    "23789238048790",
    "3489384",
    "392849348",
]


def write_data(data: list[str]) -> None:
    """Schreibe Strings in eine Datei. Weder write noch
    writelines schreiben newlines, wir müssen sie selber anhängen."""
    with open(BASE_DIR / "data2.txt", mode="w", encoding="utf-8") as f:
        f.writelines([f"{line}\n" for line in data])
        # Oder so:
        # for line in data:
        #     f.write(f"{line}\n")


write_data(data=data)


# IN einem Endlos-Loop gibt der User Strings ein.
# Die sollen via mode="a" an eine Datei namens "user.log" angehängt werden.
# per quit oder exit kann man den loop verlassen

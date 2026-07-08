"""
Datei öffnen und auslesen
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent


fp = open(BASE_DIR / "sys.log", mode="r", encoding="utf-8")
for line in fp:
    print(line.strip())  # es wird über die Zeilen iteriert

print("*" * 50)

# Den Filepointer mit seek(0) auf das erste Byte setzen
# fp.seek(0)
# for line in fp:
#     print(line.strip())

fp.close()

# Best Pracitce: Datei immer mit einem Kontext-Manager öffnen
# with sorgt dafür, dass die Datei geschlossen wird (auch im Fehlerfall)
with open(BASE_DIR / "sys.log", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

content = f.read()


############## map zum konvertieren einer Liste nutzen
values = ["1", "3", "5"]
values = list(map(int, values))

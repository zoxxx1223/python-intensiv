"""
Arbeiten mit Pfaden
"""

from pathlib import Path

# aktuelle Arbeitsverzeichnis
print("CWD:", Path.cwd())

# absoluter Pfad zu dieser Datei!
print("Absoluter Pfad zur aktuellen DAtei:", __file__)

# DAraus ein Path-Objekt machen
path = Path(__file__)
# man kann das path-Objekt nach oben navigieren, mit parent
print("Path Objekt:", path.parent)


# Absoluter Pfad zur Datei syslog im selben Verzeichnis wie dieses Skript
FILE_PATH = Path(__file__).parent / "sys.log"
# Datei öffnen, lesen und wieder schließen
fp = open(FILE_PATH)
print(fp.read())
fp.close()  # Dateien immer schließen!

if FILE_PATH.exists():
    print("die Datei existiert")

# rekursives Globben über das Tag3-Verzeichnes
for python_file in Path(__file__).parent.parent.rglob("*.py"):
    print(python_file)

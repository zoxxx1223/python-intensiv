"""
Datentyp Dict: ein Key-Value-Speicher
veränderlicher Datentyp
Keys: müssen unveränderliche Werte sein (Fehler: TypeError unhashable type: 'list')

"""

d = {}
d["name"] = "Bob"  # neues Key-Value-Paar anlegen
d["name"] = "Bobby"  # Überschreiben ist kein Problem
d["power"] = 23
d[(1, 2)] = 10  # steht auf x:1, y:2 und 10 Meter Höhe
d[""] = 42

# Zugriff auf dict erfolgt immer über den Key
print(d["name"])

# Key-Error vermeiden (weil man nicht weiß, ob Key im dict ist)
if "name" in d:
    print(d["name"])

# Alternative
if d.get(""):
    print("in dem leeren String key ist ein Wert")

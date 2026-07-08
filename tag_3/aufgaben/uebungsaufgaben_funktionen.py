"""(MITTEL)
5. Multi Replace
Schreibe eine Funktion Multi-Replace, die drei
Parameter entgegennimmt:
to_be_replaced = Liste mit zu ersetzenden Strings
replacements = Liste mit den Ersetzungen
s = ein String

Falls die Sequenzen mit den Ersetzungen
nicht die gleiche Länge haben sollten,
wird der Original-String zurückgegeben.

Beispiel:
to_be_replaced = ["Affe", "lebt", "Eis"]
replacements = ["Maki", "döst", "Schokolade"]
s = "Ein Affe lebt auf einem Baum und isst Eis"

Result:
Ein Maki döst auf einem Baum und isst Schokolade

Beispiel (mit Listen unterschiedlicher Länge)
to_be_replaced = ["rot"]
replacements = ["blau", "grün"] # !!!
s = "Ein roter Hut"

Result:
Ein  roter Hut
"""

to_be_replaced = ["Affe", "lebt", "Eis"]
replacements = ["Maki", "döst", "Schokolade"]
s = "Ein Affe lebt auf einem Baum und isst Eis"


""" (MITTEL)
6. Schreibe eine Funktion replace_umlauts, die einen String
entgegennimmt und alle deutsche Umlaute unter Berücksichtung
von Groß- und Kleinschreibung ersetzt. Der Rückgabewert
ist der String mit den Ersetzungen.

Österü => Oesterue
"""
# Testfälle für die Funktion replace_umlauts
# assert replace_umlauts("Österü") == "Oesterue"
# assert replace_umlauts("Äpfel") == "Aepfel"
# assert replace_umlauts("schön") == "schoen"
# assert replace_umlauts("für") == "fuer"
# assert replace_umlauts("Übergröße") == "Uebergroesse"
# assert replace_umlauts("aeoeue") == "aeoeue"
# assert replace_umlauts("") == ""


""" (SCHWER)
7.  Char-Counter. Schreibe eine Funktion char_counter(),
die einen String entgegennimmt und die einzelnen Zeichen des Strings zählt.
Das Ergebnis soll ein Dictionary mit den Vorkommen der Zeichen sein.
Groß- und Kleinschreibung soll ignoriert werden. 
Deutsche Umlaute werden umgeschrieben.

result = char_counter("Überlingen")
// {'u': 1, 'e': 3, 'b': 1, 'r': 1, 'l': 1, 'i': 1, 'n': 2, 'g': 1}

"""

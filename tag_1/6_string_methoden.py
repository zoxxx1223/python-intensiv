"""
Wichtige String-Methoden:
"""
example = "The quick brown fox jumps over the lazy dog"

# replace(alt, neu)
neu_example = example.replace("o", "a")
print("neu example:", neu_example)

# Prüfen, ob ein STring mit einer Zeichenkette beginnt (endswith funktioniert identisch)
if example.startswith("The"):
    print("Der String example beginnt mit The")

# Find: findet einen Substring in einem String:
print("find von example:", example.find("brown")) # -1 -> Nicht gefunden


user_input = "  \n343\n\t"
print("Stripped:", user_input.strip()) # entfernt Whitespace vorne und hinten

user_input = "####434###!##"
print("Stripped:", user_input.strip("#!"))

# strip() erzeugt neuen String, replace erzeugt neuen String, replace erzeugt neuen String
# => Funktion-Chaining
example = "abcabcabc".strip().replace("a", "x").replace("b", "y") # Ersetze a mit x und b mit y

# split => einen String aufsplitten in eine Liste
user_input = "command delete"
user_input_list = user_input.split() # per default an Leerzeichen
print(type(user_input_list), user_input_list)

"""
Aufgabe:
Ein neuer Benutzer soll auf einem Server angelegt werden.

Gib einen Benutzernamen ein und prüfe ihn anhand der folgenden
Regeln:

1. Beginnt der Benutzername mit "adm", gib aus:
   Administratorkonto erkannt.

2. Endet der Benutzername mit "$", gib aus:
   Dienstkonto erkannt.

3. Andernfalls gib aus:
   Standardbenutzer erkannt.

Verwende dazu:
- startswith()
- endswith()
- if
- elif
- else

Wir gehen von gültigen Eingaben aus.

Beispiel 1:
-----------
Bitte geben Sie den Benutzernamen ein: admmueller
Administratorkonto erkannt.

Beispiel 2:
-----------
Bitte geben Sie den Benutzernamen ein: backup$
Dienstkonto erkannt.

Beispiel 3:
-----------
Bitte geben Sie den Benutzernamen ein: max
Standardbenutzer erkannt.
"""


# username = input("Bitte geben Sie den Benutzernamen ein: ")

# if username.startswith("adm"):
#     print("Administratorkonto erkannt.")
# elif username.endswith("$"):
#     print("Dienstkonto erkannt.")
# else:
#     print("Standardbenutzer erkannt.")


# Membership Operator in
# Prüfen, ob ein Wert in einer Seq enthalten ist

host = "x.dev"
if "def" in host:
    print("def ist in host")
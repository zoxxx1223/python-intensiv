"""
Benutzereingabe: input liefert immer einen String
für numerische Aufgaben muss dieser String in int oder float konvertiert werden
"""
ui = input("Bitte eine Zahl eingeben: ") # Rückgabe von Input ist ein String
print("Usereingabe:", ui, type(ui))


# Typecast von String -> int / float
number = int(ui)
print("number:", number, type(number))

# von int nach float konvertien
float_number = float(number)
print("float_number:", float_number, type(float_number))

"""
Aufgabe:
Ein Server besitzt eine Festplatte.

Gib den Gesamtspeicher in GB und den bereits belegten Speicher
in GB ein.

Berechne, wie viel Speicherplatz noch frei ist.

Nutze Variablen, input(), int() und print().

Beispiel:
Bitte geben Sie den Gesamtspeicher ein: 500
Bitte geben Sie den belegten Speicher ein: 320

Freier Speicher: 180 GB

wir gehen aktuell von validem Input aus
"""
gesamt = int(input("Bitte geben Sie den Gesamtspeicher ein: "))
belegt = int(input("Bitte geben Sie den belegten Speicher ein: "))
result = gesamt - belegt

print("Freier Speicher:", result, "GB")
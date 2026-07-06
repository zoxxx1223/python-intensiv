"""
Bedingte Anweisungen, boolscher Datentyp.


Folgende Werte gelten als unwahr im boolschen Kontext (Falsiness)
[] => leere Liste
{} => leeres Dict
0 => Integer 0
None => None
False => bool Falsch
() => leeres Tupel
'' => Leerer String
"""
value = 0
x = bool(value)  # True oder False
print("x:", x, type(x))

value = -938749
# Trifft zu bzw. ist wahr, wenn value ungleich 0 ist
if value:
    print("Value ist ungleich 0")


# if-elif-else
city = "Hamburg"

if city == "Hamburg":
    print("Stadt ist HH")
elif city == "Nürnberg":
    print("Stadt ist Nürnberg")
elif city == "Fürth":
    print("Stadt ist Fürth")
else:
    print("Stadt ist eine unbekannte Stadt")


"""
Aufgabe: In welche Zahlenreihe fällt die Zahl?

Ein Programm erzeugt eine zufällige Zahl zwischen 1 und 100.

Gib anschließend eine Zahl ein.

Prüfe, in welche Zahlenreihe die Zahl fällt:

- 1 bis 20   -> Reihe 1 (if...)
- 21 bis 40  -> Reihe 2 (elif...)
- 41 bis 60  -> Reihe 3 (elif...)
- 61 bis 80  -> Reihe 4
- 81 bis 100 -> Reihe 5 (else...)

Gib zum Schluss die zufällig erzeugte Zahl und die passende Reihe aus.

Nutze:
- import random
- random.randint()
- input()
- int()
- if, elif und else

Beispiel:
Zufällige Zahl: 73
Die Zahl 73 gehört zu Reihe 4.

"""
# random Modul ist NICHT kryptographisch stark (dafür das secrets-Modul nutzen)
import random 

random.seed(42)

zahl = random.randint(1, 100)
print("Gewürfelte Zahl:", zahl)

if zahl <= 20:
    reihe = 1
elif zahl <= 40:
    reihe = 2
elif zahl <= 60:
    reihe = 3
elif zahl <= 80:
    reihe = 4
else:
    reihe = 5

print("Die Zahl", zahl, "ist in Reihe", reihe)


# Logischen Operatoren (and &&, or |, not !)
if zahl > 3 or zahl < 343:
    print("Zahl ist größer als 3 oder kleiner als 343")

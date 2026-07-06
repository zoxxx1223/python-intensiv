"""
Aufgabe (mittel)

Eine Datei wird auf einer Festplatte in Blöcken gespeichert.

Die Blockbelegung wird als Binärzahl dargestellt:

0 = freier Block
1 = Block gehört zur Datei

Eine Datei gilt als zusammenhängend gespeichert, wenn alle belegten
Blöcke direkt nebeneinander liegen. Gibt es mehrere getrennte Folgen
von Einsen, ist die Datei fragmentiert.

Lies die Blockbelegung über input() ein und prüfe, ob die Datei
zusammenhängend gespeichert ist.

Ausgabe:
- "Datei ist zusammenhängend gespeichert."
- "Datei ist fragmentiert."

Wir gehen von einer gültigen Binärzahl als Eingabe aus.

blockbelegung = input("Bitte geben Sie die Blockbelegung ein: ")

Beispiele:
----------
Eingabe: 00000000
Ausgabe:
Datei ist zusammenhängend gespeichert.

(Die Datei belegt keinen Block.)

Eingabe: 00111100
Ausgabe:
Datei ist zusammenhängend gespeichert.

(Alle belegten Blöcke liegen nebeneinander.)

Eingabe: 10000001
Ausgabe:
Datei ist fragmentiert.

(Die Datei liegt in zwei getrennten Bereichen.)

Eingabe: 1100011001
Ausgabe:
Datei ist fragmentiert.

(Die Datei ist auf mehrere Bereiche verteilt.)

Eingabe: 01111110
Ausgabe:
Datei ist zusammenhängend gespeichert.
"""

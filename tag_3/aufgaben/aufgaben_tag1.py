"""
1. Vokale zählen (MITTEL)
Schreibe eine Funktion count_vowels() die einen String als Parameter erwartet,
und alle Vokale  in diesem String zählt. Der Rückgabewert der Funktion ist die
Anzahl der Vokale (int). Als Vokale zählen im deutschen: aeiouüäö
Beachte Groß- und Kleinschreibung! Auge hat 3 Vokale

Beispiel:
number_of_vowels = count_vowels("teleport").
print(number_of_vowels)
// 3

number_of_vowels = count_vowels("Ööll").
print(number_of_vowels)
// 2

Diese Tests sollten erfolgreich durchlaufen.

assert count_vowels("teleport") == 3
assert count_vowels("Ööll") == 2
assert count_vowels("Auge") == 3
assert count_vowels("Python") == 1
assert count_vowels("AEIOU") == 5
assert count_vowels("äöü") == 3
assert count_vowels("") == 0
assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
"""

"""
3. Liste filtern (MITTEL)
Schreibe eine Funktion filter_input(), die eine Liste A entgegennimmt und
anhand einer weiteren Liste B mit erlaubten Werten prüft, ob diese Werte
zulässig sind. Rückgabewert der Funktion ist eine Liste mit Werten, die
mithilfe B geprüft worden ist.

Beispiel
input_filtered = filter_input([1, 3, 4, 5, 3], [3, 4])
print(input_filtered)
// [3, 4, 3]

input_filtered = filter_input([1, 3, 4, 5, 3], [])
print(input_filtered)
// []

input_filtered = filter_input(["gold", "gelb", "gelb", "rot", "gelb"], ["gelb", "rot"])
// ["gelb", "gelb", "rot", "gelb"]

"""

"""
4. Rückwärts (SCHWER)
Schreibe eine Funktion reverse_cutter(), die einen String entgegennimmt, diesen
zu Kleinbuchstaben transformiert, den ersten und letzten Index abschneidet und
das Ergebnis umgedreht zurückgibt. Ein Input kleiner gleich Länge zwei gibt
einen leeren String zurück.  Beispiel:
reversed = reverse_cutter("Petersburg")
// rubsrete

Tests sollten erfolgreich durchlaufen:
assert reverse_cutter("Petersburg") == "rubsrete"
assert reverse_cutter("Python") == "ohty"
assert reverse_cutter("Hallo") == "lla"
assert reverse_cutter("AB") == ""
assert reverse_cutter("A") == ""
assert reverse_cutter("") == ""
assert reverse_cutter("Test") == "se"
assert reverse_cutter("Äpfel") == "efp"
"""


"""
5. Max (MITTEL)
Implementiere die Funktion max. Diese soll aus einer gegebenen Liste von
Integerwerten den größten Wert zurückgeben. Nutze dazu nicht die Built-In
Funktion max oder max aus dem Numpy-Modul! Die Funktion soll None zurückgeben,
wenn eine leere Liste übergeben wurde.  

Beispiel:
values = [3, 2, 4]
x_max = max(values)
// 4

values = []
x_max = max(values)
// None

Diese Tests sollten erfolgreich durchlaufen.
Entferne die Kommentare, um sie auszuführen.

assert max_value([100, 2, 3, 1, 99, -1, 109]) == 109
assert max_value([1]) == 1
assert max_value([-5, -10, -2, -8]) == -2
assert max_value([0, -1, -2]) == 0
assert max_value([-100]) == -100
assert max_value([5, 5, 5]) == 5
assert max_value([-3, 7, -1, 4]) == 7
assert max_value([]) is None
"""

"""
6. Median (SCHWER)
Implementiere die Funktion median(), die eine Liste von Integerwerten
entgegennimmt und den Median berechnet. Prüfe die Funktion mit verschiedenen
Input-Werten! Nicht die Funktion median aus dem Numpy Modul o.ä. nutzen.
Ergebnis kann hier geprüft werden:
http://www.alcula.com/calculators/statistics/median/


Beispiel:
values = [1, 2, 4, 8, 2, 19]
x_median = median(values)
// 3.0

Diese Tests sollten erfolgreich durchlaufen.
Entferne die Kommentare, um sie auszuführen.

assert median([1, 2, 3]) == 2
assert median([1, 2, 3, 4]) == 2.5
assert median([1, 2, 4, 8, 3, 19]) == 3.5
assert median([42]) == 42
assert median([-10, -5, 5, 10]) == 0.0
"""

""" (LEICHT)
7. Schwellenwertfunktion (Heaviside, Hard Limit)
Eine Funktion, die häufig im Zusammenhang mit neuronalen Netzen 
genutzt wird, ist die Heaviside Funktion.
Sie gibt 1 zurück, wenn der Eingangswert größergleich 0 ist, ansonsten,
gibt sie 0 zurück.

Hintergrundwissen:
https://de.wikipedia.org/wiki/Heaviside-Funktion
"""

"""
(MITTEL)

Clamp-Funktion

In vielen Programmen dürfen Werte einen bestimmten Bereich nicht
verlassen. Beispielsweise darf die Lautstärke einer Musik-App nur
zwischen 0 und 100 liegen.

Schreibe eine Funktion `clamp(value, minimum, maximum)`, die einen Wert
auf einen vorgegebenen Bereich begrenzt.

Regeln:
- Ist value kleiner als minimum, gib minimum zurück.
- Ist value größer als maximum, gib maximum zurück.
- Andernfalls gib value unverändert zurück.

Hinweis:
Verwende die built-in Funktionen min() und max(), um die Funktion möglichst
kompakt zu implementieren.

Beispiele:
clamp(50, 0, 100)   -> 50
clamp(-10, 0, 100)  -> 0
clamp(120, 0, 100)  -> 100
"""

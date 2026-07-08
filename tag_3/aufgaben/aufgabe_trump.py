"""
Gruppenaufgabe

Der Trump Parser

Für unser Auftraggeber, die Newscom-Presseagentur, sollen wir einen Parser
entwickeln, der öffentliche Reden von Donald Trump einliest und nach gewissen
Kriterien filtert oder ausgibt.

Parsen bedeutet in diesem Zusammenhang: Text aufsplitten, von
Leer- Satz- und Steuerzeichen bereinigen und in einer Liste verfügbar machen.

Über ein input soll der User einen Modus wählen können.
In Abhängigkeit der Eingabe (input()) startet der Parser.

Der Parser soll folgende Modi haben:

1. Modus SENTENCE

der Datei-Content wird in Sätze gesplittet. Ein Punkt gilt als Ende eines Satzes.
Wenn das eingegebene Suchwort in diesem Satz enthalten ist, drucke den Satz aus

Die Usereingabe ist festgelegt und soll wie folgt aussehen:
SEN <SUCHWORT>

z.b.
SEN America

soll nur Sätze ausdrucken, in denen America vorkommt.

Hinweise: nutze für diesen Modus split(), for-loop, in-Operator.
Nützlich ist hier auch die String-Methode strip(),
die Worte von White-Space und Steuerzeichen befreit.


2. Modus WORD

der Datei-Content wird in Wörter gesplittet. Jedes Wort sollte
von Kommas und Punkten und anderen  bereinigt werden.
Wenn das eingegebene Suchwort in diesem Wort enthalten ist,
füge es einer Ergebnis-Liste hinzu (zb. word_list)
Diese Liste sollte von doppelten Elementen bereinigt werden.
Diese Liste muss sortiert ausgegeben werden.

Die Usereingabe ist festgelegt und soll wie folgt aussehen:
WORD <SUCHWORT>

z.b.
WORD Am

es sollen sich nur Wörter in der liste befinden, die mit `Am` starten.
'Americans', 'America', 'Amendment', [..]

Hinweise: nutze für diesen Modus split(), for-loop, in-element-Operator
Nützlich ist hier auch die String-Methode strip(), die Worte von
White-Space und Steuerzeichen befreit.

3. Modus TOP

der Datei-Content wird in Wörter gesplittet. Jedes Wort sollte von Kommas
und Punkten bereinigt werden.
Wenn das eingegebene Suchwort in diesem Wort enthalten ist,
füge es einer Ergebnis-Liste hinzu (zb. word_list)
Gesucht ist die TOP-TEN aller Wortnennungen inklusive Anzahl der Vorkommen.
Es sollen nur Worte
berücksichtigt werden, die > 5 Zeichen haben, um zumindest Pronomen und
Füllwörter etwas auszuschließen.
Hierbei bitte Groß- und Kleinshreibung NICHT beachten (case-insensitive)

Die Usereingabe ist festgelegt und soll wie folgt aussehen:
TOP

z.b.
TOP

[('people', 964), ('because', 762),

Hinweise: nutze für diesen Modus split(), for-loop, in-element-Operator, sorted.
Für diese Aufgabe muss der Datentyp Dict verwenden werden.

final_list = {}
final_list["america"] = 1
final_list["america"] += 1
# america ist der Key, 1 der Value. Der Value kann hochgezählt (inkrementiert) werden

"""

from pathlib import Path

with open(Path(__file__).parent / "trump_speeches.txt", encoding="utf-8") as file:
    content = file.read()

print(content)

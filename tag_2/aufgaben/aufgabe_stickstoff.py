"""
(MITTEL)

Schreibe ein Python-Programm zur Erfassung von Stickstoff-Messwerten.

Aufgaben:
1. Lies Messwerte mit input() ein, bis der Benutzer "ende" eingibt.
2. Akzeptiere nur Werte zwischen 0 % und 100 %. MIN_NITROGEN, MAX_NITROGEN
3. Weise ungültige Eingaben mit einer Fehlermeldung zurück.
4. Berechne den Durchschnitt aller gültigen Messwerte.
5. Gib aus, ob der Durchschnitt im optimalen Bereich von
   20 % bis 40 % liegt (len, sum). OPTIMAL_MIN, OPTIMAL_MAX

Vorgaben:
- Verwende while, if/else, input() und break.
- Nutze Konstanten für Grenzwerte und Beenden-Befehle.
- Prüfe numerische Eingaben mit:
    eingabe.replace(".", "", 1).isdigit()

Hinweis:
In Produktivcode würdest du hierfür Exception Handling (try/except)
anstelle von isdigit() und replace verwenden.

Beispiel:
-------------
Willkommen beim Stickstoff-Messgerät 2000
Kalkuliere den Stickstoff deiner Zimmerpflanze!

Gib den Stickstoffgehalt in Prozent ein
(oder "quit" zum Beenden): 22.2
(oder "quit" zum Beenden): hallo
Fehlerhafte Eingabe. Bitte gib eine Zahl ein.
(oder "quit" zum Beenden): 120
Ungültig. Bitte gib einen Wert zwischen 0 % und 100 % ein.
(oder "quit" zum Beenden): 24.1
(oder "quit" zum Beenden): 38.3
(oder "quit" zum Beenden): 11.3
(oder "quit" zum Beenden): quit

Berechne den Durchschnitt der Messwerte...
Durchschnittlicher Stickstoffgehalt: 23.975%
Der Durchschnittswert liegt im optimalen Bereich.
"""

MIN_NITROGEN = 0
MAX_NITROGEN = 100
OPTIMAL_MIN = 20
OPTIMAL_MAX = 40
EXIT_COMMANDS = ["exit", "quit"]

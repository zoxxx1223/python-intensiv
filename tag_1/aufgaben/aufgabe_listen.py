"""
Aufgabe 1:
Gib alle Servernamen aus der Liste einzeln aus.
"""

servers = ["srv-web01", "srv-db01", "srv-backup01"]


"""
Aufgabe 2:
Gib alle Servernamen mit ihrer Positionsnummer aus.
"""

servers = ["srv-web01", "srv-db01", "srv-backup01"]


"""
Aufgabe 3:
Filtere alle Server, deren Name mit "srv-web" beginnt.
"""

servers = ["srv-web01", "srv-db01", "srv-web02", "test01"]


"""
Aufgabe 4:
Filtere alle Ports zwischen 1024 und 10000.
Gib die gefilterte Liste sortiert aus.
"""

ports = [22, 80, 443, 3306, 8080, 9999, 12000]


"""
Aufgabe 5:
Gib das letzte Logfile aus, falls die Liste nicht leer ist.
"""

logfiles = ["auth.log", "syslog", "kernel.log"]


"""
Aufgabe 6:
Übernimm nur erlaubte Statuscodes in eine neue Liste.
"""

status_codes = [200, 404, 500, 200, 301, 403, 500]
allowed_codes = [200, 301]


"""
Aufgabe 7:
Entferne Unterstriche aus Benutzernamen.
Leere Namen sollen nicht übernommen werden.
"""

users = ["max_muster", "admin_user", "_", "backup_"]


"""
Aufgabe 8:
Bereinige Hostnamen.
Entferne Leerzeichen, Steuerzeichen und den Buchstaben "x".
Leere Hostnamen sollen nicht übernommen werden.
"""

hosts = [" xweb01 ", "\ndbx01", "\tproxy ", " x "]


"""
Aufgabe 9:
Kombiniere die Servernamen mit den IP-Endungen.

Die erste Liste enthält Servernamen.
Die zweite Liste enthält die letzte Zahl einer IP-Adresse.

Erzeuge eine neue Liste, in der beide Werte miteinander kombiniert
werden.

Die kürzere Liste bestimmt die Anzahl der Ergebnisse.

Beispiel:
----------
Servernamen:
["web", "db", "backup", "monitor"]

IP-Endungen:
[10, 20, 30]

Ergebnis:
["web10", "db20", "backup30"]

oder
["web", "db"]
[10, 20, 30]
Ergebnis:
["web10", "db20"]
"""
names = ["web", "db", "backup", "monitor"]
numbers = [10, 20, 30]

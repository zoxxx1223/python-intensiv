"""
1.  (MITTEL)
Erstelle eine Funktion filter_integer_data, die eine Liste
als Parameter entgegennimmt und jedes Element prüft, ob es vom
Typ integer ist. Der Rückgabewert der Liste ist eine Liste mit
Integerwerten. Nutze zum Prüfen des Typs die Funktion type() oder isinstance()

type(x) is int
isinstance(x, int) => oft die bessere Wahl, weil es Vererbung berücksichtigt

result = filter_integer_data(["a", 3, 1, 3.3])
Result: [3, 1]

Diese Tests sollten erfolgreich durchlaufen.
Entferne die Kommentare, um sie auszuführen.

# assert filter_integer_data(["a", 3, 1, 3.3]) == [3, 1]
# assert filter_integer_data([1, 2, 3]) == [1, 2, 3]
# assert filter_integer_data([1.1, 2.2, 3.3]) == []
# assert filter_integer_data(["x", True, 5]) == [True, 5]   # bei isinstance()
# assert filter_integer_data(["x", None, [], {}, 7]) == [7]
# assert filter_integer_data([]) == []

2. (MITTEL)
Erstelle eine Funktion check_values, die eine Liste mit float-Werten und einen
tupel übergeben bekommt. Die Funktion prüft, ob alle Elemente
im geschlossenen Interval [a, b] liegen. Der Rückgabewert ist ein boolean.

Erinnerung: geschlossenes Interval bedeutet, das alle Werte inklusive der
Grenzwerte zwischen zwei bestimmten Zahlen einschließt

Ist values leer, soll die Funktion True zurückgeben.

def check_values(values, interval):
    ...

values = [2, 2.2, 4, 2.3, 0.1]
interval = (1, 5.3)
result = check_values(values, interval)
Result: False  # Nicht alle Werte von values liegen im Interval [1, 5.3]

Diese Tests sollten erfolgreich durchlaufen.
Entferne die Kommentare, um sie auszuführen.

# assert check_values([2, 2.2, 4, 2.3], (1, 5.3)) is True
# assert check_values([2, 2.2, 4, 2.3, 0.1], (1, 5.3)) is False
# assert check_values([1, 5.3], (1, 5.3)) is True
# assert check_values([1.0, 3.2, 5.3], (1, 5.3)) is True
# assert check_values([0.99], (1, 5.3)) is False
# assert check_values([5.31], (1, 5.3)) is False
# assert check_values([], (1, 5.3)) is True
"""

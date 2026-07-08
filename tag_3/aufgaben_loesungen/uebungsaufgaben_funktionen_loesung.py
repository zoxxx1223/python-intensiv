"""
# Aufgabe 5, Multi Replace
"""

to_be_replaced = ["Affe", "lebt", "Eis"]
replacements = ["Maki", "döst", "Schokolade"]
s = "Ein Affe lebt auf einem Baum und isst Eis"


def multi_replace(to_be_replaced, replacements, s):
    if len(to_be_replaced) != len(replacements):
        return s

    for a, b in zip(to_be_replaced, replacements):
        s = s.replace(a, b)
    return s


result = multi_replace(to_be_replaced, replacements, s)
print(result)


"""
5. Schreibe eine Funktion replace_umlauts, die einen String
entgegennimmt und alle deutsche Umlaute unter Berücksichtung
von Groß- und Kleinschreibung ersetzt. Der Rückgabewert
ist der String mit den Ersetzungen.

Österü => Oesterue
"""


def replace_umlauts(s):
    """Replace german umlauts case-sensitive"""
    umlaute = {
        "ä": "ae",
        "ü": "ue",
        "ö": "oe",
        "Ö": "Oe",
        "Ä": "Ae",
        "Ü": "Ue",
    }
    for umlaut, replacement in umlaute.items():
        s = s.replace(umlaut, replacement)

    return s


print(replace_umlauts("Österü"))


def better_umlauts(s):
    """Die Funktion multi_replace nutzen"""
    umlaute = {
        "ä": "ae",
        "ü": "ue",
        "ö": "oe",
        "Ö": "Oe",
        "Ä": "Ae",
        "Ü": "Ue",
    }
    return multi_replace(umlaute.keys(), umlaute.values(), s)


print(better_umlauts("Österü"))

"""
5.  Char-Counter. Schreibe eine Funktion char_counter(), die einen String entgegennimmt und die einzelnen Zeichen des Strings zählt.
Das Ergebnis soll ein Dictionary mit den Vorkommen der Zeichen sein.
Groß- und Kleinschreibung soll ignoriert werden. Deutsche Umlaute werden umgeschrieben.

result = char_counter("Überlingen")
// {'u': 1, 'e': 3, 'b': 1, 'r': 1, 'l': 1, 'i': 1, 'n': 2, 'g': 1}

"""


def char_counter(string):
    # kürzeste Variante mit Counter aus den Collections Modul
    # return col.Counter(string.lower())

    # Variante mit DefaultDict aus den collections
    # d = defaultdict(int)
    # for char in string.lower():
    #     d[char] += 1
    # return d

    # klassische Variante
    counter = {}
    string = replace_umlauts(string)  # Umlaute ersetzen
    for char in string.lower():
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter


print(char_counter("Überlingen am Bodensee"))
# {'u': 1, 'e': 6, 'b': 2, 'r': 1, 'l': 1, 'i': 1, 'n': 3, 'g': 1, ' ': 2, 'a': 1, 'm': 1, 'o': 1, 'd': 1, 's': 1}

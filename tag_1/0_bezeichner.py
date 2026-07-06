""" 
Modul-Docstring

Python Variablen und Dateinamen: Konventionen und Best Practices

In Python ist es wichtig, sowohl bei der Benennung von Variablen als auch
bei Dateinamen klare und konsistente Konventionen zu verwenden. Dadurch
wird der Code lesbarer, verständlicher und einfacher zu warten.

Konventionen:
- Variablennamen:
  - Verwenden Sie Kleinbuchstaben und Unterstriche (snake_case).
  - Vermeiden Sie reservierte Schlüsselwörter oder Namen, die leicht mit
    integrierten Funktionen verwechselt werden können (z. B. `list`, `str`).
  - Namen sollten aussagekräftig sein und den Zweck der Variable
    beschreiben.
  - Variablen dürfen nicht mit einer Zahl beginnen.

- Dateinamen:
  - Verwenden Sie ebenfalls snake_case.
  - Namen sollten beschreiben, was das Skript tut oder wofür es gedacht
    ist.
  - Keine Sonderzeichen oder Leerzeichen in Dateinamen verwenden.
  - Modulnamen sollten nicht mit einer Zahl beginnen, wenn sie später
    importiert werden sollen
"""

# Das ist ein Zeilenkommentar
# Snake-Case: lowercase und mit Underscore
max_value = 3

# 0_a = 42  Syntax Error
# x = 2
# y = 34

print("Max Value ist", max_value, "tollö", sep=",")  # kommasepariert
print("Nächste Zeile")
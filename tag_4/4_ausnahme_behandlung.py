"""
Exception Handling in Python

try:
    ...
except ValueError:
    ...
except TypeError:
    ...
else:
    ...
finally:
    ...
"""

y = 0
try:
    x = 7 / y
except Exception as e:
    print(f"Fehler aufgefangen, das Fehlerobjekt {type(e)}")


y = 0
try:
    x = 7 / 0
except ArithmeticError as e:
    print(f"Fehler aufgefangen, das Fehlerobjekt {type(e)}")
except NameError as e:
    print(f"Fehler aufgefangen, das Fehlerobjekt {type(e)}")
finally:
    print("Hier könnte man Aufräumarbeiten machen")


# Aufgabe: Schreibe eine Fukntion is_float(value: str) -> bool:
# soll prüfen, ob ein Wert als float gecastet werden
# die Ausnahme muss spezifiert werden!
def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

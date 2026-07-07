"""
Ternary Operator
x = a < b ? 10 : 11

Python
x = 10 if a < b else 11


"""

a = 3
b = 4

# klassisch
if a < b:
    x = 10
else:
    x = 11

# als ternary
x = 10 if a < b else 11

# im f-String
print(f"{10 if a < b else 11}")

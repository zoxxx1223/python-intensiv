"""
List Comprehensions und Generator-Expressions
"""

import os
import sys
import psutil


pid = os.getpid()

process = psutil.Process(pid)  # aktueller Prozess
print("current memory befre:", process.memory_info().rss / 1024**2)  # MB

e = [(i, i**2) for i in range(10**6)]
print(len(e))
print("current memory after:", process.memory_info().rss / 1024**2)  # MB
e = None

# eine Generator-Expression braucht keinen Speicher
f = ((i, i**2) for i in range(10**6))
print("current memory generator:", process.memory_info().rss / 1024**2)  # MB
# print(f[20])
# print(next(f))
# print(next(f))

# Summe mit List-Comprehension
sum([i for i in range(109)])
# Summe ohne Klammern als Generator Expresseion
sum(i for i in range(109))

# for entry in f:
#     print(entry)

x = iter([1, 2])
print(x)

# ein Set-Iterator
values = {"1", "2", "3"}
for value in values:
    print(value)

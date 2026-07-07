"""
Performance messen: Lookup in set vs. Lookup in list
"""

from time import perf_counter
import string
import random

CHARS = string.ascii_letters
N = 10_000_000
werte = [random.choice(CHARS) for _ in range(N)]

chars_list = list(CHARS)
chars_set = set(CHARS)

# print("Let's start with benchmarking ....")
# start = perf_counter()
# for c in werte:
#     c in chars_list
# end = perf_counter()
# print(f"Listen-Lookup hat {end - start:.2f} Sekunden gedauert")

# start = perf_counter()
# for c in werte:
#     c in chars_set
# end = perf_counter()
# print(f"Set-Lookup hat {end - start:.2f} Sekunden gedauert")


x, y = 3, 5
assert x < y, "3 ist kleiner als 32"

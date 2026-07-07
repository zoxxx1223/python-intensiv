"""
zwei Dicts kombinieren
"""

food_1 = {"pizza": 2, "hamburger": 1, "snickers": 1}
food_2 = {"snickers": 2, "döner": 1}

# ab python 3.10
food_3 = food_1 | food_2
print(food_3)

# früher in dunklen Zeiten...
food_3 = {**food_1, **food_2}
print(food_3)

# Update
food_1.update({"mars": 32, "pizza": 42})
print(food_1)

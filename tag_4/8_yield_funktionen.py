values = [1, 2, 3, 4]


def filter_values(values: list) -> list:
    """Erzeugt neue Liste und gibt sie zruück"""
    new_values = []
    for value in values:
        if value > 2:
            new_values.append(value)

    return new_values


def filter_values_neu(values: list):
    for value in values:
        if value > 2:
            yield value  # hier wartet der loop


result = filter_values(values)
print(result)

result = filter_values_neu(values)
# print(list(result))
# print(next(result))
# print(next(result))
# print(next(result)) # StopIteration

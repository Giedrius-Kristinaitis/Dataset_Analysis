from collections import Counter
from math import floor
from math import ceil
from math import sqrt
from math import pow

"""
I do not care about the quality of this code, but it SHOULD be refactored, for example:
a new service responsible for calculations should take attribute data and perform calculations, thus decoupling
attribute class from the calculations

Performance SHOULD be improved too by saving calculation results and not re-doing them every time on the fly,
but fuck it, too much typing for something I don't care about

Plus, this code violates DRY principle

I'm not responsible for any brain damage this code might cause

Do not take this code as an example
"""

class Attribute:
    values = []

    def __init__(self, name: str) -> None:
        self.name = name

    def num_of_values(self) -> int:
        return len(self.values)

    def percent_of_missing_values(self) -> float:
        empty_values = 0

        for value in self.values:
            if not value:
                continue

            empty_values += 1

        return empty_values / len(self.values) * 100

    def cardinality(self) -> int:
        return len(Counter(self.values).keys())


class NumericAttribute(Attribute):

    def min_value(self) -> float:
        return min(filter(lambda x: x is not None, self.values))

    def max_value(self) -> float:
        return max(filter(lambda x: x is not None, self.values))

    def quartile(self, index: int) -> float:
        if index not in [1, 2, 3]:
            raise ValueError("Invalid quartile index, possible indexes: 1, 2, 3")

        values = list(filter(lambda x: x is not None, self.values))

        values.sort()

        index = len(values) * 0.25 * index

        if index % 1 != 0:
            return (values[floor(index)] + values[ceil(index)]) / 2
        else:
            return values[int(index)]

    def average(self) -> float:
        values = list(filter(lambda x: x is not None, self.values))

        return sum(values) / len(values)

    def standard_deviation(self) -> float:
        values = list(filter(lambda x: x is not None, self.values))

        values = list(map(lambda x: x * x, values))

        return sqrt(sum(values) / len(values) - pow(self.average(), 2))


class CategoricalAttribute(Attribute):

    def mode(self, index: int) -> str:
        if index != 1 or index != 2:
            raise ValueError("Invalid mode index, supported indexes: 1 and 2")

        counter = Counter(list(filter(lambda x: x is not None, self.values)))

        values = list(set(counter.values()))
        values.sort(reverse=True)

        max_value = values[len(values) - index]

        return list(counter.keys())[list(counter.values()).index(max_value)]

    def value_frequency(self, value: str) -> int:
        counter = Counter(list(filter(lambda x: x is not None, self.values)))

        return list(counter.keys())[list(counter.values()).index(max(list(counter.values())))]

    def frequency_percentage(self, frequency: int) -> float:
        return frequency / len(list(filter(lambda x: x is not None, self.values))) * 100

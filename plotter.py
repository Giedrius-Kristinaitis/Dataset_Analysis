from attributes import Attribute
from math import log
from matplotlib import pyplot

def plot_histograms(attributes: [Attribute]) -> None:
    for attribute in attributes:
        plot_histogram(attribute)

def plot_histogram(attribute: Attribute) -> None:
    values = attribute.get_filtered_values()

    bins = int(1 + 3.22 * log(len(values)))

    pyplot.xlabel(attribute.name)
    pyplot.hist(values, bins=bins)
    pyplot.show()

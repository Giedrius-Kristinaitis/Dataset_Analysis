from attributes import Attribute
from attributes import NumericAttribute
from math import log
from matplotlib import pyplot
from pandas import DataFrame
from relations import correlation

def plot_histograms(attributes: [Attribute]) -> None:
    for attribute in attributes:
        plot_histogram(attribute)

def plot_histogram(attribute: Attribute) -> None:
    values = attribute.get_filtered_values()

    bins = int(1 + 3.22 * log(len(values)))

    pyplot.xlabel(attribute.name)
    pyplot.hist(values, bins=bins)
    pyplot.show()

def plot_correlation_matrix(attributes: [NumericAttribute]) -> None:
    data = {}
    labels = []

    for a in attributes:
        data[a.name] = []
        labels.append(a.name)

        for b in attributes:
            corr = correlation(a, b)

            data[a.name].append(corr)

    data_frame = DataFrame(data, columns=labels)

    corr = data_frame.corr()
    corr.style.background_gradient(cmap='coolwarm')

    pyplot.figure(figsize=(10, 5))
    pyplot.matshow(corr, fignum=1, aspect="auto")
    pyplot.colorbar()
    pyplot.xticks(range(len(corr.columns)), corr.columns, fontsize=8)
    pyplot.yticks(range(len(corr.columns)), corr.columns)
    pyplot.savefig("matrix.png")

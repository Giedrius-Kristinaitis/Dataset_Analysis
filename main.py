from file_reader import read_file
from plotter import plot_histograms
from plotter import plot_correlation_matrix
from attributes import NumericAttribute
from relations import print_attribute_covariations_and_correlations
from plotter import plot_scatter_diagram
from plotter import plot_box_diagram
from attributes import print_categorical_attribute_info
from attributes import print_numeric_attribute_info

attribute_types = {
    "country": "categorical",
    "year": "numeric",
    "sex": "categorical",
    "age": "categorical",
    "suicides_no": "numeric",
    "population": "numeric",
    "suicides/100k pop": "numeric",
    "country-year": "categorical",
    "HDI for year": "numeric",
    "gdp_for_year ($)": "numeric",
    "gdp_per_capita ($)": "numeric",
    "generation": "categorical"
}

data = read_file("data.csv", attribute_types)

# step 1 and 2
print_numeric_attribute_info(data)

print('\n')

print_categorical_attribute_info(data)

# step 4
plot_histograms(data)

# step 5
for attribute in data:
    attribute.fill_missing_values()

    if isinstance(attribute, NumericAttribute):
        attribute.remove_outliers()

numeric_attributes = list(filter(lambda x: isinstance(x, NumericAttribute), data))

# step 7
print_attribute_covariations_and_correlations(numeric_attributes)
plot_correlation_matrix(numeric_attributes)

# step 6
plot_scatter_diagram(data[5], data[4])
plot_scatter_diagram(data[5], data[9])
plot_scatter_diagram(data[1], data[4])
plot_scatter_diagram(data[5], data[8])

plot_box_diagram(data[6], data[11])
plot_box_diagram(data[4], data[3])

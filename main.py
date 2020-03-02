from file_reader import read_file
from plotter import plot_histograms
from attributes import NumericAttribute
from relations import print_attribute_covariations_and_correlations

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

# step 4
# plot_histograms(data)

# step 5
for attribute in data:
    attribute.fill_missing_values()

numeric_attributes = list(filter(lambda x: isinstance(x, NumericAttribute), data))

# step 7
print_attribute_covariations_and_correlations(numeric_attributes)

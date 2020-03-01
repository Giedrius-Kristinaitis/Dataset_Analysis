from file_reader import read_file

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

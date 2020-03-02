from attributes import NumericAttribute

def covariation(a: NumericAttribute, b: NumericAttribute) -> float:
    avg_a = a.average()
    avg_b = b.average()
    length = a.num_of_values()
    total_sum = 0

    for i in range(length):
        total_sum += (a.values[i] - avg_a) * (b.values[i] - avg_b)

    return (1 / (length - 1)) * total_sum

def correlation(a: NumericAttribute, b: NumericAttribute) -> float:
    return covariation(a, b) / (a.standard_deviation() * b.standard_deviation())

def print_attribute_covariations_and_correlations(attributes: [NumericAttribute]) -> None:
    label = '{:40} {:>25} {:>25}'.format('Atributai', 'Kovariacija', 'Koreliacija')

    print(label)

    for a in attributes:
        for b in attributes:
            if a == b:
                continue

            cov = covariation(a, b)
            corr = correlation(a, b)

            line_output = '{:40} {:>25} {:>25}'.format(a.name + ", " + b.name, round(cov, 4), round(corr, 4))

            print(line_output)

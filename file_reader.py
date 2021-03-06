from attributes import NumericAttribute
from attributes import CategoricalAttribute
from typing import Dict
from itertools import islice

def read_file(file_name: str, attribute_types: Dict[str, str]) -> list:
    lines = read_file_lines(file_name)

    data = initialize_attributes(lines[0], attribute_types)

    for line in islice(lines, 1, None):
        parts = line.split('\t')

        for index, part in enumerate(parts):
            value = part.strip()

            if not value:
                data[index].add_value(None)
            elif is_int(value):
                data[index].add_value(int(value))
            elif is_float(value):
                data[index].add_value(float(value))
            else:
                data[index].add_value(value)

    return data

def initialize_attributes(name_line: str, attribute_types: Dict[str, str]) -> list:
    data = []

    for part in name_line.split('\t'):
        attribute_name = part.strip()

        if attribute_name in attribute_types:
            attribute_type = attribute_types[attribute_name]

            if attribute_type == 'numeric':
                data.append(NumericAttribute(attribute_name))
            elif attribute_type == 'categorical':
                data.append(CategoricalAttribute(attribute_name))
            else:
                raise ValueError("Invalid attribute type: " + attribute_type)
        else:
            raise RuntimeError("File contains non-existent attribute name: " + attribute_name)

    return data

def read_file_lines(file_name: str) -> list:
    file = open(file_name, 'r', encoding="utf-8-sig")

    lines = file.readlines()

    file.close()

    return lines

def is_int(value: str) -> bool:
    try:
        int(value)
    except ValueError:
        return False

    return True

def is_float(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False

    return True

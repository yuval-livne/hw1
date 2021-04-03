import pandas
import math

def sum(values):
    sum = 0
    for index in range(len(values)):
        sum += values[index]
    return sum

def mean(values):
    return float(sum(values)) / len(values)

def median(values):
    sorted_values = sorted(values)
    if len(sorted_values) % 2 == 0:
        return (sorted_values[int(len(sorted_values) / 2 + 1)])
    return sorted_values[math.ceil(len(sorted_values) / 2)]

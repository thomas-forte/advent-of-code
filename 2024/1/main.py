"""
Advent of Code
year: 2024
part: 1
"""

DELIMITER = "   "


def part_1(input_lines):
    """
    Take a list of space delimited integers and return the sum of the absolute differences between the first and second
    after sorting the list from least to greatest.
    """

    converted_list = [[int(y) for y in x.split(DELIMITER)] for x in input_lines]

    list_a = sorted([x[0] for x in converted_list])
    list_b = sorted([x[1] for x in converted_list])

    list_distances = [abs(list_a[i] - list_b[i]) for i in range(len(list_a))]

    sum_distances = sum(list_distances)

    return sum_distances


def part_2(input_lines):
    """
    Take the same list of space delimited integers, iterating through the first list and counting the number of times
    each number appears in the second list, multiplying the current number by how many times it appears in the second
    list. Sum all those values and return the result.
    """
    converted_list = [[int(y) for y in x.split(DELIMITER)] for x in input_lines]

    list_a = [x[0] for x in converted_list]
    list_b = [x[1] for x in converted_list]

    similarity_score = 0
    for i in list_a:
        similarity_score += list_b.count(i) * i

    return similarity_score

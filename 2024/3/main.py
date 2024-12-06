"""
Advent of Code
year: 2024
part: 3
"""

import re


def part_1(input_lines):
    """
    Take all the lines of scrambled input looking for the pattern mul(X,Y). Sum up all those products.
    The X/Y values are always 1-3 digits long.
    """

    mul_search = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")

    merged_data = "".join([line.strip() for line in input_lines])

    results = mul_search.findall(merged_data)

    sum_of_multiples = sum(int(x) * int(y) for x, y in results)

    return sum_of_multiples


def part_2(input_lines):
    """
    Same as the first part except also process the do() and don't() functions.
    """

    merged_data = "".join([line.strip() for line in input_lines])

    dirty_processing = [segment.split("don't()")[0] for segment in merged_data.split("do()")]

    sum_of_multiples = part_1(["".join(dirty_processing)])

    return sum_of_multiples

"""
Advent of Code
year: 2023
part: 1
"""


def part_1(input_lines):
    """
    The newly-improved calibration document consists of lines of text; each line originally contained a specific
    calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining
    the first digit and the last digit (in that order) to form a single two-digit number.
    """
    calibration_sum = 0

    for line in input_lines:
        filtered_line = [c for c in line if c.isdecimal()]
        calibration_sum += int(filtered_line[0] + filtered_line[-1])

    return calibration_sum


SPELLED_NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def insert_numbers(line):
    for num, name in enumerate(SPELLED_NUMBERS):
        line = line.replace(name, f"{name}{num+1}{name}")
    return line


def part_2(input_lines):
    """
    Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one,
    two, three, four, five, six, seven, eight, and nine also count as valid "digits".
    """
    calibration_sum = 0

    for line in input_lines:
        filtered_line = [c for c in insert_numbers(line) if c.isdecimal()]
        calibration_sum += int(filtered_line[0] + filtered_line[-1])

    return calibration_sum

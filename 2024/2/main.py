"""
Advent of Code
year: 2024
part: 2
"""

DELIMITER = " "
SAFE_LEVEL_CHANGE = 3


def part_1(input_lines):
    """
    Take a list of space delimited integers they are of different lengths representing a 2d list. Count the rows that
    are consistently increasing or decreasing by the safe level change. Return the number of rows that are safe.
    Repeated numbers are not considered increasing or decreasing.
    """

    converted_list = [[int(y) for y in x.split(DELIMITER)] for x in input_lines]

    safe_reports = 0

    for report in converted_list:
        is_safe = True
        is_increasing = None

        for i, level in enumerate(report):

            # skip the first level
            # set direction from second level
            if i == 0:
                continue
            elif i == 1:
                is_increasing = level > report[i - 1]

            # if changed from increasing to decreasing or vice versa, break and dont count
            if is_increasing and level <= report[i - 1]:
                is_safe = False
                break
            elif not is_increasing and level >= report[i - 1]:
                is_safe = False
                break

            # if change is greater than safe level, break and dont count
            if abs(level - report[i - 1]) > SAFE_LEVEL_CHANGE:
                is_safe = False
                break

        if is_safe:
            safe_reports += 1

    return safe_reports


def part_2(input_lines):
    """
    Same as before but if a row is not safe, start removing a single level to see if it becomes safe. If it does,
    count that bad boy.
    """

    converted_list = [[int(y) for y in x.split(DELIMITER)] for x in input_lines]

    safe_reports = 0

    for report in converted_list:
        violations = report_processing(report)

        if len(violations) == 0:
            safe_reports += 1
        else:
            for i in range(len(report)):
                edited_report = report.copy()
                edited_report.pop(i)
                if len(report_processing(edited_report)) == 0:
                    safe_reports += 1
                    break

    return safe_reports


def report_processing(report, is_increasing=None):
    violations = []

    for i, level in enumerate(report):

        # skip the first level
        # set direction from second level
        if i == 0:
            continue
        elif i == 1:
            is_increasing = level > report[i - 1]

        # if changed from increasing to decreasing or vice versa, break and dont count
        if is_increasing and level <= report[i - 1]:
            violations.append(i)
            break
        elif not is_increasing and level >= report[i - 1]:
            violations.append(i)
            break

        # if change is greater than safe level, break and dont count
        if abs(level - report[i - 1]) > SAFE_LEVEL_CHANGE:
            violations.append(i)
            break

    return violations

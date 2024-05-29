"""
Advent of Code
year: 2023
part: 3
"""

import re

pattern = re.compile(r"[^\.]")


def part_1(input_lines):
    """
    The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of
    numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally,
    is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
    """
    part_number_sum = 0

    line_index = 0

    for line in input_lines:
        current_part = ""
        count_current_part = False
        # previous_adjacent = False

        char_index = 0

        print(f"Current line: {line}", end="")

        for c in line:
            # print(f"{c}", end="")

            if c.isdecimal():
                current_part += c

                if not count_current_part:
                    # top check
                    if line_index > 0 and pattern.search(input_lines[line_index - 1][char_index]):
                        count_current_part = True

                    # bottom check
                    if line_index + 1 < len(input_lines) and pattern.search(input_lines[line_index + 1][char_index]):
                        count_current_part = True

            else:
                # end of part
                if current_part:
                    if not count_current_part:
                        # this check
                        if pattern.search(input_lines[line_index][char_index]):
                            count_current_part = True

                        # top check
                        if line_index > 0 and pattern.search(input_lines[line_index - 1][char_index]):
                            count_current_part = True

                        # bottom check
                        if line_index + 1 < len(input_lines) and pattern.search(
                            input_lines[line_index + 1][char_index]
                        ):
                            count_current_part = True

                    if count_current_part:
                        print(f" (++{int(current_part)}) ", end="")
                        part_number_sum += int(current_part)

                    current_part = ""

                # possible start of part
                else:
                    count_current_part = False

                    # this check
                    if pattern.search(input_lines[line_index][char_index]):
                        count_current_part = True

                    # top check
                    if line_index > 0 and pattern.search(input_lines[line_index - 1][char_index]):
                        count_current_part = True

                    # bottom check
                    if line_index + 1 < len(input_lines) and pattern.search(input_lines[line_index + 1][char_index]):
                        count_current_part = True

            # if count_current_part:
            #     print("*", end="")

            # if char_index + 1 < len(line):
            #     print(" -> ", end="")

            char_index += 1

        print()
        line_index += 1

    return part_number_sum


def part_2(input_lines):
    """
    Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one,
    two, three, four, five, six, seven, eight, and nine also count as valid "digits".
    """
    lines = [line.rstrip() for line in input_lines]

    res = 0

    m = len(lines)
    n = len(lines[0])

    counts = [[0] * n for _ in range(m)]
    prods = [[1] * n for _ in range(m)]

    for i in range(m):
        j = 0
        while j < n:
            ctr = 1
            while j < n - 1 and lines[i][j].isdigit() == lines[i][j + 1].isdigit():
                ctr += 1
                j += 1
            if lines[i][j].isdigit():
                num = int(lines[i][j - ctr + 1 : j + 1])
                valid = False
                for x in range(i - 1, i + 2):
                    for y in range(j - ctr, j + 2):
                        if 0 <= x < m and 0 <= y < n and lines[x][y] != "." and not lines[x][y].isdigit():
                            valid = True
                        if 0 <= x < m and 0 <= y < n and lines[x][y] == "*":
                            counts[x][y] += 1
                            prods[x][y] *= num
                            break
                if valid:
                    res += num
            j += 1

    ratios = 0

    for i in range(m):
        for j in range(n):
            if counts[i][j] == 2:
                ratios += prods[i][j]

    print(res)
    print(ratios)

    return 0

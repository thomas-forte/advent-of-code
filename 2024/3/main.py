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

    sum_of_multiples = 0
    mul_search = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")

    merged_data = "".join([line.strip() for line in input_lines])

    results = mul_search.findall(merged_data)

    sum_of_multiples += sum(int(x) * int(y) for x, y in results)

    return sum_of_multiples


# def part_2(input_lines):
#     """
#     wtf
#     """

#     sum_of_multiples = 0

#     merged_data = "".join([line.strip() for line in input_lines])

#     dirty_processing = [segment.split("don't()")[0] for segment in merged_data.split("do()")]

#     sum_of_multiples += part_1(["".join(dirty_processing)])

#     return sum_of_multiples


# 82868252 WRONG


# Really annoying cursor parsing

# import math


# def part_2(input_lines):
#     """ """
#     sum_of_multiples = 0

#     for line in input_lines:
#         cursor = 0
#         do = True

#         # print(line)
#         # for i in range(len(line)):
#         #     print((i + 1) % 10, end="")
#         # print()

#         while cursor < len(line):
#             next_mul = line.find("mul(", cursor)
#             next_do = line.find("do()", cursor)
#             next_dont = line.find("don't()", cursor)

#             # print(f"\n\nDBG: {line[cursor:][:50]}")

#             if next_mul == -1:
#                 break

#             if next_do == -1:
#                 next_do = math.inf

#             if next_dont == -1:
#                 next_dont = math.inf

#             if next_mul < next_do and next_mul < next_dont:
#                 cursor = next_mul + 4

#                 mul_end = line.find(")", next_mul + 4)

#                 segment = line[cursor:mul_end]

#                 # print(f"MUL '{segment}'", end=" ")

#                 if len(segment) <= 7 and "," in segment:
#                     # print("valid", end=" ")
#                     print(segment) if " " in segment else None
#                     cursor = mul_end + 1

#                     if do:
#                         # print("do", end=" ")
#                         a, b = map(int, segment.split(","))
#                         # print(f"MUL '{segment}' -> {a} * {b} = {a * b}")
#                         sum_of_multiples += a * b

#                     else:
#                         pass
#                         # print("dt")
#                 else:
#                     print(f"MUL '{segment}'", end=" ")
#                     print("fake")

#             else:
#                 if next_do < next_dont:
#                     do = True
#                     # print(f"DO {line[next_do:next_do + 4]}")
#                     cursor = next_do + 4
#                 else:
#                     do = False
#                     # print(f"DT {line[next_dont:next_dont + 7]}")
#                     cursor = next_dont + 7

#     return sum_of_multiples


# 88125394 WRONG

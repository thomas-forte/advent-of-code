"""
Advent of Code
year: 2023
part: 1
"""


def part_1(input_lines):
    """
    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes,
    and 14 blue cubes. What is the sum of the IDs of those games?
    """
    possible_sum = 0

    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for line in input_lines:
        header_data, game_data = line.split(": ")
        game_id_number = int(header_data[4:])

        inconceivable = False

        picks = game_data.split("; ")
        for pick in picks:
            pick_data = pick.split(", ")
            for pick_datum in pick_data:
                count, color = pick_datum.split(" ")
                if int(count) > bag[color]:
                    inconceivable = True
                    break
            if inconceivable:
                break

        if not inconceivable:
            possible_sum += game_id_number

    return possible_sum


def part_2(input_lines):

    return 0

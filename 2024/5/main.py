"""
Advent of Code
year: 2024
part: 5
"""


def part_1(input_lines):
    """
    Find a list with an a valid order defined by the rules. If valid take the middle element and sum it up.
    """

    rules = {}

    updates = []

    process_updates = False

    # parse input
    for line in input_lines:
        if "" == line:
            process_updates = True
            continue

        if process_updates:
            updates.append(line.split(","))
        else:
            line_split = line.split("|")
            if line_split[0] in rules:
                rules[line_split[0]].append(line_split[1])
            else:
                rules[line_split[0]] = [line_split[1]]

    valid_update_sum = 0

    for update in updates:

        update_invalid = False

        for i in range(len(update)):

            flipped_i = len(update) - 1 - i
            current_page = update[flipped_i]

            if current_page in rules:
                if any([rule in update[:flipped_i] for rule in rules[current_page]]):
                    update_invalid = True

        if not update_invalid:
            valid_update_sum += int(update[(len(update) - 1) // 2])

    return valid_update_sum


def part_2(input_lines):
    """ """

    rules = {}

    updates = []

    process_updates = False

    # parse input
    for line in input_lines:
        if "" == line:
            process_updates = True
            continue

        if process_updates:
            updates.append(line.split(","))
        else:
            line_split = line.split("|")
            if line_split[0] in rules:
                rules[line_split[0]].append(line_split[1])
            else:
                rules[line_split[0]] = [line_split[1]]

    invalid_entries = []

    # test entries
    for update in updates:

        update_invalid = False
        rule_results = {}

        for i in range(len(update)):

            flipped_i = len(update) - 1 - i
            current_page = update[flipped_i]

            if current_page in rules:
                rule_test_list = [rule in update[:flipped_i] for rule in rules[current_page]]
                if any(rule_test_list):
                    rule_results[current_page] = rule_test_list
                    update_invalid = True

        if update_invalid:
            invalid_entries.append(
                [
                    update,
                    rule_results,
                ]
            )

    # fix entries
    for invalid_entry in invalid_entries:

        if len(invalid_entry[1]) == 1:
            remove = invalid_entry[1].popitem()[0]
            print()
            print()
            print("the list", invalid_entry[0])
            print("item to remove", remove)
            print("item in list", remove in invalid_entry[0])
            print("list.index()", invalid_entries[0].index(remove))
            print()
            print()
            print()
            problem = invalid_entries[0].pop(invalid_entries[0].index(remove))
            print(problem)

    print(invalid_entries)

    return len(invalid_entries)

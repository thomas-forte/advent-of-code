def part_1(input_lines):
    calibration_sum_1 = 0

    for line in input_lines:
        filtered_line = [c for c in line if c.isdecimal()]
        calibration_sum_1 += int(filtered_line[0] + filtered_line[-1])

    return calibration_sum_1


def part_2(input_lines):
    return 0

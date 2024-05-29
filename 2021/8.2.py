with open("8.txt") as f:
    data = f.read().splitlines()

count = 0
for line in data:
    unique_patterns = line.split(" | ")[0].split(" ")
    output_values = line.split(" | ")[1].split(" ")

    unique_pattern_lengths = list(map(lambda x: len(x), unique_patterns))
    decoded_patterns = [""] * 10
    decoded_patterns[1] = unique_patterns[unique_pattern_lengths.index(2)]
    decoded_patterns[4] = unique_patterns[unique_pattern_lengths.index(4)]
    decoded_patterns[7] = unique_patterns[unique_pattern_lengths.index(3)]
    decoded_patterns[8] = unique_patterns[unique_pattern_lengths.index(7)]
    eight_minus_four = decoded_patterns[8]
    for s in decoded_patterns[4]:
        eight_minus_four = eight_minus_four.replace(s, "")

    for i, unique_pattern_length in enumerate(unique_pattern_lengths):
        if unique_pattern_length == 6:
            if decoded_patterns[1][0] in unique_patterns[i] and decoded_patterns[1][1] in unique_patterns[i]:
                if (
                    decoded_patterns[4][0] in unique_patterns[i]
                    and decoded_patterns[4][1] in unique_patterns[i]
                    and decoded_patterns[4][2] in unique_patterns[i]
                    and decoded_patterns[4][3] in unique_patterns[i]
                ):
                    decoded_patterns[9] = unique_patterns[i]
                else:
                    decoded_patterns[0] = unique_patterns[i]
            else:
                decoded_patterns[6] = unique_patterns[i]

        elif unique_pattern_length == 5:
            if decoded_patterns[1][0] in unique_patterns[i] and decoded_patterns[1][1] in unique_patterns[i]:
                decoded_patterns[3] = unique_patterns[i]
            else:
                if (
                    eight_minus_four[0] in unique_patterns[i]
                    and eight_minus_four[1] in unique_patterns[i]
                    and eight_minus_four[2] in unique_patterns[i]
                ):
                    decoded_patterns[2] = unique_patterns[i]
                else:
                    decoded_patterns[5] = unique_patterns[i]

    for x in range(len(decoded_patterns)):
        decoded_patterns[x] = set(decoded_patterns[x])

    decoded_value = ""
    for value in output_values:
        value = set(value)
        for i, pattern in enumerate(decoded_patterns):
            if value == pattern:
                decoded_value = decoded_value + str(i)

    count = count + int(decoded_value)

print(f"Count the sum of the decoded output panel: {count}")

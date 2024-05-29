gamma = ""
epsilon = ""


def process_command(command):
    command = command.strip().split(" ")
    return [command[0], int(command[1])]


with open("3.txt") as f:
    lines = f.readlines()


number_length = len(lines[0].strip())
total_numbers = len(lines)

for x in range(number_length):
    zero_count = 0
    for line in lines:
        if line[x] == "0":
            zero_count += 1
    if zero_count / total_numbers > 0.5:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_number = int(gamma, 2)
epsilon_number = int(epsilon, 2)
print(f"gamma {gamma} => {gamma_number}")
print(f"epsilon {epsilon} => {epsilon_number}")
print(f"power consumption {gamma_number * epsilon_number}")

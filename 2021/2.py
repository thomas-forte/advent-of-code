x = 0
y = 0

def process_command(command):
    command = command.strip().split(' ')
    return [command[0], int(command[1])]

with open('2.txt') as f:
    lines = f.readlines()

commands = list(map(process_command, lines))

for command in commands:
    if command[0] == 'up':
        y = y - command[1]
    elif command[0] == 'down':
        y = y + command[1]
    elif command[0] == 'forward':
        x = x + command[1]


print(f'X: {x}')
print(f'Y: {y}')
print(f'X * Y: {x * y}')

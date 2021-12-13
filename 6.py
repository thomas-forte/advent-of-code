def process_day(fishies):
    born_again_fishies = fishies[0]

    new_fishies = {
        0: fishies[1],
        1: fishies[2],
        2: fishies[3],
        3: fishies[4],
        4: fishies[5],
        5: fishies[6],
        6: fishies[7] + born_again_fishies,
        7: fishies[8],
        8: born_again_fishies,
    }

    return new_fishies

with open('6.txt') as f:
    data = f.read().splitlines()

fishies = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

fish_data = data[0].split(',')

for fish in fish_data:
    fish = int(fish)
    fishies[fish] = fishies[fish] + 1

for day in range(80):
    fishies = process_day(fishies)

print(f'After 80 days the amount of fish is: {sum(fishies.values())}')

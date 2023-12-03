with open('8.txt') as f:
    data = f.read().splitlines()

count = 0
for line in data:
    output_values = line.split(' | ')[1].split(' ')
    output_lengths = list(map(lambda x: len(x), output_values))
    count_1s = output_lengths.count(2)
    count_4s = output_lengths.count(4)
    count_7s = output_lengths.count(3)
    count_8s = output_lengths.count(7)
    count = count + count_1s + count_4s + count_7s + count_8s

print(f'Count the number of times 1, 4, 7, 8 appear on the output panel: {count}')

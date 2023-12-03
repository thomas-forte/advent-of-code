# crappy pre processing solution but was way quicker to formulate
with open('1.txt') as f:
    lines = f.readlines()

numbers = list(map(int, lines))

group_dex = 0
groups = []
for number in numbers:
    if len(groups) == group_dex + 1:
        groups[group_dex].append(number)
    else:
        groups.append([])
        groups[group_dex].append(number)

    if group_dex - 1 >= 0:
            groups[group_dex - 1].append(number)
    if group_dex - 2 >= 0:
        groups[group_dex - 2].append(number)

    group_dex += 1

group_name = 'A'
prev = None
increases = 0

for group in groups:
    if len(group) == 3:
        group_sum = sum(group)
        if prev is None:
            print(f'{group_name}: {group_sum} (N/A - no previous sum)')
        elif group_sum == prev:
            print(f'{group_name}: {group_sum} (no change)')
        elif group_sum > prev:
            increases += 1
            print(f'{group_name}: {group_sum} (increased)')
        else:
            print(f'{group_name}: {group_sum} (decreased)')

        prev = group_sum
        group_name = chr(ord(group_name) + 1)

print(f'There were {increases} sums that are larger than the previous sum.')

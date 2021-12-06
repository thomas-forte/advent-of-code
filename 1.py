with open('1.txt') as f:
    lines = f.readlines()

numbers = list(map(int, lines))

prev = None
increases = 0

print(numbers)

for number in numbers:
    if prev is None:
        print(f'{number} (N/A - no previous measurement)')
    elif number > prev:
        increases += 1
        print(f'{number} (increased)')
    else:
        print(f'{number} (decreased)')

    prev = number

print(f'There were {increases} measurements that are larger than the previous measurement.')

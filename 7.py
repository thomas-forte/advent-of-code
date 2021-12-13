def calculate_fuel_cost(position_data, goal_position):
    cost = 0
    for position in position_data:
        if position != goal_position:
            if position > goal_position:
                cost = cost + (position - goal_position)
            else:
                cost = cost + (goal_position - position)
    return cost

with open('7.txt') as f:
    data = f.read().splitlines()

position_data = list(map(int, data[0].split(',')))

max_position = max(position_data)

fuel_cost = []
for i in range(max_position):
    fuel_cost.append(calculate_fuel_cost(position_data, i + 1))

print(f'The cheapest fuel cost is: {min(fuel_cost)}')

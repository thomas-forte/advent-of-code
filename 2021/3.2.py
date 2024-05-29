def filter_by_index(data, index, high_mode=True):
    total_count = 0
    zero_count = 0
    for dattum in data:
        total_count = total_count + 1
        if dattum[index] == "0":
            zero_count = zero_count + 1

    if high_mode:
        if zero_count / total_count > 0.5:
            filter_value = "0"
        else:
            filter_value = "1"
    else:
        if zero_count / total_count <= 0.5:
            filter_value = "0"
        else:
            filter_value = "1"

    return list(filter(lambda x: x[index] == filter_value, data))


# read data
with open("3.txt") as f:
    data = f.read().splitlines()

# get binary length
number_length = len(data[0])

index = 0
oxygen_generator_ratings = data
while len(oxygen_generator_ratings) > 1 and index < number_length:
    oxygen_generator_ratings = filter_by_index(oxygen_generator_ratings, index)
    index = index + 1

oxygen_generator_rating = oxygen_generator_ratings[0]

index = 0
co2_scrubber_ratings = data
while len(co2_scrubber_ratings) > 1 and index < number_length:
    co2_scrubber_ratings = filter_by_index(co2_scrubber_ratings, index, high_mode=False)
    index = index + 1
co2_scrubber_rating = co2_scrubber_ratings[0]

oxygen_generator_rating_number = int(oxygen_generator_rating, 2)
co2_scrubber_rating_number = int(co2_scrubber_rating, 2)
print(f"oxygen generator rating {oxygen_generator_rating} => {oxygen_generator_rating_number}")
print(f"co2 scrubber rating {co2_scrubber_rating} => {co2_scrubber_rating_number}")
print(f"life support rating {oxygen_generator_rating_number * co2_scrubber_rating_number}")

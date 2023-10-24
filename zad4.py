dresses = [int(x) for x in input("Enter dresses with spaces: ").split(" ")]
rack_capacity = int(input("Enter rack capacity: "))

def count_racks(dresses, capacity):
    rack_count = 0
    current_rack_capacity = 0

    for dress in dresses:
        dress_weight = int(dress)

        if current_rack_capacity + dress_weight <= capacity:
            current_rack_capacity += dress_weight
        else:
            rack_count += 1
            current_rack_capacity = dress_weight

    if current_rack_capacity > 0:
        rack_count += 1

    return rack_count


result = count_racks(dresses, rack_capacity)
print(result)

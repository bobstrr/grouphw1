food_for_the_day = int(input("food for the day: "))
orders = [int(x) for x in input("enter orders with spaces: ").split(" ")]
total_orders = 0
current_number = 0
max_number = 0

for order in orders:
    total_orders += order
    current_number = order
    if current_number > max_number:
        max_number = current_number

for order in orders:
    if order <= food_for_the_day:
        food_for_the_day -= order
    else:
        remaining_orders = orders[orders.index(order):]
        print(f"Biggest order: {max_number}")
        print(f"Remaining orders: {remaining_orders}")
        break
else:
    print(f"Biggest order: {max_number}")
    print("Orders complete")

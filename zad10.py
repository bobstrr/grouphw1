nuggets_in_plate = int(input("Enter the amount of nuggets at the start: ")) 
queue = []

while True:
    #print(queue, "Queue")
    command = input("Enter names of people, Start, refill or END: ")
    queue.append(command)

    if command == "Start":
        queue.pop(-1)
        for name in queue.copy():
            wanted_nuggets = int(input("Enter wanted nuggets: "))
            if wanted_nuggets <= nuggets_in_plate:
                print(f"{str(name)} takes {wanted_nuggets}")
                queue.pop(0)
                nuggets_in_plate = nuggets_in_plate - wanted_nuggets
                continue

            elif wanted_nuggets > nuggets_in_plate:
                print(f"{name} must wait!")
                continue

    if command.startswith("refill"):
        nuggets = int(command[-1])
        nuggets_in_plate = nuggets_in_plate + nuggets
        queue.pop(-1)
        for name in queue.copy():
            wanted_nuggets = int(input("Enter wanted nuggets: "))
            if wanted_nuggets <= nuggets_in_plate:
                print(f"{str(name)} takes {wanted_nuggets}")
                queue.pop(0)
                nuggets_in_plate = nuggets_in_plate - wanted_nuggets
                continue

            elif wanted_nuggets > nuggets_in_plate:
                print(f"{name} must wait!")
                continue


    if command == "END":
        print(f"{nuggets_in_plate} left in plate")
        break
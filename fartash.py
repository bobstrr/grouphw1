initial_bites = int(input())
queue = []
while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill"):
        _, bites_to_add = command.split()
        bites_to_add = int(bites_to_add)
        initial_bites += bites_to_add
    else:
        bites_needed = int(command)
        if queue:
            person_name = queue[0]
            if bites_needed <= initial_bites:
                print(f"{person_name} takes {bites_needed} bites")
                initial_bites -= bites_needed
                queue.pop(0)
            else:
                print(f"{person_name} must wait")
                queue.pop(0)

print(f"Leftover bites: {initial_bites}")
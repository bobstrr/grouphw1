queue = []

while True:
    command = input()

    if command == "PAID":
        while queue:
            print(queue.pop(0))
    else:
        queue.append(command)
    
    

    
    if command == "END":
        remaining = len(queue)
        print(remaining - 1)
        break

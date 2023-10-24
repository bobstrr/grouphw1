names = [str(x) for x in input("Enter names with spaces: ").split(" ")]
throws_for_death = int(input("Enter an amount of throws for the hot potato to remove a player: "))

circle = names.copy()
while len(circle) > 1:
    for i in range(throws_for_death - 1):
        circle.append(circle.pop(0))
    removed_child = circle.pop(0)
    print(f"Removed {removed_child}")

winner = circle[0]
print(f"The Winner is {winner}")

# Sample Input:
# 4
# север 10
# запад 20
# юг 30
# восток 40

# Sample Output:
# 20 -20

num_steps = int(input())
steps = []
for _ in range(num_steps):
    direction, distance = input().split()
    steps.append((direction, int(distance)))

x, y = 0, 0

for direction, distance in steps:
    if direction == "север":
        y += distance
    elif direction == "юг":
        y -= distance
    elif direction == "восток":
        x += distance
    elif direction == "запад":
        x -= distance

print(x, y)

sum_square = []
s = 1
a = []
while s != 0:
    a.append(int(input()))
    s = sum(a)

for i in a:
    sum_square.append(i**2)

print(sum(sum_square))

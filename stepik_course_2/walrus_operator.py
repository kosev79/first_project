# s = 0
# while (d := int(input())) != -1:
#     s += d

# print(s)

# _______

n = 10
lst = [b for x in range(n) if (b := x * x) < n]
print(lst)

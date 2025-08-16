# Выведите таблицу размером n x n
#  заполненную числами от 1 до n*2 по спирали
n = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]
value = 1
max_index = n
min_index = 0

while value <= n**2:
    for j in range(min_index, max_index):
        matrix[min_index][j] = value
        value += 1
    min_index += 1
    for i in range(min_index, max_index):
        matrix[i][max_index - 1] = value
        value += 1
    max_index -= 1
    for j in range(max_index - 1, min_index - 1, -1):
        matrix[max_index][j] = value
        value += 1
    for i in range(max_index, min_index - 1, -1):
        matrix[i][min_index - 1] = value
        value += 1

for row in matrix:
    print(" ".join(map(str, row)))

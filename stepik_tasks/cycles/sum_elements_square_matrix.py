# на вход подается прямоугольная матрица произвольного размера построчно
# пок не напишем в косоли слово "end"
# на выходе выводится матрица того же размера, в ячейках значения
# суммы четырех соседних чисел для каждого элемента первоначальной матрицы
matrix = []

while True:
    line = input().strip()
    if line.lower() == "end":
        break
    row = list(map(int, line.split()))
    matrix.append(row)

if not matrix:
    print("Матрица пуста!")
else:
    cols = len(matrix[0])
    is_rectangular = all(len(row) == cols for row in matrix)

    if not is_rectangular:
        print("Матрица не прямоугольная!")
    else:
        rows = len(matrix)
        cols = len(matrix[0])

        sum_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sum_matrix[i][j] = (
                    matrix[(i + 1) % rows][j]  # снизу
                    + matrix[i - 1][j]  # сверху
                    + matrix[i][(j + 1) % cols]  # справа
                    + matrix[i][j - 1]  # слева
                )

        for row in sum_matrix:
            print(" ".join(map(str, row)))

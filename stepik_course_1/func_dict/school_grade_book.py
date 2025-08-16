# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
# где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает исходный файл с подобной структурой
# и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом.
# Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам
# и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.
# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику
# и одной строкой со средними оценками по трём предметам.

path = r"C:\Git_repository\first_project\stepik_tasks\func_dict\dataset_3363_42.txt"

grade_book = []
average_student_grade = []

with open(path, "r") as file:
    for line in file:
        grade_book.append(line.strip().split(";"))
        # parts = line.strip().split(";")
        # student_data = [parts[0]]  # сохраняем имя студента
        # grades = list(map(int, parts[1:]))  # преобразуем оценки в int
        # student_data.extend(grades)
        # grade_book.append(student_data)

num_subjects = len(grade_book[0]) - 1 if grade_book else 0
average_grade_subject = [0] * num_subjects

for item in range(len(grade_book)):
    sum = 0
    index = 0
    for value in range(len(grade_book[item])):
        if grade_book[item][value].isdigit():
            index += 1
            grade_book[item][value] = int(grade_book[item][value])
            sum += grade_book[item][value]
            average_grade_subject[value - 1] += grade_book[item][value]
    average_student_grade.append(sum / index)

    # for student in grade_book:
    # grades = student[1:]  # пропускаем имя студента
    # average_student_grade.append(sum(grades) / len(grades))
    # for i in range(num_subjects):
    #     average_grade_subject[i] += grades[i]

average_grade_subject = [x / len(grade_book) for x in average_grade_subject]

with open("C:\\Git_repository\\first_project\\stepik_tasks\\task_resh.txt", "w") as ouf:
    for element in average_student_grade:
        ouf.write(f"{element}\n")
    for digit in average_grade_subject:
        ouf.write(f"{digit} ")
    # for avg in average_student_grade:
    #   ouf.write(f"{avg}\n")
    # ouf.write(" ".join(map(str, average_grade_subject)))

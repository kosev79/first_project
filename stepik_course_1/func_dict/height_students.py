"""Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает
для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов,
а в качестве роста используется натуральное число,
но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса
(для классов с первого по одиннадцатый). Если про какой-то класс нет информации,
необходимо вывести напротив него прочерк.
В качестве ответа прикрепите файл с полученными данными о среднем росте."""

path = r"C:\Git_repository\first_project\stepik_tasks\func_dict\dataset_3380_5.txt"
table_result = {x: "-" for x in range(1, 12)}
school = []
with open(path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        num_class, person, height = line.split("\t")
        num_class, height = int(num_class), float(height)

        if table_result[num_class] == "-":
            table_result[num_class] = [height]
        else:
            table_result[num_class] = table_result[num_class] + [height]

with open(
    "C:\\Git_repository\\first_project\\stepik_tasks\\func_dict\\solution.txt", "w"
) as file:
    for key in table_result.keys():
        if table_result[key] != "-":
            table_result[key] = sum(table_result[key]) / len(table_result[key])
        file.write(f"{key}  {table_result[key]}\n")

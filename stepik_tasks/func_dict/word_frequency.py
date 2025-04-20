# Напишите программу, которая считывает текст из файла
# в файле может быть больше одной строки
# выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое
path = r"C:\Git_repository\first_project\stepik_tasks\dataset_3363_3 (2).txt"
my_string = ""
with open(path, "r") as inf:
    for line in inf:
        my_string += line.lower().strip() + " "

my_string = my_string.split()

my_dict = {word: my_string.count(word) for word in my_string}

sort_list = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))

print(sort_list)

# На вход программе первой строкой передаётся количество  d известных нам слов, после чего на
# d строках указываются эти слова. Затем передаётся количество  l строк текста для проверки,
# после чего  l строк текста.
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

# Sample Input:
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic

# Sample Output:
# stepic
# champignons
# the

num_dict_words = int(input())
correct_words = {input().lower() for _ in range(num_dict_words)}
number_lines_check = int(input())
lines_to_check = [input().lower().split() for _ in range(number_lines_check)]
misspelled_words = set()
for line in lines_to_check:
    for word in line:
        if word not in correct_words:
            misspelled_words.add(word)

print("\n".join(misspelled_words))

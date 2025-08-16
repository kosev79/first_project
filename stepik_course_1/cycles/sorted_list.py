#  принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
#  которые встречаются в нём более одного раза.
digits_list = [int(i) for i in input().split()]
digits_list.sort()
sorted_list = []

for i in range(len(digits_list) - 1):
    if digits_list[i + 1] == digits_list[i]:
        sorted_list.append(digits_list[i])

sorted_list = set(sorted_list)
sorted_list = list(sorted_list)

for i in range(len(sorted_list)):
    print(sorted_list[i], end=" ")

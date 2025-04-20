# ввводим с клавиатуры числа через пробел. получаем список
# программа считает для каждого элемента сумму его соседей и выводит в новый список

digits_list = [int(i) for i in input().split()]
sum_digits = []

if len(digits_list) == 1:
    sum_digits.append(digits_list[0])
else:
    for i in range(len(digits_list)):
        if i == 0:
            sum_digits.append(digits_list[1] + digits_list[-1])
        elif i == len(digits_list) - 1:
            sum_digits.append(digits_list[0] + digits_list[-2])
        else:
            sum_digits.append(digits_list[i - 1] + digits_list[i + 1])


for i in range(len(sum_digits)):
    print(sum_digits[i], end=" ")

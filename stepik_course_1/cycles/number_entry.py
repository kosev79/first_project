# на вход подается список из чисел
# потм вводится еще число
# на выходе программа проверяет есть ли данное число в списке и выдает номер позиии
list_digits = [int(i) for i in input().split()]
check_num = int(input())

for i in range(0, len(list_digits)):
    if list_digits[i] == check_num:
        print(i, end=" ")

print()
if list_digits.count(check_num) == 0:
    print("Отсутствует")

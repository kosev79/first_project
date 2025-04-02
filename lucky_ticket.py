# определяем счастливый билет
lucky_ticket = input()
sum_first = sum(int(char) for char in lucky_ticket[:3])
sum_last = sum(int(char) for char in lucky_ticket[3:])
print("Счастливый" if sum_first == sum_last else "Обычный")

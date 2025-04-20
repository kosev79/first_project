# компрессия генома в укороченный вариант
# пример:  на входе aaaccddddb
# на выходе a3c2d4b

genome = input()

i = 0
new_genome = ""

while i < len(genome):
    current_char = genome[i]
    count = 1
    while i + 1 < len(genome) and genome[i + 1] == current_char:
        count += 1
        i += 1
    new_genome += f"{current_char}{count if count > 1 else '1'}"
    i += 1

print(new_genome)


number = input()  # СОРТИРОВКА ЦИФР С ОТБРАСЫВАНИЕМ 0 В КОНЕЦ СПИСКА

new_number = []
zero_list = []

for i in range(0, len(number)):
    if number[i] == "0":
        zero_list.append(number[i])
    else:
        new_number.append(number[i])


def sum_lists(new_number, zero_list):
    last_list = "".join(new_number + zero_list)
    return last_list


print(sum_lists(new_number, zero_list))

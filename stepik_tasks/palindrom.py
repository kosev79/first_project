genome = input()  # проверяем вхождение символов без учета регистра

g = genome.upper().count("g".upper())
c = genome.upper().count("c".upper())

print((g + c) / len(genome) * 100)

# палиндром

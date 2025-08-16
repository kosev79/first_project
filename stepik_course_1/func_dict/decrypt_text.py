# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины, на первой строке записаны
# символы исходного алфавита, на второй строке — символы конечного алфавита,
# после чего идёт строка, которую нужно зашифровать переданным ключом,
# и ещё одна строка, которую нужно расшифровать.
# Sample Input 1:
# abcd
# *d%#
# abacabadaba
# #*%*d*%

# Sample Output 1:
# *d*%*d*#*d*
# dacabac

in_text = list(input())
decoder = list(input())
apply_dict = dict(zip(in_text, decoder))
invert_dict = dict(zip(decoder, in_text))
encrypt = list(input())
decrypt = list(input())

encrypt_text = []
for item in encrypt:
    for key in apply_dict.keys():
        if item == key:
            encrypt_text.append(apply_dict[key])

decrypt_text = []
for item in decrypt:
    for key in invert_dict.keys():
        if item == key:
            decrypt_text.append(invert_dict[key])

print("".join(encrypt_text))
print("".join(decrypt_text))

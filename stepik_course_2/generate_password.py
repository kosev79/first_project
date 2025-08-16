import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
# chars = ""
chars = digits + lowercase_letters + uppercase_letters + punctuation


def generate_password(length, chars):
    password = random.sample(chars, length)
    return "".join(password)


length_password = int(input("Длина пароля: "))

print(generate_password(length_password, chars))

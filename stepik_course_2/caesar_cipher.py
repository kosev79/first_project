def caesar_cipher(text, shift):
    # alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for char in text:
        if char.upper() in alphabet:
            original_pos = alphabet.index(char.upper())
            new_pos = (original_pos + shift) % 26
            new_char = alphabet[new_pos]
            result.append(new_char if char.isupper() else new_char.lower())
        else:
            result.append(char)
    return "".join(result)


text = input().split()
# encrypted = []
for i in range(len(text)):
    cnt = 0
    for j in range(len(text[i])):
        if text[i][j].isalpha():
            cnt += 1
    encrypted = caesar_cipher(text[i], cnt)
    print(encrypted, end=" ")

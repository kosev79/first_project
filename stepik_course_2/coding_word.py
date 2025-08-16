"""Username: [u-1042][u-1072][u-1089][u-1103]; City: [u-1050][u-1072][u-1079][u-1072][u-1085][u-1100]
кодировка символов
"""

message = input()
new_text = ""
i = 0
while i < len(message):
    code = ""
    if message[i] == "[" and message[i + 1] == "u" and message[i + 2] == "-":
        i += 3
        while message[i] != "]":
            code += message[i]
            i += 1
        new_text += chr(int(code))
        i += 1
    else:
        new_text += message[i]
        i += 1
print(new_text)

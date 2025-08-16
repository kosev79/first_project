# иттерация по последнему и предпоследнему символу в строке чтобы определить склонение слова
n = int(input())
string_value = str(n) 

if len(string_value) > 1 and string_value[-2] == "1" or string_value[-1] == "0":
    print(f"{n} программистов")
elif string_value[-1] == "1":
    print(f"{n} программист")
elif string_value[-1] == "2" or string_value[-1] == "3" or string_value[-1] == "4":
    print(f"{n} программиста")
else:
    print(f"{n} программистов")
    
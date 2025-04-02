# Напишите программу, которая получает на вход три целых числа, 
# по одному числу в строке, и выводит на консоль в три строки
# сначала максимальное, потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.
a = int(input())
b = int(input())
c = int(input())

if b >= a and b >= c and c >= a:
    max = b
    min = a
    other = c
    
elif b >= a and b >= c and a >= c:
    max = b
    min = c
    other = a
    
elif c >= b and c >= a and a >= b:
    max = c
    min = b
    other = a
    
elif c >= b and c >= a and b >= a:
    max = c
    min = a
    other = b
    
elif a >= b and a >= c and b >= c:
    max = a
    min = c
    other = b
    
elif a >= b and a >= c and c >= b:
    max = a
    min = b
    other = c
     
print(max)
print(min)
print(other)
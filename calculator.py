# Калькулятор
a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
operation = input('Введите операцию: \n'
                  '"+" - сложение \n'
                  '"-" - вычитание \n'
                  '"/" - деление \n'
                  '"*" - умножение \n'
                  '"mod" - взятие остатка от деления\n'
                  '"pow" - возведение в степень \n'
                  '"div" - целочисленное деление\n'
                  )

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == 'pow':
    print(a ** b)
else:   
    if b == 0:
        print('Деление на 0!')
    else:
        if operation == '/':
            print(a / b)
        elif operation == 'mod':
            print(a % b)
        elif operation == 'div':
            print(a // b)
   


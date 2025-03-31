# Игра "Быки" и "Коровы"
import random

def get_four_digits_number():
    while True:
        check_number = random.randint(1000, 9999)
        final_numb = str(check_number)
        if len(set(final_numb)) == 4:
            return final_numb
        
        
secret_random_number = get_four_digits_number()
# print(secret_random_number, type(secret_random_number))

print('   Начинаем игру "Быки и Коровы", вам нужно будет угадать четырехзначное число.   \n'
      '\n'
      '************   Каждая цифра в числе уникальна и не повторяется.*******************\n'
      '\n'
      '*   Если вы угадали цифру из загаданного числа, но она стоит не на своем месте   *\n'
      '*********************   это называется "Корова"   ********************************\n'
      '\n'
      '**************   Если вы угадали цифру из загаданного числа,   *******************\n'
      '************   и она стоит на своем месте это называется "Бык"   *****************\n'
      '\n'
      '******************   Цель найти всех четырех "Быков".   **************************\n'
      )


bulls = 0
cows = 0
attempts = 1

while True:
    number = input('Пожалуйста введите число:')
    
    if number == secret_random_number or bulls == 4:
        break
    for i in range(len(number)):
        for j in range(len(secret_random_number)):
            if number[i] == secret_random_number[j] and i == j:
                bulls += 1
            elif number[i] == secret_random_number[j] and i != j:
                cows += 1
    
    if bulls == 1:
        bulls_str = "Бык"
    elif bulls == 0:
        bulls_str = "Быков"
    else:
        bulls_str = "Быка"
        
    if cows == 1:
        cows_str = "Корова"
    elif cows == 0:
        cows_str = "Коров"
    else:
        cows_str = "Коровы"
        
    print(f"В вашем числе {bulls} {bulls_str} и {cows} {cows_str}")
    print()
    
    bulls = 0
    cows = 0
    attempts += 1
    
attempts_str = str()    

if attempts == 1:
    attempts_str = 'попытку'
elif  1 < attempts <= 4:
    attempts_str = 'попытки'
else:
    attempts_str = 'попыток'
    
print(f'Вы угадали за {attempts} {attempts_str}! Загаданное число {secret_random_number} ')

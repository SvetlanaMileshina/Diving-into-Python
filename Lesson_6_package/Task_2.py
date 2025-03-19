'''Cоздать модуль с функцией внутрию
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

import random  


def guess_number(lower_limit,upper_limit,count):
    random_integer = random.randint(lower_limit,upper_limit)
    while count > 0:
        print('Попытка '+ str(count)) 
        count -= 1
        num = int(input('Введите число загаданное компьютером : '))
        if num < random_integer:
            print('Больше')
        elif num > random_integer:  
            print('Меньше')
        else:
            break
    else:
        print('Исчерпаны все попытки')
    print('Было загадано число '+ str(num))    
   
    
if __name__ == '__main__': # Спрятали все вызовы, теперь можем импортировать как файл
   # print(guess_number(0,100,10))
    lower_limit = int(input('Введите нижнюю границу : '))
    upper_limit = int(input('Введите нижнюю границу : '))
    count = int(input('Введите количество попыток : '))
    guess_number(lower_limit,upper_limit,count)
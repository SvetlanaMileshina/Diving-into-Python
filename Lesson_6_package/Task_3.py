'''К задаче 2.Добавить возможность запуска функции" угадайка" из модуля
в командной строке терминала.Строка должна принимать от 1 до 3 аргументов
:параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение
'''

import random  
from sys import argv

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

    
if __name__ == '__main__': # делает доступной для импорта, 
    #при этом запускается функция после импорта внутри другого файла
   # print(guess_number(0,100,10))                                              путь =0     1    
    print(argv) # работаем в терминале > python 'task_3.py' 1 2 3 получаем =>['task_3.py', '1', '2', '3']
    m = len(argv) 
    match m :
        case 1:
            lower_limit = 0
            upper_limit = 100
            count = 10
            
        case 2:
            lower_limit = int(argv[1])
            upper_limit = 100
            count = 10
        case 3:
            lower_limit = int(argv[1])
            upper_limit = int(argv[2])
            count = 10
        case _:
            lower_limit = int(argv[1])
            upper_limit = int(argv[2])
            count = int(argv[3])
    
    guess_number(lower_limit,upper_limit,count)
    
    #guess_number(*map(int,argv[1:]))
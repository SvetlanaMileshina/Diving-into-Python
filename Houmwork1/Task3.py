'''Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)'''


import random  

LOWER_LIMIT = 0
UPPER_LIMIT = 1001
random_integer = random.randint(LOWER_LIMIT, UPPER_LIMIT)
count = 10
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
#print("The random integer is :", random_integer)
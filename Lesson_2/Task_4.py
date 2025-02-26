'''Напишите программу, которая вычисляет площадь круга и длину окружности 
по введенному диаметру.Диаметр не превышает 1000у.е.Точность вычисления должна составлять
не менее 42 знаков после запятой.'''

import decimal
import math

decimal.getcontext().prec = 50 #  не 42 а 50 т.к. есть еще цифры до запятой (1000)

d_circle = decimal.Decimal(input('Введите диаметр: '))
pi = decimal.Decimal(math.pi) 


if d_circle<=1000:
    r = d_circle/2
    s_circle = pi * r ** 2
    сircumference_length = 2*pi*r
    print(s_circle,сircumference_length)
else:
    print('Cлишком большое число')

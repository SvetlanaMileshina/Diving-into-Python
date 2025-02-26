'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions'''

import fractions

string_first = input('Введите дробь вида “a/b”  : ')
string_second = input('Введите дробь вида “a/b”  : ')

result_first = string_first.split("/") # ['1', '3']
result_second = string_second.split("/") # ['1', '3']


list_first = [int(x) for x in result_first] # [1, 3]
list_second =[int(y) for y in result_second] # [1, 3]

number1,number2 = list_first
number3,number4 = list_second

result1 = (number1 / number2) + (number3 / number4)
result2 = (number1 / number2) * (number3 / number4)
print(f'Сумма дробей: {result1}')
print((f'Произведение дробей: {result2}')) 


# проверка модуль fractions
f1 = fractions.Fraction(string_first)
print(f1)
f2 = fractions.Fraction(string_second)
print(f2)
print(f'Произведение дробей: {f1 * f2}')
print(f'Сумма дробей: {f1 + f2}')

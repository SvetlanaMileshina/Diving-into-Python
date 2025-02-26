'''Напишите программу, которая получает целое число и возвращает 
его двоичное  и восьмеричное строковое представление. Функцию bin используйте для проверки своего результата.'''
'''Для перевода числа 123 в двоичную систему счисления, мы будем ,
пока число не станет равным 0. Затем мы запишем остатки в обратном порядке.'''

'''BASE = 2

number = int(input('Введите число: '))
print (bin(number))
result = ' '
while number > BASE:
    result += str(number % BASE)# делить число на 2 и записывать остатки от деления  в result
    number //= BASE # number = number // 2
result += str(number)
print(result[::-1])'''

BASE = 8

number = int(input('Введите число: '))
print (oct(number))
result = ' '
while number > BASE:
    result += str(number % BASE)# делить число на 2 и записывать остатки от деления  в result
    number //= BASE # number = number // 2
result += str(number)
print(result[::-1])
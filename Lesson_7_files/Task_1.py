'''
Напишите функцию которая заполняет файл(добавляет в конец) случайными парами чисел.
Первое число int, второе float разделены вертикальной чертой.
Минимально - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргумент функции.
'''
import os
import random as rd

MIN = -1000
MAX = 1000


def generate_number_file(count: int, filename:str):#принимает количество строк и имя файла
    """Создает и заполняет числами файл."""
    
    with open(filename, 'w' ,encoding= 'utf-8') as f:# Открывает на запись,но w- СТИРАЕТ и перезаписывает до цикла
        for i in range(count):
            f.write(f'{rd.randint(MIN,MAX)} | {rd.random() * 2000 - 1000}')
    # первое число int(MIN,MAX)       float(от 0 до 1)
    # не ставит переход строки, а print -ставит
            f.write('\n' if i < count -1 else'') #Тернарный оператор if в одну строчку
    # переход строки если строка не последняя, в противном случае ничего
    
if __name__ == '__main__':
    
    generate_number_file(10,'data.txt')

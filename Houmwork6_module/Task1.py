'''
 В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''
__all__ = ['check_date','_isleap']
from datetime import datetime as dt
from calendar import isleap
from sys import argv 
#argv — это список строк, 
# который содержит аргументы командной строки,
# переданные программе из командной строки.
# Первый аргумент (с индексом 0) в списке — это название самого скрипта. 
# Остальные представлены в виде последовательности.

def check_date(date: str):# Существует или нет дата
    try:# Для нейтрализации ошибок функция try-except
        t = dt.strptime(date, '%d.%m.%Y') #Встроенная функция для форматирования даты, возвращает ошибку,если нет такой даты,
        _isleap(t.year)
        return True 
    except:
        return False


def _isleap(year: int):#Проверка на високосность
    print("Високосный" if isleap(year) else "Не високосный")
    
if __name__ == '__main__':
    if len(argv) == 2: # Только путь и дата, больше данных нет
        print(check_date(argv[1]))
    print(check_date(input('Введите дату: ')))   
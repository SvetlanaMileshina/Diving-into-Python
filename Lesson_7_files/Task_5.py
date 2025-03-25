"""
Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы
Расширение и количество байтов функция принимает 
Количество переданных расширений может быть любым
Количество файлов для каждого расширения различной
Внутри используется вызов функции из прошлой задачи
"""

from Task_4 import generate_files

def generate_with_dictioary(dictionary: dict):# Словарь расширений
    for key, value in dictionary.items(): #key- расширение(extention), value-количество  файлов которое нужно создать
        generate_files(key,'files',num_files=value)
        
        
if __name__ == '__main__':
    d = {
        'doc': 5,
        'jpg': 10,
        'png': 23,
        'txt': 15,
    }
    generate_with_dictioary(d)
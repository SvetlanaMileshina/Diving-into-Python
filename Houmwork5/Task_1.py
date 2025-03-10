'''
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
import os

def file_git(file_path):
    path, filename = os.path.split(file_path)#('https://github.com/SvetlanaMileshina', 'Diving-into-Python.git')
    name, extension = os.path.splitext(filename)#('https://github.com/SvetlanaMileshina', 'Diving-into-Python', '.git')
    return path, name, extension

if__name__ = '__main__'
print(file_git( input('Введите адрес ссылки: '))) 



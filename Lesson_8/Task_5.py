'''
Напишите функцию, которая ищет json файлы в указанной дирректории
и сохраняет их содержимое в виде одноименных pickle файлов.
'''
import json
import pickle
import os

def json_to_pickle(directory = '.'):# '.'=>просматриваем текущую директорию
    for file in os.listdir(directory):# указали текущую папку и все файлы в ней перебираем
        file_name,file_exten = os.path.splitext(file)# разбивает на имя и расширение
        if file_exten == '.json':
            with open (os.path.join(directory, file), 'r', encoding= 'utf-8') as f:# json читаем
                data = json.load(f) # загружаем данные из json
            with open (os.path.join(directory, file_name + '.pickle'), 'wb') as f: # pickle записываем
                pickle.dump(data,f)

if __name__ == '__main__':
    json_to_pickle()
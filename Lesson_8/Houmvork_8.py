'''Напишите функцию, которая получает на вход директорию и
рекурсивно обходит ее и все вложенные директории. Результаты обхода сохраняются в файлах JSON, CSV и Pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого условия укажите файл или каталог.
Для файлов сохраните его размер в байтах, а для каталогов — размер файлов в ней с учётом всех вложенных файлов и каталогов.
Соберите из созданных на уроке и в рамках домашнего задания пакет функций для работы с файлами разных форматов'''

import os
import json
import csv
import pickle


def write_json_csv_pickle(directory):
    # write_JSON
    result_dict_json = {}
    for dir_path, dir_file, file_name in os.walk(directory):#абсолютный путь до каталога,список с названиями всех каталогов, находящихся в dir_path,список с названиями всех файлов, находящихся в dir_path
        result_dict_json[f'DIRECTORY - {dir_path}'] = [
            f'FILE - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
    with open('json_file.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_dict_json, json_file, indent=4, separators=(',', ':'))
    
 
    # write_CSV
    data = [["Dir", "Files"]]
    for key, value in result_dict_json.items():
        data.append([key, value])
    with open('csv_file.csv', 'w', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel-tab',delimiter=',')
        write_csv.writerows(data)
   
    # write PICKLE
    with open('pickle_file.bin', 'wb') as pickle_file:
        pickle.dump(result_dict_json, pickle_file)


write_json_csv_pickle(directory='Lesson_8')
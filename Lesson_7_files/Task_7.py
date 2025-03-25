"""
Создйте функцию для сортировки созданных файлов по директориям: текстовые отдельно,
фото отдельно.
В исходной папке должны остаться  только те файлы"rnd" должны остаться в отдельной
"""
import os
# Coздаем словарь который говорит что куда положить
DICTIONARY = {
        'doc': 'text',
        'txt': 'text',
        'png': 'pictures',
        'jpg': 'pictures',
        }


# Если вложенные папки то лучше Wolk
def sort_files(directory):
    for f in os.listdir(directory):# u x q a t g m t.rnd
        extension = f.rsplit('.')[-1]# разбиваем строку по точке с зади(срез) до точки
        if extension not in DICTIONARY:#если в файле нет расширения которое указано в созданном словаре,то с ними ничего не делаем
            continue
        new_directory = f'{directory}/{DICTIONARY[extension]}' #Получаем название новой папки куда бкдем собирать нужные расширения
        if not os.path.exists(new_directory) or not os.path.isdir(new_directory):#Если директория не существует,либо она не директория а просто файл
            os.mkdir(new_directory)# Если ее не существует, мы ее создаем в папке directory  новую new_directory
        os.rename(f'{directory}/{f}', # переименовываем- из старой папки переносим в новую
                  f'{new_directory}/{f}')
           

        
if __name__ == '__main__':
    sort_files('files')
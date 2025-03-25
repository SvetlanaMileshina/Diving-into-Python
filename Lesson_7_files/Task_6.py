"""
Существующие файлы не должны удаляться.
В случае совпадения имен
"""

import random
import os

MIN_LETTER = ord('a')
MAX_LETTER = ord ('z')

def generate_text(length):# Генерирует имя переданной длины
    """Генерирует случайное имя файла"""
    name = []
    for i in range(length):# для каждой буквы генерируем ее код
         name.append(chr(random.randint(MIN_LETTER,MAX_LETTER)))
    return " ".join(name)

def generate_files(extension:str,
                   directory:str,
                   min_length = 6,
                   max_length = 30,
                   min_bytes = 256,
                   max_bytes = 4096,
                   num_files = 42):
    "Генерирует файлы с заданными параметрами."
    if not os.path.exists(directory) or not os.path.isdir(directory):
        #Если директория не существует,либо она не директория а просто файл
        os.mkdir(directory)
        # Если ее не существует, мы ее создаем

    for i in range(num_files):
        name_length = random.randint(min_length,max_length)
        filename = generate_text(name_length)
        text_length = random.randint(min_bytes,max_bytes)
        text = generate_text(text_length)
        while True:
            try:
                with open(f'{directory}/{filename}.{extension}', 'x' ,encoding= 'utf-8') as f:# "x"-выдает ошибку,если такой файл есть
                    f.write(text)
            except:
               filename =  generate_text(name_length) #Перегенирируем имя
            else:
                break
                


if __name__ == '__main__':
    generate_files('rnd','files')
"""
Напишите функцию, которая создает файлф с указанным расширением.
Принимает параметры: 
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер дожны быть в расках переданного  
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
        with open(f'{directory}/{filename}.{extension}', 'w' ,encoding= 'utf-8') as f:
            f.write(text)


if __name__ == '__main__':
    generate_files('rnd','files')
'''
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,состоять из 4-7 букв,
среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
'''

import random

MAX_LEN = 7
MIN_LEN = 4
MIN_LETTER = ord('a')
MAX_LETTER = ord ('z')
VOWELS = {'a','o','y','i','u','e'}
def generate_name_file(filename:str, count_name: int):
    """Генерация псевдоимен."""
    with open(filename, 'w' ,encoding= 'utf-8') as f:
        for j in range(count_name):
            len_name = random.randint(MIN_LEN,MAX_LEN)
            name = []
            for i in range(len_name):# для каждой буквы генерируем ее код
                name.append(chr(random.randint(MIN_LETTER,MAX_LETTER))) # дает код юникода, получаем случайную букву латиницы
            # Проверка гласных
            hash_vowels = False
            for letter in name:
                if letter in VOWELS:
                    hash_vowels = True # значит что есть хотя бы одна гласная
                    break
            if not hash_vowels:#Для условия,что есть хотя бы одна гласная,любую согласную заменяем на случайную гласную
                ind = random.randint(0,len_name -1) #Какую букву будем менять
                letter = random.choice(list(VOWELS)) #выбираем случайную гласную на которую будем менять
                name[ind] = letter # По этому индексу берем и заменяем на случайную гласную
            print(f'{"".join(name).capitalize()}', file=f, end='')
            f.write('\n' if j < count_name -1 else'')

if __name__ == '__main__':
    
    generate_name_file('name.txt',20)
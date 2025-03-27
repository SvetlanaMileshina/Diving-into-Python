'''Напишите функцию, которая в бесконечном цикле запрашивает имя, 
личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавьте новую информацию в файл JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны быть сохранены.
'''
import os
import json
from pathlib import Path

def access_users(name = 'db.json'):
    db = {} #Создаем пустой словарь 
    if os.path.exists(name) and os.path.isfile(name):# Убедиться есть ли словарь
        with open (name, 'r', encoding= 'utf-8') as f: #Если он существует и он файл, то мы его открываем и читаем из него базу
            db = json.load(f) # Загружаем словарь хранится в db, иначе остается пустой словарь
    
    # если не существует,создаем новый
    with open (name, 'w', encoding= 'utf-8') as f:  
        while True: #Если ввели текст а не цифры,  
            while True:
                try:
                    user_level = int(input("Введите уровень от 1 до 7 или буквы для выхода: ")) #то сбрасывем в дейсон
                except:
                    json.dump(db,f)
                    exit()#и выходим из программы
                else:
                    break  # Дальше проверяем условия про цифры
            if not 1<= user_level <=7:# Если не в этом диапазоне тогда вернем обратно на while True
                continue
            if user_level not in db:# Если уровня нет, то мы его создадим
                db[user_level] = {} # Словарь Для идентификаторов
            while True:
                try:
                    user_id = int(input("Введите идентификатор: ")) 
                except:
                    print('Некорректный вввод')
                else:
                    flag = False
                    for level in db:
                        for ident in db[level]:
                            if ident == user_id:
                                print('Идентификатор должен быть уникальным')
                                flag = True
                                break
                     #Если проходи цикл и нет ни одного похожего идентификатора тогда выходим
                    if flag:
                        continue
                    else:
                       break
            while True:
                user_name = input("Введите имя: ") 
                if user_name :
                    break
                else:
                    print('Имя не должно быть пустым')
            db[user_level][user_id] = user_name
            
if __name__ == '__main__':
    access_users()
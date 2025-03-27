'''Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдоименами и произведениями чисел.
Напишите функцию, которая создает из созданного ранее файла новый файл с данными в формате JSON.
Имена пишите большими буквами.
Каждую пару сохраняйте с новой строкой'''

import json

def text_to_json(name = 'res.txt'):    # открываем файл res с псевдонимом    
    with open (name, 'r', encoding= 'utf-8') as f,\
    open ('res.json','w',encoding= 'utf-8') as f2:   
        res_list = []
        for line in f: # читаем его строка за строкой
            res_list.append(line.capitalize())
        json.dump(res_list,f2,indent=4)
        
if __name__ == '__main__':
    text_to_json()
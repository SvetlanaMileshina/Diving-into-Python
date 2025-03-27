'''
Прочитайте созданный в прошлом заданный файл csv без использования csv.DictReader.

Дополните идентификатор до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Полученные записи сохраняются в файле json, где логические строки файла csv представлены как отдельный словарь json.
Имя исходного и конечного файлов можно использовать в качестве аргументов функции
'''
import json
import csv
from pathlib import Path

def csv2json(from_file: Path, to_file: Path) ->None:
    json_list = []
    with open (from_file, 'r', encoding= 'utf-8') as f:
        csv_write = csv.reader (f, dialect='excel')
        for i, line in enumerate(csv_write):
            json_dict = {}
            if i == 0:
                continue
            else:
                level,id,name = line
                json_dict['level'] = int (level)
                json_dict['id'] = f"{int(id):010}"
                json_dict['name'] = name.title()
                json_dict['hash'] = hash (f"{json_dict['name']}{json_dict['id']}")
                json_list.append(json_dict)
    
    with open (to_file, 'w', encoding= 'utf-8') as f_json:
        json.dump(json_list, f_json, indent=2)
        
if __name__ == '__main__':
    csv2json(Path('db.csv'),Path('new_db.json'))
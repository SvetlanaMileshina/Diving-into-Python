'''
Напишите функцию , которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи 4 семинара
Должна извлекать ключи словаря для заголовка столбца из  переданного файла
'''
import pickle
import csv
from pathlib import Path

def pickle_to_csv(file:Path)->None:
    with(
        open(file,'+rb') as f_read,
        open(f'{file.stem}to.csv','w',newline= '',encoding= 'utf-8') as f_write,
    ):
        #data = pickle.load(f_read)
        #print(data)
        data = [["level", "id","name"]]
        keys = list(data[0].keys()) # Про заголовки''
        csv_write = csv.DictWriter(f_write,fieldnames=keys,dialect='exel-tab',quoting=csv.QUOTE_NONNUMERIC)
        
        csv_write.writeheader()
        csv_write.writerows(data)
        
if __name__ == '__main__':
    pickle_to_csv(Path('db.pickle'))
""" Три друга взяли вещи в поход.
Сформируйте словарь где ключ- имя друга
значение- кортеж вещей.
Какие вещи взяли все три друга.
Какие вещи уникальны, есть только у одного
Какие есть у всех, кроме одного и имя того у кого
данная вещь отсутствует.Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей
"""

dic_things = {
    'Юра':('палатка','рюкзак','котелок'),
    'Сергей':('рюкзак','палатка','спички','лопата'),
    'Саша':('стол', 'рюкзак', 'продукты'),   
}
first = list(dic_things.keys())[0] # Получаем первый список для пересечения со множеством [0]-индекс в словаре-Юра
res = set(dic_things[first])# Список вещей
for k, v in dic_things.items():
    res = res.intersection(set(v)) # Делаем пересечение значений словаря
print('У всех есть',*res)

dic_count = {}
for k, v in dic_things.items():
    for value in v:
        dic_count[value] = dic_count.get(value,0) + 1
friends = len(list(dic_things.keys())) -1 # Код должен расширяться на любое большее количество друзей

things = []
for k, v in dic_count.items():
    if v == friends:
        things.append(k)

for k, v in dic_things.items():
    for item in things:
        if item not in v:
            print(f'{item} нет у {k}!')
            break
list_things = []
for k, v in dic_count.items():
    if v == 1:
        list_things.append(k)
print('Вещи в единственном экземпляре:',*list_things)

print(dic_count)







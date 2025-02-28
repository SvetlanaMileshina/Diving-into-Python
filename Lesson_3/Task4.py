'''
Cоздайте в ручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды'''

from collections import Counter

list_1 = [1, 1, 1, 5, 4, 7, 7, 8, 9, 9, 10]
#dic2 = Counter(list_1) # Решение "из коробки" 

dic = {} # Создаем основу словаря  счeтчиков, где ключ-элемент, значение-количество таких элементов
for item in list_1:#{1: 3, 5: 1, 4: 1, 7: 2, 8: 1, 9: 2, 10: 1}
    if item not in dic:# Eсли нет значения
        dic[item] = 0 # Внутри цикла считаем элементы
    dic[item] += 1  #Второй способ в одну строку dic[el] = dic.get(el,0)      
for k, v in dic.items():# Проходит по всему словарю и парами вытаскивает ключ-значение
    if v == 2: # Удаляем только те которых -2
        list_1.remove(k)
        list_1.remove(k) # Два раза т.к. два значения 7 и 9 повторяются по 2 раза
print(list_1) # [1, 1, 1, 5, 4, 8, 10]
print(dic)
# Сортирует еще по количеству повторений по убыванию Counter({1: 3, 7: 2, 9: 2, 5: 1, 4: 1, 8: 1, 10: 1})
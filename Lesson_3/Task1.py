'''В ручную создайте список с целыми числами, которые повторяются.
Получите новый список, который содержит уникальные элементы исходного списка'''

list_1 = [1,2,3,5,7,2,8,5,6]
# Используем множество
print(list(set(list_1)))
# Перебор и добавление в новый список элемента которого еще нет в новом
list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)   
print(list_2)
    

''' Продолжаем задачу 2.Возьмите словарь,который получили
сохраните его итератор.
выведите первые 5 пар ключ-значение
обращаясь к итератору а не к словарю.
'''
import sys
text = 'Снова осень и дождь в окно сткчится'
dictionary = {key:ord(key)for key in text }
iterator = iter(dictionary.items())
#print(iterator,type(iterator),sys.getsizeof(iterator),sys.getsizeof(dictionary))
print(next(iterator)) #/Пять штук которые достали next, for уже не видит и идет дальше доставать
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print('Начало цикла for')
#for item in iterator:
#    print(item)
    
for item in range(5):
    print(next(iterator))
'''Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.'''

def school_print(**kwargs)-> dict :
    for key, value in kwargs.items():
        key,value = value,key
        print(f'оценка "{str(key)}" предмет  {str(value)}')
        

school_print(химия=5, физика=4, математика=5, физра=5)


'''def school_print(**kwargs)-> dict :
    d = {}
    s = set() # проверка на хешируемость
    for key, value in kwargs.items():
        try:
            s.add(value)
        except:    
           value = str(value)
        d[value] = key
    return d    

print(school_print(химия = 5, физика = 4))'''
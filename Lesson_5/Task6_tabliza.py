'''Выведите в консоль таблицу умножения.
Таблицу создайте в виде однострочного генератора 
отдельный элемент таблицы
Для вывода исмользуйте print без перехода на новую строку
'''
print(*(f"{j} * {i} = {i * j}\t\t" if i < 10 else ('\n') for i in range(2,10) for j in range(2,6)))   
print(' ') 
print(*(f"{j} * {i} = {i* j}\t\t" if i < 10 else ('\n ') for i in range(2,10) for j in range(6,10)))

'''
print(*(f"{i} * {j} = {i * j}\t" if i < 6 else ('\n') for j in range(2,11) for i in range(2,7)))   
print(' ') 
print(*(f"{j} * {i} = {i* j}\t" if i < 10 else ('\n ') for j in range(2,10) for i in range(6,11)))
'''
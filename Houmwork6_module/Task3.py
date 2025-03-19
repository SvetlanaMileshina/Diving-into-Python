'''Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки'''

import random

n = 8
count = 0
dct = dict()


def check_queen_8x8(x: list, y: list) -> bool:
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                flag = False
        if flag:
            return True
        return False


while True:
    x = list()
    y = list()
    for i in range(n):
        new_x, new_y = random.sample(list(range(1, 9)), k=2)
        x.append(new_x)
        y.append(new_y)
    if check_queen_8x8(x, y):
        lst = [list(i) for i in zip(x, y)]
        dct[count + 1] = lst
        count += 1
    if count == 4:
        break

if __name__ == '__main__':
    for k, v in dct.items():
        print(f"Комбинация №{k}, с координатами ферзя: {v}")

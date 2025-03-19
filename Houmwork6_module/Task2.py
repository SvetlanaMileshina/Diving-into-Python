'''Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Eсли ферзи не бьют друг друга верните истину, а если бьют - ложь'''

__all__ =['is_queen_beat']
    
# Через функцию
'''def is_queen_beat(new_x :list[int], new_y:list[int] ) -> bool:
    n = 8
    x = []
    y = []
    for i in range(n):
        new_x, new_y = [int(s) for s in input('Введите два элемента через пробел : ').split()] 
        x.append(new_x)
        y.append(new_y)
    
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
 
    if correct:
        return True  # ферзи не бьют др др
    else:
        return False # # ферзи  бьют др др

if __name__ == '__main__':
    print(is_queen_beat(new_x=1,new_y=2))
    '''
    
    
    
def is_queen_beat(position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]): 
                correct = False
    if correct:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    print(is_queen_beat([[1, 2], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]]))  #функция определяет успешно или нет расставлены ферзи на доске 8*8'''
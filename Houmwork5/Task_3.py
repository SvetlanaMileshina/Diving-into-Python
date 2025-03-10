'''
Создайте функцию генератор чисел Фибоначчи
'''

def fibonachi(n: int):
    a, b = 0, 1
    yield a
    yield b
    
    for _ in range(n):
        yield a + b
        a, b = b, a + b
 
n = int(input("Введите число элементов: "))
res = [i for i in fibonachi(n)]
print(*res)

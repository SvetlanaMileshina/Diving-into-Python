''' 
Напишите программу, которая решает квадратное уравнение даже если дискриминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.
Комплексные числа вида a+bi, где a и b— вещественные числа, а i — мнимая единица, то есть число, для которого выполняется равенство: i**2=-1
'''

a = int(input('Введите длину стороны а: '))
b = int(input('Введите длину стороны b: '))
c = int(input('Введите длину стороны c: '))

d = b**2 - 4*a*c
if d > 0:
    print((-b+d**0.5)/(2*a))
    print((-b-d**0.5)/(2*a))
elif d == 0:
    print((-b)/(2*a))
else :
    d = complex(d)
    print((-b+d**0.5)/(2*a))
    print((-b-d**0.5)/(2*a))
# Ввести 3,4,5-комплексные числа
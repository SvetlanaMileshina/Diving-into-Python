#Посчитать сумму четных элементов от 1 до n исключая кратные e.
'''n = int(input('Введите число: '))
e = int(input('e:'))
count = 2
sum1 = 0
while True:
    if count > n:
        break
    if count % e == 0:
        count +=2
        continue
    sum1 += count
    count += 2
    print(sum1)
print(sum1)'''

n = int(input('Введите число: '))
e = int(input('e:'))
count = 2
sum1 = 0
while count <= n:
    if count % e == 0:
        count +=2
        continue
    sum1 += count
    count += 2
    print(sum1)
print(' ') # Пропуск строки
print(sum1)
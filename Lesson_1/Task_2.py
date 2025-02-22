# Напишите программу, которая запрашивает год и проверяет его на високосность
'''year = int(input('Введите дату в формате YYYY : '))
if year % 4!= 0 :
    print('Обычный')
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Oбычный")
else:
    print("Високосный") '''
    
'''year = int(input('Введите дату в формате YYYY : '))  
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("Обычный")
else:
    print("Високосный")'''
         
'''year = int(input('Введите дату в формате YYYY : '))  
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Високосный")
else:
    print("Обычный")'''
    
IGNORE = 1582
year = int(input('Введите год после 1582 : '))
if year < IGNORE:
    print('Слишком ранний год')
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Високосный")
    else:
        print("Oбычный")

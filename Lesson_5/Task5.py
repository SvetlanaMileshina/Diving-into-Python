'''Напишите программу,которая выводит на экран числа от 1 до 100
При этом вместо чисел кратных 3,программа выводит-"Fizz"
вместо чисел кратных 5-"Buzz".
Если число кратно и 3 и 5-"FizzBuzz/
Превратите решение в генераторное выражение
 '''
 
'''for i  in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else: 
        print(i)'''
        
        
print(*("FizzBuzz" if i % 3 == 0 and i % 5 == 0 
        else "Fizz" if i % 3 == 0 
        else "Buzz" if i % 5 == 0 
        else i 
        for i  in range(1, 101)))
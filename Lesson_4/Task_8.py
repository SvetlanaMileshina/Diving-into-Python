'''Создайте несколько переменных оканчивающихся и не оканчивающихся на "S".
Напишите функцию, которая при запуске заменяет содержимое переменных 
оканчивающихся на "S"(кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноименные переменные без S на конце.
[ ]
'''

def no_s():# ничего не принимаетб т.к. достает все из globals
    """ Удаляет S из имен переменных"""
    lst = {}# словарь
    for var, val in globals().items():#var-название переменной, val- ee значение
        if var != "s" and var.endswith("s") and var != "no_s":# если это не s но заканчивается на s
            lst [var[:-1]] = val #обрезаем последнюю s и кладем в одноименную переменную
            globals()[var] = None
    for k, v in lst.items():
        globals()[k] = v


if__name__ ='__main__'
items = 0
names = "dsdsd"
s = 5
value = "fff"
print(globals())
no_s()
print(globals())
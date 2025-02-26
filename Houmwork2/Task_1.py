'''Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.'''

number = int(input('Введите целое число :'))

hex_str = format(number,'x')
print(hex_str)  

hex_fstring = f"{number:02X}"
print(hex_fstring) 

# Проверка
hex_value = hex(number)
print(hex_value)
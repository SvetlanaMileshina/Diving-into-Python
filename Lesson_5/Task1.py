''' Пользователь вводит строку из 4 или более целых чисел,
разделенных символом "/"
Сформируйте словарь где:
второе и третье число являются ключами
первое число является значением для первого ключа
четвертое и все возможные последующие числа храняться в картеже
как значения второг ключа'''

a, b, c, *d = input('Введите строку из 4 или более чисел разделенных "/": ').split('/')
dictionary = {c: tuple(d), b:a}
print(dictionary)

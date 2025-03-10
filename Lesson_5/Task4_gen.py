'''Создайте генератор четных чисел от 0 до 100.
Из последовательности исключите числа, сумма цифр которых=8
Решение в одну строку
'''
print(*(i for i  in range(0, 101, 2) if sum(map(int, str(i)))!= 8))# В условии if после перевода каждой цифры в строку
# map разделяет двузначные числа на отдельные цифры, превращает str в int(опять в цифры) которые потом складываютя sum
# и сравниваются с 8.map-как итератор достает по одной цифре из двузначного числа и подает к суммированию
print(*(i for i  in range(0, 101, 2) if sum ([int(j) for j in str(i)]) != 8))
# Разбиваем цисло на цифры в строковом варианте при прохождении в цикле for, j это цифра из числа i
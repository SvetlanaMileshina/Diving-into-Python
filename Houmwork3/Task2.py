'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
'''
from collections import Counter

texst_list = input('Введите строку: ').split()
lowercase_texst_list = [s.lower() for s in texst_list]
dic = Counter(lowercase_texst_list)
most_common = dic.most_common(10)
#print(lowercase_texst_list)
#print(dic)
print(*most_common)
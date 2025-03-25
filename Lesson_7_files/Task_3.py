'''
Напишите функцию, которая открывает на чтение 
созданные в прошлых задачах файлы с числами и именами.
Перемножте пары чисел.В новый файл сохраните имя и произведение.
Если результат умножения отрицательный,
сохраните имя записанное строчными буквами и произведение его по модулю.
Если положительный сохраните имя прописными буквами
и произведение округленное до целого
В результирующем файле должно быть столько же строк
сколько в новом файле 
при достижении конца более короткого файла, возвращайтесь в его начало.
'''

# Функция читает следующую строку файла, либо если файл закончился 
# переходит на начало файла и читает его первую строку


def read_line_or_begin(fd:str) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def process_files(file_numbers, file_names, file_res):
    with open(file_numbers, 'r' ,encoding='utf-8') as f_num:
        with open(file_names, 'r' ,encoding='utf-8') as f_names:
            with open(file_res, 'w' ,encoding='utf-8') as f_res:
                length1 = len(f_num.readlines())  # Прочитает все строки файла,даст количество эти строк файла с числами
                length2 = len(f_names.readlines()) #Длина второго файла с именами
                length = max(length1,length2)# Определяемся с максимальной длиной у этих файлов, чтобы узнать длину цикла
                for i in range(length):
                    line_num = read_line_or_begin(f_num)  #Читаем строку с числами
                    line_name = read_line_or_begin(f_names)  #Читаем строку со словами
                    
                    a, b = line_num.split('|') # Список из двух чисел разделенных |, одно число пойдет в а другое в b
                    a = int (a)
                    b = float(b)
                    res = a * b
                    if res < 0:
                        res *= -1 # Произведение по модулю
                        line_name = line_name.lower() # Строчными буквами
                    else:
                        res = round(res)  #Округление до целого
                        line_name = line_name.upper() #Прописными
                    f_res.write(f'{line_name} {res}')
                    f_res.write('\n' if i < length -1 else'')
                        
                    
if __name__ == '__main__':
    
    process_files('data.txt', 'name.txt','res.txt')
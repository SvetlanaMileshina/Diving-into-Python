'''Напите программу банкомат.
Начальная сумма = 0.Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50у.е.
Процент за снятие-1,5% от суммы снятия но не мение 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляется 3%
Нельзя снять больше, чем на счете.При привышении суммы в 5 млн вычитать налог на богатство 10%
перед каждой операцией, даже ошибочной.Любое действие выводит сумму денег.
Возьмите задачу о банкомате из семинара.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''
from decimal import Decimal
from datetime import date

MIN_SUM = 50 # кратны 50у.е
PROCENT_СOMISSION = Decimal(0.015)  # Процент за снятие
MIN_COMISSION = 30 # суммы снятия
MAX_COMISSION = 600 # суммы снятия
BONUS = Decimal(0.03) # каждой третьей операции пополнения или снятия начисляется 3%
LIMIT_BEFORE_TAX = 5_000_000 # привышении суммы в 5 млн
TAX_RATE = Decimal(0.1) # вычитать налог на богатство 10%

list_operation = []

def menu(balance: Decimal,count: int,is_flag: bool):
    """ Функция меню: обработка запросов.
    :вычитает налог на богатство 10%
    :проверяет корректность введения
    :после каждой третьей операции пополнения или снятия начисляется 3%
    :выводит баланс после каждой операции"""
    
    
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1-TAX_RATE)
    dict = {'1':'Пополнить счет',# Создали словарь
            '2':'Снять со счета',
            '3':'История операций',
            '4':'Выйти из программы'}
    
    
    for k,v in dict.items():# Идем по словарю
        if k.isdigit():# Возвращает True, если все символы в строке являются цифрами
            print(f'{k}: {v}')
        else:
            print(v)
    
    choice = input('Выберите команду:')
    if choice == '4':
        is_flag = False
        print("Баланс= ", round(balance,2))
        return balance,is_flag
    elif choice == '1':
        balance = giv_money(balance)
        count += 1 #  про 3%
    elif choice == '2':
        balance = get_money(balance) 
        count += 1 # про 3%
    elif choice == '3':
        print(*list_operation)    
    else:
        print('Неверная команда')
    if count % 3 == 0:
        balance *= (1 + BONUS)
    print("Баланс= ", round(balance,2))
    return round(balance,2),is_flag

def get_money(balance: Decimal):
    """Снятие со счета.
    :процент за снятие-1,5% от суммы снятия но не мение 30 и не более 600 у.е.
    :добавляет сумму снятия в список операций
    :проверяет кратность суммы пополнения
    :  проверяет наличие нулевого баланса"""
    
    money_to_get = Decimal(input('Введите сумму снятия :'))
    procent = money_to_get * PROCENT_СOMISSION
    
    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION
            
        if money_to_get + procent <= balance:
            list_operation.append([str(date.today()),-1* money_to_get])
            return balance - (money_to_get + procent)
        else:
            print('Недостаточно средств')
            return balance
    else:
        print ('Ошибка снятия денег, сумма должна быть кратна 50')
        return balance
    

def giv_money(balance: Decimal):
    """ Пополнение счета
    :добавляет сумму снятияпополнения в список операций
    :проеряет кратность суммы пополнения"""
    money_to_giv = Decimal(input('Введите сумму пополнения: '))
    
    if money_to_giv % MIN_SUM == 0:
        list_operation.append([str(date.today()), money_to_giv])
        return balance + money_to_giv
    else:
        print('Ошибка пополнения, сумма не кратна 50')
        return balance
   
   
if __name__ == '__main__':
    print('Добро пожаловать в банкомат')
    balance = 0
    count = 0
    is_flag = True
    while is_flag:
        balance,is_flag = menu(balance, count, is_flag)
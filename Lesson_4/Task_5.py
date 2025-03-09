'''Функция принимает на вход три списка одинаковой длины:
имена-str ставка-int премия-str с указанием процентов "10.25%". 
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма расчитывается как ставка умонж на процент премии
{'Oлег': 6150.0, ' Ольга': 6000.0, 'Юлия': 3825.0}
'''

def calculate_bonus(names:list[str] , rates: int, percents: list[str]) -> dict:
    """ Рассчет премии"""

    calculation = {}
    for name, rate,percent in zip (names,rates,percents):
      percent = float(percent[ :-1])# превращаем int в float и берем без последнего знака- срез
      calculation [name] = rate * percent/100
    return calculation

if__name__ = '__main__'
names = ["Oлег"," Ольга", "Юлия"]
rates = [60_000, 75_000, 85_000]
persents = ["10.25%","8.0%","4.5%"]
print(calculate_bonus(names,rates,persents))

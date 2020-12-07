from sys import argv

name, time, salary, bonus = argv
try:
    time = float(time)
    salary = float(salary)
    bonus = float(bonus)
    res = time * salary + bonus
    print(f'Заработная плата сотрудника:  {res} руб.')
except ValueError:
    print('Not a number')
def my_func():
    sum_nam = 0
    while True:
        numbers = input('Введите в строку числа через пробел или & для выхода: ').split()
        for i in numbers:
            try:
                if i == '&':
                    print(f'Сумма чисел равна: {sum_nam}')
                    return
                else:
                    sum_nam += int(i)
            except ValueError:
                    print('Введено недопустимое значение')
        print(f'Сумма чисел равна: {sum_nam}')

my_func()
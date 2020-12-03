def my_sum(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"

print(f'{my_sum(int(input("Введите первое число: ")), int(input("Введите второе число: ")))}')
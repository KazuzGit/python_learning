def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp

n = int(input("Укажите факториал какого числа Вы хотите узнать? "))
for _ in fact(n):
    print(_)
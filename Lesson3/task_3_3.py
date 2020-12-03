def my_func(a, b, c):
    d = [a, b, c]
    d.remove(min(a, b, c))
    return d

print(f'{my_func(int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: ")))}')
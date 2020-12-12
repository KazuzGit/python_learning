try:
    with open("5.txt", "w", encoding="utf-8") as f:
        line = input("Введите числа через пробел: ")
        f.write(line)
        nam = line.split()
        print(f'Сумма введённых чисел - {sum(map(int, nam))}')

except IOError:
    print('Ошибка в файле')

except ValueError:
    print('Введены неверные данные!')


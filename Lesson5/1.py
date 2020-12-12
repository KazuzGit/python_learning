with open("1.txt", "w", encoding="utf-8") as f:
    while True:
        line_new = input("Введите данные строки: ")
        if line_new == '':
            break
        else:
            f.write(line_new + '\n')

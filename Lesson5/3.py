with open("3.txt", "r", encoding="utf-8") as f:
    summa = 0
    count = 0
    sotr = []
    for line in f:
        tokens = line.split(' ')
        if int(tokens[1]) < 20000:
            sotr.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = round((summa / count), 2)
print(f"Сотрудники с зарплатой меньше 20 тыс.: {sotr}")
print(f"Средняя зарплата по организации: {result}")
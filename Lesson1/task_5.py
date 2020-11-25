profit = round(float(input("Введите выручку фирмы: ")), 2)
costs = round(float(input("Введите затраты фирмы: ")), 2)

if costs > profit:
    print("Издержки больше выручки")
elif costs < profit:
    print("Выручка больше издержек")
    print(f"Коэффицент рентабильности фирмы: {round(((profit - costs) / profit * 100), 2)}")
    staff = int(input("Введите кол-во сотрудников фирмы: "))
    print(f"Прибыль фирмы на одного сотрудника: {round((profit - costs) / staff, 2)}")
else:
    print("Выручка равна издержкам")


print()
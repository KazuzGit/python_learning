dist = int(input("Введите кол-во километров пройденных за первый день: "))
dist_fin = int(input("Введите кол-во километров до результата: "))
day = 1
while dist < dist_fin:
    day = day + 1
    dist = dist * 0.1+dist

print(f"На {day} день спортсмен достиг результата — не менее {dist_fin} км")

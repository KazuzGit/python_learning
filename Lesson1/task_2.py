timein = int(input("Введите время в секундах: "))
hour = timein // 3600
minut = timein % 3600 // 60
second = timein % 3600 % 60

if hour < 10:
    hour = str(0) + str(hour)

if minut < 10:
    minut = str(0) + str(minut)

if second < 10:
    second = str(0) + str(second)

print(f"{hour}:{minut}:{second}")
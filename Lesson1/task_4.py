numb = int(input("Введите целое число: "))
maxnamb = 0

while (numb != 0):
    if maxnamb < numb % 10:
      maxnamb = numb % 10
    numb = numb // 10

print(maxnamb)

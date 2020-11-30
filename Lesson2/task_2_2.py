new_lst = []
k = int(input("Какое колличество элементов вы хотите внести в список: "))
for i in range(0, k):
    ele = input("Введите элемент списка:")
    new_lst.append(ele)
    if (i + 1) % 2 == 0:
        new_lst[i] = new_lst[i-1]
        new_lst[i-1] = ele

print(new_lst)
new_str = input("Введите строку: ")
new_str = new_str.split()
for i, el in enumerate(new_str, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. {el}")
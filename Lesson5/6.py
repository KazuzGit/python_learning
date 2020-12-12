new_dict = {}

with open("6.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()
        new_dict[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())

print(new_dict)



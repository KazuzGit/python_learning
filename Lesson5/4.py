translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("4_new.txt", "w", encoding="utf-8") as f_n:
    with open("4.txt", "r", encoding="utf-8") as f:
        for line in f:
              f_n.write(line.replace((line.split()[0]), translater.get(line.split()[0])))
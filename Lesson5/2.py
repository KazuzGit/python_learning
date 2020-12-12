with open("2.txt", "r", encoding="utf-8") as f:
#    print(f'Кол-во строк в файле {f.name}: {sum(1 for _ in f)}')
#    f.seek(0)
    index = 0
    for line in f:
        index += 1
        print(f'Кол-во слов в строке {index} - {len(line.split())}')

    print(f'Кол-во строк в файле {f.name}: {index}')
from json import dumps

results = [{}, {}]

with open("7.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        name, _, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

results[1]['average_profit'] = round(sum(profit for _, profit in results[0].items() if profit > 0) / len(results[0]))

with open("7.json", "w", encoding="utf-8") as fn:
    fn.write(dumps(results))

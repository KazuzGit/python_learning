goods = []
while input("Хотите добавить продукт? Введите да/нет: ") == 'да':
    number = int(input("Введите номер продукта: "))
    features = {}
    while input("Хотите ввести параметры продукта? Введите да/нет: ") == 'да':
        feature_key = input("Введите параметры продукта: ")
        feature_value = input("Введите значения параметров продукта: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)
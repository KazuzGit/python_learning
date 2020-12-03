def user(**kwargs):
    return list(kwargs.values())

print(user(name=input('Введите имя: '),
           soname=input('Введите фамилию: '),
           b_date=input('Введите дату рождения: '),
           town=input('Введите город проживания: '),
           e_mail=input('Введите e-mail: '),
           tel=input('Введите номер телефона: ')))
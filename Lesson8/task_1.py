import time

class Date:
    def __init__(self, date: str):
        self.__date = time.strftime('%d.%m.%Y', time.strptime(date, '%d-%m-%Y'))

    @property
    def date(self):
        try:
            Date.validate_date(self.__date)
        except ValueError as error:
            print(error)
            exit(1)
        else:
            return self.__date

    @classmethod
    def date_to_timestamp(cls, date):
        date = Date(date).date
        split_date = date.split('.')
        return (f'число: {int(split_date[0])}, число: {int(split_date[1])}, число: {int(split_date[2])}')

    @staticmethod
    def validate_date(date):
        splitted_date = date.split('.')
        if len(splitted_date[2]) != 4 \
                or len(splitted_date[1]) != 2 or int(splitted_date[1]) < 1 or int(splitted_date[1]) > 12 \
                or len(splitted_date[0]) != 2 or int(splitted_date[0]) < 1 or int(splitted_date[0]) > 31:
            raise ValueError('Date is incorrect')

print(Date.date_to_timestamp('25-01-2010'))
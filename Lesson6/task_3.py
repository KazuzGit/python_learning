class Worker:

    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self, reverse=False):

        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):

        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Пётр',
            'surname': 'Сергеев',
            'position': 'Техник',
            'wage':  45000,
            'bonus': 3000
        },
        {
            'name': 'Василий',
            'surname': 'Смактуновский',
            'position': 'Менеджер',
            'wage':  50000,
            'bonus': 20000
        },
    ]

    for item in position_data:
        position = Position(**item)

        print('name: ', position.name)
        print('surname: ', position.surname)
        print('full name: ', position.get_full_name())
        print('position: ', position.position)
        print('total income: ', position.get_total_income())


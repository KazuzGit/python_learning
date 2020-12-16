class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} едет'

    def stop(self):
        return f'\n{self.name} остановка'

    def turn(self, direction):
        return f'\n{self.name} поворот {direction}'

    def show_speed(self):
        return f'\nваша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nПревышение скорости! Ваша скорость: {self.speed}'
        else:
            return f'Скорость {self.name} допустима в горотских условиях'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость слишком низкая! Ваша скорость: {self.speed}'
        else:
            return f'Скорость {self.name} допустима в горотских условиях'


class PoliceCar(Car):
    pass


town = TownCar('Ниссан', 75, 'Серебристый', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('на лево'), town.turn('на право'), town.stop())

sport = SportCar('Ламборджини', 150, 'Красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('на лево'), sport.stop())

work = WorkCar('ГАЗ', 30, 'Чёрный', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('на право'), work.stop())

police = PoliceCar('Форд', 100, 'Спецокрас', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('на право'), police.stop())
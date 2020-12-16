from time import sleep

class TrafficLight:
    __states = {'красный': 7, 'жёлтый': 2, 'зелёный': 4}
    __color = ''

    def running(self):
        for color, sw_time in self.__states.items():
            self.__color = color

            print(f"Включен {self.__color} свет на {sw_time} сек.")

            sleep(sw_time)


t = TrafficLight()
t.running()
class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print(f"{self.title} пишет")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print(f"{self.title} чертит")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print(f"{self.title} рисует")


pen = Pen()
pen.draw()

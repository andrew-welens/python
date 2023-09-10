class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):
    def __init__(self, name, max_speed, mileage, seatCapacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.seatCapacity = seatCapacity

    def setCapacity(self, seatCapacity):
        self.seatCapacity = seatCapacity

    def seatingCapacity(self):
        return f"Вместимость одного автобуса {self.name}  {self.seatCapacity} пассажиров"


autobus = Autobus('Renault Logan', 80, 1000, 50)

print(autobus.seatingCapacity())
autobus.setCapacity(100)
print(autobus.seatingCapacity())

class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}"
        elif wheels == 3:
            return f"Это трицикл марки {self.name}"
        elif wheels == 4:
            return f"Это машина марки {self.name}"
        else:
            return f"Я не знаю таких ТС марки {self.name}"

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо, {self.name}, можно брать."
        elif self.mileage <= 100000:
            return  f"{self.name}, нужно проверить внимательно."
        elif self.mileage <= 150000:
            return f"{self.name}, нужно провести полную диагностику."
        else:
            return f"{self.name}, лучше не покупать."

vehicle1 = Vehicle("BMW", 30000)
vehicle2 = Vehicle("Audi", 75000)
vehicle3 = Vehicle("Toyota", 120000)
vehicle4 = Vehicle("Bugatti", 160000)

print(vehicle1.get_vehicle_type(2))
print(vehicle1.get_vehicle_advice())
print()
print(vehicle2.get_vehicle_type(3))
print(vehicle2.get_vehicle_advice())
print()
print(vehicle3.get_vehicle_type(4))
print(vehicle3.get_vehicle_advice())
print()
print(vehicle4.get_vehicle_type(5))
print(vehicle4.get_vehicle_advice())

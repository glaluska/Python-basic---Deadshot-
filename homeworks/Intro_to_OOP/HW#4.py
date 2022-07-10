# 1
class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self):
        return self.total_capacity * 100


vehicle = Vehicle('Name', 10, 20)
print(vehicle.fare())


# 2
class Bus(Vehicle):
    def __int__(self, name, max_speed, total_capacity):
        super().__int__(name, max_speed, total_capacity)


class Car(Vehicle):
    def __int__(self, name, max_speed, total_capacity):
        super().__int__(name, max_speed, total_capacity)


# 3
car_1 = Car('BMW', 140, 110)
car_2 = Car('Audi', 150, 120)
car_3 = Car('Mazda', 170, 130)
bus_1 = Bus('IKARUS', 110, 150)
bus_2 = Bus('Volvo', 120, 155)


# 4
print(isinstance(car_1, Car))
print(isinstance(car_2, Vehicle))
print(isinstance(bus_1, Car))
print(isinstance(bus_1, Vehicle))


# 5
class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

    def fare(self):
        return self.total_capacity * 100 * 1.1


# 6
class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity
        if used_capacity > total_capacity:
            raise 'Error'

# 7
    def __len__(self):
        return len(self.name)

# 8


class Engine:
    def __init__(self, volume):
        self.volume = volume

    def get_volume(self):
        return self.volume

# 9


class Car(Vehicle, Engine):
    def __int__(self, name, max_speed, total_capacity):
        super().__int__(name, max_speed, total_capacity)



# 10


print(Car.mro())
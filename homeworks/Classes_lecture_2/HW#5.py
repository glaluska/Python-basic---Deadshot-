# 1
class Laptop:
    def __init__(self, color, name, memory, capacity):
        self.color = color
        self.name = name
        self.memory = memory
        self.battery = Battery(capacity)


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

dell = Laptop("white", "Dell", 160, 2000)
pass




# 2
class Guitar:
    def __init__(self, guitarString):
        self.guitarString = guitarString



class GuitarString:
    def __init__(self, material):
        self.material = material


guitarString = GuitarString("wood")
guitar = Guitar(guitarString)

# 3

class Calc:
    @staticmethod
    def add_nums(a,b,c):
        return a + b + c

print(Calc.add_nums(1,2,3))

# 4
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        ingredients = ['forcemeat', 'tomatoes']
        return cls(ingredients)

    @classmethod
    def bolognaise(cls):
        ingredients = ['bacon', 'parmesan', 'eggs']
        return cls(ingredients)


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)

pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)

 # 5

class Concert:
    max_visitors_num = 0

    def __init__(self):
        self.__visitors_count = 0

    @property
    def visitors_count(self):
        return self.__visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value > Concert.max_visitors_num:
            self.__visitors_count = Concert.max_visitors_num
        else:
            self.__visitors_count = value


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)
print(Concert.max_visitors_num)

# 6
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    adress: str
    email: str
    birthday: str
    age: int

# 7

from collections import namedtuple

AddressBookDataClass = namedtuple('AddressBookDataClass', ["key", "name", "phone_number", "address", "email", "birthday", "age"])

addressbook_1 = AddressBookDataClass('1', 'Tom','+380978856443', 'Lviv, Ukraine', 'tom1999@gmail.com', '22.02.1999', 23)
print(addressbook_1)

# 8


class AddressBook(AddressBookDataClass):
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        super().__init__()

addressbook_2 = AddressBook('2', 'Anna','+380970096443', 'Lviv, Ukraine', 'anna1999@gmail.com', '01.02.1999', 23)

print(str(addressbook_2))

# 9

class Person:
    name = "John"
    age = 36
    country = "USA"

setattr(Person, 'age', 20)
print(Person.age)

# 10

class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


setattr(Student, 'email', 'anna1999@gmail.com')

student_email = getattr(Student, 'email')

print(student_email)

# 11

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        temperature_f = (self._temperature * 1.8) + 32
        return temperature_f

temperature_today = Celsius(20)

print(temperature_today.temperature)


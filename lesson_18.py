# from  abc import  ABC
# @abstra
# class Shape(ABC):
#
#
#     def area(self,width,height):
#         return width * height
#
#
#
#



# class Animal:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#
#     def run(self):
#         return f"{self.name}is running"
#
#     def eat(self):
#         return f"{self.name} is eating"
#
#
#
# class Dog(Animal):
#     def __init__(self,name,color,age):
#         super().__init__(name, color)
#         self.age = age
#
#
# dog = Dog("asd","dasd", 321)
# print(dog.run())
# print(dog.eat())
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#

class Electronica:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.price = price
        self.model = model




class Washingmachine(Electronica):
    def __init__(self, brand, model,price, capacity):
        super().__init__(brand, model,price)
        self.capacity = capacity


class Mobile(Electronica):
    def __init__(self, brand, model, price, screen_size):
        super().__init__(brand, model, price)
        self.screen_size = screen_size



class Laptop(Electronica):
    def __init__(self, brand, model, price, weight):
        super().__init__(brand, model, price)
        self.weight = weight



class Microwave(Electronica):
    def __init__(self, brand, model, price, power_consumption):
        super().__init__(brand, model, price)
        self.power_consumption = power_consumption


class Induction_cooker(Laptop):
    def __init__(self,brand,model,price,weight,power):
        super().__init__(brand.model,price,weight,weight)
        self.power = power


class Head_phone(Washingmachine):
    def __init__(self, brand, model,price, capacity,distance):
        super().__init__(brand, model,price,capacity)
        self.distance = distance




class TV(Mobile):
    def __init__(self, brand, model, price, screen_size,number_of_channels):
        super().__init__(brand, model, price,screen_size)
        self.number_of_channels = number_of_channels




class Toaster(Microwave):
    def __init__(self, brand, model, price, power_consumption,modes):
        super().__init__(brand, model, price,power_consumption)
        self.modes = modes







obj = Washingmachine("AEG","LFR61144BE",89000,10)
obj_2 = Mobile("redmi","redmi note 13",30000,14)
obj_3 = Laptop("linova","K14",45000,3)
obj_4 = Microwave("Midea","MM970",7239,15)
obj_5 = Induction_cooker("fasf","faw", 2313, 213, 33214)
obj_6 = Head_phone("utdkj", "fsf2",34123,3424,)
obj_7 = TV()
obj_8 = Toaster()
# class People:
#     def speak(self):
#         print('people speak')
#
#
# class Europen(People):
#     def speak(self):
#         print('Europrn speak')
#
#
# class Asian(People):
#     def speak(self):
#         print('Asian speak')
#
#
# people = People()
# europen = Europen()
# asian = Asian()
#
#
# people.speak()
# europen.speak()
# asian.speak()


#
# class TV:
#     def __init__(self, brand, price, size):
#         self.brand = brand
#         self._price = price
#         self.__size = size
#
#
# tv = TV('sony', 1000, 70)
# print(tv.brand)
# print(tv._price)
# print(tv._TV__size)

#

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_product_name(self):
        print(f'Product {self.name}')

class Food(Product):
    def __init__(self, weight, price, name ):
        super().__init__(name,price)
        self.weight = weight


    def get_product_name(self):
        print(f'Food: {self.name }, weight: {self.weight}')


class  Technicue(Product):
    def __init__(self, name, price, color, size):
        super().__init__(name,price)
        self.color = color
        self.__size = size

    def det_product_name(self):
        print(f'TEchnicue: {self.name}, color:{self.color}, size: {self.size}')

    @property
    def get_size(self):
        return self.__size

    @color.setter
    def color(self, value):
        if value == 'green':
            self.screen_size = value


phone = Technicue('samsung', 1000, 'black', 10)
phone.set_size = 15





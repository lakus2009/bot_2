# class Car:
#     def __init__(self, name , color, speed):
#         self.name = name
#         self.color = color
#         self.speed = speed
#
#     def __str__(self):
#         return f'Helloo My name is Timur'
#
# car = Car('Supra', 'black', 200)
# print(car)
from xml.etree.ElementPath import prepare_parent

#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f'Title: {self.title}, {self.author}, {self.pages}'
#
#     def __len__(self):
#         return  self.pages
#
#
#     def __eq__(self, other):
#         return self.pages == other.pages
#
#
#     def __gt__(self, other):
#         return self.pages < other.pages
#
#
#     def __lt__(self, other):
#         return self.pages < other.pages
# #
# #
# #
# # obj = Book('One Punchman', 'Anime Jakadzaki', 500)
# # obj_2 = Book('Kyzyl Alma', 'Chyngyz Aitmatov', 1000)
# # print(obj == obj_2)
# # print(obj > obj_2)
# # print(obj + obj_2)




# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
# obj = Point(3, 5)
# obj_2 = Point(4, 2)
# print(obj + obj_2)




import requests
from bs4 import BeautifulSoup


url = 'https://new.technodom.kg/category/fototehnika-i-kvadrokoptery'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
products = soup.find_all('div', class_="search__results__list rees-search-results-list")
for product in products:
    name = product.find('div', class_='common__recommendations__list__item__title').text
    price = product.find('div', class_='common__recommendations__list__item__price').text
    image_elem= product.find('div', class_='common__recommendations__list__item__img').text
    print(name)
    print(price)
    print(image_elem)

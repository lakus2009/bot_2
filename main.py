# my_list = [1, 2, 3, 4, 5]
#
# def square_list(x: list):
#     square_list = []
#     for i in x:
#         square_list.append(i ** 2)
#     return square_list
#
#
# print(square_list(my_list))
# def numbers():
#     return [i**2 for i in range21]
# my_group = ["daniel", "laura", "rayana", "sabina", "yzak", "muhammed", "aydin", "akyl", "tabyldy"]
# def mmm(x:list):
#     sorted(x).append(my_group)
#
#     return my_group
# print(my_group)
# import math
# from itertools import count
# from operator import itemgetter
# from tkinter.font import names


# def greeting_2(name):
#     print(f"welcom to lesson 2 {name}")
#
#
# greeting_2()
# def calculate(num_1=5, num_2=3, operator="+"):
#     if operator in ["+", "-", "*", "/"]:
#         if operator == "+":
#             return num_1 + num_2
#         elif operator == "-":
#             return num_1 - num_2
#         elif operator == "*":
#             return num_1 * num_2
#         elif operator == "/":
#             if num_2 == 0:
#                 return  "error : cannot divide by zero"
#         return  num_1 / num_2
#     return "please enter a valid operator"
#
# print(calculate(num_1=5, num_2=3, operator="+"))

# def generator(a,b):
#     return [i for i in range(a, b+1)]
# print(generator(a=1,b=15))
# count = 0
# def some_func():
#     global count
#     count += 1
#
# print(count)
# some_func()
# print(count)\

# def outer():
#     x = "outer"
#     def inner():
#         nonlocal x
#         x = "inner"
#     inner()
#     print(x)
#
# outer()
# def factotial(n: int) -> int :
#     if n == 0:
#         return 1
#     else:
#         return n * factotial(n - 1)
# print (factotial((998)))# outer()
# def factotial(n: int) -> int :
#     if n == 0:
#         return 1
#     else:
#         return n * factotial(n - 1)
# print (factotial((998)))

# def finc(*args:int):
#     if args == 0:
#      return 1
#     else:
#         return args * finc(args - 1)
#     mu_list = [i**math.pi*400 for i in args]
#     return mu_list
#
#
# print(finc())
# while True:
# #     finc()
# #     print(finc())
# # def func(**kwargs):
# #     print(kwargs)
# #     print(tupe((kwargs)))
# #     for key, value, in kwargs.items():
# #         print(key,value)
# #
# # func(name="fsf")
# # a = 0
# # def finc(*args:int):
# #     count = 0
# #      = [i for i in args]
# #     return count
# # print(finc(213,424,53))
# k = 0
# def func(**kwargs:int):
#     for v in kwargs.items():
#         if v == 4:
#             kwargs.apendd(k)
#             return
#         if v == 3:
#             kwargs()
#         return
#
# func(Dan=4, say=4, adi=4, aman=4,aydin=3, akyl=3, yzak=3, aydar=3)
#
#
# print(func())
# my = [1,2,3,]
# print((list(reduce(lambda x:x,y: x + y,my)))



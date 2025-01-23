# class Bird:
#     def __init__(self,color):
#         self.color = color
#
#
#     def fly(self):
#         print("Bird fly")
#
#
# class Sparrow(Bird):
#     def __init__(self,color):
#         super().__init__(color)
#
#
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#
#
#     def decription(self):
#         return self.make, self.model, self.year
#
#
# class Bird:
#     def __init__(self,color):
#         self.color = color
#
#
#     def decribe(self):
#         return f"Birds color: {self.color}"



class BankAccount:
    def __init__(self,owner, balance, transfers):
        self.owner = owner
        self._transfers = transfers
        self.__balance = balance

    def get_balance(self):
        return self.__balance


    def debit_balance(self,amount):
        self.__balance += amount
        return "ok"


    def withrday_balance(self,amount):
        self.__balance -= amount
        return "ok"
acc = BankAccount("fawfdw", 2222222220,"e3wfreq")


print(acc.owner)
print(acc.balance)
print(acc.transfers)



# def add_stars(func):
#     def wrapper():
#         print("************")
#         func()
#         print("************")
#     return wrapper

# @add_stars
# def greet():
#     print("Hello, World")

# @add_stars
# def greet_class():
#     print("Hello, Class")

# greet() 
# greet_class()
# # add_stars(greet)
# # add_stars(greet_class)

class Animal:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < self.__price:
            print("Insufficient amount")
        else:
            self.__price = new_price


a = Animal("Lucy", 500)
print(f"Animal price is {a.price}")
a.price = 1
print(f"Animal price is {a.price}")
#a.set_price(1)

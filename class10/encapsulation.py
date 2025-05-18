# Access modifiers
# public, private, protected
class Animal:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price < self.__price:
            print("Insufficient amount")
        else:
            self.__price = new_price


cat = Animal("Lucy", 1000)
print(f"Name of cat is {cat.name}")
print(f"price of cat is {cat.get_price()}")
cat.set_price(1)
print(f"price of cat is {cat.get_price()}")

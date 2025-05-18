# Access modifiers
# public, private, protected
class Animal:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def sell_animal(self):
        print(f"{self.__price} price is {self.__price}")


cat = Animal("Lucy", 1000)
cat.sell_animal()
print(cat.__price)

cat.sell_animal()

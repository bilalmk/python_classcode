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

    def sell_animal(self, price):
        if price <= 0:
            print("invalid amount)")
        elif price >= self.__price:
            print(f"Animal sold at {price}")
        else:
            print("invalid amount")


a = Animal("Lucy", 500)
print(f"Animal price is {a.get_price()}")
a.sell_animal(500)

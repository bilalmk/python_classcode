# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"{self.x},{self.y}"

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)

#     def __eq__(self, other):
#         if self.x == other.x and self.y == other.y:
#             return True
#         else:
#             return False


# p1 = Point(10, 10)
# p2 = Point(10, 20)

# # p3 = p1 + p2
# # print(p3)
# if p1 == p2:
#     print("objects are same")
# else:
#     print("objects are different")


class BankAccount:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        self.facilities = ["withdraw", "deposit", "transfer", "credit card"]

    def __str__(self):
        return f"{self.title} has {self.balance} rs balance"

    def __add__(self, other):
        return BankAccount(f"{self.title} & {other.title}", self.balance + other.balance)
    
    def __len__(self):
        return len(self.facilities)
    
    def __getitem__(self, index):
        return self.facilities[index]

a1 = BankAccount("Bilal", 1000)
a2 = BankAccount("Aneeq", 2000)

# a = a1 + a2
# print(a)

#print(len(a1))
print(a1[1])
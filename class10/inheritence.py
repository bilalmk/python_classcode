# class Father:
#     def __init__(self):
#         self.eye_color = "Green"

#     def speak(self):
#         print("Father says: Always speak truth")


# class Mother:
#     def __init__(self):
#         self.good_at_math = True

#     def help_to_solve_problem(self):
#         return "Let me help you in math"


# class Child(Father, Mother):
#     def __init__(self):
#         Father.__init__(self)
#         Mother.__init__(self)
#         self.name = "Jamal"
#         self.sports = "Cricket"

#     def play_cricket(self):
#         print(f"{self.name} like to bowl")


# f = Father()
# c = Child()

# print(f"Father Eye color : {f.eye_color}")
# print(f"Child name : {c.name}")
# print(f"Child Eye Color : {c.eye_color}")
# c.speak()
# print("="*30)
# print("Child is good at math", c.good_at_math)
# print("child is love to help:", c.help_to_solve_problem())
# print("="*30)
# print("child hobby is :",c.sports)
# print("Love to :",c.play_cricket())


# class Car:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model

#     def start_engine(self):
#         print("engine start")

#     def drive(self):
#         print("clucth press")
#         print("gear change")
#         print("accelrator press")
#         print("release clutch")
#         print("move")

#     def stop(self):
#         print("press break")
#         print("car stop")


# class AutoCar(Car):
#     def __init__(self, name, model, car_type):
#         super().__init__(name, model)
#         self.car_type = car_type

#     def drive(self):
#         print("gear change")
#         print("accelrator press")
#         print("move")

# manual = Car("Toyota", 2024)
# manual.drive()
# print("="*30)
# auto = AutoCar("Toyota", 2024, "Automatic")
# auto.drive()

# class A():
#     def name(self):
#         print("value is A")

# class B(A):
#     def name(self):
#         print("value is B")

# class C(A):
#     def name(self):
#         print("value is C")

# class D(C,B):
#     def name(self):
#         print("value is D")

# d = D()
# d.name()


# class Humen:
#     def __init__(self, name):
#         self.name = name
#         self._age = 30
#         self.__salary = 1000


# class Student(Humen):
#     def __init__(self, n, r):
#         super().__init__(n)
#         self.roll_number = r


# class Teacher(Student):
#     def __init__(self, name, roll_number):
#         super().__init__(name, roll_number)


# t = Teacher("Ratan", 12345)
# print(t.name, t.roll_number)


# ===================================
class Animal:
    def __init__(self, color, age):
        self.__color = color
        self._age = age

    def get_color(self):
        return self.__color

    def make_noise(self):
        print("animal makes noise")


class Dog(Animal):
    def __init__(self, color, age, price):
        super().__init__(color, age)
        self.__price = price

    def sell(self, price):
        print("sold at ", price)

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price < self.__price:
            print("Insufficient amount")
        else:
            color = self.get_color()
            self.__price = new_price
            if color == "White":
                self.__price += 500
            if self._age >= 4:
                self.__price += 500
                
            
d = Dog("White", 5, 1000)
d.set_price(2000)
print("\n\n")
print(d.get_price())

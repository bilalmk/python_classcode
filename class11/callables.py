def greet():
    print("hello world")


# greet()

# print(callable(greet))


# class Person:
#     def speak(self):
#         print("Person can speak")

#     def __call__(self, message):
#         print(message)


# p = Person()
# # print(callable(Person))
# # print(callable(p))
# p("Hello I am callable object")


class AddNumbers:
    def __init__(self, base_number):
        self.base_number = base_number

    def add_number(self, number):
        print(number + self.base_number)

    def __call__(self, number):
        print(number + self.base_number)


add_to_10 = AddNumbers(10)
# add_to_10.add_number(15)
# add_to_10.__call__(10)
add_to_10(10)
class Student:
    internet = "Gerrys"
    cmd = "Screen"
    quarter = "q3"
    city = "Karachi"
    counter = 0

    def __init__(self, name, roll_number):
        # instance variables
        # only available through instances
        self.name = name
        self.roll_number = roll_number
        Student.counter += 1

    @classmethod
    def get_quarter(cls):
        return cls.quarter

    @classmethod
    def change_quarter_value(cls, quarter_name):
        cls.quarter = quarter_name

    def get_roll_number(self):
        return self.roll_number

    @staticmethod
    def is_adult(age):
        if age >= 18:
            print("Yes its adult")
        else:
            print("its minor")


s1 = Student("Ali", 1)
print(s1.counter)
s2 = Student("Jamal", 2)
print(s2.counter)

# print("student 1 city", s1.city)
# Student.city = "Lahore"
# print("student 2 city", s2.city)
# print(Student.city)
print(Student.get_quarter())
Student.change_quarter_value("q4")
print(Student.get_quarter())
Student.is_adult(17)
s1.is_adult(19)


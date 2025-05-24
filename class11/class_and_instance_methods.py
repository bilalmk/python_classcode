class Student:
    # 1) class variables can be accessed by the class name
    # 2) class variables can be accessed but can not modified by the instance of the class
    # 3) class variables are shared by all instances of the class
    # 4) class variables are defined outside of __init__ method
    # 5) class variables are defined inside the class but outside of any method
    internet = "Gerrys"
    cmd = "Screen"
    quarter = "q3"
    city = "Karachi"
    counter = 0

    def __init__(self, name, roll_number):
        # instance variable can only accessed by the instance of the class
        # instance variable can only be updated by the instance of the class
        # instance variable are defined inside __init__ method
        # class instances can only access class variables but can not modified them
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


class Person:
    def __init__(self, name):
        print("constructor is calling")
        self.name = name
    
    def __del__(self):
        print("destructor is calling")
        
p = Person("Salman")
del p
    

class Person():
    def __init__(self , n , a , e , g):
        self.name = n
        self.age = a
        self.email = e
        self.game = g
    
    def hello(self):
        return f"hello {self.name}"
        
    def helloAge(self):
        return f"hello {self.age}"
        
        
        
    
p1 = Person("ratan lal", 25, "ratan@lal.com", ["A", "B", "C"])
p2 = Person("chaman lal", 50, "chaman@lal.com", ["E", "F", "G"])
p3 = Person("gulzari lal", 70, "gulzari@lal.com", ["E", "F", "G"])

print(p1.name,p1.age,p1.email, p1.game, p1.helloAge())
print(p2.name,p2.age,p2.email, p2.game, p2.hello())
print(p3.name,p3.age,p3.email, p3.game)
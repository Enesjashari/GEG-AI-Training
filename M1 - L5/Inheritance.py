

#Python 

#Inheritance = Trashegemia ne OOP ,

# pse perdoret ?
# Perdoret qe mos me peresit kodin , DRY

# Pse eshte e rendesishme qe me pas DRY ? 
# Maintainable i kodit 

# pass  == kalo



# Single Inheritance
from pyclbr import Class


class Users:
    def Password(self):
        return "Password must be min 8 chars...."


class Student(Users):
    pass
    

student1 = Student() 
# print(student1.Password())







# MultiLevel Inheritance

class Vehicle:
    def start_engine(self):
        return "Engine has started ...."
    

class Kerri(Vehicle):
    def ece(self):
        return "Automjekti po ece ...."
    

class Aeroplani(Kerri):
    def fly(self):
        return "Aeroplane can fly"


v1 = Vehicle()
k1 = Kerri()

# print(k1.start_engine())
# print(k1.ece())



a1 = Aeroplani()

print()

# print(a1.start_engine())
# print(a1.ece())
# print(a1.fly())






# Hierarchical  Inheritance

class Users():
    def can_check_in(self):
        return "Perdorusi munden me ba check in/scan"
    

class Profesori(Users):
    def upload_lecture(self):
        return "Profesori mund te vendos ligjeraten ne e-service"
        
    def nota(self):
        return "Profesori vendos noten e lendes"


class Student(Users):
    def attend_exams(self):
        return "Studenti mund te hyje ne provim."
    

class Admin(Users):
    def add():
        return "Mund te shtoj perdorus te ri"
    
    def delete():
        return "Mund te fshij perdorus aktual"
    




# Multiple Inheritance

class Njeriu:
    def ece(self):
        return "Mund te ec"
    

class Fish:
    def notoj(self):
        return "Mund te noton"
    

class Duck(Njeriu , Fish):
    pass
    #sepse Duck edhe mund te ece edhe te noton


d = Duck()

print(d.ece())
print(d.notoj())



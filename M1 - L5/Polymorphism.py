#Polymorphism - Eshte perdororimi i te njejtes metode mirpo ne forma ne ndryshme(kthen output tjeter secilen here)



class Cat:
    def speak(self):
        return "Cat can not speak"
    
class Parrot:
    def speak(self):
        return "Parrot Can speak"
    


def polymoprpism(animal):
    print(animal.speak())


c = Cat()
p = Parrot()

polymoprpism(c)
polymoprpism(p)





class Admin:
    def access(self):
        return "Admin has all access"
    
class User:
    def access(self):
        return "User has limited access"
    


def polymoprpism(human):
    print(human.access())



a = Admin()
u = User()


polymoprpism(a)
polymoprpism(u)
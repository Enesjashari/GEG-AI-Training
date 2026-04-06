

#Encapsulation - Menyra e fshehjes se te dhenave

#public     = Preferohet/Mundet te perdoret ne te gjithe file dhe files te tjere
#protected  = Preferohet qe attr/metoda te perdoret vetem brenda klases dhe file
#private    = Mund te perdoret vetem brenda class



class Number:
    a = 10
    _b = 20
    __c = 30

    
    def get_c(self):
        return self.__c

    def set_c(self,new_c):
        self.__c = new_c
        
n = Number()

n.a=10.2
print(n.a)

n._b = 20.23
print(n._b)

n.set_c(33)
print(n.get_c())


# print(n.__c)   AttributeError: 'Number' object has no attribute '__c'
# Nese na duhet me perdor jashte class ateher duhet me perdor getters & setters








# Per cka perdoret class

# class perdoret zakonisht(IRL : Per me kriju Tabela te Databazes , check datatypes(FastAPI Schemas) , )



# class User:
#     ID
#     name
#     surname




# class Profesori:
#     lenda 
#     notimi


# class Studenti :
#     semestri
#     lenda
#     mesatarja
#     provimi 


# Global Variable
# name = "Eliot"





'''class Useri:
    # Class Variables dhe jane Local Variables
    name = "Eliot"
    surname = "Alderson"
    age = 27


# Objekt apo Instance
user1 = Useri()
user2 = Useri()
#Objekti ==  variable = Class_name() 


print(user1.name)
print(user1.surname)
print(user1.age)


print(user2.name)
print(user2.surname)
print(user2.age)'''



# __init__   = Konstruktori- Pranon vlera nga jasht
# self -> Nje default variable e cila sherben per me ju qase variablave ne objektit brenda klases(ne metoda etj )
class Useri:
    def __init__(self ,name ,surname ,age):
        self.name    = name
        self.surname = surname
        self.age     = age
        
    # self perdoret ne funksion nese don me ju qase variable te konstuktorit
    def return_user(self):
        print(self.name, self.surname, self.age)


user1 = Useri("Elliot" ,"Alderson" ,27)
user2 = Useri("Alma",'Hoxha',20)
user3 = Useri("Ereza","Thaqi",20)



user1.return_user()
user2.return_user()
user3.return_user()



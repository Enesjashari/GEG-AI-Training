
# CRUD me list,array x
# Dimenzionet x
#Shape 
#Reshaping
# Join
# Search
#Filter
#Sort


#Ex1  Array1

#----------------------------------
#Tuple, dictionary , set


import numpy as np 

#                   0   1   2    3  4
array1 = np.array([100,200,300,400,500])


# print(array1[2])


#lista
list1 = [100,200,300,400,500]

#CRUD ne list 
#append() -> Shton nje element ne fund te listes
#insert() -> Shton nje element ne baze te indexit


print("Para: ",list1)

list1.append(600)
list1.append('apple')


# list1.
list1.insert(4,'orange')
list1.insert(0,"kiwi")




#Read

print(list1[0])
print(list1[5])
print(list1[-1])
# print(list1)

#Update
#Syntax  list_name[index] = new_value

list1[2] = "Kosova"
list1[-1] = "Austria"

list1[-4] = "mango"


#delete dhe remove
del list1[0]
del list1[-3]

list1.remove("mango")
list1.remove("Austria")

print("Pas: ",list1)


#Te krijohet nje list me 5 elemente qfardo x
#te shtohet nje element ne fund dhe nje ne indexin 4
#te behen update 2 elementet e para 
#te fshihen 2 elementet e para
#printo te gjithe listen

'''# lista me 5 elemente
lista = [10, 20, 30, 40, 50]
print(lista)
 
# Te shtohet nje element ne fund dhe nje me indeksin 4
lista.append(60)
lista.insert(4, 45)
print("Pas shtimit:", lista)
 
# Te behen update 2 elementet e para
lista[0] = 15
lista[1] = 25
print("Pas update:", lista)
 
# Te fshihen dy elementet e para
del lista[0]
lista.remove(25)
 
# Printo listen perfundimtare
print("Lista perfundimtare:", lista)
'''



print('------------------------------')


array3 = np.array([1000 , 2000 , 3000 , 4000])


#CRUD
#Create
print("Para: ", array3)
new_array = np.append(array3 , 5000)
# print("Pas: ", new_array)


#Read
print(new_array[4])
print(new_array[0])

#Update
new_array[0] = 5
new_array[1] = 2

#delete
new_array  = np.delete(new_array ,2 )
new_array  = np.delete(new_array ,3 )

print("Pas: ", new_array)



#Numpy

# ctrl + `` == open terminal 


# Cka quajm array ?

# Array quajm nje grup te disa elementeve/vlerave , 


# Si doket nje array ?

# [1 ,3 ,4 ,5 ,7 , 9 ,1, 10]



# List vs Array(Numpy in Python)


# Listat jane data structure ne Python te cilat perdoren per me rujt vlera/elemente .


# definimi i nje liste ne python 

#         0     1    2    3   4   5   6  7? 
numrat = [10 , 20 , 30 , 40 ,50 ,60 ,70 ]

# type() => Type kthen tipin e nje variable(string , integer , bool , float , list , tuple , dictionray)
print(numrat)  # Atehere po printohen te gjitha elementet qe jane brenda listes 
print(type(numrat))


print(numrat[4])

print(numrat[6])

# print(numrat[7])  #IndexError: list index out of range


# Task 2 min 
# Desc: Te krijohet nje list e cila perman 15 elemente , dhe prino elementet me index tek ?


# List vs Array(Numpy in Python) ? 
 
# Arrays jane 70x me te shpejta se listat ne Python ?
# Listat munden me pas elemente te tipi ne nje list , ndersa arrays duhet me qene te tipit te njejt

#           0      1        2        3       4    5
list_mix = [10 , 3.14 , 'Python' , False , True , 100]  
#           -6   -5      -4         -3      -2     -1

# Nje element perfaqesohet prej 2 indexave , njani pozitiv dhe tjetri negativ, mirpo nje index nuk mundet me i perfaqsu 2 elemente.


print(list_mix[0]) # ? 10 , 100 
print(list_mix[-5])
print(list_mix[1])



# Array


# Si te krijojm nje array ?

print('----------------------------------------------')
import numpy 


array1  = numpy.array([100,200,300,400,500])

print(array1)

# Si mujm me vertetu qe eshte array dhe list == type()

print(type(array1))

# Indexing

print(array1[0])
print(array1[1])
print(array1[2])


#                           0            1          2         3          4        5
array2 = numpy.array(['Fushe Kosove','Prishtin','Ferizaj','Mitrovic','Lipjan',"Rahovec"])


print(array2[0])
print(array2[4])


# Qytetet ku kemi me shume perdorus te applikacionit E-Kosova
qytetet_kosove = numpy.array([
    "Prishtinë","Vushtrri","Prizren","Pejë","Gjilan",
    "Prishtinë","Pejë","Vushtrri","Prishtinë","Gjilan",
    "Prizren","Prishtinë","Pejë","Vushtrri","Prishtinë",
    "Gjilan","Prishtinë","Prizren","Pejë","Prishtinë",
    "Vushtrri","Gjilan","Prishtinë","Pejë","Prishtinë",
    "Prishtinë","Vushtrri","Prishtinë","Gjilan","Prizren",
    "Pejë","Prishtinë","Gjilan","Vushtrri","Prishtinë",
    "Pejë","Prishtinë","Gjilan","Vushtrri","Prishtinë",
    "Prizren","Pejë","Prishtinë","Gjilan","Prishtinë",
    "Vushtrri","Prishtinë","Pejë","Gjilan","Prishtinë"
])

# sum() -> Ben mbledhjen 

count0 = qytetet_kosove == "Prishtinë"

print(count0)

# Output
"""[ True False False False False  True False False  True False False  True
 False False  True False  True False False  True False False  True False
  True  True False  True False False False  True False False  True False
  True False False  True False False  True False  True False  True False
 False  True]"""

count = numpy.sum(qytetet_kosove == 'Prishtinë')

print(count)





array2 = numpy.array(['Fushe Kosove','Prishtin','Ferizaj','Mitrovic','Lipjan',"Rahovec"])


# .size -> tregon sa elemente i kemi brenda ne Array


print(array2.size)
print(qytetet_kosove.size)



# Task:  Generate nje list me 10 nota te studentit dhe gjej mesataren e notave ?

# Shembull: [6,8,10,10,10,9,7,8,10]





# Alma Hoxha

import numpy as np
 
notat = np.array([8, 9, 7, 10, 6, 9, 8, 7, 10, 8])
mesatarja = np.mean(notat)
 
print("Mesatarja:", mesatarja)
 


# Agnesa Baliu

import numpy as np
 
#  Lista
notat_studentit = np.array([6, 8, 10, 7, 6, 8, 9, 10, 7, 9])
 
# 3 mesatarja e notave
mesatarja = np.mean(notat_studentit)

print("Mesatarja e notave:", mesatarja)



# Lorjana Maliqi
notat = [ 8, 9, 10, 8, 7, 6, 8, 9]
 
mesatarja = 0

c=len(notat)

for i in notat:

	mesatarja+=i

mesatarja=mesatarja/c

print(mesatarja)
 


# Ne Numpy kemi funksione te gatshme si mean , median , min , max

notat_studentit = np.array([6, 8, 10, 7, 6,1, 8, 9, 10, 7, 9])

# mean() -> Mean e kthen mesataren e array

print(notat_studentit.mean())

#median() -> Kthen vleren e 2 numrave te mesit 

print(numpy.median(notat_studentit))


#max() -> Kthen vleren maximale ne array

print(notat_studentit.max())


#min() -> Kthen vleren minimale ne array

print(notat_studentit.min())

# Ne numpy kemi Array Multi Dimenzionale , next Lecture >>>








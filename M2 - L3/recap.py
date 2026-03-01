


#CRUD - Create , Read , Update , Delete


numrat = [ 50 , 35 ,45 ,80, 90]

#Ne rastin kur kemi list brenda list , quhet nested list 



#           0                1                    2    3   4   5
numrat = [ 50 ,['Prishta','Prezreni','Ferizaj'] , 35 ,45 ,80, 90]
#                 0            1         2 


print(numrat)
print(numrat[0])
print(numrat[1])
print(numrat[4])
print(numrat[1][0])
print(numrat[1][1])
print(numrat[1][2])


#             0                          1                           2                    3                 4                      5 
shtetet = ['Kosova',['Prishtine','Ferizaj','Vushtrri',"Mitrovic"],'Shqiperi',['Tirana','Durrsi','Vlore'],'Amerika',['Florida','Utah','New Mexico']]
#                       0            1         2          3                      0         1        2                   0        1        2

print(shtetet)
print(shtetet[1][2])
print(shtetet[3][0])
print(shtetet[5][2])




x =[ 
    'Kosova',['Prishtine','Ferizaj','Vushtrri',"Mitrovic"],
    'Shqiperi',['Tirana','Durrsi','Vlore'],
    'Amerika',['Florida','Utah','New Mexico']
    ]





universiteti = [
    "UBT", [
        ["Shkenca Kompjuterike", ["Programim", "Algoritme", "Databaza"]],
        ["Menaxhment", ["Marketing", "Financa", "Kontabilitet"]],
        ["Arkitekturë", ["Projektim", "Urbanizëm", "Konstruksione"]]
    ]
]


# Shfaq:
# Algoritme
# Kontabilitet
# Projektim


# Algoritme
print(universiteti[1][0][1][1])

# Kontabilitet
print(universiteti[1][1][1][2])

# Projektim
print(universiteti[1][2][1][0])

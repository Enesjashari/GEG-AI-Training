



import numpy as np 


array1 = np.array(10)


# D = Dimensions
# .ndim -> Kthen int , tregon numrin e D
# .shape -> Kthen tuple, Tregon madhesin se secilit D
print(array1.ndim)
print(array1.shape)


#Sa D i kemi ne Python

#0 D
#1 D
#2 D
#3 D
#4 D
# Multi Dimensionals


# x = [[10,20]]


print('-------------')
array2 = np.array([1,2,3,4,50])


print(array2.ndim)
print(array2.shape)


print('-------------')

array3 = np.array([ [10,20,30],[40,50,60] ])

print(array3.ndim)
print(array3.shape)

# (shape) = (numri i rreshtave, numri i kolonave)




#Old 

# select * from Users where name = "Enes"; None

'''
            Users
-------------------------------
name , surname , email, ...
Rron   
Enis ,  Jashari  ,  ejashari@auk.org
Arta
'''



# old way of search  



'''
            Users
-------------------------------
name , surname , email, ...
Rron   
Enes ,  Jashari  ,  ejashari@auk.org
Arta
'''


'''

          embedding
------------------------------
name ,                    surname , email, ...
[-0912,92,3,21,54,321,23]   
[0.128,54,56,18,385] ,  Jashari  ,  ejashari@auk.org
Arta

'''


# Vector Databases

'''
import numpy as np

# lejo printim të plotë
np.set_printoptions(threshold=np.inf)

embedding = np.random.rand(3072)

print("Shape:", embedding.shape)
print("Dimensions:", embedding.ndim)
print(embedding)
'''
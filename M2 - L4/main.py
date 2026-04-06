
# Search 
# Sort



# where -> funksion i cili kerkon nje vlere brenda nje array
import numpy as np


array1 = np.array([10,20,30,40,50,60,70,80,90,100])


number1 = np.where(array1 == 70 )
number2 = np.where(array1 == 20 )
number3 = np.where(array1 == 110 )

print(number1)
print(number2)
print(number3)



array2 = np.array( [ [0,1,2,3,4,5,6,7,8,9] , [10,20,30,40,50,60,70,80,90,100] ] )


number5 = np.where(array2 == 5)
number5 = np.where(array2 == 1)


number5 = np.where(array2 == 10)
number5 = np.where(array2 == 100)

print(number5)


#-----------------------------------------------------------------------
# sort 

array_1d = np.array([42, 7, 19, 3, 88, 25, 61])

array_1d_sorted = np.sort(array_1d)

print(array_1d_sorted)


#--------------------------------------
array_2d = np.array([
    [9, 2, 15, 4],
    [20, 1, 7, 13],
    [6, 18, 5, 11]
])

array_2D_sorted = np.sort(array_2d)

print(array_2D_sorted)




#--------------------------------------
print()
array_3d = np.array([
    [
        [5, 12, 1],
        [9, 3, 14]
    ],
    [
        [7, 10, 2],
        [8, 6, 11]
    ]
])

array_3d_sorted = np.sort(array_3d)

print(array_3d_sorted)



#--------------------------------------
print()
print()
print()


array_4d = np.array([
    [
        [
            [4, 9],
            [1, 7]
        ],
        [
            [12, 3],
            [8, 5]
        ]
    ],
    [
        [
            [6, 2],
            [11, 10]
        ],
        [
            [14, 13],
            [0, 15]
        ]
    ]
])


array_4d_sorted = np.sort(array_4d)

print(array_4d_sorted)
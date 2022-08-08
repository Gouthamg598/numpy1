'''printing of matrix elements in spiral format'''


'''printing matrix in spiral formate  [row=i][column=j]'''

import numpy as np

# a=np.array([i for i in range(1,17)])
# m=a.reshape(4,4)
# print(m)

m=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])
i=0
for j in range(4):
    print(m[i][j],end=' ')
for i in range(1,4):
    print(m[i][j],end=' ')
for j in range(2,-1,-1):
    print(m[i][j],end=' ')
for i in range(2,0,-1):
    print(m[i][j],end=' ')
for j in range(1,3):
    print(m[i][j],end=' ')
for j in range (2,0,-1):
    print(m[2][j],end=' ') 
    
    '''==output=='''
    
    1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 


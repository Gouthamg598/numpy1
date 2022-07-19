'''equal number of elements should be arrange in each row'''
# from operator import matmul
# import numpy as np

# a=np.array([[1,2,3,6]])
# b=np.array([[2,9,7,4]])

# print(a+b)#[[ 3 11 10 10]]
# print(a-b) #[[-1 -7 -4  2]]

# a=([5,8,7],[8,9,6])
# b=([9,8,6])
# c=np.array(a)+np.array(b)
# print(c)#[[14 16 13] 
            # [17 17 12]]
    
# a=np.array([[5,8,7],[8,9,6]])
# b=np.array([[9,8,6],[1,2,3]])
# print(a+b) # [[14 16 13] 
#            # [ 9 11  9]]

# a=([5,8,7],[8,9,6])
# b=([9,8])
# c=np.array(a)+np.array(b)
# print(c)#ValueError: operands could not be broadcast together with shapes (2,3) (2,)

# a=np.array([[5,8,7],[8,9,6]])
# b=np.array([[9,8,6],[1,2,3]])
# print(a-b) # [[-4  0  1] 
#             # [ 7  7  3]]

'''normal multiplication '''
# a=np.array([[5,8,7],[8,9,6]])
# b=np.array([[9,8,6],[1,2,3]])
# print(a*b)#[[45 64 42] 
          #  [ 8 18 18]] 
          
'''matrix multiplication two methods using "@" and matmul(a,b)'''
# import numpy as np
# a=np.array([[1,2,3],[7,5,3],[7,8,9]])
# b=np.array([[2,3,6],[2,5,8],[1,3,6]])
# print(a@b)#[[  9  22  40] 
#         #    [ 27  55 100] 
#         #    [ 39  88 160]]

# a=np.array([[1,2,3],[7,5,3],[7,8,9]])
# b=np.array([[2,3,6],[2,5,8],[1,3,6]])
# print(matmul(a,b))#[[  9  22  40] 
                    # [ 27  55 100] 
                    # [ 39  88 160]]
'''we can't multiply more than two matrices using matmul(a,b)'''
'''but usiing "@" we can multiply '''   
# import numpy as np 
             
# a=np.array([[1,2,3],[7,5,3],[7,8,9]])
# b=np.array([[2,3,6],[2,5,8],[1,3,6]])
# c=np.array([[2,3,6],[2,5,8],[1,3,6]])
# d=np.array([[2,3,6],[2,5,8],[1,3,6]])
# e=np.array([[2,3,6],[2,5,8],[1,3,6]])
# # print(matmul(a,b,c,d,e))#TypeError: matmul expected 2 arguments, got 5

# print(a@b@c@d@e)    #[[ 13866  35033  64064] 
#                     #  [ 35484  89648 163940] 
                    #  [ 56010 141509 258776]]   
                    
# a=np.array([[1,11,22,33],[1,11,111,1111]])

# print(a+5)#[[   6   16   27   38] 
            #  [   6   16  116 1116]
            
# print(a*2)
#[[   2   22   44   66] 
#  [   2   22  222 2222]]

# print(a/2)

# a=np.array([[20,3,4],[20,3,4],[20,3,4]])
# print(a**2)
# [[400   9  16] 
#  [400   9  16] 
#  [400   9  16]]

# import numpy as np
'''eye is a idntity matrix-I [1 0][0 1] defalt it is in float, eye(size of matrix)'''
# a=np.eye(2)
# print(a)  # [[1. 0.] 
            #  [0. 1.]]
            
# a=np.eye(2,dtype=int)
# print(a) #[[1 0] 
#         #  [0 1]]

# a=np.eye(3,dtype=int)
# print(a) #[[1 0 0] 
        #  [0 1 0] 
        #  [0 0 1]]
        
# a=np.eye(2,dtype=bool)
# print(a)#[[ True False] 
           #  [False  True]]
           
# b=np.array([x for x in range(9)])
# a=b.reshape(3,3)
# print(a)
        #[[0 1 2] 
#  [3 4 5] 
#  [6 7 8]]

# b=np.array([x for x in range(12)])
# a=b.reshape(4,3)
# print(a)
# [[ 0  1  2] 
#  [ 3  4  5] 
#  [ 6  7  8] 
#  [ 9 10 11]]
'''to chage the datatype from float to int using ==astype'''
# a=np.array([[1.5,2.6,3.3]])
# print(a.astype('int'))
# # [[1 2 3]]
'''to make arrays horizontal using==hstack(variables)'''
# a=np.array([[1,2,3],[7,8,9]])
# b=np.array([[4,5,6],[10,11,12]])
# print(np.hstack((a,b)))  #[[ 1  2  3  4  5  6] 
#                             #[ 7  8  9 10 11 12]]

'''to make arrays vertical using==vstack(variables)'''
# a=np.array([[1,2,3],[7,8,9]])
# b=np.array([[4,5,6],[10,11,12]])
# print(np.vstack((a,b))) 
# [[ 1  2  3] 
#  [ 7  8  9] 
#  [ 4  5  6] 
#  [10 11 12]]
'''tio make list into  array using np.array(variable) or using np.arange(start,end,increment)'''
# t=[x for x in range(9)]
# u=np.array(t)
# print(u)  #[0 1 2 3 4 5 6 7 8]
# print(u.reshape(3,3))#[[0 1 2] 
#  [3 4 5] 
#  [6 7 8]]

# a=np.arange(0,20,2)
# print(a)#[ 0  2  4  6  8 10 12 14 16 18]
# print(a.reshape(5,2))

# [[ 0  2]
#  [ 4  6]
#  [ 8 10]
#  [12 14]
#  [16 18]]


# print(a.reshape(2,5))   #[[ 0  2  4  6  8] 
                        #  [10 12 14 16 18]]

'''to know the matching postions between two arrays'''

# a=np.array([1,2,3,4,5])
# b=np.array([1,3,2,4,5])
# print(np.where(a==b))#(array([0, 3, 4], dtype=int64),)


'''to get similar elements use==np.fill(rows,columns)'''

# a=np.full((3,2),5)
# print(a)#[[5 5] 
        #  [5 5] 
        #  [5 5]]

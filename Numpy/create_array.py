import numpy as np


"""1 dimension"""
A = np.array([1,2,3])
print(A)
#[1 2 3]
print(type(A))
#[1 2 3]
print(np.zeros(7))
#[0. 0. 0. 0. 0. 0. 0.]
print(np.ones(12))
#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
print(np.empty(3).size)
#np.empty create an array but dont assign  value
print(np.arange(10,dtype= float))
#[0 1 2 3 4 5 6 7 8 9]
print(np.arange(10,20))
#[10 11 12 13 14 15 16 17 18 19]
print(np.arange(10,20,3))
#[10 13 16 19]
print(np.linspace(0,10,5))
#[ 0.   2.5  5.   7.5 10. ]
print(np.asarray(A)) # copy
#[1 2 3]
print(np.ones_like(A)) 
#create an nd array same as a but value are all one
#[1 1 1] 
print(np.zeros_like(A)) 
#create an nd array same as a but value are all zero
#[0 0 0] 
print(np.empty(A)) 
#create an nd array same as a but value are all empty
print(np.full(5,8))
#[8 8 8 8 8]
print(np.random.random((2,3)))
#[[0.57281141 0.98874283 0.44597598]
 #[0.0412086  0.64839552 0.04160949]]
print("+++++++++++++++++++")


""" two dimension """
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])
print(A.shape)
#(2,3)
print(A.size)
#6
print(A.sum())

print(np.empty([3,2]))
#[[0. 0.]
#[0. 0.]
#[0. 0.]]
print(np.zeros([2,3]))
print(np.ones([2,3]))
#[[0. 0. 0.]
# [0. 0. 0.]]
print(np.eye(3))
#print(np.identity(3))
#[[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]


""" three dimension"""
print(np.array([
    [[1,2,3],[4,5,6]],
    [[1,2,3],[4,5,6]],
    [[1,2,3],[4,5,6]]
]   
))
#3*2*3
print(np.empty([3,1,2]))
print(np.ones([2,2,2]))
print(np.zeros([1,1,4]))

"""high dimension"""
print(np.array([
    [
        [1,1],
        [2,2]   
    ]
]))
print(np.ones([2,1,1,2]))

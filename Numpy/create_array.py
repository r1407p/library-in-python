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
print(np.arange(10))
#[0 1 2 3 4 5 6 7 8 9]
print(np.arange(10,20,3))
#[10 13 16 19]

""" two dimension """
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])
print(np.empty([3,2]))
#[[0. 0.]
#[0. 0.]
#[0. 0.]]
print(np.zeros([2,3]))
print(np.ones([2,3]))
#[[0. 0. 0.]
# [0. 0. 0.]]

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
print(np.array([2,1,1,2]))
import numpy as np

#creating arrays

arr = np.array([5,6,7,3])
a = np.array([[1,1,2],[3,4,3]])

# dimension, size and shape of the array

print("The dimension is: ",arr.ndim)
print("arr.size = The total no. of ele in the array: ",arr.size)
print("a.shape = The no.of ele stored in each dimension",a.shape)

# The main difference between the two is that range is a built-in Python class, 
# while arange() is a function that belongs to a third-party library (NumPy). In addition, their purposes are different! Generally, 
# range is more suitable when you need to iterate using the Python for loop.

print(np.arange(1,7,2)) #arange(start, stop, step)
print(np.zeros(6))
print(np.ones(4))

#create empty array with 3 elements

print(np.empty(3))

# linspace and arange : linspace allows number of steps and arange allows the size of steps

print(np.arange(1,10,2)) 
print(np.linspace(1,10,2))

print("np.sort(arr): After sorting: ",np.sort(arr))
b = np.array([[1,2],[4,5]])
c = np.array([[1,1],[4,5]])
print("After concatenating :\n ",np.concatenate((b,c),axis=1))  #axis=1 rowwise 0 column wise

print("After reshaping : ",a.reshape(3,2))

# INDEXING 

d = np.array([1,2,3,4]) #one dim
print("first ele: ",d[0])


e = np.array([[1,2,3],[4,5,6]])
print(e[0,1])

f = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,0],[1,2]]])
print("f[0,2,1] : ",f[0,2,1]) # 3d


# SLICING

# he basic slice syntax is i:j:k where i is the starting index, 
 # j is the stopping index, and k is the step
    
s = np.array([1,2,3,4,66,51])  # 1d array slicing
s[2:5:1]  # x[i : j-1: k]

#both are same

print(s[::-1])
print(s[:])

print(s[1:-1])

print("\n")

print("To create an array from existing data: Indexing, Slicing, hstack, vstack, hsplit, view, copy ")

print("\n")

v1 = np.arange(1,10,2)
print(v1)
v2 = np.arange(10,20,2)
print(v2)
print("stacking vertically:  ",np.vstack((v1,v2))) # no.of elements must be same in two arrays

h1 = np.ones(v1.shape)
print(h1)
h2 = np.zeros(v2.shape)
print(h2)
print("Stacking Horizontally: ",np.hstack((h1,h2)))

# creating arrays

import numpy as np

a = np.array([2,3,4,6])

print(np.zeros(a.shape))

print(np.ones(a.shape))

print(np.full((a.shape),3)) # np.full(shape,element to full)

print(np.eye(3,dtype="int")) # np.eye(no.of rows) creates Identity matrix

v1 = np.arange(1,10,2) # np.arange(start, stop, size.ofsteps)
print(v1)

print(np.linspace(1,10,3)) # np.linspace(start, stop, no. of steps)

print("\n")

# numpy.random.random() is one of the function for doing random sampling in numpy. 
# It returns an array of specified shape 
# and fills it with random floats in the half-open interval [0.0, 1.0).

print(np.random.random((2,3))) # np.random.random(size)


      




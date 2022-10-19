#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
# Convert list to numpy array
normalList = [1,2,3]
numpyArray = np.array(normalList)
print(numpyArray)

# Iteration in Python list
for i in normalList:
    print(i)
for i in numpyArray:
    print(i)

# Append values into list 

List = normalList + [4]
print(List)
List.append(5)
print(List)

# Append values into numpyArray is not Possible

Array = numpyArray + [4]
print(Array)
# Array.append(5)

# Array Operations 
Array1 = Array + Array
print("Array1 = ",Array1)

# List result to Concatinations
List1 = List + List
print("List1 = ",List1)

# Vector Addition of a list
List2 = []
for i in List:
    List2.append(i + i)

print("List2 = ",List2)    

# Multiplication in Python Array

print("Multiplication = ", (Array1 * 2))

# Multiplication in List
List3 = []
print("Multiplication2 = ",(List2 * 2))
for i in List2:
    List3.append(i * 2)
print(List3)

# Power of Python Array

print("Power of = ",(Array1**2))

# Power of Python List
List3 = []
for i in List2:
    List3.append((i**2))
print(List3)    
    
# Square Root of Array
print("Square root of Array = ",(np.sqrt(Array1)))

# Logarithm in each element of an Array

print("Log of an Array = ", (np.log(Array1)))

# Exponent of each element of an Array

print("Exponent of Array = ",(np.exp(Array1)))


# Python Array Operations

a = np.array([1,2,3])
b = np.array([[1,2],[3,4],[5,6]])

print("a[0] = ", a[0])
print("b[0] = ", b[0])
print("b[0][0] = ", b[0][0])

# Numpy Matrix

M = np.matrix([[1,2],[3,4],[5,6]])
print(M)
print(b[0,0])
print(M[0,0])
print("b =  ", b)
# Transpose of Matrix
print("b.T = ", b.T)

# Matrix Dimensions
print("Dimension = ",b.shape)

c = b.T
print("C-Dimension = ",c.shape)

# Number Dimension of Matrix / Array

print("b.ndim = ",b.ndim)

# Size of Matrix / Array

print("b.size = ", b.size)
print("c.size = ", c.size)

# Data Type of Matrix / Array
print("b.dtype = ",b.dtype)
print("c.dtype = ",c.dtype)

# Floating point in Numpy Array
floatArr = np.array([1.2, 2.4,3.6,4.0])
print("floatArr = ", floatArr)
floatMatrix = np.matrix([[1.2, 2.4,3.6],[2.3,4.5,6.7]])
print("floatMatrix = ",floatMatrix)

# Checking Type of an Array / matrix

print("Type of floatArr: ",floatArr.dtype)
print("Type of floatMatrix: ", floatMatrix.dtype)


# Change Data Type of an Array
float1 = np.array([3,2,1], np.dtype('float64'))
print("float1 = ", float1)
# Size
print("float1 size = ",float1.size)

# Item Size
print("float1 Item Size = ", float1.itemsize)
print("Item Size of a = ", a.itemsize)

# Maximum and Minimum
print("Maximum of b = ",b.max())
print("Minimum of b = ", b.min())

# Sum of Array Element
print("Sum of  b = ", b.sum())

# Vertical (axis = 0) & Horizontal (axis = 1) Sum
print("Sum of axis 0 = ",b.sum(axis = 0))
print("Sum of axis 1 = ", b.sum(axis = 1))

# Array of zeros with specific Dimensions
print("Zeros Array = ", np.zeros((3,3)))

# Array of ones with specific Dimensions
print("Ones Array = ", np.ones((3,3)))

# Array of ones with specific Dimensions and Data Type
print("Ones Array = ", np.ones((3,3), np.dtype('int64')))

# Array of zeros with specific Dimensions and Data Type
print("Zeros Array = ", np.zeros((3,3), np.dtype('int64')))

# Array of empty variables with specific Dimensions and Data Type
print("Empty Array = ", np.empty((3,3), np.dtype('int16')))

# Array of empty List with specific Dimensions and Data Type
print("Empty Array = ", np.empty([3,3], np.dtype('int64')))

# Array range
print("Array Range = ", np.arange(1,5))
# Array range with Interval of 2
print("Array Range = ", np.arange(0,10,2))

# Space values
print("Space values = ",np.linspace(0,5))

# Space values
print("Space values = ",np.linspace(0,5, 10))

# Array of Random Numbers
print("Random Numbers = ",np.random.random((3,3)))

# Reshape Array
reshape = np.zeros((2,3))
print("reshape = ",reshape)
print("reshapes = ",reshape.reshape((3,2)))

# Vertical & Horizontal stack
v = np.zeros((3,3))
h = np.ones((1,3))
print("v = ", v)
print("h = ",h)

g = np.vstack((v,h))
print("g = ",g)

f= np.ones((3,1))
print("f = ",f)
i = np.hstack((v,f))
print("i = ", i)

# Vertical  & Horizontal Split
print("Split Vertical ", np.vsplit(i,3))
print("Split Horizontal ", np.hsplit(g,3))



# In[ ]:





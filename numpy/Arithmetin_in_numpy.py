import numpy as np
#
# #these are basic scalar arithmetic
# array = np.array([1.1,2.2,3.1] )
#
# print(array+1)
#
# print(array/2)
#
# print(array-1)
#
# print(array**5)
#
#
# # now we are usung vectorIZED MATH FUNCTION
#
#
# print(np.sqrt(array))
#
# print(np.ceil(array))
#
# print(np.pi)


#find the area
print("the area of ciircel")
radii =np.array([1,2,3])

print(np.pi*(radii**2))

print("element wise arithemetic")
#Element wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1*array2)
print(array1/array2)
print(array1**array2)

#to check the scores of the students and return a boollean valure or the scores it self basically COMPARISION OPRATORS
scores = np.array([91,23,56,100,82,64])

print(scores>60)

scores[scores<60]=0
print(scores)



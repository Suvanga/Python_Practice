#slicing example using numpy
import numpy as np

array =np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

print(array[0:2:2]) #This is row selection

#array[start:end:step]

print("Column selection")
print(array[:,1:3]) #start end step is after the [":",start:end:step ]

print("now we are selecting both rows and columns")

print(array[0:2,2:4])
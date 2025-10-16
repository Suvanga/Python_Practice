import numpy as np

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape)
print(array2.shape)

print("the way we know that both of them are compatible is by comparing the the shape aligned with each other is either a 1 "
      "or it is the same number example 10 10 or 10 1")
print(array1*array2)

print("another example is that it will npt be compatible if tghey can not be multipleed that is what basically bpradcasrting with matrix mean")
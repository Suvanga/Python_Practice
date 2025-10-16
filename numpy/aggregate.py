# here we discuss the statisitic math function we can use for matrixes
import numpy as np

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.max(array))
print(np.min(array))
print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.median(array))
print(np.var(array))

print(""
      "if you want to find the index of the value")
print(np.argmin(array))

print("we can also select the axis for the arrays, we choose axis 0 for column sum and 1 for row sum")
print(np.sum(array, axis =0))
print(np.sum(array, axis =1 ))
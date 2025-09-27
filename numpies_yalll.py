import numpy as np

# array = np.array([1,2,3,4,5])

print(np.__version__)
print("hello world")
array = np.array(
[[['A','B','C'],['D','E','F'], ['G','H','I']],
[['j','k','l'],['m','n','o'], ['p','q','r']],
[['A','B','C'],['D','E','F'], ['G','H',' ']]]
)

print(array.ndim)
print(array.shape)

word = array[0,0,0] + array[0,0,2]+ array[0,2,1] + array[0,2,2] + " "+ array[1,0,1] + array[0,2,1]+ array[0,0,0]
print(word)

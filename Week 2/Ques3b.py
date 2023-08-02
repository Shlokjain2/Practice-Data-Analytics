import numpy as np

x = np.random.random((5, 5))
print("Original Array:")
print(x)
print(x[::2, 1::2])
#x[startAt:endBefore:skip]
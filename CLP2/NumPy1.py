import numpy as np  

matrix = np.random.randint(1, 10, size=(5, 5))

row_sums = matrix.sum(axis=1)

print("Matrix:\n", matrix)
print("Row-wise sums:", row_sums)

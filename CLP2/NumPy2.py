import numpy as np

arr = np.random.rand(100)

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("Normalized array:", normalized)

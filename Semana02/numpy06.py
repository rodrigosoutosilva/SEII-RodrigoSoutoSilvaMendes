import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3, 2, 1],[5,-5,4],[6,0,1]])
c = np.array([4,3,0])

print(np.linalg.solve(A,c))
print(np.linalg.eig(A))

w, v = np.linalg.eig(A)
print(A@v[:,1])
print(w[1]*v[:,1])
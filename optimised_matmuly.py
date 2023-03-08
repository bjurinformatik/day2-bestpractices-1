# Finished after day2 so improved using numpy

import numpy as np

# NxN matrix
def RandomMatrix1(N):
    X = np.random.randint((100), size = (N,N))
    return(X)

#Nx(N+1) matrix
def RandomMatrix2(N):
    Y = np.random.randint((100), size = (N,N+1))
    return(Y)

# Multiply matrices
def MultiplyMatrix(X, Y):
    result = np.matmul(X, Y)   
    return(result)

# Run and print out result
N = 250
X = RandomMatrix1(N)
Y = RandomMatrix2(N)
result = MultiplyMatrix(X, Y)
print(result)

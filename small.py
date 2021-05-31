import numpy as np
def multmatrix():
    
    X = np.random.rand(100,100)
    Y = np.random.rand(100,100)
    result = np.zeros((100,100))
    for i in range(len(X)):
   # iterate through columns of Y
        for j in range(len(Y[0])):
       # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
                

    for r in result:
        print(r)

if __name__ == "__main__":
    #solver()
    multmatrix()
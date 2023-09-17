import numpy as np

def mahala(x,y,mcov):
    resta=np.array(x) - np.array(y)
    invmcov=np.linalg.inv(mcov)
    maha = np.sqrt(np.dot(np.dot(resta, invmcov), resta))
    
    return maha

# Ejemplo de uso
v1 = [1, 2, 3]
v2 = [4, 5, 6]
matriz_cov = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
dist = mahala(v1, v2, matriz_cov )
print(f"Distancia Mahalanobis: {dist}")
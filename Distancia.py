def Minkowski(x, y, p):
    if len(x) != len(y):
        print("Las medidas de 'x' y 'y' deben coincidir")
        return None
        
    suma = 0
    for i in range(len(x)):
        suma += abs(x[i] - y[i])**p
    
    mink = suma**(1/p)
    return mink

# Manhattan
v1 = [1, 2, 3]
v2 = [4, 5, 6]
p_manhattan = 1
dist_manhattan = Minkowski(v1, v2, p_manhattan)

print(f"Distancia de Manhattan: {dist_manhattan}")

# Euclidiana
p_euclidiana = 2
dist_euclidiana = Minkowski(v1, v2, p_euclidiana)

print(f"Distancia Euclidiana: {dist_euclidiana}")




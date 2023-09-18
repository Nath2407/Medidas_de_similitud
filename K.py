import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Generar un conjunto de datos de Iris con seis puntos de forma aleatoria
iris = datasets.load_iris()
X, y = iris.data, iris.target

puntos_por_clase = 2

# Inicializar lista
indices_seleccionados = []

# Recorrer cada clase
for clase in np.unique(y):

    # Obtener los índices de la clase actual
    indices_clase = np.where(y == clase)[0]
    
    # Seleccionar aleatoriamente 2 puntos de la clase actual
    indices_seleccionados_clase = np.random.choice(indices_clase, puntos_por_clase, replace=False)
    
    # Agregar los índices seleccionados a la lista (extend para que no los agarre como un par)
    indices_seleccionados.extend(indices_seleccionados_clase)

# Obtener los puntos y etiquetas de los puntos seleccionados
puntos_seleccionados = X[indices_seleccionados]
etiquetas_seleccionadas = y[indices_seleccionados]

# Distancia euclidiana
def distancia_euclidiana(punto1, punto2):
    return np.linalg.norm(punto1 - punto2)

# Inicializar diccionario que guarde las distancias entre los puntos seleccionados y el resto de los puntos
distancias = {}

# Enumerate para darle seguimiento de la posición y valor al mismo tiempo
for i, punto1 in enumerate(puntos_seleccionados):
    distancias[i] = {}
    for j, punto2 in enumerate(X):
        if i != j:  # Evitar un posible error al calcular distancia en un mismo punto
            dist = distancia_euclidiana(punto1, punto2)
            distancias[i][j] = dist

# Imprimir las distancias del 1-150 de cada punto
for i, dist_dict in distancias.items():
    print(f'Distancias para Punto {i + 1}:')
    for j, dist in dist_dict.items():
       print(f'  Punto {j + 1}: {dist:.4f}')

# Ordenar las distancias para cada punto seleccionado en orden ascendente e imprimirlo
for i, dist_dict in distancias.items():
    # Sorted para ordenar el diccionario 
    distancias_ordenadas = sorted(dist_dict.items(), key=lambda x: x[1])
    
    print(f'Distancias en orden asdcendente para Punto {i + 1}:')
    for j, dist in distancias_ordenadas:
        print(f'  Punto {j + 1}: {dist:.4f}')
        

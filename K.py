import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Generar un conjunto de datos de Iris con seis puntos de forma aleatoria
iris = datasets.load_iris()
X, y = iris.data, iris.target
np.random.seed(0)
indices = np.random.choice(range(len(X)), 6, replace=False)
X_sample = X[indices]
y_sample = y[indices]

# Dividir los datos en conjunto de entrenamiento y prueba (opcional)
X_train, X_test, y_train, y_test = train_test_split(X_sample, y_sample, test_size=0.2, random_state=42)

# Crear un clasificador k-NN con k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el clasificador con los datos de entrenamiento
knn.fit(X_train, y_train)

# Realizar predicciones en los datos de prueba
y_pred = knn.predict(X_test)

# Imprimir las predicciones y las etiquetas verdaderas
print("Predicciones:")
print(y_pred)
print("Etiquetas verdaderas:")
print(y_test)

# Calcular la precisión del modelo
accuracy = np.mean(y_pred == y_test)
print("Precisión del modelo:", accuracy)

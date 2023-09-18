 K vecinos
k = 6

# Clasificar los puntos evaluados
etiquetas_estimadas = []
for i, dist_dict in distancias.items():
    # Obtener los k vecinos más cercanos
    k_vecinos = sorted(dist_dict.items(), key=lambda x: x[1])[:k]
    
    # Obtener las etiquetas de los k vecinos
    etiquetas_k_vecinos = [y[j] for j, _ in k_vecinos if j < len(y)]
    
    # Votar por la clase más común
    clase_estimada = max(set(etiquetas_k_vecinos), key=etiquetas_k_vecinos.count)
    etiquetas_estimadas.append(clase_estimada)

# Graficar todos los puntos
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs = axs.ravel()

# Colores y etiquetas para cada clase
colors = ['red', 'green', 'blue']
labels = ['Setosa', 'Versicolor', 'Virginica']

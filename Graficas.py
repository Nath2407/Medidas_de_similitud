# Graficar todos los puntos
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs = axs.ravel()

# Colores y etiquetas para cada clase
colors = ['purple', 'black', 'red']
labels = ['Setosa', 'Versicolor', 'Virginica']

for i in range(4):
    for j, (color, label) in enumerate(zip(colors, labels)):
        axs[i].scatter(X[y==j, i], X[y==j, (i+1)%4], c=color, cmap='viridis', label=label)
        axs[i].scatter(puntos_seleccionados[:, i], puntos_seleccionados[:, (i+1)%4], c=etiquetas_seleccionadas, cmap='viridis', marker='x', label='Evaluado')
        for k, punto in enumerate(puntos_seleccionados):
            axs[i].text(punto[i], punto[(i+1)%4], f'{etiquetas_estimadas[k]}', fontsize=8, ha='center')
        axs[i].set_xlabel(iris.feature_names[i])
        axs[i].set_ylabel(iris.feature_names[(i+1)%4])
        axs[i].set_title('Clasificación de puntos evaluados')
        axs[i].legend()

plt.show()
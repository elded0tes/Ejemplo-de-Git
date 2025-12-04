#Importamos los paquetes necesarios

import pandas as pd 
import matplotlib.pyplot as plt

import seaborn as sns

atletas = pd.read_csv('corredores.csv', index_col=0)
#index_col=0 indicamos que tenemos titulo de columnas
atletas.info()

#Ver encabezados y primeros 5 filas
atletas.head()

#Crear histograma de la variable tiempo
plt.figure(1)
plt.hist(atletas['Tiempo'], 15, color='blue', ec='black')
plt.title('Histograma Tiempo Actualizado')
plt.savefig('Histograma.jpg')

#Conocer la frecuencia de una variable que es categorica
plt.figure(2)
sns.countplot(x=atletas['Velocidad'], palette='ocean')
plt.savefig('Velocidades.jpg')

#Crear grafico con velocidades de hombres y mujeres
plt.figure(3)
grafico3 = sns.countplot(x='Genero', hue='Velocidad', palette='hot_r', data=atletas)
grafico3.set(title='Velocidades por Genero', xlabel='Genero', ylabel='Total')
plt.title('Grafico de Barras vs Genero')
plt.savefig('Genero.jpg')
plt.show()





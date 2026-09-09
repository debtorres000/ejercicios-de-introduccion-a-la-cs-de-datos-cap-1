import matplotlib.pyplot as plt
from pathlib import Path

# Ejercicio 1.1
#Grafica de Muertes por accidentes por Celular

años = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

muertes = [311, 276, 258, 240, 199, 205, 197, 194]

plt.figure(figsize=(10, 5))
plt.plot(años, muertes, marker='o', color='red', linestyle='--')
plt.title('Muertes automovilistica por celular')
plt.xlabel('Años')
plt.ylabel('Contador de Muertes')
plt.grid(True)

carpeta_imagenes = Path(__file__).resolve().parents[1] / 'Imagenes'
plt.savefig(carpeta_imagenes / 'grafica_ejercicio_1_1.png', dpi=150, bbox_inches='tight')
plt.show()
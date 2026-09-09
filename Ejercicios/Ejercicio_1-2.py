import matplotlib.pyplot as plt
from pathlib import Path

# Ejercicio 1.2
# Altura de los árboles

datos_arboles = {
    'Coast redwood': 116.92,
    'Sitka spruce': 101.2,
    'Yellow meranti': 99.53,
    'Southern blue gum': 91.7,
    'Manna gum': 89.9,
    'Brown top\nstringybark': 89.5,
    'Mengaris': 86.76,
    'Shorea angoretiifolia': 85.85,
    'Shining gum': 85.3,
    'Western hemlock': 84.34
}

arboles = list(datos_arboles.keys())
alturas = list(datos_arboles.values())

plt.figure(figsize=(12, 6))
plt.bar(arboles, alturas, color='lightblue')
plt.title('Altura de árboles en un ambiente específico')
plt.xlabel('Especie del árbol')
plt.ylabel('Altura (m)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

carpeta_imagenes = Path(__file__).resolve().parents[1] / 'Imagenes'
plt.savefig(carpeta_imagenes / 'grafica_ejercicio_1_2.png', dpi=150)
plt.show()
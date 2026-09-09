import matplotlib.pyplot as plt
from pathlib import Path

# Ejercicio 1.3
# Distribución de actividades evaluadas

datos_actividades = {
    'Assignments': 10,
    'Quizzes': 5,
    'Graded discussion board': 5,
    'Practical labs': 5,
    'Midterm exams': 30,
    'Final term exams': 40
}

actividades = list(datos_actividades.keys())
porcentajes = list(datos_actividades.values())

etiquetas = [
    f'{actividad}\n{porcentaje}%'
    for actividad, porcentaje in datos_actividades.items()
]

plt.figure(figsize=(8, 8))
plt.pie(porcentajes, labels=etiquetas, startangle=90)
plt.title('Distribución de las actividades')
plt.tight_layout()

carpeta_imagenes = Path(__file__).resolve().parents[1] / 'imagenes'
plt.savefig(carpeta_imagenes / 'grafica_ejercicio_1_3.png', dpi=150)
plt.show()
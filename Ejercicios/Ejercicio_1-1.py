import matplotlib.pyplot as plt

# Ejercicio 1.1

años = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

muertes = [311, 276, 258, 240, 199, 205, 197, 194]

plt.figure(figsize=(10, 5))
plt.plot(años, muertes, marker='o', color='b', 	linestyle='-')
plt.title('Muertes automovilistica por celular')
plt.xlabel('Años')
plt.ylabel('Contador de Muertes')
plt.grid(True)
plt.show()
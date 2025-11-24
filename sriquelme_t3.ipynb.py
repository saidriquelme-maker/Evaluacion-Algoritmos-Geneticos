#Corea del Sur - Población por Regiones
# nOMBRE: Said Amaro Riquelme Ríos
# Carrera: Ing. Mecánica
#Ramo: Lenguaje de Programacion (Sección 1)
#Fecha: 09-11-2025
# Aqui esta la explicación profesor melquisedec
# 
# en el siguiente programa se muestra la población de Corea del Sur dividida en tres zonas:
# 1- Norte 2- Centro 3- Sur 
# 
#aQUI utilice programación orientada a objetos (POO)
#para definir clases que representan las regiones y el país como es solicitado en intranet.
# 
# Luego se usa matplotlib para crear un gráfico de barras con la población de cada zona.

import matplotlib.pyplot as plt

# ## Clases (POO)
class Region:
    def __init__(self, nombre, poblacion):
        self.nombre = nombre
        self.poblacion = poblacion

class Pais:
    def __init__(self, nombre, regiones):
        self.nombre = nombre
        self.regiones = regiones

    def graficar(self):
        nombres = []
        poblaciones = []
        for r in self.regiones:
            nombres.append(r.nombre)
            poblaciones.append(r.poblacion)

        plt.bar(nombres, poblaciones, color=["skyblue", "lightgreen", "salmon"])
        plt.title(f"Población por regiones de {self.nombre}")
        plt.xlabel("Regiones")
        plt.ylabel("Habitantes")

        # Mostrar números arriba de cada barra
        for i, p in enumerate(poblaciones):
            plt.text(i, p + 200000, f"{p:,}", ha="center")

        plt.show()
# crear las regiones y graficar (Matplotlib)

# datos sacados según del internet
norte = Region("Norte", 8000000)
centro = Region("Centro", 30000000)
sur = Region("Sur", 13000000)

# KR CON las regiones
corea = Pais("Corea del Sur", [norte, centro, sur])
corea.graficar()
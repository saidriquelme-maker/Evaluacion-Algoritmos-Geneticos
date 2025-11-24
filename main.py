import numpy as np
import random
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

# ==========================================
# CONFIGURACIÓN DEL ALGORITMO GENÉTICO
# ==========================================
TAMANO_POBLACION = 10
GENERACIONES = 5
PROBABILIDAD_MUTACION = 0.1

# Cargamos datos de Scikit-Learn (Iris Dataset)
data = load_iris()
X, y = data.data, data.target

# ==========================================
# DEFINICIÓN DE FUNCIONES (DOCUMENTADO)
# ==========================================

def crear_individuo():
    """
    Crea un 'individuo' (una posible solución).
    En este caso, el individuo es un número entero que representa 
    la profundidad máxima (max_depth) del árbol de decisión (entre 1 y 10).
    """
    return random.randint(1, 10)

def crear_poblacion(tamano):
    """Genera una lista de individuos iniciales aleatorios."""
    return [crear_individuo() for _ in range(tamano)]

def fitness(individuo):
    """
    Función de Aptitud (Fitness): Evalúa qué tan bueno es el individuo.
    Entrena un modelo de Scikit-Learn con el parámetro del individuo
    y retorna su precisión (accuracy).
    """
    # Creamos el modelo con el gen (parametro) del individuo
    clf = DecisionTreeClassifier(max_depth=individuo, random_state=42)
    
    # Usamos validación cruzada para probar su rendimiento real
    scores = cross_val_score(clf, X, y, cv=5)
    return scores.mean()

def seleccion(poblacion):
    """
    Selecciona a los mejores padres basándose en su puntaje de fitness.
    Ordena la población y se queda con la mitad superior.
    """
    # Ordenamos por fitness de mayor a menor
    poblacion_ordenada = sorted(poblacion, key=fitness, reverse=True)
    # Retornamos la mejor mitad (elitismo simple)
    return poblacion_ordenada[:len(poblacion)//2]

def cruce(padre1, padre2):
    """
    Operador de Cruce (Crossover).
    Toma dos padres y produce un hijo. Aquí usamos un promedio simple 
    convertido a entero, simulando mezcla genética.
    """
    hijo = int((padre1 + padre2) / 2)
    # Aseguramos que el hijo sea válido (al menos profundidad 1)
    return max(1, hijo)

def mutacion(individuo):
    """
    Operador de Mutación.
    Con una probabilidad baja, cambiamos el gen aleatoriamente para
    introducir diversidad y evitar estancamiento.
    """
    if random.random() < PROBABILIDAD_MUTACION:
        return random.randint(1, 10)
    return individuo

# ==========================================
# EJECUCIÓN PRINCIPAL (MAIN LOOP)
# ==========================================

if __name__ == "__main__":
    print(f"--- Iniciando Algoritmo Genético con Scikit-Learn ---")
    
    # 1. Crear población inicial
    poblacion = crear_poblacion(TAMANO_POBLACION)
    
    for generacion in range(GENERACIONES):
        print(f"\nGeneración {generacion + 1}: {poblacion}")
        
        # 2. Selección (Sobreviven los más aptos)
        padres = seleccion(poblacion)
        
        # 3. Reproducción (Llenar la nueva generación)
        nueva_poblacion = padres[:] # Mantenemos a los padres (elitismo)
        
        while len(nueva_poblacion) < TAMANO_POBLACION:
            # Seleccionar dos padres al azar de los ganadores
            p1 = random.choice(padres)
            p2 = random.choice(padres)
            
            # Cruzar
            hijo = cruce(p1, p2)
            
            # Mutar
            hijo = mutacion(hijo)
            
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion

    # RESULTADO FINAL
    mejor_individuo = seleccion(poblacion)[0]
    print(f"\n--- Optimización Finalizada ---")
    print(f"El mejor hiperparámetro encontrado (max_depth) es: {mejor_individuo}")
    print(f"Precisión estimada: {fitness(mejor_individuo)*100:.2f}%")
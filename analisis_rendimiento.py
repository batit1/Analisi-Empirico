
import time
import timeit
import random

N_ELEMENTOS = 1_000_000 
LISTA_GRANDE = [random.randint(1, 100) for _ in range(N_ELEMENTOS)]


try:
    from memory_profiler import profile
except ImportError:
    print("ADVERTENCIA: 'memory_profiler' no se cargó. Asegúrate de usar 'python -m memory_profiler <archivo>.py'")
    def profile(func):
        return func


def suma_con_bucle(lista):
    """Suma con bucle for (Puro Python). Más lenta debido al overhead del intérprete."""
    total = 0
    for elemento in lista:
        total += elemento
    return total

def suma_con_sum(lista):
    """Suma con función nativa sum() (Implementación en C). Mucho más rápida."""
    return sum(lista)

def medir_tiempo_sumas():
    print("\n" + "="*50)
    print("=== 1. MEDICIÓN DE TIEMPO (1 MILLÓN DE ELEMENTOS) ===")
    print("="*50)

    print("\n--- 1.1 Medición con 'time' (Medición única) ---")
    
    inicio_bucle = time.time()
    suma_con_bucle(LISTA_GRANDE)
    tiempo_bucle = time.time() - inicio_bucle
    print(f"Bucle for (time): {tiempo_bucle:.6f} segundos")

    inicio_sum = time.time()
    suma_con_sum(LISTA_GRANDE)
    tiempo_sum = time.time() - inicio_sum
    print(f"Función sum (time): {tiempo_sum:.6f} segundos")

    print("\n--- 1.2 Medición con 'timeit' (5 repeticiones) ---")

    SETUP_CODE = f'import random; LISTA_GRANDE = [random.randint(1, 100) for _ in range({N_ELEMENTOS})]'
    
    TIMEIT_BULOOP = timeit.repeat(
        setup=SETUP_CODE,
        stmt='suma_con_bucle(LISTA_GRANDE)',
        repeat=5,
        number=1,
        globals={'suma_con_bucle': suma_con_bucle, 'LISTA_GRANDE': LISTA_GRANDE}
    )
    avg_time_bucle = min(TIMEIT_BULOOP)
    print(f"Bucle for (timeit min): {avg_time_bucle:.6f} segundos")

    TIMEIT_SUM = timeit.repeat(
        setup=SETUP_CODE,
        stmt='suma_con_sum(LISTA_GRANDE)',
        repeat=5,
        number=1,
        globals={'suma_con_sum': suma_con_sum, 'LISTA_GRANDE': LISTA_GRANDE}
    )
    avg_time_sum = min(TIMEIT_SUM)
    print(f"Función sum (timeit min): {avg_time_sum:.6f} segundos")
    
    print("\n--- Conclusión de Tiempo ---")
    if avg_time_sum > 0:
        print(f"La función sum() (C-implementada) es aproximadamente {(avg_time_bucle / avg_time_sum):.2f} veces más rápida que el bucle for (Python puro).")
    print("Ambos enfoques tienen una complejidad asintótica de O(N).")


@profile
def crear_lista_grande(n):
    """
    Crea una lista. La memoria aumenta linealmente O(N).
    """
    print(f"\n--- 2.1 CREAR LISTA (O(N) Memoria) ---")
    
    lista = [random.randint(1, 100) for _ in range(n)]
    
    print(f"Tamaño final de la lista: {len(lista)}")
    return len(lista)

@profile
def crear_generador_grande(n):
    """
    Crea un generador. La memoria se mantiene constante O(1).
    """
    print(f"\n--- 2.2 CREAR GENERADOR (O(1) Memoria) ---")

    def generador_numeros(n):
        for i in range(n):
            yield random.randint(1, 100)
    
    gen = generador_numeros(n) 
    
    contador = 0
    for _ in gen:
        contador += 1
    
    print(f"Elementos producidos por el generador: {contador}")
    return contador

def medir_memoria():
    print("\n" + "="*50)
    print("=== 2. MEDICIÓN DE MEMORIA ===")
    print("="*50)
    print(f"Probando con N = {N_ELEMENTOS} elementos.")
    
    crear_lista_grande(N_ELEMENTOS)
    crear_generador_grande(N_ELEMENTOS)

    print("\n--- Conclusión de Memoria ---")
    print("El generador exhibe O(1) (constante) uso de memoria, mientras que la lista exhibe O(N) (lineal).")



if __name__ == '__main__':
    medir_tiempo_sumas()
    medir_memoria()
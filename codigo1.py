import time
import timeit
import random

LISTA_GRANDE = [random.randint(1, 100) for _ in range(1_000_000)]

def suma_con_bucle(lista):
    """Calcula la suma de los elementos de una lista usando un bucle for."""
    total = 0
    for elemento in lista:
        total += elemento
    return total

def suma_con_sum(lista):
    """Calcula la suma de los elementos de una lista usando la función nativa sum()."""
    return sum(lista)

print("--- Medición con 'time' ---")

inicio_bucle = time.time()
resultado_bucle = suma_con_bucle(LISTA_GRANDE)
fin_bucle = time.time()
tiempo_bucle = fin_bucle - inicio_bucle

print(f"Resultado (bucle): {resultado_bucle}")
print(f"Tiempo de ejecución (bucle): {tiempo_bucle:.6f} segundos")

inicio_sum = time.time()
resultado_sum = suma_con_sum(LISTA_GRANDE)
fin_sum = time.time()
tiempo_sum = fin_sum - inicio_sum

print(f"Resultado (sum): {resultado_sum}")
print(f"Tiempo de ejecución (sum): {tiempo_sum:.6f} segundos")


print("\n--- Medición con 'timeit' (5 repeticiones) ---")

SETUP_CODE = '''
import random
LISTA_GRANDE = [random.randint(1, 100) for _ in range(1_000_000)]
def suma_con_bucle(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
def suma_con_sum(lista):
    return sum(lista)
'''

TIMEIT_BULOOP = timeit.repeat(
    setup=SETUP_CODE,
    stmt='suma_con_bucle(LISTA_GRANDE)',
    repeat=5,
    number=1 
)
avg_time_bucle = min(TIMEIT_BULOOP)
print(f"Tiempo promedio/mínimo (bucle con timeit): {avg_time_bucle:.6f} segundos")


TIMEIT_SUM = timeit.repeat(
    setup=SETUP_CODE,
    stmt='suma_con_sum(LISTA_GRANDE)',
    repeat=5,
    number=1
)
avg_time_sum = min(TIMEIT_SUM) / 1
print(f"Tiempo promedio/mínimo (sum() con timeit): {avg_time_sum:.6f} segundos")

print("\n--- Comparación de Resultados ---")
print(f"El enfoque con sum() fue aproximadamente {(avg_time_bucle / avg_time_sum):.2f} veces más rápido.")
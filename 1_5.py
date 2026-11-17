import time
import numpy as np
# Импортируем наш скомпилированный модуль Cython
import sum_squares

def sum_python(arr):
    total = 0
    for x in arr:
        total += x * x
    return total

print("Генерация данных")
n_elements = 10**7
data = list(np.random.rand(n_elements))

start = time.time()
res_py = sum_python(data)
time_py = time.time() - start
print(f"Время Python: {time_py:.4f} сек")

start = time.time()
res_cy = sum_squares.sum_squares_cython(data)
time_cy = time.time() - start
print(f"Время Cython: {time_cy:.4f} сек")

print(f"Результаты совпадают: {np.isclose(res_py, res_cy)}")

if time_cy > 0:
    print(f"Ускорение: в {time_py / time_cy:.1f} раз")
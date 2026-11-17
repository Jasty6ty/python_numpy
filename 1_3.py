import numpy as np
import time

print("\nзадача 3.1")
file_name = 'large_array.dat'
shape = (1000, 1000)
mmap_array = np.memmap(file_name, dtype='float64', mode='w+', shape=shape)
mmap_array[:] = np.random.rand(*shape)
print(f"Файл {file_name} создан. Размер: {mmap_array.nbytes / 1e6:.2f} MB")

print("\nзадача 3.2")
read_mmap = np.memmap(file_name, dtype='float64', mode='r', shape=shape)

col = read_mmap[:, 500]
row = read_mmap[500, :]
print(f"Прочитан столбец (форма {col.shape}), первые 3 элемента: {col[:3]}")
print(f"Прочитана строка (форма {row.shape}), первые 3 элемента: {row[:3]}")

print("\nзадача 3.3")
def obxod_row(arr):
    total = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            total += arr[i, j]
    return total

def obxod_col(arr):
    total = 0
    for j in range(arr.shape[1]):
        for i in range(arr.shape[0]):
            total += arr[i, j]
    return total

# Замеряем время
start = time.time()
obxod_row(read_mmap)
time_row = time.time() - start

start = time.time()
obxod_col(read_mmap)
time_col = time.time() - start

print(f"Время обхода по строкам (row-major): {time_row:.4f} сек")
print(f"Время обхода по столбцам (column-major): {time_col:.4f} сек")

import numpy as np

print("задача 2.1")
A = np.random.randint(-10, 10, size=(4, 5))
print("Массив A:\n", A)

row_1 = A[1, :]
print("\nВторая строка:", row_1)

col_3 = A[:, 3]
print("Столбец с индексом 3:", col_3)

sub_array = A[1:4, 2:5]
print("Подмассив (строки 1-3, столбцы 2-4):\n", sub_array)


print("\nзадача 2.2")
fancy_result = A[[0, 2, 3], [1, 4, 1]]
print("Элементы по индексам:", fancy_result)


print("\nзадача 2.3")
A_copy = A.copy()
A_copy[A_copy < 0] = 0
print("Массив после замены отрицательных чисел на 0:\n", A_copy)


print("\nзадача 2.4")
# Создаем массив B формы (4, 1)
B = np.array([[1], [2], [3], [4]])
# Создаем массив C формы (1, 5)
C = np.array([[10, 20, 30, 40, 50]])

print("Массив B (4, 1):\n", B)
print("Массив C (1, 5):\n", C)

result = B + C
print("\nРезультат сложения (B + C) без циклов:\n", result)
print("Форма результата:", result.shape)
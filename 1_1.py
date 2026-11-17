import numpy as np

print("задача 1.1")
arr = np.array([0.1, 0.2, 0.3], dtype=np.float32)
sum_float32 = np.sum(arr)
e_sum = 0.1 + 0.2 + 0.3

print(f"Сумма float32: {sum_float32}")
print(f"Точное значение (float64): {e_sum}")
print(f"Разница: {abs(sum_float32 - e_sum)}")

print("задача 1.2")
info32 = np.finfo(np.float32)
info64 = np.finfo(np.float64)

print(f"Машинное эпсилон для float32: {info32.eps}")
print(f"Машинное эпсилон для float64: {info64.eps}")



print("задача 1.3")

a = 1.000000000000001
b = 1.000000000000000
result = a - b

print(f"a = {a}")
print(f"b = {b}")
print(f"a - b = {result}")


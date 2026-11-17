import numpy as np
import scipy.sparse as sp
import time

print("задача 4.1")
d_5x5 = np.random.rand(5, 5)
d_5x5[d_5x5 > 0.2] = 0

csr_mat = sp.csr_matrix(d_5x5)
print("Матрица CSR:\n", csr_mat.toarray())
print("Плотность:", csr_mat.nnz / (5*5))

print("\nзадача 4.2")
coo_mat = csr_mat.tocoo()
csc_mat = csr_mat.tocsc()
print("Преобразование выполнено.")

print("\nзадача 4.3")
vector = np.array([1, 2, 3, 4, 5])
result = csr_mat.dot(vector)
print("Результат умножения:", result)

print("\задача 4.4")
N = 1000
density = 0.01
sparse_large = sp.random(N, N, density=density, format='csr')
dense_large = sparse_large.toarray()
vec_large = np.random.rand(N)

start = time.time()
_ = sparse_large.dot(vec_large)
time_sparse = time.time() - start

start = time.time()
_ = dense_large.dot(vec_large)
time_dense = time.time() - start

print(f"Время умножения разреженной матрицы: {time_sparse:.6f} сек")
print(f"Время умножения плотной матрицы: {time_dense:.6f} сек")
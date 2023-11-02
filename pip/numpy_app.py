import numpy as np

vector_a = np.array([1, 2, 3, 4])
print(vector_a)
print(vector_a**2)
print(vector_a*5)

# bedanya dengan list, list tidak bisa di kuadrat
# contoh list: data = [1,2,3,4]
# alasan menggunakan numpy karena memprmudah dalam matrix atau vector

# matrix ordo 2
matrix_b = np.array([(1, 2), (3, 4)])
print(matrix_b)
print(matrix_b**2)

# matrix 0
zeros_c = np.zeros((2, 2))
print(zeros_c)

# matrix 1
ones_d = np.ones((2, 2))
print(ones_d)

# melakukan perhitungan matrix
jumlah = matrix_b + matrix_b**2 + ones_d
print(jumlah)

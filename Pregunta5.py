# Pivoteo parcial por filas
# Solución a Sistemas de Ecuaciones

from numpy import array, zeros, dot, diag

A = array([[4., -1., 0., -1.], [-1., 4., -1., 0.], [-1., 0., -1., 4.], [0., -1., 4., -1.]])
B = array([[30.], [60.], [70.], [40.]])


def GEPP(A, b):

#Eliminacion Gaussiana con pivoteo
    n = len(A)
    if b.size != n:
        raise ValueError("Argumento inválido: tamaños incompatibles entre A y B", b.size, n)

    for k in range(n - 1):
        maxindex = abs(A[k:, k]).argmax() + k
    if A[maxindex, k] == 0:
        raise ValueError("La Matriz es singular")

    if maxindex != k:
        A[[k, maxindex]] = A[[maxindex, k]]
        b[[k, maxindex]] = b[[maxindex, k]]

    for row in range(k + 1, n):
        multiplier = A[row][k] / A[k][k]

        A[row][k] = multiplier
        for col in range(k + 1, n):
            A[row][col] = A[row][col] - multiplier * A[k][col]
        b[row] = b[row] - multiplier * b[k]
    x = zeros(n)
    k = n - 1
    x[k] = b[k] / A[k, k]
    while k >= 0:
        x[k] = (b[k] - dot(A[k, k + 1:], x[k + 1:])) / A[k, k]
        k = k - 1
    return x


print('La  Matriz ingresada es:\n')
print(A, B)
Aug = GEPP(A, B)
print('\nLas soluciones para este sistema de ecuaciones (X1, X2, X3, X4) respectivamente son:\n')
print(Aug)
#PROGRAMA QUE UTILIZA EL MÉTODO DE SUSTITUCIÓN REGRESIVA
#DE UNA MATRIZ 3X3


#Lectura del número de incógnitas
n = int(input('Ingrese el número de incógnitas: '))

#Matriz de tamaño n x n+1 e inicializando
# a cero para almacenar la matriz aumentada
a = np.zeros((n, n + 1))

#Creando una matriz de tamaño n e inicializando
# a cero para almacenar el vector solución
x = np.zeros(n)

#Lectura de los coeficientes de la matriz aumentada
print('Introduzca los coeficientes de la matriz aumentada:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

#Aplicación de la eliminación de Gauss
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divición por cero detectado!')

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

#Sustitución regresiva
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]

#Solución
print('\nLa solución es: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')


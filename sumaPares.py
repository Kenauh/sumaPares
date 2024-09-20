def sumaPares(matriz):
    suma_pares = 0
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] % 2 == 0:        
                # Si el número es par
                suma_pares += matriz[i][j]
    return suma_pares

# ejemplos
matriz1 = [ [4, 9], [16, 7]]  # Resultado esperado: 4 + 16 = 20
print(sumaPares(matriz1))  

matriz2 = [ [6, 2, 5], [11, 14, 9], [8, 4, 7]]  # Resultado esperado: 6 + 2 + 14 + 8 + 4 = 34
print(sumaPares(matriz2))  

matriz3 = [ [17, 20, 19, 22], [13, 28, 30, 3], [26, 5, 12, 9], [32, 21, 18, 16]]  # Resultado esperado: 20 + 22 + 28 + 30 + 26 + 12 + 32 + 18 + 16 = 204
print(sumaPares(matriz3))

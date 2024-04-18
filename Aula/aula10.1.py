#Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um número k.
#Imprima a matriz na tela antes e depois da multiplicação
# ex:
# [[1,2,3],
#  [2,4,5],
#  [4,8,2]]

# resultado: k = 2
# [[2,2,3],
#  [2,8,5],
#  [4,8,4]]

#Diagonal:
# [0][0], [1][1] e [2][2]

matriz = []
for _ in range(3): #linhas
    matriz.append(input().split())

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(matriz[i][j])

k = int(input('Digite o fator da multiplicação: '))

# GENERALIZANDO PARA QUALQUER TAMANHO DE MATRIZ (só trocar 3 pelo len)
# for x in range(3):
#     for y in range(3):
#         if x == y:
#             matriz[x][y] = matriz[x][y] * k

for i in range(len(matriz)):
    matriz[i][i] = matriz[i][i] * k


#PENSANDO EM EXATAMENTE 3 VCALORES NA DIAGONAL:
# matriz[0][0] = matriz[0][0] * k
# matriz[1][1] = matriz[1][1] * k
# matriz[2][2] = matriz[2][2] * k

for z in range(len(matriz)):
    print(matriz[z])
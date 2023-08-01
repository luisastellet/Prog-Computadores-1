#faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. 
#Imprima na tela a matriz, a linha de maior soma e a soma

# ex:
# [[1,2,3],
#  [2,4,5],
#  [4,8,2]]

# soma1 = 6
# soma2 = 11
# soma3 = 14

#[4,8,2]
#14

linhas = 3

matriz = []
for linha in range(linhas):
    matriz.append(list(input().split()))
    for coluna in range(len(matriz[linha])):
        matriz[linha][coluna] = int(matriz[linha][coluna])

maior = -1 #qualquer valor será maior

for i in range(len(matriz)): #linhas
    soma = 0
    for j in matriz[i]:
        soma += j
    if soma > maior:
        maior = soma
        resp = matriz[i]

print(matriz)
print(resp)
print(maior)
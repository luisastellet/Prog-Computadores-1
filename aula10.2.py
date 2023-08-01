#Faça um programa que leia duas matrizes A e B 2x2 e imprima a matriz C que é a soma das matrizes A e B.

# A = 
# [[1,3],
#  [5,7]]

# B = 
# [[5,1],
#  [9,0]]

# C =
# [[6,4]
#  [14,7]]

A = [0] * 2
B = [0] * 2

for i in range(len(A)):
    A[i] = input().split()
    for j in range(len(A[i])):
        A[i][j] = int(A[i][j])
    
for i in range(len(B)):
    B[i] = input().split()
    for j in range(len(B[i])):
        B[i][j] = int(B[i][j])
    
C = []
for i in range(len(A)): #ou len(B) ou só 2 
    linha = []
    for j in range(len(A[i])):
        linha.append(A[i][j] + B[i][j])
    C.append(linha)

for i in range(len(C)):
    print(C[i])
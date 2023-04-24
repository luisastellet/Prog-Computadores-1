import math
#Como coletar 3 informações q virem 3 pares ordenados?
# A = 2 -4 (algo nesse sentido) ---> Xa = 2 e Xb = -4 
Xa, Ya = int(input("Digite as coordenadas do ponto A: "))
Xb, Yb = int(input("Digite as coordenadas do ponto B: "))
Xc, Yc = int(input("Digite as coordenadas do ponto C: "))
A = (Xa, Ya)
B = (Xb, Yb)
C = (Xc, Yc) 

#distancia entre A e B -> lado 1
#distancia entre B e C -> lado 2
#distancia entre C e A -> lado 3

#Tem isso na biblioteca math?
L1 = math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2)
L2 = math.sqrt((Xc - Xb)**2 + (Yc - Yb)**2) 
L3 = math.sqrt((Xa - Xc)**2 + (Ya - Yc)**2)

# Precisaria colocar o |módulo| na subtração
if L1 > L2 - L3 and L1 < L3 - L2 or L2 > L1 + L3 and L2 < L3 - L1 or L3 > L1 + L2 and L3 < L2 - L1:
    if L1 == L2 == L3: 
        print("Esse triângulo é equilátero")
    elif L1 == L2 or L1 == L3 or L2 == L3:
        print("Esse triângulo é isósceles")
    else:
        print("Esse triângulo é escaleno")
else:
    print("Não é possível realizar um triângulo com esses pontos.")
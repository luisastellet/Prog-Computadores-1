import math
Xa = float(input("Digite o X do ponto A: "))
Ya = float(input("Digite o Y do ponto A: "))
Xb = float(input("Digite o X do ponto B: "))
Yb = float(input("Digite o Y do ponto B: "))
Xc = float(input("Digite o X do ponto C: "))
Yc = float(input("Digite o Y do ponto C: "))

#distancia entre A e B -> lado 1
#distancia entre B e C -> lado 2
#distancia entre C e A -> lado 3

#Tem isso na biblioteca math?
L1 = math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2)
L2 = math.sqrt((Xc - Xb)**2 + (Yc - Yb)**2) 
L3 = math.sqrt((Xa - Xc)**2 + (Ya - Yc)**2)

if L1 < L3 + L2 and L3 < L1 + L2 and L2 < L3 + L1:
    if L1 == L2 == L3: 
        print("Esse triângulo é equilátero.")
    elif L1 == L2 or L1 == L3 or L2 == L3:
        print("Esse triângulo é isósceles.")
    else:
        print("Esse triângulo é escaleno.")
else:
    print("Não é possível realizar um triângulo com esses pontos.")
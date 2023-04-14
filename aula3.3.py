import math
x1 = int(input('Qual o x1? '))
y1 = int(input('Qual o y1? '))
x2 = int(input('Qual o x2? '))
y2 = int(input('Qual o y2? '))
A = (x1, y1)
B = (x2, y2)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
print('A distância entre o ponto A {} e o ponto B {} é de {:.2f}' .format(A, B, distancia))
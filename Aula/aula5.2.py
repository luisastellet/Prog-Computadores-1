frase_original = input("Entre com uma frase: ")
frase_analise = frase_original.lower()
posicao = 0
frase_final = ''
for letra in frase_analise:
    if frase_analise.find(' ') == posicao:
        frase_final += ' ' + frase_analise[posicao+1].upper()
    elif posicao == 0:
        frase_final += frase_analise[0].upper()
    else:
        frase_final += frase_analise[posicao]
    posicao += 1
print(frase_final)


frase = input("Entre com uma frase: ").lower()
posicao = 0
frasefinal = ""
while posicao != -1:
    frasefinal += frase[posicao].upper()
    posicaoanterior = posicao
    posicao = frase.find(" ", posicao)
    if posicao != -1:
        posicao += 1 
        frasefinal += frase[posicaoanterior+1 : posicao]
    else:
        frasefinal += frase[posicaoanterior+1 : len(frase)]

print(frasefinal)

#Exemplo do professor e seu nome todo
nome = input("Entre com o nome completo: ")
lista = nome.split() #Ex: Luisa Muniz Stellet
ultimo = lista[len(lista)-1].upper()
resposta = ultimo + ',' 
iniciais = ''
posicao = -1 
for c in range(len(lista)-1):
    iniciais = iniciais + nome[posicao+1] + '.'
    posicao = nome.find(' ', posicao+1, len(nome))
resposta += iniciais.upper()
print(resposta)
centavos = int(input('Quantos centavos você tem? '))
umreal = centavos // 100
if umreal != 0:
    centavos = centavos - (umreal * 100)

cinquenta = centavos // 50
if cinquenta != 0:
    centavos = centavos - (cinquenta * 50)

vintecinco = centavos // 25
if vintecinco != 0:
    centavos = centavos - (vintecinco * 25)

dez = centavos // 10
if dez != 0:
    centavos = centavos - (dez * 10)

cinco = centavos // 5
if cinco != 0:
    centavos = centavos - (cinco * 5)

um = centavos // 1
if um != 0:
    centavos = centavos - (um * 1)

print('Você precisará de {} moedas de 1 real, {} moedas de 50 centavos, {} moedas de 25 centavos, {} moedas de 10 centavos, {} moedas de 5 centavos e {} moedas de 1 centavo.' .format(umreal, cinquenta, vintecinco, dez, cinco, um))


''' OPERADORES MATEMÁTICOS: 
+ -> SOMA   
- -> SUBTRAÇÃO   
* -> MULTIPLICAÇÃO   
/ -> DIVISÃO   
// -> DIVISÃO INTEIRA(QUOCIENTE)  
% -> RESTO DA DIVISÃO   
** -> EXPOENCIAÇÃO '''
altura = float(input("Digite a sua altura (em metros): "))
massa = float(input("Digite a sua massa (em kilos): "))
imc = massa / altura ** 2
if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif 18.6 < imc < 24.9:
    print("VocÊ está saudável")
elif 25.0 < imc < 29.9:
    print("Você está com peso em excesso")
elif 30.0 < imc < 34.9:
    print("Você está com obesidade grau 1")
elif 35.0 < imc < 39.9:
    print("Você está com obesidade grau 2")
else:
    print("O seu IMC é", imc, "você está com obesidade grau 3")
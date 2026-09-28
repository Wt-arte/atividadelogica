peso = int(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros" \
": "))
imc = peso / (altura ** 2)
if imc < 20:
    print(f"Seu IMC é {imc:.2f}, você está abaixo do peso.")
elif imc >= 20 and imc < 25:
    print(f"Seu IMC é {imc:.2f}, você está com o peso ideal.")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é {imc:.2f}, você está acima do peso.")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é {imc:.2f}, você está com obesidade.")
elif imc >= 40:
    print(f"Seu IMC é {imc:.2f}, você está com obesidade mórbida.")
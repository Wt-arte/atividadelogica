numeroA = int(input("Digite o primeiro número: "))
numeroB = int(input("Digite o segundo número: "))
if numeroA > numeroB:
    print(f"O número {numeroA} é maior que o número {numeroB}.")
elif numeroA < numeroB:
    print(f"O número {numeroA} é menor que o número {numeroB}.")
else:
    print(f"Os números {numeroA} e {numeroB} são iguais.")
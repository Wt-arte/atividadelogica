numeroA = int(input("Digite o primeiro número: "))
numeroB = int(input("Digite o segundo número: "))
if numeroA % numeroB == 0:
    print(f"O número {numeroA} é divisível por {numeroB}.")
else:
    print(f"O número {numeroA} não é divisível por {numeroB}.")
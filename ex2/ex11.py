numero = int(input("Digite um número: "))
if numero % 3 == 0 and numero % 7 == 0:
    print(f"O número {numero} é divisível por 3 e 7.")
elif numero % 3 == 0:
    print(f"O número {numero} é divisível por 3.")
elif numero % 7 == 0:
    print(f"O número {numero} é divisível por 7.")
else:
    print(f"O número {numero} não é divisível por 3 nem por 7.")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a > b:
    print(f"o quadrado do menor numero é {b ** 2} e a raiz do maior numero é {a ** (1/2)}")
elif a < b:
    print(f"o quadrado do menor numero é {a ** 2} e a raiz do maior numero é {b ** (1/2)}")
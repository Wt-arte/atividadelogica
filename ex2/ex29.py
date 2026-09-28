a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
if a + b > c and a + c > b and b + c > a:
    print(f"Os valores {a}, {b} e {c} podem formar um triângulo.")
else:
    print(f"Os valores {a}, {b} e {c} não podem formar um triângulo.")
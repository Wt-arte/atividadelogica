a = int(input("Digite o número: "))
if a == 5:
    print(f"O número {a} é igual a 5.")
elif a == 200:
    print(f"O número {a} é igual a 200.")
elif a == 400:
    print(f"O número {a} é igual a 400.")
if a < 5 and a > 200:
    print(f"O número {a} nao esta entre 5 e 200.")
elif a > 200 and a < 400:
    print(f"O número {a} está entre 200 e 400.")
elif a > 400 and a < 500:
    print(f"O número {a} está entre 400 e 500.")
elif a > 500 and a < 1000:
    print(f"O número {a} está entre 500 e 1000.")

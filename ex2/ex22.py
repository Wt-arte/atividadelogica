saldo = int(input("Digite o saldo médio do cliente: "))
if saldo >= 0 and saldo <= 500:
    print("O cliente não possui crédito.")
elif saldo > 500 and saldo <= 1000:
    print(f"O cliente possui crédito de 30% do saldo médio totalizando {saldo * 0.3}")
elif saldo > 1000 and saldo <= 3000:
    print(f"O cliente possui crédito de 40% do saldo médio totalizando {saldo * 0.4}")
elif saldo > 3000:
    print(f"O cliente possui crédito de 50% do saldo médio totalizando {saldo * 0.5}")
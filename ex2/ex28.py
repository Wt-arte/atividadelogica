compra = int(input("Digite o valor da compra:R$ "))
if compra <= 10:
    print(f"O valor da compra é R$ {compra} e o valor da venda é R$ {compra * 0.7}.")
elif compra > 10 and compra <= 30:
    print(f"O valor da compra é R$ {compra} e o valor da venda é R$ {compra * 0.5}.")
elif compra > 30 and compra <= 50:
    print(f"O valor da compra é R$ {compra} e o valor da venda é R$ {compra * 0.4}.")
elif compra > 50:
    print(f"O valor da compra é R$ {compra} e o valor da venda é R$ {compra * 0.3}.")

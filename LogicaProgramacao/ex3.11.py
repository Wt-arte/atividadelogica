mercadoria = float(input("Digite o valor da mercadoria: R$ "))
desconto = float(input("Digite o percentual de desconto (em %): "))
valor_desconto = mercadoria * desconto / 100
novo_valor = mercadoria - valor_desconto
print(f"O valor do desconto é: R${valor_desconto:.2f}")
print(f"O novo valor da mercadoria é: R${novo_valor:.2f}")


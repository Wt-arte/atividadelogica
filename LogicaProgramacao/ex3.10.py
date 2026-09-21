
salario = float(input("Digite o salário do funcionário: R$ "))
aumento = float(input("Digite o percentual de aumento (em %): "))
novo_salario = salario + (salario * aumento / 100)
print(f"Seu aumento foi de: R${salario * aumento / 100:.2f}")
print(f"O novo salário é: R${novo_salario:.2f}")
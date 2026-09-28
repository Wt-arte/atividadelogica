salario_bruto = float(input("Digite o salário bruto: "))
prestação = float(input("Digite o valor da prestação: "))
if prestação > (salario_bruto * 0.3):  
    print("Empréstimo não concedido. A prestação excede 30% do salário bruto.")
else:
    print("Empréstimo concedido.")
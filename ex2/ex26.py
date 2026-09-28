idade = int(input("Digite a sua idade: "))
if idade <= 10:
    print("Você deverá pagar R$ 30,00 pelo plano de saúde.")
elif idade > 10 and idade <= 29:
    print("Você deverá pagar R$ 60,00 pelo plano de saúde.")
elif idade > 29 and idade <= 45:
    print("Você deverá pagar R$ 120,00 pelo plano de saúde.")
elif idade > 45 and idade <= 59:
    print("Você deverá pagar R$ 150,00 pelo plano de saúde.")
elif idade > 59 and idade <= 65:
    print("Você deverá pagar R$ 250,00 pelo plano de saúde.")
elif idade > 65:
    print("Você deverá pagar R$ 400,00 pelo plano de saúde.")
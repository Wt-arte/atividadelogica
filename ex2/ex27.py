nota1 = int(input("Digite a nota do primeiro trimestre: "))
nota2 = int(input("Digite a nota do segundo trimestre: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"A média do aluno é {media}, portanto ele foi aprovado.")
elif media >= 3 and media < 7:
    print(f"A média do aluno é {media}, portanto ele está em exame.")
else:
    print(f"A média do aluno é {media}, portanto ele foi reprovado.")
#calculadora de média escolar
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n3 = float(input("Digite a quarta nota: "))

#calculo da média 
media = (n1 + n2 + n3 + n3) / 4
if media >= 7.0:
    situacao= "Aprovado👌"
elif media >= 5.0:
    situacao= "Recuperação⚠️"
else:
    situacao = "Reprovado❌"
print(f"\nmedia: {media:.2f}, Situação:{situacao}")
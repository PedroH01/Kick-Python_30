import os

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 6:
 print(f'Sua média é {media:.2f} e você foi aprovado')
elif media < 6:
 print(f'Sua média é {media:.2f} e você foi reprovado')

os.system("pause")
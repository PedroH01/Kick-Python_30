import os

peso = float(input("Digite o seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso/(altura**2)

if imc <=18.5:
    print('Magreza')
elif imc <=25:
    print('Normal')
elif imc<= 30:
    print('Sobrepeso')
elif imc<=40:
    print('obesidade')
else:
    print('Obesidade grave')

os.system("pause")
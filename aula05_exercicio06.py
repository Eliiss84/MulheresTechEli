#6 Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.



#  valor do usuário
valor = float(input("Digite um valor: "))

#  valor é positivo, negativo ou zero
if valor >= 0:
    print("O valor é positivo.")
else:
    print("O valor é negativo.")

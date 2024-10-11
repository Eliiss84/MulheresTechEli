#  2 Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²

# Preço do combustível
preco_combustivel = 4.87


odometro_inicial = float(input("Digite a marcação do odômetro no início do dia (km): "))  # Marca inicial
odometro_final = float(input("Digite a marcação do odômetro no final do dia (km): "))      # Marca final
litros_gastos = float(input("Digite o número de litros de combustível gasto: "))            # Litros de combustível
valor_total_recebido = float(input("Digite o valor total (R$) recebido dos passageiros: "))  # Valor recebido

# Exibe os valores armazenados
print(f"Odômetro inicial: {odometro_inicial} km")
print(f"Odômetro final: {odometro_final} km")
print(f"Litros gastos: {litros_gastos} L")
print(f"Valor total recebido: R$ {valor_total_recebido:.2f}")


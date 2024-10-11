




# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;'''

preco_combustivel = 4.87

odometro_inicial = float(input("Digite a marcação do odômetro no início do dia (km): "))
odometro_final = float(input("Digite a marcação do odômetro no final do dia (km): "))
litros_gastos = float(input("Digite o número de litros de combustível gasto: "))
valor_total_recebido = float(input("Digite o valor total (R$) recebido dos passageiros: "))

# Cálculos
distancia_percorrida = odometro_final - odometro_inicial

# Verifica se a distância percorrida é maior que zero
if distancia_percorrida > 0:
    media_consumo = distancia_percorrida / litros_gastos
else:
    media_consumo = 0  # Se não percorreu distância, consumo é zero

# Calcula o custo do combustível
custo_combustivel = litros_gastos * preco_combustivel

# Calcula o lucro líquido
lucro_liquido = valor_total_recebido - custo_combustivel

# Exibe os resultados
print(f"A média do consumo é: {media_consumo:.2f} km/L")
if lucro_liquido > 0:
    print(f"O lucro líquido do dia é: R$ {lucro_liquido:.2f}")
else:
    print(f"O motorista teve um prejuízo de: R$ {abs(lucro_liquido):.2f}")


# 3 Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

# Preço do combustível

preco_combustivel = 4.87

# Lê as entradas do usuário
odometro_inicial = float(input("Digite a marcação do odômetro no início do dia (km): "))  # Marca inicial
odometro_final = float(input("Digite a marcação do odômetro no final do dia (km): "))      # Marca final
litros_gastos = float(input("Digite o número de litros de combustível gasto: "))            # Litros de combustível
valor_total_recebido = float(input("Digite o valor total (R$) recebido dos passageiros: "))  # Valor recebido

# Cálculos
distancia_percorrida = odometro_final - odometro_inicial

# Verifica se a distância percorrida e os litros gastos são válidos
if distancia_percorrida > 0 and litros_gastos > 0:
    media_consumo = distancia_percorrida / litros_gastos
else:
    media_consumo = 0  # Se não percorreu distância ou não gastou combustível

# Cálculo do custo do combustível
custo_combustivel = litros_gastos * preco_combustivel

# Cálculo do lucro líquido
lucro_liquido = valor_total_recebido - custo_combustivel

# Exibe os resultados
print(f"A média do consumo é: {media_consumo:.2f} km/L")
if lucro_liquido > 0:
    print(f"O lucro líquido do dia é: R$ {lucro_liquido:.2f}")
else:
    print(f"O motorista teve um prejuízo de: R$ {abs(lucro_liquido):.2f}")

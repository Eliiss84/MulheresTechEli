#1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável. 

# def calcular_multa(peso_peixes):
#     limite = 100
#     valor_multa_por_quilo = 10.0
    
#     if peso_peixes > limite:
#         excesso = peso_peixes - limite
#         multa = excesso * valor_multa_por_quilo
#         return multa
#     else:
#         return 0.0

# # Exemplo de uso
# peso = 120  # peso dos peixes em quilos
# multa = calcular_multa(peso)
# if multa > 0:
#     print(f"O pescador deve pagar uma multa de R$ {multa:.2f}.")
# else:
#     print("O pescador não deve pagar multa.")

#2 Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.
    
# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)

# def classificar_imc(imc):
#     if imc < 18.5:
#         return "Abaixo do peso"
#     elif 18.5 <= imc < 24.9:
#         return "Peso normal"
#     elif 25 <= imc < 29.9:
#         return "Sobrepeso"
#     elif 30 <= imc < 34.9:
#         return "Obesidade classe I"
#     elif 35 <= imc < 39.9:
#         return "Obesidade classe II"
#     else:
#         return "Obesidade classe III"

# def ler_dados():
#     n = int(input("Quantas pessoas você deseja avaliar? "))
#     resultados = []

#     for _ in range(n):
#         peso = float(input("Digite o peso (kg): "))
#         altura = float(input("Digite a altura (m): "))
#         imc = calcular_imc(peso, altura)
#         classificacao = classificar_imc(imc)
#         resultados.append((peso, altura, imc, classificacao))

#     return resultados

# # Exemplo de uso
# resultados = ler_dados()

# print("\nResultados:")
# for peso, altura, imc, classificacao in resultados:
#     print(f"Peso: {peso:.2f} kg, Altura: {altura:.2f} m, IMC: {imc:.2f}, Classificação: {classificacao}")

# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta.


def mostrar_cardapio():
    cardapio = {
        1: ("Pizza Margherita", 30.00),
        2: ("Hambúrguer Gourmet", 25.00),
        3: ("Salada Caesar", 20.00),
        4: ("Torta de Limão", 15.00)
    }

    print("Cardápio:")
    for chave, valor in cardapio.items():
        print(f"{chave}. {valor[0]} - R$ {valor[1]:.2f}")
    
    return cardapio

def realizar_pedido(cardapio):
    pedidos = []
    while True:
        try:
            opcao = int(input("Escolha um item do cardápio (0 para finalizar o pedido): "))
            if opcao == 0:
                break
            elif opcao in cardapio:
                pedidos.append(cardapio[opcao])
                print(f"Adicionado: {cardapio[opcao][0]} - R$ {cardapio[opcao][1]:.2f}")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    return pedidos

def fechar_conta(pedidos):
    total = sum(item[1] for item in pedidos)
    print("\nConta finalizada:")
    for item in pedidos:
        print(f"{item[0]} - R$ {item[1]:.2f}")
    print(f"Total: R$ {total:.2f}")

# Exemplo de uso
cardapio = mostrar_cardapio()
pedidos = realizar_pedido(cardapio)
fechar_conta(pedidos)

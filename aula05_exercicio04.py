# 4) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela que foi passada.
 
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser encarado como “Importado”;

# Lê o código de origem do produto
codigo = input("Digite o código de origem do produto: ")

# Verifica a origem do produto com base no código
if codigo == "1":
    regiao = "Sul"
elif codigo == "2":
    regiao = "Sudeste"
elif codigo == "3":
    regiao = "Centro-Oeste"
elif codigo == "4":
    regiao = "Nordeste"
elif codigo == "5":
    regiao = "Norte"
else:
    regiao = "Importado"

# Exibe a região de procedência
print(f"A região de procedência do produto é: {regiao}")


#TRATAMENTO DE EXCEÇÕES (TRY e EXCEPT)

#Reformulando a função de divisão:
# def dividir(a,b):
#     try:
#         resultado=a/b
#     except ZeroDivisionError:
#         print("Erro: não é possível dividir por zero!")
#     else:
#         print(f"O resultado da divisão é {resultado}.")
#     finally:
#         print("Operação finalizada.")

#Testando a função reformulada:
# dividir(20,2)
# dividir(20,0)
# dividir(2,5)

#ATIVIDADE: (github)

#Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.

class NumeroImparError(Exception):
    """Exceção personalizada para números ímpares."""
    pass

def ler_par():
    while True:
        try:
            a = int(input("Digite o primeiro número do par: "))
            b = int(input("Digite o segundo número do par: "))
            
            # Verifica se os números são ímpares
            if a % 2 != 0 or b % 2 != 0:
                raise NumeroImparError("Os números devem ser pares.")
            
            return a, b
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")
        except NumeroImparError as e:
            print(e)

def main():
    for i in range(3):
        print(f"\nPar {i + 1}:")
        a, b = ler_par()
        soma = a + b
        print(f"A soma de {a} e {b} é: {soma}")

if __name__ == "__main__":
    main()

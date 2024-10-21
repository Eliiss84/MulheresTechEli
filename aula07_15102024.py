#estrutura de armazenamento  listas:continuação  #w3schools (site para duvidas no python)


#lista1=[2,4,6,8,10]
#lista1.remove(6) #removeu o elemnto "6" da minha lista pelo proprio elemento.
#lista1.remove(lista1[2]) #removeu o elemnto de 'indice 2' da minha lista pelo indice
#print(lista1) #[2,4,10]

#lista2=lista1.insert(2,1000)
#print(lista2) #vai resultar em 'None", pois eu salvei um comando da lista1 nessa nova lista.
#lista2=lista1.copy()
#print(lista2) #[2,4,1000,10]

#lista3=lista1.copy()
#lista4=lista1.copy()
#lista3.clear() #limpa todo o conteudo da lista, deixando-a vazia.
#print(lista3) #[]
#lista4.pop(0) #estou removendo o elemento de 'índice zero' da minha lista.
#print(lista4) #[4, 1000, 10]
#lista4.sort() #coloquei meus elementos da lista em ordem crescente.
#print(lista4) #[4, 10, 1000]
#lista4.reverse() #coloquei meus elementos em ordem inversa.
#print(lista4) #[1000, 10, 4] 

#print(lista1,lista2,lista3,lista4)

'''frutas=['uva','maçã','carambola','melancia']
frutas.sort() # o comando tbm funciona para elementos do tipo 'string'
print(frutas)

#TUPLAS #são imutaveis : podemos consultar e reordenar tuplas, nuca adicionar ou remover itens.

frutas2=tuple(frutas)
print(frutas2.index('uva')) #eu consultei em qual índice se encontra o elemento 'uva'
print(frutas2.count('uva')) #eu consultei quantas vezes o elemento 'uva' aparece na tupla'''

#DICIONÀRIOS: estruturas que salvam as 

# estados={'RJ':'Rio de Janeiro',
#          'SP':'São Paulo',
#          'MG':'Minas Gerias',
#          'ES':'Espírito Santo'}

# print(estados)

# print(estados.keys())
# print(estados.values())

# candidatos={'Larissa':28,
#             'Anna':20
# }
# print(estados.get('RJ'))

#Crie um código que seja capaz de ler e armazenar
# uma sequência de 20 números pares e 20 números ímpares.
# Obs: utilize estruturas de repetição para fechar esse conjunto
# de números.

def ler_numeros():
    pares = []
    impares = []

    # Ler 20 números pares
    while len(pares) < 20:
        numero = int(input("Digite um número par: "))
        if numero % 2 == 0:
            pares.append(numero)
        else:
            print("Esse número não é par. Tente novamente.")

    # Ler 20 números ímpares
    while len(impares) < 20:
        numero = int(input("Digite um número ímpar: "))
        if numero % 2 != 0:
            impares.append(numero)
        else:
            print("Esse número não é ímpar. Tente novamente.")

    return pares, impares

# Exemplo de uso
pares, impares = ler_numeros()
print("Números pares:", pares)
print("Números ímpares:", impares)

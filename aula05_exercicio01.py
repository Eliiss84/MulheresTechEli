#1 Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;


#variaveis simples - sao as que calculam a entrada de dados
Lampada_potencia=float(input('digite a potencia da lampada (watts);')) 
largura_comodo=float(input('digite a lagura do comodo'))
Comprimento_comodo=float(input('digite o comprimento do comodo'))

#variaveis para o calculo de area e de potencia
area_comodo=largura_comodo*Comprimento_comodo  
potencia_real=3*Lampada_potencia

#variaveis para o calculo de numero de lampadas e bocais
numero_lampadas=int(potencia_real/Lampada_potencia)
bocais=int(area_comodo/3)
 #exibiçao dos resultados (quqlquer das formataçoes sao validos)
print('lampadas:',numero_lampadas)
print(f"numero de lampadas necessarias:{numero_lampadas:.2f}")
print(f"numero de bocais necessarios:{bocais}")

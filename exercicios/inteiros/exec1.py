# 1. Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados.

numero =int(input('Digite um número e 0 para parar o calcúlo: '))

while numero != 0:
    quadrado = numero **2
    
    print('O quadrado é: ',quadrado)
   
    numero =int(input('Digite um número e 0 para parar o calcúlo: '))
   
    if numero == 0:
        print('Okay,já deu!Vamos parar.')
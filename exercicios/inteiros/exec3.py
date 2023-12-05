# 3.  Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
# Exemplo: Para n=4 a saída deverá ser 1,3,5,7.

# not (i % 2 == 0) - ímpar
# i < n

n = int(input('Digite seu número:'))
i = 1 

while i <= n * 2:  
    print('Número ímpar:', i)
    i += 2  


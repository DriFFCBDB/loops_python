# 2.  Dado um número inteiro positivo n, calcular a soma dos n primeiros números inteiros positivos.

n = int(input('Digite um número inteiro positivo.'))
soma = 0
i = 1

while i <= n:
    soma = soma + i
    i = i + 1
    print(soma)
 


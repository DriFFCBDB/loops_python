#  Dados n e dois números inteiros positivos i e j diferentes de 0, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.

#  Exemplo: Para n = 6 , i = 2 e j = 3 a saída deverá ser : 0,2,3,4,6,8.

n = int(input("Digite um n: "))
i = int(input("Digite um i: "))
j = int(input("Digite um j: "))

numeros = []
mult_i, mult_j = i, j

for _ in range(n):
    if mult_i < mult_j:
        numeros.append(mult_i)
        mult_i += i
    elif mult_i > mult_j:
        numeros.append(mult_j)
        mult_j += j
    else:
        numeros.append(mult_i)
        mult_i += i
        mult_j += j

print(numeros)

            
            
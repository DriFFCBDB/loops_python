#Dados o número n de alunos de uma turma de Introdução aos Autômatos a Pilha (MAC 414) e 
#suas notas da primeira prova, determinar a maior e a menor nota obtidas por essa turma 
#(Nota máxima = 100 e nota mínima = 0).
import random

maior_nota = 0
menor_nota = 0

for aluno in range(20):
    
    notas_aleatorias = random.randint(0,100)

    if notas_aleatorias > maior_nota:
        maior_nota = notas_aleatorias
    
    if notas_aleatorias < maior_nota:
        menor_nota = notas_aleatorias

print(f"A maior nota foi {maior_nota},e a menor nota da turma foi de {menor_nota}")
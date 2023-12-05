# Uma loja de discos anota diariamente durante o mês de março a quantidade de discos vendidos.
# Determinar em que dia desse mês ocorreu a maior venda e qual foi a quantidade de discos vendida nesse dia.
import random

dia_maior_venda = 0
maior_venda = 0

for dia in range(1,32):

    notas_aleatorias = random.randint(0,200)
   
    print(notas_aleatorias)
   
    if notas_aleatorias > maior_venda:
        maior_venda = notas_aleatorias
        dia_maior_venda = dia

print(f"A maior venda ocorreu no dia {dia_maior_venda} de março, com {maior_venda} discos vendidos.")







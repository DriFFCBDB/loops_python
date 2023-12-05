# Dados n e uma seqüência de n números inteiros, determinar a soma dos números pares.

import random

for numero in range(10):
    sequencia = random.randint(0, 10)
    if sequencia % 2 == 0:
        soma = sequencia + sequencia

print(f"A soma dos número pares são soma deles é de {soma}")

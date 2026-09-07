import random

num = random.randint(1,50)
carton = random.sample(range(1,51),25)
sorteados = random.sample(range(1,51),50)

tablero = []
for i in range(0,5):
    tablero.append(carton[i*5:(i+1)*5])


print(tablero)

for fila in tablero:
    for alado in fila:
        print(alado, end = ' ')
    print(' ')

for num in sorteados:
    for fila in tablero:
        for elemento in fila:
            if num == elemento:
                elemento = "X"





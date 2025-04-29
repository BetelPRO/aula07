numeros = [0]*5
for i in range(len(numeros)):
    numeros[i] = int(input("Digite um número: "))
for y in range(len(numeros)-1, -1, -1):
    print(numeros[y], end=" ")

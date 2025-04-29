a = [0]*5
m = [0]*5
for i in range(len(a)):
    a[i] = int(input("Digite um número: "))
x = int(input("Digite o multiplicador: "))
m = [y * x for y in a]
"""for y in range(len(m)):
    m[y] = a[y]*x
"""
print(m)
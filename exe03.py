nomes = ['']*5
for i in range(len(nomes)):
    nomes[i] = input("Digite um nome: ")
consulta = input("Quem você es´ta procurando?\n")
for x in range(len(nomes)):
    if nomes[x] == consulta:
        print(x)
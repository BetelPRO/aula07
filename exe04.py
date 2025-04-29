notas = [0.0]*5
notaTotal, cont = 0, 0
for i in range(len(notas)):
    notas[i] = float(input("Digite uma nota: "))
for x in notas:
    notaTotal += x
media = notaTotal/5
for y in notas:
    if y > media:
        cont += 1
print(f"A média da turma é {media} e {cont} alunos estão acima da média")
usuarios = ["joão", "maria", "mario", "maria", "josefa"]
senhas = [1234, 3432, 5432, 3333, 6666]

usuario = input("Digite o seu login: ")
senha = int(input("Digite sua senha: "))
for o in range(len(usuarios)):
    if usuarios[o] == usuario:
        if senhas[o] == senha:
            print("Login efetuado com sucesso!!!")
            break
        else:
            print("Senha inválida")
            break
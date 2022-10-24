def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcado = False
    jogando = False
    lista = ["_", "_", "_", "_", "_", "_"]

    while not enforcado and not jogando:
        chute = input("Qual letra você deseja? ").lower().strip()
        posicao = 0
        for letra in palavra_secreta:
            if chute == letra:
                lista[posicao] = chute
            posicao += 1
        for i in lista:
            print(i, end=" ")
        print("\nJogando...")
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
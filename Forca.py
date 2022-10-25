def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    chances = 0
    lista = ["_", "_", "_", "_", "_", "_"]

    while chances != 6:
        chute = input("Qual letra você deseja? ").lower().strip()
        posicao = 0
        for letra in palavra_secreta:
            if chute == letra:
                lista[posicao] = chute
            posicao += 1
        if chute not in "banana":
            print(f"Menos uma chance! Restam apenas {5 - chances}!")
            chances += 1
        for i in lista:
            print(i, end=" ")

        print("\nJogando...")
    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()
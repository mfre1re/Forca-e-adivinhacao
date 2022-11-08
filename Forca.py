def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "flecha"
    chances = 0
    enforcado = False
    lista = ["_" for letra in palavra_secreta]

    while enforcado == False:
        chute = input("Qual letra você deseja? ").lower().strip()
        posicao = 0

        for letra in palavra_secreta:
            if chute == letra:
                lista[posicao] = chute
            posicao += 1
        if chances == 5 and chute not in palavra_secreta:
            break
        elif chute not in palavra_secreta:
            print(f"Menos uma chance! Restam apenas {5 - chances}!")
            chances += 1
        for i in lista:
            print(i, end=" ")

        enforcado = "_" not in lista
        print("\nJogando...")
    if "_" not in lista:
        print("\nParabéns! Você descobriu a palavra!")
    else:
        print("\nVocê foi enforcado! Fim de jogo!")

if __name__ == "__main__":
    jogar()
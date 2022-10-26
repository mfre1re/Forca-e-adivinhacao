def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    chances = 0
    enforcado = False
    lista = ["_", "_", "_", "_", "_", "_"]

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
    print("\nFim de jogo!")

if __name__ == "__main__":
    jogar()
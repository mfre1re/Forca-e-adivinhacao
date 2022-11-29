import random

def jogar():

    mostrar_abertura()
    palavra_secreta = abrir_txt_definir_palavra()
    lista = ["_" for letra in palavra_secreta]
    chances = 0
    enforcado = False

    while enforcado == False:
        chute = input("Qual letra você deseja? ").upper().strip()
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

def mostrar_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def abrir_txt_definir_palavra():
    palavra = []
    with open(r"D:\Estudos Programação\Python Projects\palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.upper().strip()
            palavra.append(linha)
    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero]
    return palavra_secreta

if __name__ == "__main__":
    jogar()
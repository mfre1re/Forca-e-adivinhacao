import random

def jogar():

    mostrar_abertura()
    palavra_secreta = abrir_txt_definir_palavra()
    lista = ["_" for letra in palavra_secreta]
    chances = 0
    enforcado = False

    while enforcado == False:
        chute = pergunta_a_letra()
        posicao = 0
        for letra in palavra_secreta:
            if chute == letra:
                lista[posicao] = chute
            posicao += 1
        if chances == 5 and chute not in palavra_secreta:
            desenha_forca(chances+1)
            break
        elif chute not in palavra_secreta:
            print(f"Menos uma chance! Restam apenas {5 - chances}!")
            chances += 1
            desenha_forca(chances)
        for i in lista:
            print(i, end=" ")

        enforcado = "_" not in lista
        print("\nJogando...")
    if "_" not in lista:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    escolha = input("Deseja jogar novamente? (S/N) \n").upper()
    if escolha == "S":
        jogar()

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

def pergunta_a_letra():
    chute = input("Qual letra você deseja? ").upper().strip()
    return chute

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(chances):
    print("  _______     ")
    print(" |/      |    ")

    if(chances == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(chances == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(chances == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if(chances == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(chances == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (chances == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()
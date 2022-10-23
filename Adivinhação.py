import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(0, 101)
    tentativas = 1
    chances = 0
    dificuldade = 0

    while dificuldade != 1 and dificuldade != 2 and dificuldade != 3:
        dificuldade = int(input("Qual o nível de dificuldade você deseja?\n (1) - Fácil\n (2) - Médio\n (3) - Difícil\n "))
        if dificuldade == 1:
            chances = 9
        elif dificuldade == 2:
            chances = 7
        elif dificuldade == 3:
            chances = 5

    while chances != 5 or chances != 7 or chances != 9:

            for tentativas in range (1, chances + 1):
                print(f"Tentativa {tentativas} de {chances}")
                chute = int(input("Digite seu número de 0 a 100: "))
                if chute > 100 or chute < 0:
                    print("Você digitou um número inválido!")
                    continue
                if numero_secreto == chute:
                    print("Parabéns!!!")
                    break
                elif(chute > numero_secreto):
                    print("Você errou! O número digitado é maior que o alvo.\n")
                else:
                    print("Você errou! O número digitado é menor que o alvo.\n")
                tentativas += 1
            if tentativas == chances + 1 or chute == numero_secreto:
                print(f"O número sorteado foi o {numero_secreto}.")
                break

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()

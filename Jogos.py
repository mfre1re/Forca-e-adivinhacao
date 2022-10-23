import Adivinhação
import Forca

print("Bem vindo a sua área de jogos!\nTemos dois jogos para a sua escolha e são Adivinhação e Forca.")
print("Por favor, selecione a opção para o jogo que desejar: (1) Adivinhação e (2) Forca")

jogo = int(input("Qual o jogo? "))

if jogo == 1:
    Adivinhação.jogar()
elif jogo == 2:
    Forca.jogar()

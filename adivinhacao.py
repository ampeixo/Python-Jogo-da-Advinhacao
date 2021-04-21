# 15/02/2021 jogo da adivinhação da Alura (curso python parte 01)
import random


def jogar():
    print("*******************************")
    print("Bem vindo ao jogo da adivinhação")
    print("*******************************")

    # random.seed(100)
    numero_secreto = random.randrange(1, 101)
    # print(numero_secreto)
    total_tentativas = 0
    pontos = 1000

    nivel = int(input("Escolha um nível para jogar\n(1)Fácil (2)Médio (3)Difícil: "))
    if nivel == 1:
        total_tentativas = 10
    elif nivel == 2:
        total_tentativas = 6
    elif nivel == 3:
        total_tentativas = 4
    else:
        print("Digite um número valido entre 1 e 3")

    for rodada in range(0, total_tentativas + 1):

        # por padrão a função de input sempre retorna uma string
        chute_str = input("digite um número inteiro entre 1 e 100: ")

        # converter a váriavel de STR para INT
        chute = int(chute_str)

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        print("Tentativa {} de {}".format(rodada, total_tentativas))
        print("Você digitou o número: " + chute_str)

        if chute < 1 or chute > 100:
            print("Você digitou um número invalido, digite um número entre 1 e 100")
            continue

        if acertou:
            print("Parábens, você acertou o número secreto!\nVocê fez {} pontos".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if chute_maior:
                print("Infelizmente você errou o número secreto pois você digitou um número maior "
                      "que o número secreto!")
                if rodada == total_tentativas:
                    print("O número secreto era {}.\nVocê fez {}".format(numero_secreto, pontos))
            elif chute_menor:
                print("Infelizmente você errou o número secreto pois você digitou um número menor "
                      "que o número secreto!")
                if rodada == total_tentativas:
                    print("O número secreto era {}.\nVocê fez {}".format(numero_secreto, pontos))

    print("FIM DO JOGO!")


if __name__ == "__main__":
    jogar()

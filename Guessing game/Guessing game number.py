from random import randint
import time
pergunta = "S"
n = 0
cont = 0
dificuldade = 0
pontuacao = 0
perda = 0
recorde = 0
menu = 1

print ('Carregando...')
time.sleep(1)
print('Iniciado!')
print('=-=-= Jogo da advinhação =-=-=')

# menu do jogo
while pergunta == "S":
    menu = int(input('Você deseja:\n1-Jogar\n2-Sair\n'))
    if menu not in [1, 2]:
        print("Valor inválido.\nDigite 1 ou 2.")
        menu = int(input('Você deseja:\n1-Jogar\n2-Sair\n'))
    # definiçao do botão 2 como saida
    if menu == 2:
        print("Tenha um bom dia!")
        pergunta = "N"
    if menu == 1:       #Jogo
        pontuacao += 100
        print("Antes de iniciarmos, escolha a dificuldade:")
        dificuldade = int(input('Você deseja:\n1-Fácil\n2-Médio\n3-Difícil\n4-Tentativas limitadas\n5-Infinit\n'))
        if dificuldade not in [1, 2, 3, 4, 5]:
            print('Esse valor não é aceito.\nDigite um dos valores válidos.')
            dificuldade = int(input('Você deseja:\n1-Fácil\n2-Médio\n3-Difícil\n4-Tentativas limitadas\n5-Infinit\n'))
        if dificuldade != 4 and dificuldade != 5:
            # definição da dificuldade
            if dificuldade == 1:
                aleatorio = randint(1,50)
                print("Certo vamos começar.\nIrei pensar em um número entre \033[31;1m1\033[m e \033[31;1m50\033[m.\n")   #def
            elif dificuldade == 2:
                aleatorio = randint(1,100)
                pontuacao += 25
                print("Certo vamor começar.\nIrei pensar em um número entre \033[31;1m1\033[m e \033[31;1m100\033[m.\n")
            elif dificuldade == 3:
                aleatorio = randint(1,500)
                pontuacao += 50
                print("Certo vamor começar.\nIrei pensar em um número entre \033[31;1m1\033[m e \033[31;1m500\033[m.\n")
            cont = 0
            n = int(input('Tente adivinhar: '))
            cont += 1
            # definição se o valor é mais baixo ou mais alto
            while n != aleatorio:
                if aleatorio > n:
                    print("Muito baixo")
                    n = int(input('Tente novamente: '))
                    cont += 1
                if aleatorio < n:
                    print("Muito alto.")
                    cont += 1
                    n = int(input('Tente novamente: '))
                # definição da perda por pontuação
                if dificuldade == 1:
                    perda = 9
                elif dificuldade == 2:
                    perda = 9.5
                elif dificuldade == 3:
                    perda = 11
                pontuacao -= perda
            print("Você acertou!\nO número era: \033[32;1m{}\033[m\nE você precisou de \033[32;1m{}\033[m tentativas". format(aleatorio, cont))
            print("Sua pontuação foi de: {}.".format(pontuacao))
            print("Perfeito" if pontuacao >= 100 else "Otimo" if 80 <= pontuacao < 100 else 'Você tem potencial' if 50 <= pontuacao < 80 else "Dá para melhorar" if 20 <= pontuacao < 50 else "Mais sorte na próxima")
            if pontuacao > recorde:
                recorde = pontuacao
            print("Seu recorde de pontuação atual é de: {}".format(recorde))
            pontuacao = 0    #zerar pontuacao para próxima rodada
        if dificuldade == 4:
            cont = 0
            aleatorio = randint(1, 100)
            print("Você entrou no modo de tentativas limitadas.\nVocê terá 7 tentativas para encontrar o número entre 1 e 100.")
            n = int(input('Tente adivinhar: '))
            cont += 1
            while cont < 7 and n != aleatorio:
                    if n < aleatorio:
                        print('Muito baixo.')
                        cont += 1
                        n = int(input('Tente novamente: '))
                    if n > aleatorio:
                        print('Muito alto.')
                        cont += 1
                        n = int(input('Tente novamente: '))
                    if n == aleatorio:
                        print("Você conseguiu antes das chances acabarem!\nO número era: {}\nVocê usou {} tentativas".format(aleatorio, cont))
                        cont += 7
                    if cont == 7 and n != aleatorio:
                        print("Você perdeu.\nO valor era: {}".format(aleatorio))
                        print("Tente novamente.")
        if dificuldade == 5:
            pontuacao *= 0
            cont = 0
            aleatorio = randint(1, 500)
            print("Você entrou no modo infinito.\n Você tentará acertar números de 1 a 500 e, sempre que acertar, o número mudará.\nQuando quiser encerrar o modo, digite \033[31;1m999\033[m.")
            n = int(input('Tente adivinhar:'))
            while n != 999:
                if n == aleatorio:
                    print("Boa você acertou.\nO número era: {}".format(aleatorio))
                    aleatorio = randint (1, 500)
                    pontuacao += 1
                    cont += 1
                    n = int(input('Tente adivinhar o próximo:'))
                else:
                    if n != aleatorio and n < aleatorio:
                        cont += 1
                        print("Esse ainda não é o número")
                        print("Está muito baixo")
                        n = int(input('Tente novamente:'))
                    if n != aleatorio and n > aleatorio:
                        cont += 1
                        print("Esse ainda não é o número")
                        print("Está muito alto")
                        n = int(input('Tente novamente:'))
            print("Você finalizou o modo INFINIT.\nVocê acertou {} números e teve {} tentativas".format(pontuacao, cont))
        pergunta = str(input("Deseja jogar de novo? [S/N]")).upper().strip()
    if pergunta not in ['S', 'N']:
        print('Digite um valor válido [S/N].')
        pergunta = str(input("Deseja jogar de novo? [S/N]")).upper().strip()
print("Obrigado por jogar.\nVolte sempre")

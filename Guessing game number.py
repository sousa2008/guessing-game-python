from random import randint
import time

#variaveis gerais
pergunta = "S"
n = 0
cont = 0
dificuldade = 0
pontuacao = 0
perda = 0
recorde = 0
menu = 1
#variaveis dos recordes: modo dificil
recordeDificil1 = 999
recordeDificil2 = 999
nome1 = ""
nome2 = ""

#varaiveis dos recordes: modo limitado
recordeLimit1 = 0
recordeLimit2 = 0
nomeLimit1 = ""
nomeLimit2 = ""

# Estilização do inicio do game
print ('Carregando...')
time.sleep(1)
print('\tIniciado!')
print('=-=-= Jogo da advinhação =-=-=')

# menu do jogo
while pergunta == "S":
    menu = int(input('Você deseja:\n1-Jogar\n2-Sair\n3-Recordes\n'))
    # validação para o menu não quebrar
    if menu not in [1, 2, 3]:
        print("Valor inválido.\nDigite 1, 2 ou 3.")
        menu = int(input('Você deseja:\n1-Jogar\n2-Sair\n'))
# definiçao do botão 2 como saida
    if menu == 2:
        print("Você apertou para sair.")
        print("Tenha um bom dia!")
        pergunta = "N"

# Jogo
    if menu == 1:
        pontuacao += 100
        print("")
        print("Antes de iniciarmos, escolha a dificuldade:")
        dificuldade = int(input('Você deseja:\n1-Fácil\n2-Médio\n3-Difícil\n4-Tentativas limitadas\n5-Infinit\n'))
        # validação para o menu não quebrar
        if dificuldade not in [1, 2, 3, 4, 5]:
            print('Esse valor não é aceito.\nDigite um dos valores válidos.')
            dificuldade = int(input('Você deseja:\n1-Fácil\n2-Médio\n3-Difícil\n4-Tentativas limitadas\n5-Infinit\n'))
        if dificuldade != 4 and dificuldade != 5:

# definição da dificuldade entre 1, 2 e 3
            if dificuldade == 1:
                aleatorio = randint(1,50)
                print("")
                print("Certo vamos começar.\nIrei pensar em um número entre \033[31;1m1\033[m e \033[31;1m50\033[m.\n")   #def
            elif dificuldade == 2:
                aleatorio = randint(1,100)
                pontuacao += 25
                print("")
                print("Certo vamor começar.\nIrei pensar em um número entre \033[31;1m1\033[m e \033[31;1m100\033[m.\n")
            elif dificuldade == 3:
                aleatorio = randint(1,500)
                pontuacao += 50
                print("")
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
                    if pontuacao <= 0:
                        pontuacao = 1 #não deixar zerar
                elif dificuldade == 2:
                    perda = 9.5
                    if pontuacao <= 0:
                        pontuacao = 1 #não deixar zerar
                elif dificuldade == 3:
                    perda = 11
                    if pontuacao <= 0:
                        pontuacao = 1 #não deixar zerar
                pontuacao -= perda
            print("Você acertou!\nO número era: \033[32;1m{}\033[m\nE você precisou de \033[32;1m{}\033[m tentativas". format(aleatorio, cont))
            print("Sua pontuação foi de: \033[32;1m{}\033[m.".format(pontuacao))
            print("Perfeito" if pontuacao >= 100 else "Otimo" if 80 <= pontuacao < 100 else 'Você tem potencial' if 50 <= pontuacao < 80 else "Dá para melhorar" if 20 <= pontuacao < 50 else "Mais sorte na próxima")
            # definição do recorde
            if pontuacao > recorde:
                recorde = pontuacao
            print("Seu recorde de pontuação atual é de: \033[32;1m{}\033[m.".format(recorde))
            #registrando recorde do modo dificil.
            if dificuldade == 3:
                if pontuacao > recordeDificil1:
                    nome2 = nome1
                    recordeDificil2 = recordeDificil1

                    nome1 = str(input("Digite o nome que irá para os recordes: "))
                    recordeDificil1 = pontuacao

                elif pontuacao > recordeDificil2:
                    nome2 = str(input("Digite o nome que irá para os recordes: "))
                    recordeDificil2 = pontuacao

            pontuacao = 0    #zerar pontuacao para próxima rodada

# Modo de jogo 4
        if dificuldade == 4:
            cont = 0
            aleatorio = randint(1, 100)
            print("")
            print("Você entrou no modo de tentativas limitadas.\nVocê terá 7 tentativas para encontrar o número entre 1 e 100.")
            n = int(input('Tente adivinhar: '))
            cont += 1
            # Laço para limitar o número de jogadas
            while cont < 7 and n != aleatorio:
                    if n < aleatorio:
                        print('Muito baixo.')
                        cont += 1
                        n = int(input('Tente novamente: '))
                    elif n > aleatorio:
                        print('Muito alto.')
                        cont += 1
                        n = int(input('Tente novamente: '))
                    elif n == aleatorio:
                        print("Você conseguiu antes das chances acabarem!\nO número era: \033[32;1m{}\033[m\nVocê usou \033[32;1m{}\033[m tentativas".format(aleatorio, cont))
                        cont += 7
                    elif cont == 7 and n != aleatorio:
                        print("Você perdeu.\nO valor era: \033[32;1m{}\033[m".format(aleatorio))
                        print("Tente novamente.")

            #Definição dos recordes do modo limitado
            if n == aleatorio:
                if cont < recordeLimit1:
                    nomeLimit2 = nomeLimit1
                    recordeLimit2 = recordeLimit1

                    nomeLimit1 = str(input("Digite o nome que irá para os recordes: "))
                    recordeLimit1 = cont
                elif cont < recordeLimit2:
                    nomeLimit2 = str(input("Digite o nome que irá para os recordes: "))
                    recordeLimit2 = cont

# Modo de jogo 5
        if dificuldade == 5:
            pontuacao *= 0
            cont = 0
            aleatorio = randint(1, 500)
            print("")
            print("Você entrou no modo infinito.\n Você tentará acertar números de 1 a 500 e, sempre que acertar, o número mudará.\nQuando quiser encerrar o modo, digite \033[31;1m999\033[m.")
            n = int(input('Tente adivinhar:'))
           # Laço para manter o modo rolando até digitar 999
            while n != 999:
                if n == aleatorio:
                    print("Boa você acertou.\nO número era: \033[32;1m{}\033[m".format(aleatorio))
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
            print("Você finalizou o modo INFINIT.\nVocê acertou \033[32;1m{}\033[m números e teve \033[32;1m{}\033[m tentativas".format(pontuacao, cont))

# reinicio do laço iniciado no começo do programa
        pergunta = str(input("Deseja voltar ao menu? [S/N] ")).upper().strip()

#menu de recordes
    if menu == 3:
       while True:
            print("")
            print("Você entrou no modo recordes.")
            print("Os recordes estão disponiveis para o modo dificil.")
            menu = int(input("Digite o modo que você deseja ver os recordes:\n1-Difícil\n2-Limitado\n3-Voltar\n"))
            if menu == 1:
                print("")
                print("Você selecionou o modo \033[31;1mDIFÍCIL\033[m")
                print("Abaixo estão os 2 melhores colocados no modo: ")
                print("1- \033[32;1m{}\033[m - \033[31;1m{}\033[m".format(recordeDificil1, nome1))
                print("2- \033[32;1m{}\033[m - \033[31;1m{}\033[m".format(recordeDificil2, nome2))
            elif menu == 2:
                print("")
                print("Você selecionou o modo \033[31;1mLIMITADO\033[m")
                print("Abaixo estão os 2 melhores colocados no modo: ")
                print("1- \033[32;1m{}\033[m tentativas - \033[31;1m{}\033[m".format(recordeLimit1, nomeLimit1))
                print("2- \033[32;1m{}\033[m tentativas - \033[31;1m{}\033[m".format(recordeLimit2, nomeLimit2))
            elif menu == 3:
                break

    # validação contra valores inválidos
    if pergunta not in ['S', 'N']:
        print('Digite um valor válido [S/N].')
        pergunta = str(input("Deseja jogar de novo? [S/N]")).upper().strip()

# Mensagem ao sair do laço
print("Obrigado por jogar.\nVolte sempre")

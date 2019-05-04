
numeros = '012345678'
tentativas = 0

def tela():
    print()
    print([i for i in numeros[0:3]])
    print([i for i in numeros[3:6]])
    print([i for i in numeros[6:9]])
    print()

def ganhou():
    for i in ['X', 'O']:
        if i in numeros[0] and i in numeros[1] and i in numeros[2]:
            print(f'Parabéns {i}, você ganhou 1')
            quit()
        if i in numeros[3] and i in numeros[4] and i in numeros[5]:
            print(f'Parabéns {i}, você ganhou 2 ')
            quit()
        if i in numeros[6] and i in numeros[7] and i in numeros[8]:
            print(f'Parabéns {i}, você ganhou 3')
            quit()
        if i in numeros[0] and i in numeros[3] and i in numeros[6]:
            print(f'Parabéns {i}, você ganhou 4')
            quit()
        if i in numeros[1] and i in numeros[4] and i in numeros[7]:
            print(f'Parabéns {i}, você ganhou 5')
            quit()
        if i in numeros[2] and i in numeros[5] and i in numeros[8]:
            print(f'Parabéns {i}, você ganhou 6')
            quit()
        if i in numeros[0] and i in numeros[4] and i in numeros[8]:
            print(f'Parabéns {i}, você ganhou 7 ')
            quit()
        if i in numeros[2] and i in numeros[4] and i in numeros[6]:
            print(f'Parabéns {i}, você ganhou 8')
            quit()


while True:
    tela()

    jogador_1 = str(input('Você é "X", escolha em que posição jogar, de 0 a 8\n'))

    numeros = numeros.replace(jogador_1, 'X')

    tela()

    ganhou()
    tentativas += 1
    if tentativas == 9:
        print('Deu empate')
        quit()

    jogador_2 = str(input('Você é "O", escolha em que posição jogar, de 0 a 8\n'))

    numeros = numeros.replace(jogador_2, 'O')

    tela()

    ganhou()
    tentativas += 1
    if tentativas == 9:
        print('Deu empate')
        quit()








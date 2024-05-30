import os

palavra_secreta = 'aaaooo'
letras_corretas = ''
num_tentativas = 0

while True:


    letra_digitada = input('Digite uma letra: ').lower()
    num_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra. ')
        continue

    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada   #letrars_corretas = letras_corretas + letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns você ganhou !!!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {num_tentativas}')
        letras_corretas = ''
        num_tentativas = 0
        break
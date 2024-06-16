import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2: ',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5: ',
        'Opções': ['1', '10', '25', '50', '30'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 9x9: ',
        'Opções': ['81', '9', '100', '99', '90'],
        'Resposta': '81',
    },
]

def exibir_pergunta(pergunta):
    print('Pergunta:', pergunta['Pergunta'])
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao}')
    print()

def obter_escolha_valida(opcoes):
    while True:
        escolha = input('Escolha uma opção: ')
        if escolha.isdigit():
            escolha_int = int(escolha)
            if 0 <= escolha_int < len(opcoes):
                return escolha_int
        print('Opção inválida, tente novamente.')

def verificar_resposta(pergunta, escolha):
    return pergunta['Opções'][escolha] == pergunta['Resposta']

acertos = 0

for pergunta in perguntas:
    os.system('cls')
    exibir_pergunta(pergunta)
    escolha = obter_escolha_valida(pergunta['Opções'])
    if verificar_resposta(pergunta, escolha):
        acertos += 1
        print('Resposta correta ✔')
    else:
        print('Resposta incorreta ❌')

print(f'Você acertou {acertos} de {len(perguntas)} perguntas')
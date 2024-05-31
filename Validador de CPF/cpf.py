import os
import re

cpf = input('Digite o seu CPF: ')
cpf = re.sub(r'[^0-9]','', cpf)

nove_digitos = cpf[:9]

entrada_repetida = cpf == cpf[0] * len(cpf)
print(entrada_repetida)

contador_regressivo_1 = 10

print(f'O CPF digitado foi: {cpf}')

resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
    os.system('cls')

primeiro_digito = (resultado_digito_1 * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print('O penultimo digitro é:', primeiro_digito)

contador_regressivo_2 = 11
dez_digitos = nove_digitos + str(primeiro_digito)
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
    
segundo_digito = (resultado_digito_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <=9 else 0
print('O ultimo digitro é:', segundo_digito)

cpf_calculado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == cpf_calculado:
    print(f'O CPF {cpf} é válido! ')
else:
    print(f'O CPF {cpf} é inválido ')
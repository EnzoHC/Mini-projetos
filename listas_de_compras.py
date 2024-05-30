import os

lista = []


while True:
    escolha = input('Digite uma opção: [i]nserir [l]istar [a]pagar: ')
    
    if escolha.lower() == 'i':
        os.system('cls')
        produto = input('O que deseja inserir: ')
        lista.append(produto)
        
        
    elif escolha.lower() == 'l':
        os.system('cls')
        if lista == []:
            os.system('cls')
            print('A lista está vazia! ')
        for número, escolha in enumerate(lista):
            print(número, escolha)
    
    elif escolha.lower() == 'a':
        if lista == []:
            os.system('cls')
            print('Não há itens a remover ')
        else:
            indice_str = input('Digite o índice a remover: ')
            try:
                indice = int(indice_str)
                del lista[indice]
                os.system('cls')
                print('Produto removido da lista de compras. ')
            except IndexError:
                os.system('cls')
                print('Digite um número válido! ')
            except ValueError:
                print('Digite um número inteiro. ')
            except Exception:
                print('Erro desconhecido')

            #os.system('cls')
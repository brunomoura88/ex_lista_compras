"""
Exercício lista de compras.
O usuario deve ter a possibilidasde de inserir, apagar e listar itens da sua lista.
Não permita que o programa quebre com erros de listas inexistente.

"""

print('-------LISTA DE COMPRAS-------')

import os

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Não é possivel apagar esse indice!')
        except IndexError:
            print('Índice não existe na lista! ')    
        except Exception:
            print('Erro desconhecido! ')    

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar!')

        for i, valor in enumerate(lista):
            print(i, valor)    
    else:
        print('Por favor escolha uma opção válida!')            
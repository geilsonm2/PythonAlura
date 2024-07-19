import os

def exibir_nome_do_programa():
    print('''
        🇸​​​​​🇦​​​​​🇧​​​​​🇴​​​​​🇷​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​​
''')

def exibir_opcoes():
    print('''
            1. Cadastrar Restaurantes 
            2. Listar Restaurantes  
            3. Ativar Restaurantes 
            4. Cadastrar Restaurantes
        ''' )

def finalizar_app():
    os.system('cls')
    print('Finalizando o sistema.')

def opcao_invalida():
    print('Opcao Inválida! \n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()
  
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite a opção desejada: \n'))

        print(f'Você escolheu a opção: {opcao_escolhida}')

        if opcao_escolhida == 1:
            print('Cadastrar restaurante.')
        elif opcao_escolhida == 2:
            print('Listar restaurante.')
        elif opcao_escolhida == 3:
            print('Ativar Restaurante.')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
import os

restaurantes = [{'nome':'Manai Gastronomia', 'categoria': 'Variados', 'ativo':False},
                {'nome':'Aoyama', 'categoria': 'Japonesa', 'ativo':True},
                {'nome':'Rascal', 'categoria': 'Italiana', 'ativo':False},
]

def exibir_nome_do_programa():
    '''Essa função exibe o nome da nossa aplicação.'''
    print('''
        🇸​​​​​🇦​​​​​🇧​​​​​🇴​​​​​🇷​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​​
''')

def exibir_opcoes():
    '''Essa função exibe as opções disponibilizadas em nossa aplicação.'''
    print('''
            1. Cadastrar Restaurantes. 
            2. Listar Restaurantes.
            3. Alterar estado do restaurante. 
            4. Sair.
        ''' )

def exibir_subtitulo(texto):
    '''Essa função limpa o terminal e exibe uma frase adaptada para cada opção selecionada pelo usuário.'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
   '''Essa função finaliza a nossa aplicação.'''
   exibir_subtitulo('Finalizando o sistema.')

def voltar_ao_menu_principal():
    '''Essa função retorna para o menu principal onde disponibiliza as opções de escolha ao selecionar uma tecla aleatória.'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Essa função garante que o usuário selecione apenas as opções disponíveis em nossa aplicação, retornando ao menu inicial sempre que o usuário selecionar uma opção inexistente.'''
    print('Opcao Inválida! \n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurantes():
    
    '''Essa função é responsável por cadastrar um novo restaurante.
    
    Inputs:
    - Nome do Restaurante
    - Categoria

    Outputs:
    - Adiciona ujm novo restaurante a lista de restaurantes.
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do resturante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função lista o nome dos restaurantes cadastrados em nosso sistema.'''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} |'' Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    
    '''Essa função altera o status dos nossos restaurantes cadastrados como ativado ou desativado.'''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')        

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função verifica, e executa a opção selecionada pelo usuário.'''
    try:
        opcao_escolhida = int(input('Digite a opção desejada: \n'))

        print(f'Você escolheu a opção: {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função dita qual a ordem de execução da aplicação.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

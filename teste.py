import shelve

exibirMenu = True
opcao = 0

while exibirMenu:
    print(f'======== JINGLE PLAYER ========\n')
    opcao = int(input(f'Escolha a acao desejada:\n1.Armazenar dados\n2.Listar dados\n3.Sair\n'))

    match opcao:
        case 1:
            dado = input(str('Qual dado deseja armazenar? '))
            with shelve.open('dados') as dados:

                if 'listaDados' not in dados:
                    dados['listaDados'] = []
                
                lista_dados = dados['listaDados']
                lista_dados.append(dado)
                dados['listaDados'] = lista_dados
            
        
        case 2:
            with shelve.open('dados') as dados:
                lista_dados = dados['listaDados']
                for dado in lista_dados:
                    print(dado)
        case 3:
            print('Finalizando programa')
            exibirMenu = False

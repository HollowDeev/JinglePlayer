import shelve
import os
import time

from playsound import playsound

exibirMenu = False
opcao = 0

with shelve.open('dados') as dados:
    if 'primeiraExecucao' not in dados:
        dados['primeiraExecucao'] = 'sim'

    if dados['primeiraExecucao'] == 'sim':

        print(f'\n======== JINGLE PLAYER ========\n')

        print(f'Informe alguns dados para iniciar a reprodução:')

        intervaloInicial = int(input(f'Informe o tempo de intervalo desejado em minuto [ex: informe 10 para 10 minutos] \n'))

        dados['intervalo'] = intervaloInicial * 60

        caminhoInicial = str(input(f'Qual o caminho da pasta com os Jingles? '))

        dados['caminho'] = caminhoInicial

        dados['primeiraExecucao'] = 'não'
        exibirMenu = True
    else:
        exibirMenu = True

while exibirMenu:
    print(f'\n======== JINGLE PLAYER ========\n')
    opcao = int(input(f'Escolha a acao desejada:\n1.Reproduzir Jingles\n2.Mudar Intervalo\n3.Mudar Caminho da pasta de Jingles\n4.Exibir atual intervalo e caminho\n'))

    match opcao:
        case 1:
            with shelve.open('dados') as dados:
                caminhoArquivo = dados['caminho']
                intervalo = dados['intervalo']
                arquivos = os.listdir(caminhoArquivo)
    
                temArquivosMP3 = False
                arquivosMP3 = []

                for arquivo in arquivos:
                   
                    _, extensao = os.path.splitext(arquivo)

                    if extensao == '.mp3':
                        temArquivosMP3 = True
                        arquivosMP3.append(arquivo)

                if temArquivosMP3 == False:
                    print(f'\nNão foram encontrados arquivos com a extensão MP3 para serem reproduzidos\n')
                else:
                    indice = 0
                    while True:
                        caminhoFormatado = caminhoArquivo.replace("\\", "/")

                        playsound(f'{caminhoFormatado}/{arquivosMP3[indice]}')
                        indice += 1
                        if indice == len(arquivosMP3):
                            indice = 0

                        time.sleep(intervalo)
            
        
        case 2:
            opcaoEscolhinda = int(input(f'DIGITE 0 PARA CANCELAR!\n| Informe o novo tempo de intervalo desejado em minuto [ex: informe 10 para 10 minutos] \n'))
            
            if opcaoEscolhinda != 0:
                novoIntervaloSegundos = opcaoEscolhinda * 60

                with shelve.open('dados') as dados:
                    dados['intervalo'] = novoIntervaloSegundos

        case 3:
            opcaoEscolhinda = str(input(f'DIGITE 0 PARA CANCELAR!\n| Qual o novo caminho da pasta? '))
            
            if opcaoEscolhinda != 0:
                with shelve.open('dados') as dados:
                    dados['caminho'] = opcaoEscolhinda

                print(f'Caminho alterado com sucesso!\n')

        case 4:
            with shelve.open('dados') as dados:
                intervaloFormatado = dados['intervalo'] / 60
                print(f'\nIntervalo atual: {intervaloFormatado} minuto(s)')
                print(f'Caminho atual: {dados['caminho']}')
def informacoes(**kwargs):
   
    linhas()
    endereco = input('Insira o endereço\nDigite a rua:\n')
    linhas()
    num = input('Insira o número da residência:\n')
    linhas()
    bairo = input('Digite o baiiro:\n')
    linhas()
    cep = input('Insira seu CEP:\n')
    linhas()

    print('Faremos ')
   
 
def religacao(liga_p):

    liga_p = input('[1] - Corte de energia\n[2] - URGÊNCIA\n[3] - Falta de energia\nInsira a opção desejada: ')

    if liga_p == '1':
        print('Sua energia foi cortada devido o vencimento da fatura\nCom a quitação da dívida iremos realizar o religamento da sua enrgia')
        linhas()
        print('Reinicie o programa e insira a opção consulta da fatura')

    elif liga_p == '2':
        linhas()
        input('Insira a sua emergência:\n')
        linhas()
        print('Enviaremos uma equipe para a sua residência')

    elif liga_p == '3':
        input('Insira o motivo da falta de energia:\n')
        print('Enviaremos uma equipe para a sua residência')
        
    else:
        print('Erro!')

def linhas():
    global linhas
    print('-' * 20) 

def titulo():

    linhas()
    print('Olá,Você deseja realizar a tranferência de titularidade\nPreencha o que está sendo solicitado')
    linhas()

    print('Insira o endereço que você quer se titularizar')
    linhas()

    rua = input ('insira a rua:\n')
    linhas()
    num = int(input ('insira o número da residência:\n'))
    linhas()
    bar = input ('Insira o bairro:\n')
    linhas()
    cep = input ('Insira o CEP:\n')
    linhas()
    print('A troca de título para o endereço\n',rua,num,bar,cep,'\nserá realizada em 2 à 3 dias\nMuito obrigado!')

def ligacao():
    
    linhas()
    print('Olá, você deseja realizar uma nova ligação em um novo endereço\nInsira as informaçôes necessárias para realizarmos este procedimento')
    linhas()

    linhas()
    endereco = input('Insira o endereço\nDigite a rua:\n')
    linhas()
    num = input('Insira o número da residência:\n')
    linhas()
    bairo = input('Digite o baiiro:\n')
    linhas()
    cep = input('Insira seu CEP:\n')
    linhas()

    linhas()
    print('Iremos realizar uma nova ligação neste endereço\nEntre 2 à 4 dias,com uma taxa de R$200,00 na próxima fatura\nMuito obrigado!')
    linhas()

def reinicio():
    global reinicio
    
    linhas()
    reini_1 = input('Você deseja outro servico?\n[1] - Sim  [2] - Não\nInsiria o número da opção desejada:  ')
    linhas()
    if reini_1 == '1':
         while True:
             servico_principal()
             
        
    elif reini_1 =='2':
        print('Espero ter conseguido te ajudar, muito obrigado!')
        
    else:
        print('Errouuuu')

def servico_principal():

    linhas()
    print(' Opções de serviços:')
    linhas()

    opcao = print('[1] - consulta da fatura\n[2] - Religação\n[3] - Troca de título\n[4] - Nova ligação\n[5] - Número para contato\n[6] - Sair')

    linhas()
    servico = int(input('Insira o múmero do serviço desejado: '))
    linhas()

    if servico == 1:
        print('Olá\nConsulte sua fatura aqui!')
        linhas()

        def fatura():

         linhas()
        print('O que você deseja?\n[1] - Valor da fatura\n[2] - retirar a 2° via da fatura\n[3] - Parcelamento da fatura')
        linhas()

        ser_fa = input('Qual serviço desejado?: ')
        linhas()

        import random

        
        valor_fatura = random.randint(50,1000)

        if ser_fa == '1':
            print('O valor da sua fatura é de R$',valor_fatura)
            
        
        elif ser_fa == '2':
            print('Enviamos para você sua fatura por E-mail')
            

        elif ser_fa == '3':
            print('Você consegue parcelar sua fatura em até 5x')
            parcela = float(input('Insira em quantas parcelas você deseja: '))
        
            match  parcela:

                case 1:
                    linhas()
                    print('Você pagará R$',valor_fatura)
                    linhas()
                
                case 2:
                    par_2 = valor_fatura/2
                    linhas()
                    print('Você pagará em 2x de R$',par_2)
                    linhas()

                case 3:
                    par_3 = valor_fatura/3
                    linhas()
                    print('Você pagará em 3x de R$',par_3)
                    linhas()

                case 4:
                    par_4 = valor_fatura/4
                    linhas()
                    print('Você pagará em 4x de R$',par_4)
                    linhas()

                case 5:
                    par_5 = valor_fatura/5
                    linhas()
                    print('Você pagará em 5x de R$',par_5)
                    linhas()

            

        else :
         print('Erro00000000000000\nTente novamente mais tarde!')


    elif servico == 2:

        linhas()
        print('Olá\nPor qual motivo você deseja solicitar a religação?')
        linhas()
        
    # liga = input('[1] - Corte de energia\n[2] - URGÊNCIA\n[3] - Falta de energia\nInsira a opção desejada: ')
        linhas()
        religacao('liga_p')

    elif servico == 3: 
        titulo()
        
    elif servico == 4:
        ligacao()

    elif servico == 5:
        
        linhas()
        print('Olá, fale conosco através deste número\n 0800-123-456')
        linhas()

    elif servico == 6:
        print('BYE,BYE')
        

    else:
        print('Opção inválida\nTente novamente.')

servico_principal()
reinicio()
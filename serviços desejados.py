def linhas():
    global linhas
    print('-' * 20)
    

linhas()
print(' Opções de serviços:')
linhas()

opcao = print ('[1] - consulta da fatura\n[2] - Religação\n[3] - Troca de título\n[4] - Nova ligação\n[5] - Número para contato')

linhas()
servico = int(input('Insira o múmero do serviço desejado: '))
linhas()

if servico == '1':
    print('Olá\nConsulte sua fatura aqui!')

    def fatura():

     print('O que você deseja?\n[1] - Valor da fatura\n[2] - retirar a 2° via da fatura\n[3] - Parcelamento da fatura')
    linhas()
    ser_fa = input('Qual serviço desejado?: ')

    import random

    valor_fatura = random.randint(50,1000)

    if ser_fa == '1':
        print('O valor da sua fatura é de',valor_fatura)
    
    elif ser_fa == '2':
        print('Enviamos para você sua fatura por E-mail')

    elif ser_fa =='3':
        print('Você consegue parcelar sua fatura em até 5x')
        parcela = int(input('Insira em quantas parcelas você deseja: '))
    
        match  parcela:

            case '1':
                print('Você pagará R$',valor_fatura)
            
            case '2':
                par_2 = valor_fatura/2
                print('Você pagará em 2x de R$',par_2)

            case '3':
                par_3 = valor_fatura/3
                print('Você pagará em 3x de R$',par_3)

            case '4':
                 par_4 = valor_fatura/4
                 print('Você pagará em 4x de R$',par_4)
        
            case '5':
                 par_5 = valor_fatura/5
                 print('Você pagará em 5x de R$',par_5)
    else :
        print('Erro000000000000000000000000000000000000z\nTente novamente mais tarde!')
        
elif servico == '2':

    linhas()
    print('Olá\nPor qual motivo você deseja solicitar a religação?')
    linhas()

    def religacao():

     print('[1] - Corte de energia\n[2] - URGÊNCIA\n[3] - Falta de energia ')

     if religacao == '1':
         print('Sua energia foi cortada devido o vencimento da fatura\nCom a quitação da dívida iremos realizar o religamento da sua enrgia')
         linhas()
         input('[1] - ')
         
         match religacao:
             
             case '1':
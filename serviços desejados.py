def ligacao(liga_p):

    if liga_p == "1":
        print('Sua energia foi cortada devido o vencimento da fatura\nCom a quitação da dívida iremos realizar o religamento da sua enrgia')
        linhas()
        print('Reinicie o programa e insira a opção consulta da fatura')


    elif liga_p == "2":
        linhas()
        input('Insira a sua emergência:\n')
        linhas()
        print('Enviaremos uma equipe para a sua residência')

    elif liga_p == "3":
        input('Insira o motivo da falta de energia:\n')
        print('Enviaremos uma equipe para a sua residência') 

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
    num = input ('insira o número da residência:\n')
    linhas()
    bar = input ('Insira o bairro:\n')
    linhas()
    print('A troca de título para o endereço\n',rua,num,bar,'\nserá realizada em 2 à 3 dias\nMuito obrigado!')

    
while True:

 linhas()
 print(' Opções de serviços:')
 linhas()

 opcao = print ('[1] - consulta da fatura\n[2] - Religação\n[3] - Troca de título\n[4] - Nova ligação\n[5] - Número para contato')

 linhas()
 servico = int(input('Insira o múmero do serviço desejado: '))
 linhas()

 if servico == 1:
    print('Olá\nConsulte sua fatura aqui!')

    print('O que você deseja?\n[1] - Valor da fatura\n[2] - retirar a 2° via da fatura\n[3] - Parcelamento da fatura')

    def fatura():

     linhas()
    ser_fa = input('Qual serviço desejado?: ')

    import random

    valor_fatura = random.randint(50,1000)

    if ser_fa == '1':
        print('O valor da sua fatura é de R$',valor_fatura)
    
    elif ser_fa == '2':
        print('Enviamos para você sua fatura por E-mail')

    elif ser_fa =='3':
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
       
    liga = input('[1] - Corte de energia\n[2] - URGÊNCIA\n[3] - Falta de energia\nInsira a opção desejada: ')
    linhas()
    ligacao(liga)

 elif servico == 3: 
    titulo()
    

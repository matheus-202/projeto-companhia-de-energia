import os


print("este programa irá pedir seus dados de login ")
# Dicionário de usuários e senhas

usuarios = {
    'guilherme': 'ronald',
    'joao': 'senha456',
    'flavia': 'senha789',

}
senhas= {
    'senha123':'senha456',
    'senha321':'senha789',
    
}
def logar():
    senha = input("insira sua senha: ")
    logar(senha)
logar()    
def login():
    nome = input("insira seu email ou CPF: ")
    
    login(nome)
    
    
login()    

    
   
def verificar(nome,senha):   
    for nome in senha  in usuarios:
        print("correto,continue")
    for nome in senha in usuarios:
        print("incorreto,digite novamente")

verificar(nome,senha)
   


def linhas():
    global linhas
    print('-' * 20)
    
linhas()
print(' Opções de serviços:')
linhas()

opcao = print ('[1] - consulta da fatura\n[2] - Religação\n[3] - Troca de título\n[4] - Nova ligação\n[5] - Número para contato')


linhas()
servico = input('Insira o múmero do serviço desejado: ')
linhas()
def religacao():

    if religacao == '1':
        print('Sua energia foi cortada devido o vencimento da fatura\nCom a quitação da dívida iremos realizar o religamento da sua enrgia')
        linhas()
        input('Você já realizou o pagamento de sua dívida\n[1] - Sim  [2] - Não\nInsira sua resposta: ')
        
        match religacao:
            
            case '1':
                input('insira o número do protocolo: ' ) 
                if servico == religacao: 
                    print('Enviaremos uma equipe para fazer o religamento da sua energia\nTe peço que você pague em dia suas contas, muito obrigado!')
                elif servico!= religacao:
                    print('Erro, reinicie o programa')
                else:
                    print('ERRRRRROOOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUUUUUUU')

            case '2':
                print('Reinicie o programa e selecione a opção [1] - consulte sua fatura')
    if servico == '1':
        print('Olá\nConsulte sua fatura aqui!')

    def fatura():
        print('O que você deseja?\n[1] - Valor da fatura\n[2] - retirar a 2° via da fatura\n[3] - Parcelamento da fatura')
        linhas()
    ser_fa = input('Qual serviço desejado?: ')
    
    print('O que você deseja?\n[1] - Valor da fatura\n[2] - retirar a 2° via da fatura\n[3] - Parcelamento da fatura')
    linhas()
    ser_fa = input('Qual serviço desejado?: ')
    fatura()
    
    

    import random

     
    valor_fatura = random.randint(50,1000)

    if ser_fa == '1':
        print('O valor da sua fatura é de',valor_fatura)
    
    elif ser_fa == '2':
        print('Enviamos para você sua fatura por E-mail')

    elif ser_fa == '3':
        print('Você consegue parcelar sua fatura em até 5x')
        parcela = float(input('Insira em quantas parcelas você deseja: '))
    
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
    
    else:
        print('Erro000000000000000000000000000000000000z\nTente novamente mais tarde!')
        
    if servico == '2':

        linhas()
    print('Olá\nPor qual motivo você deseja solicitar a religação?')
    linhas()

    input('[1] - Corte de energia\n[2] - URGÊNCIA\n[3] - Falta de energia \nInsira a opção desjada: ')

 
    religacao()


print('Erro000000000000000000000000000000000000z\nTente novamente mais tarde!')
        

# case: '1' #para criar uma turma
# print("Criando turma...")

# turma = input("Qual turma você deseja criar?\n")

# pasta_turmas = "turma"

# if not  os.path.exists(pasta_turmas):
#     os.makedirs(pasta_turmas)
    
# arquivo_txt =os.path.join(turma + ".txt")

# if  os.path.exists(arquivo_txt):
#     print("Esta turma já existe")
# else:
    
#     with open (pasta_turmas + '/' + arquivo_txt , 'w', encoding='utf-8') as arquivo:
#         print(f"turma {turma} criada.") #cria a turma caso exista
  

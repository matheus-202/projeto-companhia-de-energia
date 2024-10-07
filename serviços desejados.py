print("este programa irá pedir seus dados de login ")
# Dicionário de usuários e senhas

usuarios = {
    'guilherme': 'senha123',
    'joao': 'senha456',
    'flavia': 'senha789',

}
    



def login():
    cadastro_de_usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if cadastro_de_usuario not in usuarios.keys():
        print("Usuário não encontrado.")
        login()
    elif usuarios[cadastro_de_usuario] != senha:
        print("Senha incorreta.")
        login()
    else:
        print("Login bem-sucedido!")
login()

cadastrar ={
    'Nome: Ana Silva',
    'Data de Nascimento: 15/03/1990,'
    'E-mail: ana.silva@email.com',
    'Senha: senha123',
    'CPF: 123.456.789-00',
    'Endereço: Rua das Flores, 123, Centro, 12345-678, UC1',
}
def cadastrar():
Nome = input("Digite seu usuário: ")

Data_de_nascimento =input(" ")

CPF =input(" ")

Endereço_completo =input(" ")




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
    else :
        print('Erro000000000000000000000000000000000000z\nTente novamente mais tarde!')
        
fatura()
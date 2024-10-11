import random

# Função para exibir opções de login
login={}
def exibir_login():
    print("Escolha uma opção:")
    print("[1] - Fazer login")
    print("[2] - cadastre-se")

# Função para obter a opção do usuário
def obter_opcao():
    return int(input("Digite sua opção: "))

# Função para validar login (pode ser melhorada com um sistema real)
def validar_login (email_cpf ,senha):
    # Dummy validation logic for demonstration
    return True

# Função para fazer o login
def login():
    while True:
        exibir_login()
        opcao = obter_opcao()

        if opcao == 2:
            print("caso não tenha cadastro crie um agora mesmo")
            nome= input("Digite seu nome completo:")
            Endereço_completo= input("digite seu endereço completo:")
            data_de_nascimento=input("digite sua data de nascimento:")
            cpf=input("digite seu CPF:")
            senha = input("Digite sua senha: ")
            
            
            if validar_login(nome, senha ,cpf, data_de_nascimento , Endereço_completo):
                print("Login bem-sucedido!")
                return
            else:
                print("Login falhou. Tente novamente.")
            break

        if opcao == 1:
            email_cpf = input("Digite seu email ou seu CPF: ")
            senha = input("Digite sua senha: ")
            
        if validar_login(email_cpf, senha):
                print("Login bem-sucedido!")
                return
        else:
                print("Login falhou. Tente novamente.")
        break      
# Função para exibir uma linha separadora
def linhas():
    print('-' * 20)

# Função para exibir serviços disponíveis
def exibir_servicos():
    linhas()
    print('Opções de serviços:')
    linhas()
    print('[1] - Consulta da fatura')
    print('[2] - Religação')
    print('[3] - Troca de título')
    print('[4] - Nova ligação')
    print('[5] - Número para contato')
    linhas()

# Função para religação
def religacao():
    print('Sua energia foi cortada devido ao vencimento da fatura.')
    pagamento = input('Você já realizou o pagamento de sua dívida?\n[1] - Sim  [2] - Não\nInsira sua resposta: ')
    
    if pagamento == '1':
        protocolo = input('Insira o número do protocolo: ')
        print('Enviaremos uma equipe para fazer o religamento da sua energia. Obrigado!')
    elif pagamento == '2':
        print('Reinicie o programa e selecione a opção [1] - consulte sua fatura.')
    else:
        print('Opção inválida.')

# Função para consulta de fatura
def consulta_fatura():
    valor_fatura = random.randint(50, 1000)
    print('O que você deseja?\n[1] - Valor da fatura\n[2] - Retirar a 2° via da fatura\n[3] - Parcelamento da fatura')
    ser_fa = input('Qual serviço desejado?: ')
    
    if ser_fa == '1':
        print(f'O valor da sua fatura é de R$ {valor_fatura:.2f}')
    elif ser_fa == '2':
        print('Enviamos para você sua fatura por E-mail.')
    elif ser_fa == '3':
        parcelas = int(input('Insira em quantas parcelas você deseja (1 a 5): '))
        if 1 <= parcelas <= 5:
            valor_parcela = valor_fatura / parcelas
            print(f'Você pagará em {parcelas}x de R$ {valor_parcela:.2f}')
        else:
            print('Número de parcelas inválido. Max: 5')
    else:
        print('Opção inválida.')

# Fluxo principal do programa
if __name__ == "__main__":
    login()
    exibir_servicos()
    servico = input('Insira o número do serviço desejado: ')

    if servico == '1':
        consulta_fatura()
    elif servico == '2':
        religacao()
    else:
        print('Serviço não disponível. Tente novamente.')

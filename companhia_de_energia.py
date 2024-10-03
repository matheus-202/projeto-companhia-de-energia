print("este programa irá pedir seus dados de login ")
# Dicionário de usuários e senhas


    



def login():
    cadastro_de_usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if cadastro_de_usuario not in usuarios:
        print("Usuário não encontrado.")
    elif usuarios[cadastro_de_usuario] != senha:
        print("Senha incorreta.")
    else:
        print("Login bem-sucedido!")
login()

print("vamos confirmar se encontraremos seu login")
usuarios = {
    'e-mail': 'senha123',
    'e-mail': 'senha456',
    'e-mail': 'senha789',
}


def cadastro():
    
    
 
cadastro_de_usuario = input("Digite seu nome: ")
senha = input("Digite sua data de nascimento: ")
cadastro = {
    'e-mail': 'senha123',
    'e-mail': 'senha456',
    'e-mail': 'senha789',
}


def linhas():
    global linhas
    print('-' * 20)
    

linhas()
print(' Opções de serviços:')
linhas()

opcao = print ('[1] - consulta da fatura\n[2] - Religação\n[3] - Falta de energia\n[4] - Troca de título\n[5] - Nova ligação\n[6] - Número para contato')

linhas()
servico = int(input('Insira o múmero do serviço desejado: '))
linhas()

print(servico)
# Chama a função de login


  

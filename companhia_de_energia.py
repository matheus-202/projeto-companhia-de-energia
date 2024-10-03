print("este programa irá pedir seus dados de login ")
# Dicionário de usuários e senhas



def login():
    print("Bem-vindo ao sistema de login!")
    
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

   
usuarios = {
    'usuario1': 'senha123',
    'usuario2': 'senha456',
    'usuario3': 'senha789',
}

def login():
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario not in usuarios:
        print("Usuário não encontrado.")
    elif usuarios[usuario] != senha:
        print("Senha incorreta.")
    else:
        print("Login bem-sucedido!")

login()

    

linhas()
print(' Opções de serviços:')
linhas()

opcao = print ('[1] - consulta da fatura\n[2] - Religação\n[3] - Falta de energia\n[4] - Troca de título\n[5] - Nova ligação\n[6] - Número para contato')

linhas()
servico = int(input('Insira o múmero do serviço desejado: '))
linhas()

print(servico)
# Chama a função de login


  

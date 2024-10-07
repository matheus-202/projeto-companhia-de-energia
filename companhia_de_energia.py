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


  

print("este programa irá pedir seus dados de login ")
# Dicionário de usuários e senhas
usuarios ={ 
    "guilherme": "senha1234",
    "usuario2": "senha456",
    "usuario3": "senha789"
}


def login():
    print("Bem-vindo ao sistema de login!")
    
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    verdadeiro = True
   
    
    # Verifica se o usuário e a senha estão corretos
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido! Bem-vindo,", usuario)
    if usuarios != senha:
        print("incorreto")
    if usuarios == verdadeiro:
        print("correto")
    
    
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


  

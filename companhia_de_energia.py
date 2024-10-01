print("este programa irá pedir seus dados de login ")
# Dicionário de usuários e senhas
usuarios = {
    "usuario1": "senha123",
    "usuario2": "senha456",
    "usuario3": "senha789"
}




def login():
    print("Bem-vindo ao sistema de login!")
    
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    
    # Verifica se o usuário e a senha estão corretos
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido! Bem-vindo,", usuario)
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
login()

# Chama a função de login


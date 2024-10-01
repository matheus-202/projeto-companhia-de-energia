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
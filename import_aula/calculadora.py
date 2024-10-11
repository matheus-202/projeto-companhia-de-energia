from operacoes import somar, subtrair, multiplicar, dividir
from interface import exibir_menu, obter_opcao, obter_numeros

def main():
    while True:
        exibir_menu()
        opcao = obter_opcao()

        if opcao == 5:
            print("Saindo...")
            break

        a, b = obter_numeros()

        if opcao == 1:
            print(f"Resultado: {somar(a, b)}")
        elif opcao == 2:
            print(f"Resultado: {subtrair(a, b)}")
        elif opcao == 3:
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcao == 4:
            print(f"Resultado: {dividir(a, b)}")
        else:
            print("Opção inválida!")


main()
    
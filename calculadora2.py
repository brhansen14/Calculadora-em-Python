# Funções para cada operação

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x/y 
    else: 
        return "Erro: Divisão por zero não permitida!"
    
# Menu para o ususario escolher a operação

def menu():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

# Loop principal
while True:
    menu()

    # Recebe a escolha do usuário
    escolha = input("Digite a operação (1/2/3/4) ou 'sair' para encerrar: ")

    if escolha == 'sair':
        print("Encerrando a calculadora.")
        break

    if escolha in ['1', '2', '3', '4']:
        # Recebe os números do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação de acordo com a escolha
        if escolha == '1':
            print(f"{num1} + {num2} = {soma(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Opção inválida! Tente novamente.")

    print("\n")  # Pula uma linha para melhorar a leitura no console
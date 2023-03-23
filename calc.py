
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Error!")
        return 0
    else:
        return a / b


def exibir_menu():
    print("Digite a operacao desejada:")
    print("+ = Somar")
    print("- = Subtrair")
    print("* = Multiplicar")
    print("/ = Dividir")
    print("x = Sair")


while True:
    exibir_menu()
    opcao = input("Escolha uma das opcoes acima: ")
    
    if opcao == 'x':
        print("Calculo encerrado...")
        break
    
    if opcao not in ['+', '-', '*', '/']:
        print("Opcao invalida, tente novamente!")
        continue
    
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    
    if opcao == '+':
        resultado = somar(num1, num2)
        print(f"{num1} + {num2} = {resultado}")
    elif opcao == '-':
        resultado = subtrair(num1, num2)
        print(f"{num1} - {num2} = {resultado}")
    elif opcao == '*':
        resultado = multiplicar(num1, num2)
        print(f"{num1} x {num2} = {resultado}")
    elif opcao == '/':
        resultado = dividir(num1, num2)
        print(f"{num1} / {num2} = {resultado}")

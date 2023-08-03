#print('Hello world')

print('Trabalho de Linguagem de programação N-01')

class calculadora:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.resultado = 0

    def somar(self,numero1,numero2):
        self.num1 = numero1
        self.num2 = numero2
        self.resultado = self.num1 + self.num2
        return self.resultado    

    def subtrair(self,numero1,numero2):
        self.num1 = numero1
        self.num2 = numero2
        self.resultado = self.num1 - self.num2
        return self.resultado    
    
    def multiplicar(self,numero1,numero2):
        self.num1 = numero1
        self.num2 = numero2
        self.resultado = self.num1 * self.num2
        return self.resultado
    
    def dividir(self,numero1,numero2):
        self.num1 = numero1
        self.num2 = numero2
        self.resultado = self.num1 / self.num2
        return self.resultado

    def expoente(self,numero1,numero2):
        self.num1 = numero1
        self.num2 = numero2
        self.resultado = self.num1 ** self.num2
        return self.resultado

    def resto(self,numero1,numero2):
        self.num1 = numero1
        self.num2 = numero2
        self.resultado = self.num1 % self.num2
        return self.resultado
    
    def raiz(self,numero1,numero2):
        self.num1 = numero1
        self.num2 = numero2
        self.resultado = (self.num1 + self.num2) ** 0.5
        return self.resultado
    
def seguir(entrada):
    if entrada:
        return True
    else:
        return False
    
def menu():
    operacoes={1:'Somar', 2: 'Subtrair', 3:'Multiplicar',4:'Dividir',5:'Expoente',6:'Resto',7:'Raiz'}
    calcular = calculadora()
    print("""Qual é a operação matemàtica que deseja realizar?
        1- Soma
        2- Subtração
        3- Multiplicação
        4- Divisão
        5- Expoente
        6- Módulo
        7- Raiz
        Digite o número da opção e aperte ENTER para confirmar""")
    executar = True
    while executar:
        opc = input()
        if not (opc in '1 2 3 4 5 6 7'):
            print("Essa opção é inválida!")
            continue
        else:
            opc = int(opc)
            print(f"Você escolheu a opção de {operacoes[opc]}." )
            print('Trabalharemos apenas com números inteiros.')
        if opc ==1:
            numero1 = int(input("Digite o penúltimo numero do seu RU: "))
            numero2 = int(input("Digite o último numero do seu RU: "))
            resultado = calcular.somar(numero1,numero2)
            print(f"O resultado da soma é {resultado}.")
            executar = seguir(input("Aperte qualquer botão para continuar, ou pressione Enter para sair da calculadora."))
        elif opc ==2:
            numero1 = int(input("Digite o penúltimo numero do seu RU: "))
            numero2 = int(input("Digite o último numero do seu RU: "))
            resultado = calcular.subtrair(numero1,numero2)
            print(f"O resultado da subtração é {resultado}.")
            executar = seguir(input("Aperte qualquer botão para continuar, ou pressione Enter para sair da calculadora."))
        elif opc ==3:
            numero1 = int(input("Digite o penúltimo numero do seu RU: "))
            numero2 = int(input("Digite o último numero do seu RU: "))
            resultado = calcular.multiplicar(numero1,numero2)
            print(f"O resultado da multiplicação é {resultado}.")
            executar = seguir(input("Aperte qualquer botão para continuar, ou pressione Enter para sair da calculadora."))
        elif opc ==4:
            numero1 = int(input("Digite o penúltimo numero do seu RU: "))
            numero2 = int(input("Digite o último numero do seu RU: "))
            resultado = calcular.dividir(numero1,numero2)
            print(f"O resultado da divisão é {resultado}.")
            executar = seguir(input("Aperte qualquer botão para continuar, ou pressione Enter para sair da calculadora."))
        elif opc ==5:
            numero1 = int(input("Digite o penúltimo numero do seu RU: "))
            numero2 = int(input("Digite o último numero do seu RU: "))
            resultado = calcular.expoente(numero1,numero2)
            print(f"O valor do expoente é {resultado}.")
            executar = seguir(input("Aperte qualquer botão para continuar, ou pressione Enter para sair da calculadora."))
        elif opc ==6:
            numero1 = int(input("Digite o penúltimo numero do seu RU: "))
            numero2 = int(input("Digite o último numero do seu RU: "))
            resultado = calcular.resto(numero1,numero2)
            print(f"O resultado do resto é {resultado}.")
            executar = seguir(input("Aperte qualquer botão para continuar, ou pressione Enter para sair da calculadora."))
        elif opc ==7:
            numero1 = int(input("Digite o penúltimo numero do seu RU: "))
            numero2 = int(input("Digite o último numero do seu RU: "))
            resultado = calcular.raiz(numero1,numero2)
            print(f"O resultado da raiz é {resultado}.")
            executar = seguir(input("Aperte qualquer botão para continuar, ou pressione Enter para sair da calculadora."))

menu()






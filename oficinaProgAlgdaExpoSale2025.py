import numpy as np
import math

print("============ MENU ============")
print("1 - Matrizes")
print("2 - Série de Imputs")
print("3 - Conferir se um número é par ou ímpar")
print("4 - Conferir quantas vogais e caracteres tem em um texto")
print("5 - Resolver equação quadrática")
print("6 - Sequência de Fibonacci")
print("7 - Sequência de Números Primos")
print("8 - Calculadora")
print("9 - Organizador de lista em ordem crescente")

try:
    escolha = int(input("Escolha: "))

    if escolha == 1:
        matriz = ""
        filas = []
        ordem = 1
        print(np.__version__)
        A = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
        detA = np.linalg.det(A)
        print(detA)

        B = ([1,2],
            [2,1])
        B_inv = np.linalg.inv(B)
        print(B_inv)

        for i in range(3):
            filas.append(i+1)
        ordem = len(filas)
        for i in range(ordem):
            print(filas)

        matriz = (f"{filas} \n{filas} \n{filas}")
        
        print(matriz)

    elif escolha == 2:
        valor = float(input("Insira um valor para duplica-lo: "))
        print (f"Seu valor duplicado é {valor*2}")
        for i in range(2):
            for i in range (3):
                print(i+1)

    elif escolha == 3:
        numero = int(input("Digite um valor inteiro: "))
        if (numero % 2 == 0):
            print(f"O número {numero} é par")
        else:
            print(f"O número {numero} é ímpar")
    
    elif escolha == 4:
        palavra = input("Digite algo: ")
        vogais = "aeiou"
        contador = 0
        caracteres = 0
        for caractere in palavra:
            caracteres += 1
            if caractere.lower() in vogais:
                contador += 1
        print(f"O texto possui {contador} vogais dentre {caracteres} caracteres.")
    
    elif escolha == 5:
        a = float(input("Insira o valor de a: "))
        b = float(input("Insira o valor de b: "))
        c = float(input("Insira o valor de c: "))
        if (b**2 - 4*a*c)< 0:
            print("O valor de x1 e x2 é imaginário")
        else:
            x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
            x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
            print (f"O valor de x1 é {x1} e x2 é {x2}")
    
    elif escolha == 6:
        termos = int(input("Quantos termos você deseja da sequência de Fibonacci? "))
        a = 0
        b = 1
        if termos == 0:
            print("Ok, sem termos então")
        elif termos == 1:
            print(a)
        elif termos >= 2:
            print(a)
            print(a+b)
            if termos >2:
                for i in range(termos-2):
                    c = a+b
                    print (c)
                    a = b
                    b = c
    
    elif escolha == 7:
        intervalo = int(input("Digite o número para definir o intervalo de números primos desejados: "))
        primos = []
        ultimo = 0
        for num in range(2, intervalo+1):
            eh_primo = True
            # Testa divisores de 2 até a raiz quadrada do número
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:  # Se divisível por i
                    eh_primo = False
            if eh_primo == True:
                primos.append(num)
                ultimo = num
                # print(num, end=" ")
        print(primos)
        print(f"O último primo dentre {intervalo} números é o {ultimo}")
    
    elif escolha == 8:
        sair = 1
        while sair != "0":
            try:
                v1 = float(input("Digite o 1º valor: "))
                v2 = float(input("Digite o 2º valor: "))
                op = input("Digite a operação desejada (+,-,*,/,**, raiz): ").lower()

                if op == "+":
                    print(v1 + v2)
                elif op == "-":
                    print(v1 - v2)
                elif op == "*":
                    print(v1 * v2)
                elif op == "/":
                    if v2 == 0:
                        print("Indefinição matemática")
                    else:
                        print(v1 / v2)
                elif op == "**":
                    print(v1 ** v2)
                elif op == "raiz":
                    if v1 < 0:
                        print("Raiz imaginária")
                    elif v2 == 0:
                        print("Indefinição matemática")
                    else:
                        print(math.pow(v1, 1/v2))  # raiz de índice v2

                else:
                    print("Digite uma operação válida")

                sair = input("Para sair digite 0: ")
                if sair == "0":
                    break

            except ValueError:
                print("Insira um valor numérico válido!")
                break
    
    elif escolha == 9:
        lista = []
        n = int(input("Quantos números você quer adicionar na lista? "))
        def adicionar(valor):
            lista.append(valor)
            print(f"{valor} adicionado com sucesso à lista")
        for i in range(n):
            valor = float(input("Insira um valor: "))
            adicionar(valor)
        numeros_ordenados = sorted(lista)
        print(f"Sua lista tem {len(lista)} valores e ela organizada em ordem crescente fica assim:")
        print(numeros_ordenados)

except ValueError:
    exit()
import os
import math

def confere_data(data):
    try:
        dia, mes, ano = data.split("/")
        dia = dia.zfill(2)
        mes = mes.zfill(2)
        ano = ano.zfill(4)
        if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 0 <= int(ano) <= 2026:
            print(f"Data válida: Dia {dia}, Mes {mes}, Ano {ano}")
        else:
            raise Exception
    except:
        print("Data inválida")

def moeda():
    # Gera 0 (cara) ou 1 (coroa) sem usar random
    return ord(os.urandom(1)) % 2



data = input("Digite uma data para conferir se ela é válida ou não (dd/mm/yyyy): ")
confere_data(data)

#Coin flip sequence (HTT TTH)

acertou = False
gerados = ""
contador = 0
tentativas = 0
sequencia = input("Escolha uma sequência de 3 jogadas de cara/coroa (ex. HTT): ").upper()

while not acertou:
    while contador < 3:
        if moeda() == 0:
            gerados += "H"  # Cara
        else:
            gerados += "T"  # Coroa
        contador += 1
    contador = 0

    if len(gerados) >= 3:
        ultimos3 = gerados[-3:]  # pega os últimos 3
        if ultimos3 == sequencia:
            print(f"🎉 Você acertou a sequência em {tentativas+1} tentativas!")
            print(gerados)
            acertou = True
        else:
            tentativas+=1

# Números narcisistas, números de Armstrong ou números pluperfeitos digital
# número inteiro que é igual à soma dos seus próprios dígitos elevados à potência do número de dígitos que ele possui
# ex. 153 e 9474

num = input("Digite um número para conferir se ele é um número narcisista: ")
expoente = len(num)
soma=sum(int(digito) ** expoente for digito in num)

if soma == int(num):
    print(f"{num} é narcisista")
else:
    print(f"{num} NÃO é narcisista")

# Chicken McNugget Theorem, Problema da Moeda de Frobenius ou Problema do Selo Postal.
# Dados dois números inteiros positivos e coprimos (que não dividem o mesmo divisor comum além de 1),
# o maior número inteiro que NÃO pode ser escrito como combinação linear
# desses dois números (usando apenas soma e multiplicação por inteiros não negativos)
# é dado por: m*n - m - n
# ex. 9 e 20: 9 * 20 - 9 - 20 = 151 → não é possível comprar exatamente 151 nuggets
# Qualquer número maior que 151 pode ser obtido com alguma combinação de 9 e 20

m = int(input("Digite um número: "))
n = int(input("Digite outro número: "))

if m<=0 or n<=0:
    print(f"Pelo menos um dos números {m} ou {n} NÃO é positivo, logo o Problema da Moeda de Frobenius não funciona")
elif math.gcd(m, n) != 1: # Se o maior divisor comum não for 1
    print(f"Os números {m} e {n} NÃO são coprimos, logo o Problema da Moeda de Frobenius não funciona")
else:
    print(f"Os números {m} e {n} são coprimos")
    print(f"O maior número inteiro que NÃO pode ser escrito como combinação linear de {m} e {n} é: {m*n - m - n}")

# Todo Algoritmo de Euclides


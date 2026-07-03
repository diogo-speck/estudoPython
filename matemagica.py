import os

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
todas = ""
sequencia = input("Escolha uma sequência de 3 jogadas de cara/coroa (ex. HTT): ").upper()

while not acertou:
    while contador < 3:
        if moeda() == 0:
            gerados += "H"  # Cara
        else:
            gerados += "T"  # Coroa
        contador += 1

    print("Sequência gerada: ", gerados)
    todas+=gerados

    if gerados == sequencia:
        print(f"🎉 Você acertou a sequência em {tentativas+1} tentativas!")
        print(todas)
        acertou = True
    else:
        gerados = ""
        contador = 0
        tentativas+=1


# Todo Números narcisistas
# Todo Chicken McNugget Theorem
# Todo Algoritmo de Euclides
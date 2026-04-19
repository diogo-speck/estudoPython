import time
from random import choice


nome = (f"Tri{choice("bcdfghjklmnpq@rstwxyz ")}")
nome = nome.replace("g", "gag")
nome = nome.replace("q", "qu")
nome = nome.replace(" ", "")
print(f"Olá, bem vindo ao {nome+"ago"}, a sua corretora de viagens favorita!")
tecla = input("Para falar com um de nossos atendentes, digite 1: ")
print("Conectando...")
time.sleep(2)
if tecla == "1":
    print(f"Atendente: Olá, seja bem vindo ao {nome+"ago"}! Em que posso ajudar?")
    escolha = input("Atendente: Possuimos pacotes de viagens de ida e volta para Cuba, Coreia do Norte e Venezuela, o que deseja? (cu/co/ve) ")
    if escolha == "cu":
        time.sleep(2)
        print("Atendente: Ótima escolha! Cuba é um país lindo e cheio de cultura. Temos pacotes com tudo incluso, desde passagens aéreas até hospedagem e passeios turísticos.")
        time.sleep(2)
        escolha2 = input("Atendente: Para a Diária da hospedagem digite 2: ")
        if escolha2 == "2":
            diariacu = 650
            print("Atendente: Deixe-me verificar as opções disponíveis...")
            time.sleep(2)
            print(f"Atendente: O valor da diária em Cuba é de R${diariacu},00.")
            time.sleep(2)
            dias = int(input("Atendente: Quantos dias você pretende ficar? "))
            total = diariacu * dias
            print("Atendente: Certo, calculando...")
            time.sleep(2)
            print(f"Atendente: O valor total da sua estadia será de R${total},00. Obrigado por escolher o {nome+"ago"}! e boa sorte, porque você vai precisar.")
        else:
            print(f"Atendente: Desculpe não entendi, por favor ligue novamente após o BIP.")
            time.sleep(2)
            print("BIP")
            exit()
    elif escolha == "co":
        print("Atendente: Ótima escolha! A Coreia do Norte é um país cheio de história e cultura. Temos pacotes com tudo incluso, desde passagens aéreas até hospedagem e passeios turísticos.")
        escolha2 = input("Atendente: Para a Diária da hospedagem digite 2: ")
        if escolha2 == "2":
            diariaco = 500
            print("Atendente: Deixe-me verificar as opções disponíveis...")
            time.sleep(2)
            print(f"Atendente: O valor da diária na Coreia do Norte é de R${diariaco},00.")
            time.sleep(2)
            dias = int(input("Atendente: Quantos dias você pretende ficar? "))
            total = diariaco * dias
            print("Atendente: Certo, calculando...")
            time.sleep(2)
            print(f"Atendente: O valor total da sua estadia será de R${total},00. Obrigado por escolher o {nome+"ago"}! e boa sorte, porque você vai precisar.")
        else:
            print(f"Atendente: Desculpe não entendi, por favor ligue novamente após o BIP.")
            time.sleep(2)
            print("BIP")
            exit()
    elif escolha == "ve":
        print("Atendente: Ótima escolha! A Venezuela é um país cheio de belezas naturais. Temos pacotes com tudo incluso, desde passagens aéreas até hospedagem e passeios turísticos.")
        escolha2 = input("Atendente: Para a Diária da hospedagem digite 2: ")
        if escolha2 == "2":
            diariave = 400
            print("Atendente: Deixe-me verificar as opções disponíveis...")
            time.sleep(2)
            print(f"Atendente: O valor da diária na Venezuela é de R${diariave},00.")
            time.sleep(2)
            dias = int(input("Atendente: Quantos dias você pretende ficar? "))
            total = diariave * dias
            print("Atendente: Certo, calculando...")
            time.sleep(2)
            print(f"Atendente: O valor total da sua estadia será de R${total},00. Obrigado por escolher o {nome+"ago"}! e boa sorte, porque você vai precisar.")
        else:
            print(f"Atendente: Desculpe não entendi, por favor ligue novamente após o BIP.")
            time.sleep(2)
            print("BIP")
            exit()
else:
    print("Infelizmente ainda não possuímos esse destino, por favor tente novamente após o BIP.")
    time.sleep(2)
    print("BIP")
    exit()
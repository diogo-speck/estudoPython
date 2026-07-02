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




data = input("Digite uma data para conferir se ela é válida ou não (dd/mm/yyyy): ")
confere_data(data)

# Todo Números narcisistas
# Todo Chicken McNugget Theorem
# Todo HTT TTH Coin flip sequence
# Todo Algoritmo de Euclides
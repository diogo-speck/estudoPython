filmes = ["IntraMunicipal", "A ida para o passado", "Ninguém em pânico"]
print ("Olá, seja bem-vindo ao camelô Cabelo de Camelo")
print ("Aqui você encontra os melhores piores filmes de todos os tempos")
print (f"Temos {len(filmes)} filmes no nosso catálogo no momento")
print (f"Eles incluem: {filmes}")
mudar = input ("Deseja adicionar ou remover um filme do catálogo? (s/n) ")
if mudar == 's':
    while True:
        escolha = input("Você quer adicionar ou remover um filme no catálogo? (a/r) ")
        if escolha == 'a':
            add = input("Qual filme você quer adicionar no catálogo? ")
            filmes.append(add)
        elif escolha == 'r':
            print(f"Os filmes no catálogo são: {filmes}")
            remover = input(f"Existem {len(filmes)} filmes no catálogo atualmente. Qual você quer remover? ")
            if remover in filmes:
                filmes.remove(remover)
                print(f"'{remover}' foi removido do catálogo.")
            else:
                print("Esse filme não está no catálogo.")
                continue
        print(f"Os itens da lista são: {filmes}")
        sair = input("\033[31mDigite sair para sair: \033[0m")
        if sair == 'sair':
            exit()
        else:
            continue
else:
    print(f"Certo, nossos filmes são: {filmes}")
    print("Obrigado por visitar o camelô Cabelo de Camelo, volte sempre!")
lista = []
print("Eu sou a lista ANALisa, mas pode me chamar de Ana")
while True:
    item = input("\033[1;32mDigite algo para adicionar na lista: \033[0m")
    lista.append(item)
    print(f"Os itens da lista são: {lista}")
    parou = input("\033[31mDigite sair para sair: \033[0m")
    if parou == 'sair':
        print(f"Sua lista final ficou assim: {lista}")
        exit()
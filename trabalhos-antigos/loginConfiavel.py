nome = input("Bem-vindo ao site ClonaCartão.com, qual seu nome completo? ")
conf = input(f"Olá {nome} você já possui uma conta? (s/n) ")
while conf != "s" and conf != "n":
    print("Entrada inválida. Por favor, responda com 's' ou 'n'.")
    conf = input("Você já possui uma conta? (s/n)")
if conf == "n":
    print("Por favor, crie uma conta para continuar.")

email = input("Insira seu e-mail: ")
while "@" not in email and "." not in email:
    print("E-mail inválido. O e-mail deve conter @ e .")
    email = input("Insira seu e-mail: ")
senha = input("Crie uma senha: ")
# Validação da senha: mínimo 6 caracteres e pelo menos um número
while len(senha) < 6 or not any(char.isdigit() for char in senha):
    print("Senha inválida. A senha deve conter no mínimo 6 caracteres e pelo menos um número.")
    senha = input("Crie uma senha: ")

if conf == "s":
    print("Essa conta não existe, crie uma conta para continuar.")
    exit()

    print("Conta criada com sucesso!")
while True:
    print(f"Por favor {nome}, faça login para continuar.")
    emailc = input("Insira seu e-mail: ")
    senhac = input("Insira sua senha: ")
    if emailc == email and senha == senhac:
        print("Login realizado com sucesso!")
        numero = int(input("Por favor, insira o número do seu cartão de crédito para continuar: "))
        while len(str(numero)) != 16 or not str(numero).isdigit():
            print("Número de cartão inválido. O número do cartão deve conter 16 dígitos numéricos.")
            numero = int(input("Por favor, insira o número do seu cartão de crédito para continuar: "))
        cvv = int(input("Por favor, insira o código de segurança (CVV) do seu cartão: "))
        while len(str(cvv)) != 3 or not str(cvv).isdigit():
            print("CVV inválido. O CVV deve conter 3 dígitos numéricos.")
            cvv = int(input("Por favor, insira o código de segurança (CVV) do seu cartão: "))
        ano = int(input("Por favor, insira o ano de validade do seu cartão (AAAA): "))
        while ano < 2025 or ano > 2035:
            print("Ano de validade inválido. O ano deve estar entre 2025 e 2035.")
            ano = int(input("Por favor, insira o ano de validade do seu cartão (AAAA): "))
        print("Obrigado! Seus dados foram salvos com sucesso.")
        exit()

    else:
        print("E-mail ou senha incorretos. Tente novamente.")
        exit()
print("============ MENU ============")
print("1 - Calculadora de médias ponderadas")
print("2 - Calculadora de lógica Booleana")

try:
    escolha = int(input(("Escolha 1 opção: ")))

    if escolha == 1:
        calc= input ("Bem-Vindo a Caluladora de Médias da Univali onde a nota e o peso máximo é 10, deseja usa-lá? (s/n) ")
        if calc == "s":
            n1 = float (input("Digite a nota da m1: "))
            p1 = float (input("Digite a nota da p1: "))
            n2 = float (input("Digite a nota da m2: "))
            p2 = float (input("Digite a nota da p2: "))
            n3 = float (input("Digite a nota da m3: "))
            p3 = float (input("Digite a nota da p3: "))
            media = (n1*p1+n2*p2+n3*p3)/10
            if media < 5.75:
                print (f"Sua média ponderada é: {media}")
                print ("Infelizmente você terá que pagar mais um semestre $-$")
            elif media > 5.75 and media <= 10:
                print (f"Sua média ponderada é: {media}")
                print ("Parabéns, você foi aprovado")
            elif 0:
                print (f"Sua média ponderada é: {media}")
                print ("Você bateu o recorde de média mais baixa")
            else:
                print (f"Sua média ponderada seria: {media}")
                print ("Preencha as notas corretamente por favor")
        print ("Certo, agora vamos aprender sobre os operadores relacionais então")
        try:
            a = float (input ("Digite um valor para A: "))
            b = float (input ("Digite um valor para B: "))
            if a == b:
                print (f"{a} = {b}")
            else:
                print (f"{a} != {b}")
                if a>b:
                    print (f"{a} > {b}")
                else:
                    print (f"{a} < {b}")
        except ValueError:
            print ("Por favor digite números reais respeitando o padrão")

    elif escolha == 2:
        # Ordem de prioridade da lógica boleana
        print ("==== PRIORIDADE ====")
        print ("() 0")
        print ("not 1")
        print ("e 2")
        print ("xor 3")
        print ("ou 4")
        print("=== Calculadora Booleana ===")
        print("Use:")
        print("! ou não/nao  -> NÃO")
        print("&& ou e       -> E")
        print("|| ou ou      -> OU")
        print("Valores: verdadeiro ou falso")
        print("Exemplo: verdadeiro && !falso")

        expr = input("Digite a expressão lógica: ").lower()

        # Converter valores
        expr = expr.replace("verdadeiro", "True")
        expr = expr.replace("falso", "False")

        # Converter operadores
        expr = expr.replace("&&", " and ")
        expr = expr.replace(" e ", " and ")

        expr = expr.replace("||", " or ")
        expr = expr.replace(" ou ", " or ")

        expr = expr.replace("!", " not ")
        expr = expr.replace("não", " not ")
        expr = expr.replace("nao", " not ")

        try:
            resultado = eval(expr)
            # Converter saída
            if resultado == True:
                print("Resultado: verdadeiro")
            else:
                print("Resultado: falso")
        except:
            print("Expressão inválida!")

except ValueError:
    exit()
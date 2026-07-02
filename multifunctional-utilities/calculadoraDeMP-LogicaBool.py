print("""============ MENU ============
1 - Calculadora de médias ponderadas
2 - Calculadora de lógica Booleana""")

while True:
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
                print (f"Sua média ponderada é: {media} \nInfelizmente você terá que pagar mais um semestre $-$")
            elif 5.75 < media <= 10:
                print (f"Sua média ponderada é: {media} \nParabéns, você foi aprovado")
            elif media == 0:
                print (f"Sua média ponderada é: {media} \nVocê bateu o recorde de média mais baixa")
            else:
                print (f"Sua média ponderada seria: {media} \nPreencha as notas corretamente por favor")
        break

    elif escolha == 2:
        # Ordem de prioridade da lógica boleana
        print("""==== PRIORIDADE ====
        () 0
        not 1
        e 2
        xor 3
        ou 4
=== Calculadora Booleana ===
        Use:
        ! ou não/nao  -> NÃO
        && ou e       -> E
        || ou ou      -> OU
        Valores: verdadeiro ou falso
        Exemplo: verdadeiro && !falso""")

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
            if resultado:
                print("Resultado: verdadeiro")
            else:
                print("Resultado: falso")
        except:
            print("Expressão inválida!")

        break
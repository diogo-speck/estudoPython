# )> |> D |D |>º )>º |>º Dº |Dº 

print("Portas lógicas e lógica Booleana")

# Ordem de prioridade da lógica boleana
print(      """==== PRIORIDADE ====
        () ou -- 0
        not 1
        e 2
        xor 3 [IMPLEMENTAR TODO]
        ou 4
        === Calculadora Booleana ===
        Use:
        ! ou não/nao ou - -> NÃO
        && ou e ou and -> E
        || ou OU -> OU
        Valores: verdadeiro ou falso ou v/f ou 0/1
        Exemplo: verdadeiro && !falso""")

while True:
        expr = input("\nDigite a expressão lógica (para sair digite algo que não é aceito): ").lower()

        # Converte os valores
        expr = expr.replace("verdadeiro", "True")
        expr = expr.replace("true", "True")
        expr = expr.replace("v", "True")
        expr = expr.replace("falso", "False")
        expr = expr.replace("false", "False")
        expr = expr.replace("f", "False")
        expr = expr.replace("vf", "False")
        expr = expr.replace("fv", "False")

        # Converte os operadores
        expr = expr.replace("&&", " and ")
        expr = expr.replace(" e ", " and ")
        expr = expr.replace(".", " and ")
        expr = expr.replace("*", " and ")

        expr = expr.replace("||", " or ")
        expr = expr.replace(" ou ", " or ")
        expr = expr.replace("+", " or ")
        
        expr = expr.replace("!", " not ")
        expr = expr.replace(" não ", " not ")
        expr = expr.replace(" nao ", " not ")
        expr = expr.replace("-", " not ")


        #if expr == (" xor ") and expr != ("v xor v"):
        #    expr = expr.replace("xor", " or ")
        #elif expr == ("v xor v"):
        #    expr = expr.replace("v xor v", "False")


        try:
            resultado = eval(expr)
            # Converte a saída
            if resultado:
                print("Resultado: verdadeiro")
            else:
                print("Resultado: falso")
        except:
            print("Expressão inválida! Saindo...")
            break
# D Dº )> )>º |>º ))> ))>º  AND NAND OR NOR NOT XOR XNOR

print("Portas lógicas e lógica Booleana")

# Ordem de prioridade da lógica boleana
print("""
==== PRIORIDADE ====
() ou -- 0
not 1
xor 2
e 3
ou 4
=== Calculadora Booleana ===
Use:
! ou não/nao ou - -> NÃO
&& ou e ou and ou * ou .-> E
|| ou OU + -> OU
Valores: verdadeiro ou falso ou v/f ou 0/1
Exemplo: verdadeiro && !falso""")

while True:
        expr = input("\nDigite a expressão lógica: ").lower()

        # Converte os valores
        expr = expr.replace("verdadeiro", " True ")
        expr = expr.replace("true", " True ")
        expr = expr.replace("v ", " True ")
        expr = expr.replace("falso", " False ")
        expr = expr.replace("false", " False ")
        expr = expr.replace("f ", " False ")
        expr = expr.replace("0", " False ")
        expr = expr.replace("1", " True ")
        expr = expr.replace("v", " True ")
        expr = expr.replace("f", " False ")

        # Converte os operadores
        expr = expr.replace(" && ", " and ")
        expr = expr.replace(" e ", " and ")
        expr = expr.replace(" . ", " and ")
        expr = expr.replace(" * ", " and ")

        expr = expr.replace(" || ", " or ")
        expr = expr.replace(" ou ", " or ")
        expr = expr.replace(" + ", " or ")
        
        expr = expr.replace("!", " not ")
        expr = expr.replace("não ", " not ")
        expr = expr.replace("nao ", " not ")
        expr = expr.replace("-", " not ")

        # Circuitos lógicos combinacionais

        # nand
        if expr == (" True  nand  True "):
            expr = (" False ")
        elif " nand " in expr:
            expr = expr.replace(" nand ", " or True or not")

        #xnor
        expr = expr.replace("xnor", " == ")
        
        #nor
        if expr == (" False  nor  False "):
            expr = expr.replace(" False  nor  False ", " True ")
        elif expr == (" False  nor  True "):
            expr = expr.replace(" False  nor  True ", " False ")
        elif expr == (" True  nor  False "):
            expr = expr.replace(" True  nor  False ", " False ")
        elif expr == (" True  nor  True "):
            expr = expr.replace(" True  nor  True ", " False ")

        # xor
        expr = expr.replace("xor", " ^ ")



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
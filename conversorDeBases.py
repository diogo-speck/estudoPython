# Tipos de base: Decimal, Binária, Octal e Hexadecimal
def converterDecimalBinario(num):
    restos = []
    while num > 0:
        resto = num % 2
        restos.append(resto)
        num = num // 2
    restos = restos[::-1] # inverte a lista
    binario = "".join(str(r) for r in restos) # converte lista em String com .join
    return binario if binario else "0" # se binário existe, retorna int, se não retorna 0

def converterBinarioDecimal(num):
    valor = 0
    texto = str(num) # transforma o número binário em uma string
    lista = list(texto)[::-1] # pega o texto e coloca em uma lista, invertendo logo após
    for n, digito in enumerate(lista): # para n, sendo n todos os digitos(em texto) na lista pegue o índice e o valor(elemento naquela posição) ao mesmo tempo com a função enumerate
        valor += int(digito)*(2**n) # pega o valor(digito, 0 ou 1) e transforma em int para multiplicar com 2 elevado a n, sendo n o índice
    decimal = str(valor)
    return decimal if decimal else "0" # se decimal existe, retorna int, se não retorna 0

def converterDecimalOctal(num):
    num = int(num)
    restos = []
    while num > 0:
        resto = num % 8
        restos.append(resto)
        num = num // 8
    restos = restos[::-1] # inverte a lista
    octal = "".join(str(r) for r in restos) # converte lista em String com .join
    return octal if octal else "0" # se octal existe, retorna, se não retorna 0

def converterBinarioOctal(num):
    numero = converterBinarioDecimal(num)
    octal = converterDecimalOctal(numero)
    return octal

def converterOctalBinario(num):
    valor = []
    lista = list(str(num))
    if num > 0:
        for digito in lista: # para n, sendo n todos os digitos(inteiros) na lista pegue o índice e o valor(elemento naquela posição) ao mesmo tempo com a função enumerate
            binario = converterDecimalBinario(int(digito))
            valor.append(str(binario).zfill(3)) # garante 3 bits agrupando eles de 3 em 3, mas só funciona para Strings
        octal = "".join(valor) # converte int em String com .join para evitar ter 0 a esquerda
        return octal
    else:
        return "0" # se octal existe, retorna, se não retorna 0

def converterOctalDecimal(num):
    numero = converterOctalBinario(num)
    decimal = converterBinarioDecimal(numero)
    return decimal

def converterBinarioHexa(txt): #retorna String
    valor = []
    lista = list(txt)
    if txt != "0":
        while len(lista) % 4 != 0: # adiciona 0 a esquerda para ter apenas conjuntos de 4 bits
            lista.insert(0, "0")
        # Divide em blocos de 4 bits
        for i in range(0, len(lista), 4):
            bloco = lista[i:i+4]
            bi4 = "".join(bloco)
            bi4 = int(bi4)
            match(bi4):
                case 1010:
                    valor.append("A")
                case 1011:
                    valor.append("B")
                case 1100:
                    valor.append("C")
                case 1101:
                    valor.append("D")
                case 1110:
                    valor.append("E")
                case 1111:
                    valor.append("F")
                case _:
                    decimal = converterBinarioDecimal(str(bi4))
                    valor.append(str(decimal))    
            
        hexa = "".join(valor).lstrip("0") # converte lista em String com .join e remove os 0 a esquerda
        return hexa
    else:
        return "0" # se octal existe, retorna, se não retorna 0

def converterDecimalHexa(num):
    binario = converterDecimalBinario(num)
    hexa = converterBinarioHexa(binario)
    return hexa

def converterOctalHexa(num):
    binario = converterOctalBinario(num)
    hexa = converterBinarioHexa(binario)
    return hexa

def converterHexaDecimal(txt):
    digitos = "0123456789ABCDEF"
    txt = txt.upper() # garante letras maiúsculas
    valor = 0
    for algarismo in txt:
        if algarismo not in digitos:
            return "0" # se hexa não existe, retorna 0
        valor = valor * 16 + digitos.index(algarismo)
    decimal = valor
    return decimal

def converterHexaBinario(txt):
    decimal = converterHexaDecimal(txt)
    binario = converterDecimalBinario(decimal)
    return binario

def converterHexaOctal(txt):
    decimal = converterHexaDecimal(txt)
    octal = converterDecimalOctal(decimal)
    return octal

continua = True
while (continua):
    print("===Menu===")
    print("1 - Decimal")
    print("2 - Binária")
    print("3 - Octal")
    print("4 - Hexadecimal")
    base = int(input("Informe a base do número que você quer converter: "))
    match base:
        case 1:
            decimal = int(input("A base que você escolheu foi Decimal, digite seu número em decimal: "))
            escolha = input("Deseja converter para qual tipo? (d,b,o,h) ")
            match escolha:
                case "d":
                    print (int(decimal))
                case "b":
                    binario = converterDecimalBinario(decimal)
                    print (int(binario))
                case "o":
                    octal = converterDecimalOctal(decimal)
                    print(int(octal))
                case "h":
                    hexa = converterDecimalHexa(decimal)
                    print(hexa)
        case 2:
            binario = (input("A base que você escolheu foi Binário, digite seu número em binário: "))
            escolha = input("Deseja converter para qual tipo? (d,b,o,h) ")
            match escolha:
                case "d":
                    decimal = converterBinarioDecimal(binario)
                    print (int(decimal))
                case "b":
                    print (int(binario))
                case "o":
                    octal = converterBinarioOctal(binario)
                    print (int(octal))
                case "h":
                    hexa = converterBinarioHexa(binario)
                    print(hexa)
        case 3:
            octal = int(input("A base que você escolheu foi Octal, digite seu número em octal: "))
            escolha = input("Deseja converter para qual tipo? (d,b,o,h) ")
            match escolha:
                case "d":
                    decimal = converterOctalDecimal(octal)
                    print (int(decimal))
                case "b":
                    binario = converterOctalBinario(octal)
                    print (int(binario))
                case "o":
                    print (int(octal))
                case "h":
                    hexa = converterOctalHexa(octal)
                    print(hexa)
        case 4:
            hexa = input("A base que você escolheu foi Hexadecimal, digite seu número em hexadecimal: ").upper()
            escolha = input("Deseja converter para qual tipo? (d,b,o,h) ")
            match escolha:
                case "d":
                    decimal = converterHexaDecimal(hexa)
                    print (int(decimal))
                case "b":
                    binario = converterHexaBinario(hexa)
                    print (int(binario))
                case "o":
                    octal = converterHexaOctal(hexa)
                    print (int(octal))
                case "h":
                    print(hexa)
    avante = input("Deseja calcular novamente? (s/n) ")
    if avante == "n":
        continua = False
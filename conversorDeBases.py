# Tipos de base: Decimal, Binária, Octal e Hexadecimal
def converterDecimalBinario(num):
    restos = []
    while num > 0:
        resto = num % 2
        restos.append(resto)
        num = num // 2
    restos = restos[::-1] # inverte a lista
    binario = "".join(str(r) for r in restos) # converte lista em String com .join
    binario = int(binario)
    return binario if binario else 0 # se binário existe, retorna, se não retorna 0

def converterBinarioDecimal(num):
    valor = 0
    texto = str(num) # transforma o número em uma string
    lista = list(texto)[::-1] # pega o texto e coloca em uma lista, invertendo logo após
    for n, digito in enumerate(lista): # para n, sendo n todos os digitos(em texto) na lista pegue o índice e o valor(elemento naquela posição) ao mesmo tempo com a função enumerate
        valor += int(digito)*(2**n) # pega o valor(digito, 0 ou 1) e transforma em int para multiplicar com 2 elevado a n, sendo n o índice
    return valor

def converterDecimalOctal(num):
    restos = []
    while num > 0:
        resto = num % 8
        restos.append(resto)
        num = num // 8
    restos = restos[::-1] # inverte a lista
    octal = "".join(str(r) for r in restos) # converte lista em String com .join
    octal = int(octal)
    return octal if octal else 0 # se octal existe, retorna, se não retorna 0

def converterBinarioOctal(num):
    numero = converterBinarioDecimal(num)
    octal = converterDecimalOctal(numero)
    return octal

def converterOctalBinario(num): # arrumar
    valor = []
    lista = list(str(num))
    for n, digito in enumerate(lista): # para n, sendo n todos os digitos(inteiros) na lista pegue o índice e o valor(elemento naquela posição) ao mesmo tempo com a função enumerate
        binario = converterDecimalBinario(int(digito))
        valor.append(str(binario).zfill(3)) # garante 3 bits agrupando eles de 3 em 3
    octal = "".join(str(r) for r in valor) # converte lista em String com .join
    return int(octal) # converte String para int

def converterOctalDecimal(num): # arrumar
    numero = converterOctalBinario(num)
    decimal = converterBinarioDecimal(numero)
    return decimal


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
                    print(decimal)
                case "b":
                    binario = converterDecimalBinario(decimal)
                    print(binario)
                case "o":
                    octal = converterDecimalOctal(decimal)
                    print(octal)
                case "h":
                    print(hexa)
        case 2:
            binario = int(input("A base que você escolheu foi Binário, digite seu número em binário: "))
            escolha = input("Deseja converter para qual tipo? (d,b,o,h) ")
            match escolha:
                case "d":
                    decimal = converterBinarioDecimal(binario)
                    print(decimal)
                case "b":
                    print(binario)
                case "o":
                    octal = converterBinarioOctal(binario)
                    print(octal)
                case "h":
                    print(hexa)
        case 3:
            octal = int(input("A base que você escolheu foi Octal, digite seu número em octal: "))
            escolha = input("Deseja converter para qual tipo? (d,b,o,h) ")
            match escolha:
                case "d":
                    decimal = converterOctalDecimal(octal)
                    print(decimal)
                case "b":
                    binario = converterOctalBinario(octal)
                    print(binario)
                case "o":
                    print(octal)
                case "h":
                    print(hexa)
        case 4:
            hexa = input("A base que você escolheu foi Hexadecimal, digite seu número em hexadecimal: ")
            escolha = input("Deseja converter para qual tipo? (d,b,o,h) ")
            match escolha:
                case "d":
                    print(decimal)
                case "b":
                    print(binario)
                case "o":
                    print(octal)
                case "h":
                    print(hexa)
    avante = input("Deseja calcular novamente? (s/n) ")
    if avante == "n":
        continua = False
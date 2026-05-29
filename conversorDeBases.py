# Tipos de base: Decimal, Binária, Octal e Hexadecimal
def converterDecimalBinario(num):
    restos = []
    while num > 0:
        resto = num % 2
        restos.append(resto)
        num = num // 2
    restos = restos[::-1] # inverte a lista
    binario = "".join(str(r) for r in restos) # converte lista em String com .join
    return binario if binario else "0" # se binário existe, retorna, se não retorna 0

def converterBinarioDecimal(num):
    valor = 0
    for n in range(len(num)):
        valor +=num[n]*(2**n)
    return valor

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
                    print(octal)
                case "h":
                    print(hexa)
        case 3:
            octal = int(input("A base que você escolheu foi Octal, digite seu número em octal: "))
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
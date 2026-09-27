print("Calculadora de médias ponderadas com peso 10")

while True:
    calc= input ("Deseja usa-lá? (s/n) ").lower()
    if calc == "s":
        n1 = float (input("Digite a nota 1 da m1: "))
        p1 = float (input("Digite o peso 1 da m1: "))
        n2 = float (input("Digite a nota 2 da m1: "))
        p2 = float (input("Digite o peso 2 da m1: "))
        n3 = float (input("Digite a nota 3 da m1: "))
        p3 = float (input("Digite o peso 3 da m1: "))
        media = (n1*p1+n2*p2+n3*p3)/10
        if media < 5.75:
            print (f"Sua média ponderada é: {media} \nInfelizmente você terá que pagar mais um semestre $-$")
        elif 5.75 < media <= 10:
            print (f"Sua média ponderada é: {media} \nParabéns, você foi aprovado")
        elif media == 0:
            print (f"Sua média ponderada é: {media} \nVocê bateu o recorde de média mais baixa")
        else:
            raise ValueError("As notas precisam estar entre 0 e 10")
    else:
        break
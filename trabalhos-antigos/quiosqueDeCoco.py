import time
import random
import sys
sys.set_int_max_str_digits(16381)

dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

print("Bem-vindo ao quiosque do coco do seu Zé, que é aberto de domingo a domingo (sem fechar para os feriados)")
time.sleep(4)
print("Seu Zé tem uma memória muito boa para nomes e números, então você pode pedir seus cocos fiado e pagar depois dentro de uma semana")
time.sleep(4)
print("Mas cuidado, seu Zé também é agiota, então se você esquecer de pagar, talvez nunca mais veja seus cocos...")
time.sleep(6)

dia = input("Infelizmente ele não é muito bom com data, então que dia da semana é hoje? (ex. terça, sábado) ").lower()

# Verifica se o dia é válido
if dia not in dias:
    print("Dia inválido! Observação: Usamos o calendário gregoriano aqui, os dias são minúsculos e não ferimos a gramática.")
    sys.exit()

# Encontra o índice do dia atual
indice_dia_atual = dias.index(dia)
nome = input("Qual o seu nome? ")
if nome.strip() == "" or nome.lower() in ["não sei", "sei lá", "não lembro"]:
    nome = random.choice(["amigo", "parceiro", "camarada", "brother", "meu chapa", "meu consagrado"])
    print(f"Ok {nome}.")

conta = []
try:
    comanda = int(input(f"Quantos cocos você vai querer hoje ({dia}) {nome}? (R$5,00 cada) "))
    conta.append(comanda * 5)
    print(f"Ok {nome}, você pediu {comanda} cocos hoje ({dia}), sua conta até agora é de R${sum(conta)},00")
except ValueError:
    print("Seu Zé não entendeu quantos cocos você quer. Tente usar apenas números inteiros.")
    sys.exit()

# Loop pelos dias restantes da semana (começando do próximo dia)
for i in range(1, 8):  # 7 dias completos SEMPRE
    dia_atual = dias[(indice_dia_atual + i) % 7]  # %7 para circular corretamente
    if i == 7:
        resposta = input(f"Hoje é {dia_atual} de novo, dia de acerto de contas. Você vai querer adicionar mais cocos na comanda? (s/n) ").lower()
    else:
        resposta = input(f"Hoje é {dia_atual}. Você vai querer adicionar mais cocos na comanda? (s/n) ").lower()
      
    if resposta == "s":
        try:
            comanda = int(input("Quantos cocos você vai querer? "))
            conta.append(comanda * 5)
            print(f"Sua conta até agora é de R${sum(conta)},00")
        except ValueError:
            print("Seu Zé não entendeu quantos cocos você quer. Tente voltar aqui amanhã.")
            # Não adiciona nada à conta se der erro
    elif resposta == "n":
        if i < 7:
            print("Ok, até amanhã então")
        else:
            break
    else:
        print("Seu Zé não ouviu, por isso não adicionou nada em sua comanda hoje (responda com 's' ou 'n').")

print(f"Tudo bem {nome}, sua conta final é de R${sum(conta)},00. Agora pague seu Zé, ele está te esperando!")
import random
print("Bolá, bem bindo bao bontador be betros bem \033[31mbentímetros\033[0m be \033[32mbilômetros\033[0m")
input("Beseja braduzir? (b/b) ")
if random.choice([True, False]):  # 50% de chance de ser bim ou bão
    print("Bokay, Bona betite!")
    exit()
try:
    valor = float(input("Certo, digite o valor em metros: "))
    print(f"O valor de {valor} metros em centímetros é \033[31m{valor * 100} cm\033[0m")
    print(f"O valor de {valor} metros em quilômetros é \033[32m{valor/1000} km\033[0m")
except ValueError:
    print("\033[31mBá bachando bue beu basci bontem?\033[0m")
exit()
from classes import *

def main():
    c1 = Carteira()
    c2 = Carteira(100)
    print(c1 == c2)
    print(c1 != c2)
    c1 += 100
    print(c1)
    c2 -= 100
    print(c2)
    print(c1 <= c2)

if __name__ == "__main__":
    main()
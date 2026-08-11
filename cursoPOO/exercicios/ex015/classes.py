class Carteira:

    def __init__(self, valor:int|float=0):
        self.__saldo=valor

    def __str__(self):
        return(f"Você tem {self.__saldo:,.2f} de saldo")

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor:int|float):
        raise PermissionError("Você não tem permissão para alterar o saldo desse jeito")

    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    def __ne__(self, outro):
        if self.__saldo != outro.__saldo:
            return True
        else:
            return False
    
    def __iadd__(self, valor:int|float=0):
        self.__saldo+=valor
        return self

    def __isub__(self, valor:int|float=0):
        self.__saldo-=valor
        return self
    
    def __le__(self, outro):
        if self.__saldo <= outro.__saldo:
            return True
        else:
            return False
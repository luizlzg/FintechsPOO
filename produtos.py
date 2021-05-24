class Produtos:
    def __init__(self, saldo: float, nome_titular: str, tipo_produto: str):
        self.__saldo = saldo
        self.__titular = nome_titular
        self.__tipo_produto = tipo_produto

    @property
    def titular(self):
        return self.__titular

    @property
    def tipo_produto(self):
        return self.__tipo_produto

    def consultar(self):
        return self.__saldo

    def enviar(self, valor, destinatario):
        pass

    def pagar(self, valor: float, destinatario):
        if self.__saldo >= valor:
            self.__saldo -= abs(valor)
            self.enviar(valor, destinatario)
            return True

        else:
            print("Saldo Insuficiente")
            return False

    def configurar(self):
      pass
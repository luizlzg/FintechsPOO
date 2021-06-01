from produtos import Produtos


class Cartao(Produtos):
    cartoes = []

    def __init__(self, saldo: float, titular: str, tipo_produto: str, numero_cartao: str,
                 senha: str, cvv: str, validade: str, bandeira: str, tipo_cartao: str,
                 juros: float, limite: float):

        super().__init__(saldo, titular, tipo_produto)
        self.__numero_cartao = numero_cartao
        self.__senha = senha
        self.__cvv = cvv
        self.__validade = validade
        self.__bandeira = bandeira
        self.__tipo_cartao = tipo_cartao
        self.__juros = juros
        self.__limite = limite

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def senha(self):
        return self.__senha

    @property
    def cvv(self):
        return self.__cvv

    @property
    def validade(self):
        return self.__validade

    @property
    def bandeira(self):
        return self.__bandeira

    @property
    def tipo_cartao(self):
        return self.__tipo_cartao

    @property
    def juros(self):
        return self.__juros

    @property
    def limite(self):
        return self.__limite

    def gerar_cartao_virtual(self):
        from random import randint

        cvv = ""
        numero = ""
        data_validade = f"{randint(0, 2)}{randint(0, 9)}/0{randint(1, 9)}/{randint(21, 99)}"
        for i in range(16):
            numero += str(randint(0, 9))

        for i in range(3):
            cvv += randint(0, 9)

        return [numero, cvv, data_validade]

    def gerar_fatura(self):
        pass

    def parcelar(self, numero_parcelas, valor_fatura):
        valor_parcela = valor_fatura / numero_parcelas
        return valor_parcela

    def add_cartao(self):
        if self.numero_cartao in Cartao.cartoes:
            print("Infelizmente houve um erro na criação de seu cartão, por favor, tente novamente!")
            return 1
        else:
            Cartao.cartoes.append(self.numero_cartao)
            print("Seu cartão foi adquirido com sucesso!")
            return 0

from conta import Conta
from cartao import Cartao
from pessoa import Pessoa
from random import randint
from time import sleep


class Cliente(Pessoa):
    clientes = []

    def __init__(self, nome, endereco, email, telefone, renda_mensal, genero, cpf, rg, data_nascimento):
        super().__init__(nome, endereco, email, telefone)
        self.nome = nome
        self.renda_mensal = renda_mensal
        self.genero = genero
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.produtos = []
        self.contas = []

    def solicitar_ajuda(self):
        if self.nome in Cliente.clientes:
            print(f"Sua solicitação de ajuda foi processada e atendida, em instantes você será atendido(a)!")
        else:
            print(f"Desculpe, {self.nome}, infelizmente o(a) senhor(a) não faz parte do nosso grupo de clientes.")

    def solicitar_credito(self):
        if self.nome in Cliente.clientes:
            print(
                f"Parabéns, {self.nome}! sua solicitação foi processada e seu perfil estará em análise para concessão de crédito, aguarde...")
        else:
            print(f"Desculpe, {self.nome}, infelizmente o(a) senhor(a) não faz parte do nosso grupo de clientes.")

    def solicitar_cartao(self):
        cartao = 0
        if self.nome in Cliente.clientes:
            print(f"Parabéns! A sua solicitação de cartão foi aceita e seu produto será adquirido!")
            cartao = 1
        else:
            print("Infelizmente sua solicitação de cartão foi negada.")

        if cartao:
            print("Agora que sua solicitação foi aceita seu cartão será gerado!")
            sleep(15)

            numero_cartao = ""
            for i in range(1, 17):
                numero = randint(0, 9)
                if i % 4 == 0:
                    numero_cartao = numero_cartao + str(numero) + " "
                else:
                    numero_cartao = numero_cartao + str(numero)

            senha = str(randint(10 ** 3, 10 ** 4))

            codigo_seguranca = str(randint(10 ** 2, 10 ** 3))

            validade = "01/01/2100"

            bandeira = "MasterCard"

            tipo_indice = int(input(
                "Qual tipo de cartão deseja? \n Digite 1 para Cartão de Crédito \n"
                " Digite 2 para Cartão de Débito \n Digite 3 para Cartão Digital \n"))
            tipo = ""
            if tipo_indice == 1:
                tipo = "Cartão de Crédito"
            elif tipo_indice == 2:
                tipo = "Cartão de Débito"
            elif tipo_indice == 3:
                tipo = "Cartão Digital"
            else:
                print("Opção inválida")

            tipo_produto = "Cartão"
            saldo = 0
            juros = 0.01
            limite = 1000

            cartao_criado = Cartao(saldo, self.nome, tipo_produto, numero_cartao, senha, codigo_seguranca, validade,
                                   bandeira, tipo, juros, limite)
            while cartao_criado.add_cartao() != 0:

                numero_cartao = ""
                for i in range(1, 17):
                    numero = randint(0, 9)
                    if i % 4 == 0:
                        numero_cartao = numero_cartao + str(numero) + " "
                    else:
                        numero_cartao = numero_cartao + str(numero)

                cartao_criado = Cartao(saldo, self.nome, tipo_produto, numero_cartao, senha, codigo_seguranca, validade,
                                   bandeira, tipo, juros, limite)

            else:
                self.produtos.append(cartao_criado)

    def criar_conta(self):
        Cliente.clientes.append(self)
        print("Agora que seu cadastro foi aceito, sua conta será gerada! Responda as perguntas necessárias!")
        sleep(15)

        agencia = "0001"

        numero_conta = ""
        for i in range(1, 7):
            numero = randint(0, 9)
            if i % 5 == 0:
                numero_conta = numero_conta + str(numero) + "-"
            else:
                numero_conta = numero_conta + str(numero)

        taxa_rendimento = 0

        tipo_conta = "Conta Corrente"

        nome_titular = self.nome

        saldo = 0

        tipo_produto = "Conta"

        conta_criada = Conta(saldo, nome_titular, tipo_produto, agencia, numero_conta, taxa_rendimento, tipo_conta)
        while conta_criada.add_conta() != 0:

            numero_conta = ""
            for i in range(1, 7):
                numero = randint(0, 9)
                if i % 5 == 0:
                    numero_conta = numero_conta + str(numero) + "-"
                else:
                    numero_conta = numero_conta + str(numero)

            conta_criada = Conta(saldo, nome_titular, tipo_produto, agencia, numero_conta, taxa_rendimento, tipo_conta)

        else:
            self.contas.append(conta_criada)

    def acessar_cartao(self):
        tipo_cartao = int(input("Qual tipo de cartão deseja acessar? \n Digite 1 para Cartão de Crédito \n "
                                "Digite 2 para Cartão de Débito \n Digite 3 para Cartão Digital \n"))
        if tipo_cartao == 1:
            for cartao in self.produtos:
                if cartao.tipo == "Cartão de Crédito":
                    print("Pronto, seu cartão já está em suas mãos!")
                    return cartao
            else:
                print("Infelizmente o senhor não possui nenhum cartão desse tipo.")

        elif tipo_cartao == 2:
            for cartao in self.produtos:
                if cartao.tipo == "Cartão de Débito":
                    print("Pronto, seu cartão já está em suas mãos!")
                    return cartao
            else:
                print("Infelizmente o senhor não possui nenhum cartão desse tipo.")

        elif tipo_cartao == 3:
            for cartao in self.produtos:
                if cartao.tipo == "Cartão Digital":
                    print("Pronto, seu cartão já está em suas mãos!")
                    return cartao

            else:
                print("Infelizmente o senhor não possui nenhum cartão desse tipo.")
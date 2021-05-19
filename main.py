# Parte Luiz Guilherme
from random import randint

from time import sleep


class Cliente(Pessoa):
    clientes = []

    def __init__(self, nome, endereco, email, telefone, renda_mensal, genero, cpf, rg, data_nascimento):
        super().__init__(nome)
        super().__init__(endereco)
        super().__init__(email)
        super().__init__(telefone)
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

            senha = randint(10 ** 3, 10 ** 4)

            codigo_seguranca = randint(10 ** 2, 10 ** 3)

            validade = "01/01/2100"

            bandeira = "MasterCard"

            tipo_indice = int(input(
                "Qual tipo de cartão deseja? \n Digite 1 para Cartão de Crédito \n Digite 2 para Cartão de Débito \n Digite 3 para Cartão Digital \n"))
            tipo = ""
            if tipo_indice == 1:
                tipo = "Cartão de Crédito"
            elif tipo_indice == 2:
                tipo = "Cartão de Débito"
            elif tipo_indice == 3:
                tipo = "Cartão Digital"
            else:
                print("Opção inválida")

            juros = 0.01
            limite = 1000

            cartao_criado = Cartao(numero_cartao, senha, codigo_seguranca, validade, bandeira, tipo, juros, limite)
            self.produtos.append(cartao_criado)
            cartao_criado.add_cartao()

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

        bandeira = "MasterCard"

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
        tipo_cartao = int(input(
        "Qual tipo de cartão deseja acessar? \n Digite 1 para Cartão de Crédito \n Digite 2 para Cartão de Débito \n Digite 3 para Cartão Digital \n"))
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


class Conta(Produto):

    contas = []
    chaves_pix = []

    def __init__(self, saldo, nome_titular, tipo_produto, agencia, numero_conta, taxa_rendimento, tipo_conta):
        super().__init__(saldo)
        super().__init__(nome_titular)
        super().__init__(tipo_produto)
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.taxa_rendimento = taxa_rendimento
        self.tipo_conta = tipo_conta
        self.meu_pix = []

    def add_conta(self):
        if self.numero_conta in Conta.contas:
            print("Infelizmente houve um erro na criação de sua conta, por favor, tente novamente!")
            return 1
        else:
            Conta.contas.append(self.numero_conta)
            print("Sua conta foi criada com sucesso!")
            return 0

    def criar_chave_pix(self):
        tipo_chave = int(input(
            "Qual tipo de chave pix é o desejado? \n Digite 1 para CPF \n Digite 2 para E-mail \n Digite 3 para Telefone \n Digite 4 para Chave aleatória \n"))
        if tipo_chave == 1:
            cpf = int(input("Digite o número do seu CPF:"))
            if not cpf in Conta.chaves_pix:
                Conta.chaves_pix.append(cpf)
                self.meu_pix.append(cpf)
                print("Chave PIX registrada com sucesso!")
            else:
                print("Chave PIX já existente, tente novamente.")

        elif tipo_chave == 2:
            email = input("Digite o seu e-mail:")
            if not email in Conta.chaves_pix:
                Conta.chaves_pix.append(email)
                self.meu_pix.append(email)
                print("Chave PIX registrada com sucesso!")

            else:
                print("Chave PIX já existente, tente novamente.")

        elif tipo_chave == 3:
            telefone = input("Digite o número do seu telefone:")
            if not telefone in Conta.chaves_pix:
                Conta.chaves_pix.append(telefone)
                self.meu_pix.append(telefone)
                print("Chave PIX registrada com sucesso!")
            else:
                print("Chave PIX já existente, tente novamente.")

        elif tipo_chave == 4:
            alfabeto = "abcdefghijklmnopqrstuvwxyz"
            chave_aleatoria = ""
            for i in range(0, 32):
                numero_aleatorio = randint(0, 10)
                letra_aleatoria = alfabeto[randint(0, 25)]
                if i % 2 == 0:
                    chave_aleatoria = chave_aleatoria + letra_aleatoria + str(numero_aleatorio)
                if i % 4 == 0:
                    chave_aleatoria = chave_aleatoria + "-"
            if not chave_aleatoria in Conta.chaves_pix:
                Conta.chaves_pix.append(chave_aleatoria)
                self.meu_pix.append(chave_aleatoria)
                print("Chave PIX registrada com sucesso!")
            else:
                print("Chave PIX já existente, tente novamente.")

    def consultar_pix(self):
        print("Suas chaves PIX são:")
        for chave in self.meu_pix:
            print(chave)

    def transferir(self):

        tipo_transferencia = int(input(
            "Qual será o tipo de transferência? \n Digite 1 para TED \n Digite 2 para DOC \n Digite 3 para PIX \n"))

        if tipo_transferencia == 1:

            beneficiario = input("Insira o número da conta que o dinheiro será transferido:")

            if beneficiario in Conta.contas:
                valor = float(input("Qual é o valor a ser transferido?"))
                self.saldo = self.saldo - valor

                print("Gerando o comprovante...")
                sleep(30)

                comprovante = f"\t COMPROVANTE DE TRANSFERÊNCIA - TED \t \n \n Pagador: {self.numero_conta} \n Beneficiário: {beneficiario} \n \n \t Valor: R${valor}"
                print(comprovante)

            else:
                print("O número da conta do Beneficiário é inválido.")

        elif tipo_transferencia == 2:

            beneficiario = input("Insira o número da conta que o dinheiro será transferido:")

            if beneficiario in Conta.contas:
                valor = float(input("Qual é o valor a ser transferido?"))
                self.saldo = self.saldo - valor

                print("Gerando o comprovante...")
                sleep(30)

                comprovante = f"\t COMPROVANTE DE TRANSFERÊNCIA - DOC \t \n \n Pagador: {self.numero_conta} \n Beneficiário: {beneficiario} \n \n \t Valor: R${valor}"
                print(comprovante)

            else:
                print("O número da conta do Beneficiário é inválido.")

        elif tipo_transferencia == 3:

            chavepix = input("Insira a chave PIX para qual o dinheiro será transferido:")

            if chavepix in Conta.chaves_pix:
                valor = float(input("Qual é o valor a ser transferido?"))
                self.saldo = self.saldo - valor

                print("Gerando o comprovante...")
                sleep(30)

                comprovante = f"\t COMPROVANTE DE TRANSFERÊNCIA - PIX \t \n \n Pagador: {self.numero_conta} \n Chave PIX do Beneficiário: {chavepix} \n \n \t Valor: R${valor}"
                print(comprovante)

            else:
                print("A chave PIX inserida é inválida.")

    def depositar(self):
        beneficiario = input("Insira o número da conta que o dinheiro será depositado:")
        pagador = input("Insira o número da conta que será responsável por depositar o dinheiro:")

        if beneficiario and pagador in Conta.contas:
            valor = float(input("Qual é o valor a ser depositado?"))
            print("Gerando o boleto...")
            sleep(30)

            boleto = f"\t BOLETO \t \n \n Pagador: {pagador} \n Beneficiário: {beneficiario} \n \n \t Valor: R${valor}"
            print(boleto)

        else:
            print("O número da conta do Beneficiário ou do Pagador é inválido.")
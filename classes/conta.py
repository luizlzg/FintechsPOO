from time import sleep
from random import randint
from produtos import Produtos


class Conta(Produtos):

    contas = []
    chaves_pix = []

    def __init__(self, saldo, nome_titular, tipo_produto, agencia, numero_conta, taxa_rendimento, tipo_conta):
        super().__init__(saldo,nome_titular,tipo_produto)
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
            "Qual tipo de chave pix é o desejado? \n Digite 1 para CPF \n Digite 2 para E-mail \n "
            "Digite 3 para Telefone \n Digite 4 para Chave aleatória \n"))
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

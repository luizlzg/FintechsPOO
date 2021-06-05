from pessoa import Pessoa

class PessoaJuridica(Pessoa):  # Parte Luiz F
    pessoa_juridica = []

    def __init__(self, cnpj, capital, nome_fantasia, razao_social,
                 ramo_atividade, nome, endereco, email, telefone):
        super().__init__(nome, endereco, email, telefone)
        self.__cnpj = cnpj
        self.__capital = capital
        self.__nome_fantasia = nome_fantasia
        self.__razao_social = razao_social
        self.__ramo_atividade = ramo_atividade
        self.contas_juridicas = []
        self.produtos_juridicos = []

    def acessar_produto(self):  # consultar depois para melhorar
        if self.__nome_fantasia in PessoaJuridica.pessoa_juridica:
            print("Quais produtos você deseja consultar? ")
            print("(1) Cartão")
            print("(2) Conta")
            print("(3) PIX")
            escolha = int(input("Digite o numero do produto: "))

            if escolha == 1:
                for produto in self.produtos_juridicos:
                    if produto.tipo == "Cartao de Credito" or produto.tipo == "Cartao de Débito" or produto.tipo == "Cartao Digital":
                        print(produto)
            if escolha == 2:
                for conta in self.contas_juridicas:
                    print(conta)

            elif escolha == 3:
                for produto in self.produtos_juridicos:
                    if produto.tipo == "PIX":
                        print(produto)
        else:
            print("Desculpe, essa empresa não consta nos nossos registros")

    def solicitar_cartao(self):
        cartao = 0
        if self.__nome_fantasia in PessoaJuridica.pessoa_juridica:
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

            cartao_criado = Cartao(saldo, self.__nome_fantasia, tipo_produto, numero_cartao, senha, codigo_seguranca, validade,
                                   bandeira, tipo, juros, limite)
            while cartao_criado.add_cartao() != 0:

                numero_cartao = ""
                for i in range(1, 17):
                    numero = randint(0, 9)
                    if i % 4 == 0:
                        numero_cartao = numero_cartao + str(numero) + " "
                    else:
                        numero_cartao = numero_cartao + str(numero)

                cartao_criado = Cartao(saldo, self.__nome_fantasia, tipo_produto, numero_cartao, senha, codigo_seguranca, validade,
                                   bandeira, tipo, juros, limite)

            else:
                self.produtos.append(cartao_criado)

        

    def solicitar_suporte(self):
        if self.__nome_fantasia in PessoaJuridica.pessoa_juridica:
            print(f'Solicitação de suporte processada. Aguarde um momento, a equipe de suporte entrará em contato.')
        else:
            print(
                f'Desculpe, Sr(a) {self.__nome_fantasia}. Infelizmente, não encontramos registros com esse nome no nosso '
                f'banco de dados.')

    def criar_contapj(self):
      PessoaJuridica.pessoa_juridica.append(self)
      print("Solicitação de criação de conta atendida! Aguarde um momento.")

      numero_conta = str(randint(10**4,10**5))+'-'+str(randint(1,10))
      agencia = "001"
      nome_titular = self.__nome_fantasia
      tipo_conta = "Conta Corrente"
      taxa_rendimento = 0
      tipo_produto = "Conta"
      saldo = 0
      nova_conta = Conta(saldo,nome_titular,tipo_produto,agencia,numero_conta,taxa_rendimento,tipo_conta)
      self.contas_juridicas.append(nova_conta)
      print(f'Parabens! A sua empresa {nome_titular} está com a conta ativa!')
      print(f"O numero da sua conta é:{nova_conta.numero_conta}")


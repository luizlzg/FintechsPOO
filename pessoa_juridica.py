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
        if self.__razao_social in PessoaJuridica.pessoa_juridica:
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

    def solicitar_produto(self):  # falta implementar
        pass

    def solicitar_suporte(self):
        if self.__nome_fantasia in PessoaJuridica.pessoa_juridica:
            print(f'Solicitação de suporte processada. Aguarde um momento, a equipe de suporte entrará em contato.')
        else:
            print(
                f'Desculpe, Sr(a) {self.__nome_fantasia}. Infelizmente, não encontramos registros com esse nome no nosso '
                f'banco de dados.')

    def criar_contapj(self):  # falta implementar

        pass
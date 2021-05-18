class Pessoa:
    def __init__(self,nome,endereco,email, telefone, renda_mensal):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
        self.renda_mensal = renda_mensal
    def alterar_dados(self):
        opt = 0
        while opt != 6:
            print("Qual dado você deseja alterar?\n")
            print("(1) Nome \n")
            print("(2) Endereço \n")
            print("(3) E-mail \n")
            print("(4) Telefone \n")
            print("(5) Renda mensal \n")
            print("Digite 6 para sair! \n")
            opt = int(input("Insira sua opção:"))
            if opt == 1:
                novo_nome = input("Para qual nome deseja trocar?")
                self.nome = novo_nome
            elif opt == 2:
                novo_endereco = input("Para qual endereço deseja trocar?")
                self.endereco = novo_endereco
            elif opt == 3:
                novo_email = input("Para qual e-mail deseja trocar?")
                self.email = novo_email
            elif opt == 4:
                novo_telefone = input("Para qual telefone deseja trocar?")
                self.telefone = novo_telefone
            elif opt == 5:
                nova_renda = float(input("Para qual renda deseja trocar?"))
                self.renda_mensal = nova_renda
    def inserir_dados(self):
    def excluir_dados(self):
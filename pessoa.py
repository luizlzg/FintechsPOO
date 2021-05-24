class Pessoa:
    def __init__(self,nome,endereco,email,telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email
        self.__telefone = telefone
        self.__renda = 0
        self.__senha_acesso = ''
        self.__senha_digitos = 1234

    def perfil(self):
        escolha = 0
        while escolha != 7:
            print('Qual área você deseja acessar?')
            print('(1) Nome de preferência ')
            print('(2) E-mail ')
            print('(3) Endereço ')
            print('(4) Renda Mensal ')
            print('(5) Alterar senha de acesso')
            print('(6) Consultar senha de 4 dígitos ')
            print('(7) Sair do perfil ')
            escolha = int(input('\nInsira sua opção: '))

            if escolha > 7 or escolha <1:
                raise ValueError ('Não há essa opção!!!!')

            if escolha == 1:
                alterar_nome_preferencia = int(input(f'\nAtualmente, seu nome é {self.__nome}, deseja alterá-lo? \n'
                      f'(1) Sim \n(2) Não\n'))
                if alterar_nome_preferencia == 1:
                    novo_nome_preferencia = input('Digite seu novo nome de preferência: ')
                    print(f'Nome alterado com sucesso, {novo_nome_preferencia}!\n')
                else:
                    pass

            if escolha == 2:
                alterar_email = int(input(f'\nDeseja alterar seu email cadastrado? \n'
                                                     f'(1) Sim \n(2) Não\n'))
                if alterar_email == 1:
                    novo_email = input('Digite seu novo email: ')
                    confirm_novo_email = input('Digite novamente seu novo email, a fim de confirmação: ')
                    if novo_email == confirm_novo_email:
                        if novo_email == self.__email:
                            print('Email já foi cadastrado anteriormente!\n')

                        else:
                            self.__email = novo_email
                            print('Email alterado com sucesso!\n')

                    else:
                        print('Os emails não são iguais. Tente novamente.\n ')
                else:
                    pass

            if escolha == 3:
                alterar_endereco = int(input('Deseja alterar seu endereço?\n'
                                             '(1) Sim\n(2) Não\n'))
                if alterar_endereco == 1:
                    self.__endereco = input('Digite seu novo endereço: ')
                    print('Endereço alterado com sucesso!\n')

                else:
                    pass

            if escolha == 4:
                alterar_renda = int(input('Deseja alterar sua renda?\n'
                                             '(1) Sim\n(2) Não\n'))
                if alterar_renda == 1:
                    self.__renda = float(input('Digite a sua nova renda: '))
                    print('Renda alterada com sucesso! \n')
                else:
                    pass

            if escolha == 5:
                alterar_senha_acesso = int(input('Deseja alterar sua senha de acesso?\n'
                                             '(1) Sim\n(2) Não\n'))
                if alterar_senha_acesso == 1:
                    senha_atual = input('Digite sua senha atual: ')
                    if senha_atual == self.__senha_acesso:
                        nova_senha = input('Digite a nova senha: ')
                        print('Senha de acesso alterada com sucesso!\n')
                    else:
                        print('Senha incorreta! Tente novamente. \n')
                else:
                    pass

            if escolha == 6:
                consultar_senha = int(input('Deseja consultar sua senha de 4 dígitos?\n'
                                             '(1) Sim\n(2) Não\n'))
                if consultar_senha == 1:
                    print(f'Sua senha de 4 dígitos é: {self.__senha_digitos}\n')
                else:
                    pass
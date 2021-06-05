from flask import Flask, render_template, request

contas = [[123, '321', "teste", "teste@hotmail.com", "5000", "27"]]


def autenticacao(usuario, senha):
    for conta in contas:
        if usuario and senha in conta:
            return True
        else:
            pass
    else:
        return False


app = Flask(__name__, template_folder="view")


@app.route('/index')
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/autentica', methods=['POST'])
def autentica():
    user = int(request.form['usuario'])
    senha = str(request.form['senha'])
    global sessao
    if autenticacao(user, senha):
        sessao = user
        info = []
        for conta in contas:
            if sessao == conta[0]:
                info = conta
                break
            else:
                print("Usuário não encontrado.")
        name = info[2]
        return render_template("usuario.html", name=name)
    else:
        return render_template("login_erro.html")


@app.route('/signin')
def signin():
    return render_template("criar_conta.html")


@app.route('/criar_conta_pj')
def signinpj():
    return render_template("criar_conta_pj.html")


@app.route('/conta_criada', methods=["POST"])
def conta_criada():
    cpf = int(request.form['usuario'])
    senha = str(request.form['senha'])
    nome = request.form['nome']
    email = request.form['email']
    renda_mensal = request.form['renda']
    contas.append([cpf, senha, nome, email, renda_mensal, "27"])
    return render_template("conta_criada.html")


@app.route('/menu')
def menu():
    return render_template("menu.html")


@app.route('/perfil')
def perfil():
    info = []
    for conta in contas:
        if sessao == conta[0]:
            info = conta
            break
        else:
            print("Usuário não encontrado.")
    name = info[2]
    email = info[3]
    renda = "R$" + str(info[-2])
    return render_template("perfil.html", nome=name, email=email, renda=renda)


@app.route('/usuario')
def usuario():
    info = []
    encontrou = False
    for conta in contas:
        if sessao == conta[0]:
            info = conta
            encontrou = True
            break
        elif not encontrou:
            print("Usuário não encontrado.")
    user = info[2]
    return render_template("usuario.html", name=user)


@app.route('/configurar_conta')
def configurar_conta():
    return render_template("configurar_conta.html")


@app.route('/config_cartao')
def config_cartao():
    info = []
    encontrou = False
    for conta in contas:
        if sessao == conta[0]:
            info = conta
            encontrou = True
            break
        elif not encontrou:
            print("Usuário não encontrado.")
    limite = "R$" + str(float(info[-2])/2.0)
    vencimento = info[-1]

    return render_template('config_cartao.html', vencimento=f'Todo dia {vencimento}', limite=limite)


@app.route('/config_vencimento', methods=['POST'])
def config_vencimento():
    novo_vencimento = str(request.form['vencimento'])
    aux = 0
    encontrou = False
    for conta in range(len(contas)):
        if sessao == contas[conta][0]:
            aux = conta
            encontrou = True
            break
        elif not encontrou:
            print("Usuário não encontrado.")
    contas[aux][-1] = novo_vencimento

    return render_template("config_vencimento.html")


@app.route('/config_renda', methods=['POST'])
def config_renda():
    nova_renda = str(request.form['renda'])
    aux = 0
    encontrou = False
    for conta in range(len(contas)):
        if sessao == contas[conta][0]:
            aux = conta
            encontrou = True
            break
        elif not encontrou:
            print("Usuário não encontrado.")
    contas[aux][-2] = nova_renda

    return render_template("config_renda.html")


if __name__ == '__main__':
    app.run()

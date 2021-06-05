from flask import Flask, render_template, request

contas = [[123, 321,"teste","teste@hotmail.com"]]


def autenticacao(usuario,senha):
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

@app.route('/autentica',methods=['POST'])
def autentica():
    user = int(request.form['usuario'])
    senha = int(request.form['senha'])
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
        return render_template("usuario.html",name=name)
    else:
        return render_template("login_erro.html")

@app.route('/signin')
def signin():
    return render_template("criar_conta.html")

@app.route('/conta_criada',methods=["POST"])
def conta_criada():
    cpf = int(request.form['usuario'])
    senha = int(request.form['senha'])
    nome = request.form['nome']
    email = request.form['email']
    contas.append([cpf, senha,nome,email])
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
    return render_template("perfil.html",nome=name,email=email)

@app.route('/usuario')
def usuario():
    info = []
    for conta in contas:
        if sessao == conta[0]:
            info = conta
            break
        else:
            print("Usuário não encontrado.")
    user = info[2]
    return render_template("usuario.html",name=user)

@app.route('/configurar_conta')
def configurar_conta():
    return render_template("configurar_conta.html")


if __name__ == '__main__':
    app.run()

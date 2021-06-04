from flask import Flask, render_template, request

contas = [[123, 321]]
#

def autenticacao(usuario,senha):
    for conta in contas:
        if usuario and senha in conta:
            return True
        else:
            pass
    else:
        return False


app = Flask(__name__, template_folder="view")


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
    if autenticacao(user,senha):
        return render_template("usuario.html",name=user)
    else:
        return render_template("login_erro.html")

@app.route('/signin')
def signin():
    return render_template("criar_conta.html")

@app.route('/conta_criada',methods=["POST"])
def conta_criada():
    cpfcnpj = int(request.form['usuario'])
    senha = int(request.form['senha'])
    contas.append([cpfcnpj, senha])
    return render_template("conta_criada.html")


if __name__ == '__main__':
    app.run()

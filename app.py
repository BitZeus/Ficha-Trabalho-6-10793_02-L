
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RespostaForm, AvancarForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo'
respostas = ['co2']  # Lista que contem as respostas

# Função que redireciona para a página home.html (inicio)
@app.route("/", methods=['GET', 'POST'])
def home():
    form = AvancarForm()
    if form.validate_on_submit():
        return redirect(url_for('desafio1'))  # Redireciona para a rota desafio1
    return render_template('home.html', form=form)
@app.route("/desafio1", methods=['GET', 'POST'])

# Função que redireciona para a página desafio1.html
def desafio1():
    form = RespostaForm()
    if form.validate_on_submit(): # Ao pressionar o botao executa as operações abaixo
        if form.resposta.data.lower() == respostas[0]:  # Verifica se a resposta corresponde na lista de respostas
            return redirect(url_for('fim'))  # Redireciona para a pagina fim se resposta correcta
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')  # Devolve mensagem de erro que resposta incorrecta
    return render_template('desafio1.html', form=form)
@app.route("/fim", methods=['GET', 'POST'])


# Função que redireciona para a página fim.html
def fim():

        
    return render_template('fim.html')


if __name__ == "__main__":
    app.run()

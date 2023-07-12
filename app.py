
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RespostaForm, AvancarForm, ComentarioForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo'
respostas = ['co2', 'solar', 'electricos', 'reciclar']  # Lista que contem as respostas
comentarios = []  # lista para guardar os comentarios

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
        if form.resposta.data.lower() == respostas[0]:  # Verifica se a resposta corresponde na lista de respostas na posição 0
            return redirect(url_for('desafio2'))  # Redireciona para a pagina desafio2 se resposta correcta
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')  # Devolve mensagem de erro que resposta incorrecta
    return render_template('desafio1.html', form=form)  # Usa a template definida para a pagina desafio1
@app.route("/desafio2", methods=['GET', 'POST'])

# Função que redireciona para a página desafio2.html
def desafio2():
    form = RespostaForm()
    if form.validate_on_submit():  # Ao pressionar o botao executa as operações abaixo
        if form.resposta.data.lower() == respostas[1]:  # Verifica se a resposta corresponde na lista de respostas na posição 1
            return redirect(url_for('desafio3'))  # Redireciona para a pagina desafio3 se resposta correcta
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafio2.html', form=form)  # Usa a template definida para a pagina desafio2
@app.route("/desafio3", methods=['GET', 'POST'])  # Decorador para a pagina desafio3

def desafio3():
    form = RespostaForm()
    if form.validate_on_submit():  # Ao pressionar o botao executa as operações abaixo
        if form.resposta.data.lower() == respostas[2]:  # Verifica se a resposta corresponde na lista de respostas na posição 2
            return redirect(url_for('desafio4'))  # Redireciona para a pagina desafio4 se resposta correcta
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafio3.html', form=form)  # Usa a template definida para a pagina desafio3
@app.route("/desafio4", methods=['GET', 'POST'])  # Decorador para a pagina desafio4

def desafio4():
    form = RespostaForm()
    if form.validate_on_submit():  # Ao pressionar o botao executa as operações abaixo
        if form.resposta.data.lower() == respostas[3]:  # Verifica se a resposta corresponde na lista de respostas na posição 3
            return redirect(url_for('fim'))  # Redireciona para a pagina fim se resposta correcta
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafio4.html', form=form)  # Usa a template definida para a pagina desafio4
@app.route("/fim", methods=['GET', 'POST'])  # Decorador para a pagina fim

# Função que redireciona para a página fim.html
def fim():
    form = ComentarioForm() # 
    if form.validate_on_submit():
        comentario = form.comentario.data
        comentarios.append(comentario)  # Insere o comentario na lista
        print(f'Mensagem recebida: {comentario}') # Print da mensagem no terminal
        flash(f'Mensagem enviada com sucesso! Já existem {len(comentarios)} mensagem(s).', 'success')
        return redirect(url_for('ver_comentarios'))
    return render_template('fim.html', form=form)  # Usa a template definida para a pagina fim
@app.route("/ver_comentarios", methods=['GET', 'POST'])


# Função para adicionar comentarios
def ver_comentarios():
    return render_template('comentarios.html', comentarios=comentarios)


if __name__ == "__main__":
    app.run()

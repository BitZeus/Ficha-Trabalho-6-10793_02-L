from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# Classe Resposta( responsavel pela introdução de texto, e submissão do mesmo)
class RespostaForm(FlaskForm):
    resposta = StringField('Resposta:')  # Campo de formulário para a resposta
    submit = SubmitField('Submeter')  # Botão de submissão do formulário

# Classe Avancar ( responsavel pelo inicio do desafio)
class AvancarForm(FlaskForm):
    submit = SubmitField('Avançar')  # Botão de submissão do formulário para avanço para a proxima pagina
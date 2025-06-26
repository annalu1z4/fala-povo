import json
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

ARQUIVO_DADOS = 'denuncias.json'

def carregar_denuncias():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_denuncia(denuncia):
    denuncias = carregar_denuncias()
    denuncias.append(denuncia)
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(denuncias, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/denunciar', methods=['GET', 'POST'])
def denunciar():
    if request.method == 'POST':
        anonimo = 'anonimo' in request.form

        dados = {
            'nome': 'Anônimo' if anonimo else request.form['nome'],
            'email': 'Anônimo' if anonimo else request.form['email'],
            'telefone': 'Anônimo' if anonimo else request.form['telefone'],
            'categoria': request.form['categoria'],
            'descricao': request.form['descricao'],
            'cep': request.form['cep'],
            'logradouro': request.form.get('logradouro', ''),
            'numero': request.form.get('numero', ''),
            'bairro': request.form.get('bairro', ''),
            'cidade': request.form.get('cidade', ''),
            'uf': request.form.get('uf', ''),
            'referencia': request.form.get('referencia', ''),
            'anexo': request.files.get('anexo').filename if request.files.get('anexo') else None
        }

        salvar_denuncia(dados)
        return redirect('/sucesso')

    return render_template('denunciar.html')

@app.route('/denuncias')
def denuncias():
    todas = carregar_denuncias()
    return render_template('denuncias.html', denuncias=todas)

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)

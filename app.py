import sqlite3
import os
from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__)

ARQUIVO_DADOS = 'denuncias.json'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'mp4'}
DATABASE_URL = os.environ.get("postgresql://fala_povo_db_user:1h897s6Rki1raVwAhUNpLSmADqjMK78j@dpg-d1fh52er433s73fidc40-a/fala_povo_db")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def conectar_banco():
    return sqlite3.connect('denuncias.db')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def salvar_denuncia(dados):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO denuncias (
            nome, email, telefone, categoria, descricao,
            cep, logradouro, numero, bairro, cidade, uf,
            referencia, anexo
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        dados['nome'], dados['email'], dados['telefone'],
        dados['categoria'], dados['descricao'], dados['cep'],
        dados['logradouro'], dados['numero'], dados['bairro'],
        dados['cidade'], dados['uf'], dados['referencia'],
        dados['anexo']
    ))

    conn.commit()
    conn.close()

def carregar_denuncias():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM denuncias ORDER BY data_envio DESC")
    colunas = [col[0] for col in cursor.description]
    registros = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]

    conn.close()
    return registros

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/denunciar', methods=['GET', 'POST'])
def denunciar():
    if request.method == 'POST':
        anonimo = 'anonimo' in request.form
        
        file = request.files.get('anexo')
        filename = None

        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

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
            'anexo': filename
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

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
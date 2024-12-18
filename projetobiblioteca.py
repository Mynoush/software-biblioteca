import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_password = os.getenv('DB_PASSWORD')

# Configuração do Banco de Dados MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=db_password,
    database="biblioteca"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livros', methods=['GET', 'POST'])
def livros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']

        cursor.execute(
            "INSERT INTO livros (titulo, autor) VALUES (%s, %s)",
            (titulo, autor)
        )
        db.commit()
        return redirect(url_for('index'))

    return render_template('livros.html')

@app.route('/unidades', methods=['GET', 'POST'])
def unidades():
    if request.method == 'POST':
        nome_unidade = request.form['nome_unidade']
        endereco = request.form['endereco']

        cursor.execute(
            "INSERT INTO unidades (nome_unidade, endereco) VALUES (%s, %s)",
            (nome_unidade, endereco)
        )
        db.commit()
        return redirect(url_for('index'))

    return render_template('unidades.html')

@app.route('/emprestimos', methods=['GET', 'POST'])
def emprestimos():
    if request.method == 'POST':
        livro = request.form['livro']
        usuario = request.form['usuario']
        data_emprestimo = request.form['data_emprestimo']

        cursor.execute(
            "INSERT INTO emprestimos (livro, usuario, data_emprestimo) VALUES (%s, %s, %s)",
            (livro, usuario, data_emprestimo)
        )
        db.commit()
        return redirect(url_for('index'))

    return render_template('emprestimos.html')

@app.route('/devolucoes', methods=['GET', 'POST'])
def devolucoes():
    if request.method == 'POST':
        livro = request.form['livro']
        usuario = request.form['usuario']
        data_devolucao = request.form['data_devolucao']

        cursor.execute(
            "INSERT INTO devolucoes (livro, usuario, data_devolucao) VALUES (%s, %s, %s)",
            (livro, usuario, data_devolucao)
        )
        db.commit()
        return redirect(url_for('index'))

    return render_template('devolucoes.html')

if __name__ == "__main__":
    app.run(debug=True)

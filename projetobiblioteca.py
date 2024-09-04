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

if __name__ == "__main__":
    app.run(debug=True)
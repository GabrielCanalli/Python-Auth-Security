import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Função para conectar ao banco de dados e criar a tabela de usuários.
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Chama a função para criar o banco ao iniciar o arquivo
init_db()

@app.route('/')
def home():
    return "Servidor rodando com segurança e pronto para o auth!"

if __name__ == '__main__':
    app.run(debug=True)
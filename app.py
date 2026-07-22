import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(_name_)
bcrypt = Bcrypt(app)

# Função para conectar ao banco de dados e criar a tabela de usuários.
# Function to connect to the database and create the users table.

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

    
@app.route('/')
def home():
    return "Servidor rodando com segurança e pronto para o auth!"

    if _name_ == '_main_':
    app.run(debug=True)
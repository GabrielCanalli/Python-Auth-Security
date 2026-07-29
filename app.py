import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'supersecretkey'  # Chave secreta para sessões

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Usuário ou senha incorretos!"

    return '''
        <form method='POST'>
            <h2>Login</h2>
            <input type='text' name='username' placeholder='Nome de usuário' required><br><br>
            <input type='password' name='password' placeholder='Senha' required><br><br>
            <button type='submit'>Entrar</button>
        </form>
        <br><a href='/register'>Não tem uma conta? Cadastre-se</a>
    '''


@app.route('/')
def home():
    return "Servidor rodando com segurança e pronto para o auth!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            return "Usuário já existe!"

    return '''
        <form method='POST'>
            <h2>Cadastro de Usuário
            <input type='text' name='username' placeholder='Nome de usuário' required><br><br>
            <input type='password' name='password' placeholder='Senha' required><br><br>
            <button type='submit'>Cadastrar</button>
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return f"Painel secreto! Bem-vindo, {session['username']}. <br><a href='/logout'>Sair</a>"


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
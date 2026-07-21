from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(_name_)
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return "Servidor rodando com segurança e pronto para o auth!"

    if _name_ == '_main_':
    app.run(debug=True)
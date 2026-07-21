from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(_name_)
bcrypt = Bcrypt(app)
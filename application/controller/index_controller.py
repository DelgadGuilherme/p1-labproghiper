from flask import render_template, request
from application import app 
from application.model.dao.categoria_dao import CategoriaDAO
from application.model.entity.categoria import Categoria

@app.route('/')
@app.route('/home')
def home():
    categoria_dao = CategoriaDAO()
    categoria_lista = categoria_dao.listar()
    return render_template('index.html', categoria_lista = categoria_lista )
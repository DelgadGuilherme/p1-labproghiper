from application import app
from application.model.dao.categoria_dao import CategoriaDAO
from application.model.entity.categoria import Categoria
from flask import render_template, request


@app.route("/categoria/<categoria_id>")
def categoria(categoria_id):
    categoria = CategoriaDAO().buscar_por_id(categoria_id)
    categoria_dao = CategoriaDAO()
    categoria_lista = categoria_dao.listar()
    return render_template("categoria.html", categoria=categoria,categoria_lista = categoria_lista)

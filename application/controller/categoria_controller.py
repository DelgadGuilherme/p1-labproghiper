from application import app
from application.model.dao.categoria_dao import CategoriaDAO
from application.model.entity.categoria import Categoria
from flask import render_template, request

from application import video_dao
from application import categoria_dao
from application import video_list
from application import categoria_list



@app.route("/categoria/<categoria_id>")
def categoria(categoria_id):
    categoria = categoria_dao.buscar_por_id(categoria_id, categoria_list)
    return render_template("categoria.html", categoria=categoria, categoria_lista = categoria_list)



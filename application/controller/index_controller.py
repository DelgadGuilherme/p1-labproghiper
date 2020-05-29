from flask import render_template, request
from application import app 
from application.model.dao.categoria_dao import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.video import Video

@app.route('/')
@app.route('/home')
def home():
    categoria_dao = CategoriaDAO()
    categoria_lista = categoria_dao.listar()

    for i in categoria_lista: 
        categoria_id = i.get_id() 
 
    categoria = CategoriaDAO().buscar_por_id(categoria_id) 

    mais_curtidos_organizados_lista = sorted(categoria_dao.listar_video(), key=Video.get_qntCurtida, reverse=True)
    mais_curtidos_lista = [mais_curtidos_organizados_lista[0],mais_curtidos_organizados_lista[1]]

    return render_template('index.html', categoria_lista = categoria_lista, mais_curtidos_lista = mais_curtidos_lista, categoria = categoria)
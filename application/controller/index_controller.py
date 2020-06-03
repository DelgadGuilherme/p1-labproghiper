from flask import render_template, request
from application import app 
from application.model.dao.categoria_dao import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
from application import video_list
from application import categoria_list


@app.route('/')
@app.route('/home')
def home():
    categoria_dao = CategoriaDAO()
    
    for categoria in categoria_list:
        categoria_id = categoria.get_id()
    categoria = categoria_dao.buscar_por_id(categoria_id)

    mais_curtidos_organizados_lista = sorted(video_list, key=Video.get_qntCurtida, reverse=True)
    mais_curtidos_lista = [mais_curtidos_organizados_lista[0],mais_curtidos_organizados_lista[1]]

    return render_template('index.html', categoria_lista = categoria_list, mais_curtidos_lista = mais_curtidos_lista, categoria = categoria)
    
'''
@app.route("/busca")
def buscar():
    video_id = request.args.get('id')
    
    periodo = PeriodoDAO().buscar_por_id(int(periodo_id))
    return render_template("busca.html", periodo=periodo)
'''
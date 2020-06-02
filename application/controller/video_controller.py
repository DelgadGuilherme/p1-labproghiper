from application import app
from application.model.dao.video_dao import VideoDAO
from application.model.entity.video import Video
from application.model.dao.categoria_dao import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.comentario import Comentario
from flask import render_template, request, current_app

from application import video_dao
from application import categoria_dao
from application import video_list
from application import categoria_list

@app.route("/video/<video_id>", methods=['GET'])
def video(video_id):
    video = video_dao.buscar_video_por_id(video_list,video_id)
   
    comentario_lista = video.get_comentario()
    return render_template("video.html", video = video, categoria_lista = categoria_list, comentario_lista = comentario_lista)

@app.route("/video/<video_id>/comentario", methods=['POST'])
def inserir(video_id):
    video = video_dao.buscar_video_por_id(video_list,video_id)
    autor = request.values.get('nome') 
    coment = request.values.get('coment')
    comentario = Comentario(autor,coment)
    video.set_comentario(comentario)
    comentario_lista = video.get_comentario()
    return render_template("video.html", video = video, categoria_lista = categoria_list, comentario_lista = comentario_lista), 201, {'content-type': "text/html"}
'''
@app.route("/categoria/<categoria_id>/video/<video_id>/curtir")
def curtir(categoria_id,video_id):
    categoria = CategoriaDAO().buscar_por_id(categoria_id)
    categoria_dao = CategoriaDAO()
    categoria_lista = categoria_dao.listar()

    video = CategoriaDAO().buscar_video_por_id(categoria,video_id)
   
    comentario_lista = video.get_comentario()



    return render_template("video.html", video = video, categoria=categoria, categoria_lista = categoria_lista, comentario_lista = comentario_lista)


'''
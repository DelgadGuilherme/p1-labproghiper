from application import app
from application.model.dao.video_dao import VideoDAO
from application.model.entity.video import Video
from application.model.dao.categoria_dao import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.comentario import Comentario
from flask import render_template, request, current_app
from application import video_list
from application import categoria_list

@app.route("/video/<video_id>", methods=['GET'])
def video(video_id):
    video_dao = VideoDAO()
    video = video_dao.buscar_video_por_id(int(video_id))
    video_dao.somar_visualizacao(video)
    comentario_lista = video.get_comentario()
    return render_template("video.html", video = video, categoria_lista = categoria_list, comentario_lista = comentario_lista)


@app.route('/video/<video_id>/comentario', methods=['POST'])
def inserir(video_id):
    video_dao = VideoDAO()
    video = video_dao.buscar_video_por_id(int(video_id))
    autor = request.values.get('nome') 
    coment = request.values.get('coment')
    comentario = Comentario(autor,coment)
    video.set_comentario(comentario)
    comentario_lista = video.get_comentario()
    mensagens = ['Produto cadastro com sucesso', 'Imagem armazenada com sucesso']
    return render_template('comentario.html', video = video, comentario_lista = comentario_lista)


@app.route("/video/<video_id>/curti", methods=['POST'])
def curtir(video_id):
    video_dao = VideoDAO()
    video = video_dao.buscar_video_por_id(int(video_id))
    video_dao.somar_curtida(video)
    return render_template("curtida.html", video = video), 201, {'content-type': "text/html"}


from application import app
from application.model.dao.video_dao import videoDAO
from application.model.entity.video import Video
from application.model.dao.categoria_dao import CategoriaDAO
from application.model.entity.categoria import Categoria
from flask import render_template, request


@app.route("/categoria/<categoria_id>/video/<video_id>")
def video(categoria_id,video_id):
    #video_id = request.args.get('numero')
    #video = videoDAO().buscar_por_id(int(video_id))
    #, video = video
    categoria = CategoriaDAO().buscar_por_id(categoria_id)
    categoria_dao = CategoriaDAO()
    categoria_lista = categoria_dao.listar()

    video = CategoriaDAO().buscar_video_por_id(categoria,video_id)

    return render_template("video.html", video = video, categoria=categoria, categoria_lista = categoria_lista )
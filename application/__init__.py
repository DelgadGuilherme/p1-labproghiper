from flask import Flask
import os

from application.model.dao.categoria_dao import CategoriaDAO
from application.model.dao.video_dao import VideoDAO
from application.model.entity.categoria import Categoria
from application.model.entity.video import Video

template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath('application/view/static')

app = Flask(__name__,template_folder = template_folder, static_folder = static_folder)

categoria_dao = CategoriaDAO()
video_dao = VideoDAO()

video1 = Video(1,"De boas","Um gato de boas se espreguiçando",'img/img_video/gato1.png','video/gato1.mp4')
video2 = Video(2,"Hora de nanar","Uma gata indo dormir com seus filhotinhos",'img/img_video/gato2_1.png','video/gato2.mp4')
video3 = Video(3,"Iti, o fofo","Uum cachorro dentro da caixa de boca aberta",'img/img_video/cachorro1.png','video/cachorro2.mp4')
video4 = Video(4,"Hora da diversão","Dois cachorros brincando no parque",'img/img_video/cachorro2.png','video/cachorro1.mp4')

video_list = [video1,video2,video4,video3]
        
categoria_list = []
categoria1 = Categoria(1,"Gatinhos","Nessa categoria voce pode ver uns gatos muitos fofos",'img/img_categoria/gato.jpg',[video1,video2])
categoria2 = Categoria(2,"Cachorrinhos","Nessa categoria voce pode ver uns cachorros muitos fofos",'img/img_categoria/cachorro.png',[video3,video4])
categoria_list = [categoria1,categoria2]

for categoria in categoria_list:
    for video in categoria.get_video_lista():
        video.set_categoria(categoria)
    
    

from application.controller import index_controller
from application.controller import video_controller
from application.controller import categoria_controller
from flask import Flask
import os

from application.model.entity.video import Video

template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath('application/view/static')

app = Flask(__name__,template_folder = template_folder, static_folder = static_folder)

video1 = Video(1,"De boas","Um gato de boas se espreguiçando",'img/img_video/gato1.png','video/gato1.mp4',10,2)
video2 = Video(2,"Hora de nanar","Uma gata indo dormir com seus filhotinhos",'img/img_video/gato2_1.png','video/gato2.mp4',10,4)
video3 = Video(3,"Iti, o fofo","Uum cachorro dentro da caixa de boca aberta",'img/img_video/cachorro1.png','video/cachorro2.mp4',10,20)
video4 = Video(4,"Hora da diversão","Dois cachorros brincando no parque",'img/img_video/cachorro2.png','video/cachorro1.mp4',20,3)

from application.controller import index_controller
from application.controller import video_controller
from application.controller import categoria_controller
from application.model.entity.categoria import Categoria
from application.model.entity.video import Video

class CategoriaDAO:
    def __init__(self):
        video1 = Video(1,"De boas","Um gato de boas se espreguiçando",'img/img_video/gato1.png','video/gato1.mp4')
        video2 = Video(2,"Hora de nanar","Uma gata indo dormir com seus filhotinhos",'img/img_video/gato2_1.png','video/gato2.mp4')
        video3 = Video(3,"Iti, o fofo","Uum cachorro dentro da caixa de boca aberta",'img/img_video/cachorro1.png','video/cachorro2.mp4')
        video4 = Video(4,"Hora da diversão","Dois cachorros brincando no parque",'img/img_video/cachorro2.png','video/cachorro1.mp4')
        self._categoria_list = []
        self._categoria_list.append(Categoria(1,"Gatinhos","Nessa categoria voce pode ver uns gatos muitos fofos",'img/img_categoria/gato.jpg',[video1,video2]))
        self._categoria_list.append(Categoria(2,"Cachorrinhos","Nessa categoria voce pode ver uns cachorros muitos fofos",'img/img_categoria/cachorro.png',[video3,video4]))

    def listar(self):
        return self._categoria_list

    def buscar_por_id(self, id):
        for i in range(0, len(self._categoria_list)):
            if self._categoria_list[i].get_id() == int(id):
                return self._categoria_list[i] 
        return None

    def buscar_video_por_id(self,categoria,id):
        for i in range(0, len(categoria._video_lista)):
            if categoria._video_lista[i].get_id() == int(id):
                return categoria._video_lista[i] 
        return None
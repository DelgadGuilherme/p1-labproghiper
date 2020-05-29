from application.model.entity.categoria import Categoria
from application.model.entity.video import Video

class CategoriaDAO:
    def __init__(self):
        self._video_list = [video1,video2,video4,video3]
        self._categoria_list = []
        self._categoria_list.append(Categoria(1,"Gatinhos","Nessa categoria voce pode ver uns gatos muitos fofos",'img/img_categoria/gato.jpg',[video1,video2]))
        self._categoria_list.append(Categoria(2,"Cachorrinhos","Nessa categoria voce pode ver uns cachorros muitos fofos",'img/img_categoria/cachorro.png',[video3,video4]))

    def listar(self):
        return self._categoria_list

    def listar_mais_curtidas(self):
        return self._video_list

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
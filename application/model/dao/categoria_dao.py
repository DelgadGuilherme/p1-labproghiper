from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
from application import categoria_list

class CategoriaDAO:
    def __init__(self):
        self._categoria_list = categoria_list

    def listar_categoria(self):
        return self._categoria_list

    def listar_video_categoria(self,categoria):
        return categoria.get_video_lista

    def buscar_por_id(self, id):
        for i in range(0, len(self._categoria_list)):
            if self._categoria_list[i].get_id() == int(id):
                return self._categoria_list[i] 
        return None

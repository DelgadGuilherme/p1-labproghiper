from application.model.entity.categoria import Categoria
from application.model.entity.video import Video

from flask import current_app

class CategoriaDAO:
    def __init__(self):
        pass

    def listar_categoria(self):
        return self._categoria_list

    def listar_video_categoria(self,categoria):
        return categoria.get_video_lista

    def buscar_por_id(self, id, categoria_list):
        for i in range(0, len(categoria_list)):
            if categoria_list[i].get_id() == int(id):
                return categoria_list[i] 
        return None

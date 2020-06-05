from application import video_list
from application import categoria_list

class VideoDAO:
    def __init__(self):
        self._video_list = video_list
    
    def definir_categoria(self, categoria_list):
        for categoria in categoria_list:
            for video in categoria.get_video_lista():
                video.set_categoria(categoria)

    def listar_video(self):
        return self._video_list

    def buscar_video_por_id(self,id):
        for i in range(0, len(self._video_list)):
            if self._video_list[i].get_id() == int(id):
                return self._video_list[i] 
        return None
    
    def somar_visualizacao(self,video):
        originalVisualizacao = video.get_qntVisualizacao()
        originalVisualizacao += 1
        video.set_qntVisualizacao(originalVisualizacao)

    def somar_curtida(self,video):
        originalCurtida = video.get_qntCurtida()
        originalCurtida += 1
        video.set_qntCurtida(originalCurtida)

    def remover_comentario(self,video):
        video.get_comentario().pop(0)
    
from flask import current_app

class VideoDAO:
    def __init__(self):
        pass
    '''
        self._comentario_list = []
    
    def inserir(self,comentario):
        self._comentario_list.append(comentario)

    def listar(self):
        return self._comentario_list

    def inserir_categoria(self):
        for categoria in categoria_list:
            for video in categoria.get_video_lista():
                video.set_categoria(categoria)
    '''
    def listar_video(self):
        return self._video_list

    def buscar_video_por_id(self,video_list,id):
        for i in range(0, len(video_list)):
            if video_list[i].get_id() == int(id):
                return video_list[i] 
        return None
    
    def somar_visualizacao(self,video):
        originalVisualizacao = video.get_qntVisualizacao()
        originalVisualizacao += 1
        video.set_qntVisualizacao(originalVisualizacao)

    def somar_curtida(self,video):
        originalCurtida = video.get_qntCurtida()
        originalCurtida += 1
        video.set_qntVisualizacao(originalCurtida)

    
    
    
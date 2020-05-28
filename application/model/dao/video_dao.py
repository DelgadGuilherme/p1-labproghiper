class VideoDAO:
    def __init__(self):
        self._comentario_list = []
    
    def inserir(self,comentario):
        self._comentario_list.append(comentario)

    def listar(self):
        return self._comentario_list

    def somar_visualizacao(self,video):
        originalVisualizacao = video.get_qntVisualizacao()
        originalVisualizacao += 1
        video.set_qntVisualizacao(originalVisualizacao)

    def somar_curtida(self,video):
        originalCurtida = video.get_qntCurtida()
        originalCurtida += 1
        video.set_qntVisualizacao(originalCurtida)

    
    
    
class videoDAO:
    def __init__(self):
        pass

    def somar_visualizacao(self,video):
        originalVisualizacao = video.get_qntVisualizacao()
        originalVisualizacao += 1
        video.set_qntVisualizacao(originalVisualizacao)

    def somar_curtida(self,video):
        originalCurtida = video.get_qntCurtida()
        originalCurtida += 1
        video.set_qntVisualizacao(originalCurtida)

    
    
    
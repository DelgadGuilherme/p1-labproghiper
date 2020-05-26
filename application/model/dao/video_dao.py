class videoDAO:
    def __init__(self):
        self._video_list = []

    def max_curtido(self):
        max_curtida1 = self._video_list[0]
        max_curtida2 = self._video_list[0]
        for video in self._video_list:
            if self.max_curtida.get_qntCurtida > video.get_qntCurtida():
                max_curtida1 = video

            if self.max_curtida.get_qntCurtida > video.get_qntCurtida() and =! max_curtida1:
                max_curtida2 = video

    def somar_visualizacao(self,video):
        qntVisualizacao += 1
        video.set_qntVisualizacao(qntVisualizacao)

    def somar_curtida(self,video):
        qntCurtida += 1
        video.set_qntCurtida(qntCurtida)
    
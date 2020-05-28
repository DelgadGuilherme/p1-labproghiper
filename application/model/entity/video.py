class Video:
    def __init__(self,id,titulo,descricao,fotoURL,videoURL):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._videoURL = videoURL
        self._fotoURL = fotoURL
        self._qntVisualizacao = 0
        self._qntCurtida = 0
        self._comentario = []

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def get_qntCurtida(self):
        return self._qntCurtida

    def set_qntCurtida(self,curtida):
        self._qntCurtida = curtida

    def get_qntVisualizacao(self):
        return self._qntVisualizacao

    def set_qntVisualizacao(self,visualizacao):
        self._qntVisualizacao = visualizacao
        
    def get_videoURL(self):
        return self._videoURL

    def get_fotoURL(self):
        return self._fotoURL

    def get_id(self):
        return self._id

    def set_comentario(self,comentario):     
        self._comentario.append(comentario)

    def get_comentario(self):
        return self._comentario


   
        
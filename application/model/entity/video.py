class Videos:
    def __init__(titulo,descricao,fotoURL,videoURL,categoria):
        self._titulo = titulo
        self._descricao = descricao
        self._videoURL = videoURL
        self._fotoURL = fotoURL
        self._categoria = categoria
        self._comentarios = []

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

    def get_categoria(self):
        return self._categoria

    def set_id(self,id):
        self._id = id

    def get_id(self):
        return self._id

    def set_data(self,data):
        self._data = data

    def get_data(self):
        return self._data

    def set_comentario(self,comentario):
        self._comentarios.append(comentario)


   
        
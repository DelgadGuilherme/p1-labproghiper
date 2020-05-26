class Categoria:
    def __init__(self,titulo,descricao,video_lista):
        self._titulo = titulo
        self._descricao = descricao
        self._video_lista = video_lista

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def get_video_lista(self):
        return self._video_lista

    def set_id(self,id):
        self._id = id

    def get_id(self):
        return self._id

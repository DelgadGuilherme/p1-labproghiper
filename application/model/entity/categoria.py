from flask import current_app

class Categoria:
    def __init__(self,id,titulo,descricao,fotoURL,video_lista):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._fotoURL = fotoURL
        self._video_lista = video_lista

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def get_video_lista(self):
        return self._video_lista

    def get_id(self):
        return self._id

    def get_fotoURL(self):
        return self._fotoURL
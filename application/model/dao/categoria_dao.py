class CategoriaDAO:
    def __init__(self):
        self._categoria_list = []

    def listar(self):
        return self._categoria_list

    def buscar_por_id(self, id):
        categoria_list = list(filter(lambda categoria : categoria.get_id() == id, self._categoria_list))
        if len(categoria_list) == 0:
            return None
        return categoria_list[0]
class Inscricao:
    def __init__(self,id,nome_pessoa,evento_id):
        self.id=id
        self.nome_pessoa=nome_pessoa
        self.evento_id=evento_id
    def to_dict(self):
        return {
            "id":self.id,
            "nome_pessoa":self.nome_pessoa, "evento_id":self.evento_id
        }
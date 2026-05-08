import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from auth.inscricao import Inscricao

insc=Inscricao(1,"drey",10)

print(insc.nome_pessoa)
print(insc.to_dict())
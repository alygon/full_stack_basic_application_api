from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union
from  model import Base


class Comentario(Base):
    __tablename__ = 'comentatio'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(1000))
    data_cadastro = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o comentário e um usuário.
    usuario = Column(String, ForeignKey("usuario.login"), nullable=False)

    def __init__(self, descricao:str, data_cadastro:Union[DateTime, None] = None):
        self.descricao = descricao
        if data_cadastro:
            self.data_cadastro = data_cadastro

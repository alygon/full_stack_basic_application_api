from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column("pk_usuario", Integer, primary_key=True)
    login = Column(String(15), unique=True)
    nome = Column(String(40), unique=False)
    data_cadastro = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o produto e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, login:str, nome:str, data_cadastro:Union[DateTime, None] = None):

        self.login = login
        self.nome = nome

        # se não for informada, será o data exata da inserção no banco
        if data_cadastro:
            self.data_cadastro = data_cadastro
    
    def adiciona_comentario(self, comentario:Comentario):
        self.comentarios.append(comentario)
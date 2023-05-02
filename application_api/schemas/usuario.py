from pydantic import BaseModel
from typing import Optional, List
from model.usuario import Usuario

from schemas import ComentarioSchema


class UsuarioSchema(BaseModel):
    login: str = "alygon"
    nome: str = "Alysson Gonçalves"


class UsuarioBuscaSchema(BaseModel):
    login: str = "alygon"


class ListagemUsuariosSchema(BaseModel):
    usuarios:List[UsuarioSchema]


def apresenta_usuarios(usuarios: List[Usuario]):
    result = []
    for usuario in usuarios:
        result.append({
            "login": usuario.login,
            "nome": usuario.nome
        })

    return {"usuarios": result}


class UsuarioViewSchema(BaseModel):
    id: int = 1
    login: str = "alygon"
    nome: str = "Alysson Gonçalves"
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class UsuarioDelSchema(BaseModel):
    mensagem: str = "Usuário apagado do sistema!"
    login: str = "alygon"

def apresenta_usuario(usuario: Usuario):
    return {
        "id": usuario.id,
        "login": usuario.login,
        "nome": usuario.nome,
        "total_cometarios": len(usuario.comentarios),
        "comentarios": [{"descricao": c.descricao} for c in usuario.comentarios]
    }

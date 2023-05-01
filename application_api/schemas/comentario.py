from pydantic import BaseModel

class ComentarioSchema(BaseModel):
    login: str = "alygon"
    descricao: str = "As charges continuam saindo fora do layout do facebook."

from pydantic import BaseModel


class ErrorSchema(BaseModel):
    mensagem: str = "Mensagem de erro!"

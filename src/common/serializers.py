from pydantic import BaseModel, Field
from typing import Optional


class ExceptionSerializer(BaseModel):
    code: str = Field(..., title='Código do erro')
    detail: Optional[str] = Field(None, title='Descrição do erro')
    response: Optional[str] = Field(None, title='Resposta da API')

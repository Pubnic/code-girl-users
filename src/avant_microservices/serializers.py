from pydantic import BaseModel, Field


class StatusOKSerializer(BaseModel):
    status: str = Field('OK', const=True, title='Status')

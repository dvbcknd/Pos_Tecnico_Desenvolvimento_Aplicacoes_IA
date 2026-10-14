from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Base com os campos comuns
class AtendimentoBase(BaseModel):
    nome_cliente: str
    categoria: str
    atendente: str
    data_atendimento: Optional[datetime] = None
    status: str
    avaliacao: Optional[float] = None
    tempo_minutos: int
    descricao: Optional[str] = None

# Schema usado para criar um novo atendimento (POST)
class AtendimentoCreate(AtendimentoBase):
    pass

# Schema usado para atualizar dados (PUT) - todos os campos são opcionais
class AtendimentoUpdate(BaseModel):
    nome_cliente: Optional[str] = None
    categoria: Optional[str] = None
    atendente: Optional[str] = None
    data_atendimento: Optional[datetime] = None
    status: Optional[str] = None
    avaliacao: Optional[float] = None
    tempo_minutos: Optional[int] = None
    descricao: Optional[str] = None

# Schema retornado pela API (GET, POST, PUT) incluindo o ID gerado
class AtendimentoResponse(AtendimentoBase):
    id: int

    class Config:
        from_attributes = True
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True)
    nome_cliente = Column(String, nullable=False)
    categoria = Column(String, nullable=False)      # Ex: Suporte, Vendas, Financeiro
    atendente = Column(String, nullable=False)      # Nome do atendente responsável
    data_atendimento = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False)         # Ex: Concluído, Em andamento, Cancelado
    avaliacao = Column(Float, nullable=True)        # Nota de satisfação (ex: 1.0 a 5.0)
    tempo_minutos = Column(Integer, nullable=False) # Tempo médio/duração do atendimento
    descricao = Column(String, nullable=True)       # Observações do atendimento
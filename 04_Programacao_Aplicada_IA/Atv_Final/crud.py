from sqlalchemy.orm import Session
from datetime import datetime
import models
import schemas

# Listar todos os atendimentos
def get_atendimentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Atendimento).offset(skip).limit(limit).all()

# Buscar por ID
def get_atendimento_by_id(db: Session, atendimento_id: int):
    return db.query(models.Atendimento).filter(models.Atendimento.id == atendimento_id).first()

# Criar um novo atendimento
def create_atendimento(db: Session, atendimento: schemas.AtendimentoCreate):
    dados = atendimento.model_dump()
    if dados.get("data_atendimento") is None:
        dados["data_atendimento"] = datetime.utcnow()
        
    db_atendimento = models.Atendimento(**dados)
    db.add(db_atendimento)
    db.commit()
    db.refresh(db_atendimento)
    return db_atendimento

# Atualizar um atendimento existente
def update_atendimento(db: Session, atendimento_id: int, atendimento_data: schemas.AtendimentoUpdate):
    db_atendimento = get_atendimento_by_id(db, atendimento_id)
    if not db_atendimento:
        return None
    
    dados_para_atualizar = atendimento_data.model_dump(exclude_unset=True)
    for chave, valor in dados_para_atualizar.items():
        setattr(db_atendimento, chave, valor)
        
    db.commit()
    db.refresh(db_atendimento)
    return db_atendimento

# Deletar um atendimento
def delete_atendimento(db: Session, atendimento_id: int):
    db_atendimento = get_atendimento_by_id(db, atendimento_id)
    if not db_atendimento:
        return None
    db.delete(db_atendimento)
    db.commit()
    return db_atendimento
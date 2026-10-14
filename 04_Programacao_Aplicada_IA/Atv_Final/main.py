from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import pandas as pd

import models
import schemas
import crud
from database import engine, get_db

# Criar as tabelas no SQLite ao iniciar a aplicação
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Análise de Atendimentos",
    description="API REST desenvolvida para gerenciamento e análise de atendimentos ao cliente.",
    version="1.0.0"
)

# ==========================================
# ROTAS DO CRUD (Gerenciamento de Atendimentos)
# ==========================================

@app.post("/atendimentos/", response_model=schemas.AtendimentoResponse, status_code=status.HTTP_201_CREATED, tags=["Atendimentos"])
def criar_atendimento(atendimento: schemas.AtendimentoCreate, db: Session = Depends(get_db)):
    """Registra um novo atendimento no sistema."""
    return crud.create_atendimento(db=db, atendimento=atendimento)

@app.get("/atendimentos/", response_model=List[schemas.AtendimentoResponse], tags=["Atendimentos"])
def listar_atendimentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Consulta todos os atendimentos cadastrados."""
    return crud.get_atendimentos(db=db, skip=skip, limit=limit)

@app.get("/atendimentos/{atendimento_id}", response_model=schemas.AtendimentoResponse, tags=["Atendimentos"])
def buscar_atendimento(atendimento_id: int, db: Session = Depends(get_db)):
    """Consulta um atendimento específico pelo ID."""
    db_atendimento = crud.get_atendimento_by_id(db, atendimento_id=atendimento_id)
    if db_atendimento is None:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")
    return db_atendimento

@app.put("/atendimentos/{atendimento_id}", response_model=schemas.AtendimentoResponse, tags=["Atendimentos"])
def atualizar_atendimento(atendimento_id: int, atendimento: schemas.AtendimentoUpdate, db: Session = Depends(get_db)):
    """Atualiza as informações de um atendimento."""
    db_atendimento = crud.update_atendimento(db, atendimento_id=atendimento_id, atendimento_data=atendimento)
    if db_atendimento is None:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")
    return db_atendimento

@app.delete("/atendimentos/{atendimento_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Atendimentos"])
def deletar_atendimento(atendimento_id: int, db: Session = Depends(get_db)):
    """Exclui um atendimento do sistema."""
    db_atendimento = crud.delete_atendimento(db, atendimento_id=atendimento_id)
    if db_atendimento is None:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")
    return None


# ==========================================
# ROTAS DE ANÁLISE DE DADOS (Pandas)
# ==========================================

@app.get("/analise/indicadores", tags=["Análise de Dados"])
def obter_indicadores(db: Session = Depends(get_db)):
    """
    Realiza o tratamento e análise dos dados armazenados no banco SQLite 
    utilizando a biblioteca Pandas e retorna os indicadores do negócio.
    """
    atendimentos = crud.get_atendimentos(db=db, limit=10000)
    
    if not atendimentos:
        return {"mensagem": "Nenhum atendimento cadastrado para realizar análises."}

    # Converter os dados do SQLAlchemy/SQLite para um DataFrame do Pandas
    dados = [
        {
            "id": a.id,
            "nome_cliente": a.nome_cliente,
            "categoria": a.categoria,
            "atendente": a.atendente,
            "data_atendimento": a.data_atendimento,
            "status": a.status,
            "avaliacao": a.avaliacao,
            "tempo_minutos": a.tempo_minutos
        }
        for a in atendimentos
    ]
    df = pd.DataFrame(dados)

    # 1. Total real de atendimentos cadastrados na base
    total_atendimentos = int(len(df))

    # Identificação do maior/menor ID para justificar a contagem na apresentação
    menor_id = int(df['id'].min())
    maior_id = int(df['id'].max())

    # 2. Atendimentos por Categoria, Status e Atendente
    atendimentos_por_categoria = df['categoria'].value_counts().to_dict()
    atendimentos_por_status = df['status'].value_counts().to_dict()
    atendimentos_por_atendente = df['atendente'].value_counts().to_dict()

    # 3. Atendente com maior número de atendimentos
    top_atendente = df['atendente'].mode()[0] if not df['atendente'].empty else "N/A"

    # 4. Tempo médio dos atendimentos (em minutos)
    tempo_medio = round(float(df['tempo_minutos'].mean()), 2)

    # 5. Média das avaliações de satisfação
    media_avaliacao = round(float(df['avaliacao'].dropna().mean()), 2) if not df['avaliacao'].dropna().empty else 0.0

    # 6. Maior e menor avaliação
    maior_avaliacao = float(df['avaliacao'].max()) if not df['avaliacao'].dropna().empty else 0.0
    menor_avaliacao = float(df['avaliacao'].min()) if not df['avaliacao'].dropna().empty else 0.0

    # 7. Atendimentos por período (Ano-Mês)
    df['ano_mes'] = pd.to_datetime(df['data_atendimento']).dt.strftime('%Y-%m')
    atendimentos_por_periodo = df['ano_mes'].value_counts().sort_index().to_dict()

    # 8. Análise Adicional: Satisfação Média por Atendente
    satisfacao_por_atendente = df.groupby('atendente')['avaliacao'].mean().round(2).to_dict()

    return {
        "resumo_geral": {
            "total_registros_reais": total_atendimentos,
            "intervalo_ids": f"ID {menor_id} ao ID {maior_id}",
            "tempo_medio_minutos": tempo_medio,
            "media_satisfacao_geral": media_avaliacao,
            "maior_avaliacao": maior_avaliacao,
            "menor_avaliacao": menor_avaliacao,
            "atendente_destaque": top_atendente
        },
        "distribuicoes": {
            "por_categoria": atendimentos_por_categoria,
            "por_status": atendimentos_por_status,
            "por_atendente": atendimentos_por_atendente,
            "por_periodo": atendimentos_por_periodo
        },
        "analise_adicional": {
            "satisfacao_media_por_atendente": satisfacao_por_atendente
        }
    }
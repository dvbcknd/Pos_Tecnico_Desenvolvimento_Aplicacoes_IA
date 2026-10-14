from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI(
    title="API de Análise de Vendas",
    description="API REST desenvolvida com FastAPI e Pandas para consulta e análise de registros de vendas."
)

CSV_FILE = "vendas.csv"

def carregar_dados():
    """Função auxiliar para carregar o CSV de forma segura."""
    if not os.path.exists(CSV_FILE):
        raise HTTPException(
            status_code=500, 
            detail=f"Arquivo '{CSV_FILE}' não encontrado no diretório do servidor."
        )
    try:
        df = pd.read_csv(CSV_FILE)
        # Calcula uma coluna de valor total por venda para facilitar análises
        if 'quantidade' in df.columns and 'valor_unitario' in df.columns:
            df['valor_total'] = df['quantidade'] * df['valor_unitario']
        return df
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler o arquivo CSV: {str(e)}")


@app.get("/")
def raiz():
    return {"mensagem": "API de Vendas ativa. Acesse /docs para visualizar a documentação."}


@app.get("/vendas")
def listar_vendas():
    """Retorna todos os registros de vendas armazenados no CSV."""
    df = carregar_dados()
    # Converte o DataFrame para um dicionário compatível com JSON
    return df.to_dict(orient="records")


@app.get("/vendas/{id_venda}")
def obter_venda_por_id(id_venda: int):
    """Busca uma venda específica pelo seu ID."""
    df = carregar_dados()
    venda = df[df['id_venda'] == id_venda]
    
    if venda.empty:
        raise HTTPException(status_code=404, detail="Venda não encontrada.")
        
    return venda.to_dict(orient="records")[0]


@app.get("/analises/faturamento-total")
def faturamento_total():
    """Calcula o faturamento bruto total de todas as vendas."""
    df = carregar_dados()
    total = float(df['valor_total'].sum())
    quantidade_itens = int(df['quantidade'].sum())
    
    return {
        "faturamento_total": total,
        "total_itens_vendidos": quantidade_itens
    }


@app.get("/analises/por-categoria")
def analise_por_categoria():
    """Realiza um agrupamento para analisar o faturamento por categoria de produto."""
    df = carregar_dados()
    
    # Agrupa por categoria somando a quantidade e o valor total
    agrupado = df.groupby('categoria').agg(
        total_vendas=('id_venda', 'count'),
        itens_vendidos=('quantidade', 'sum'),
        faturamento=('valor_total', 'sum')
    ).reset_index()
    
    return agrupado.to_dict(orient="records")

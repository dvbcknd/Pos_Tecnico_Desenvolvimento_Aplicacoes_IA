from database import SessionLocal, engine
import models
from datetime import datetime, timedelta
import random

models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

def popular_banco():
    # Verifica se já existem registros
    if db.query(models.Atendimento).first():
        print("O banco de dados já possui registros!")
        return

    clientes = ["Ana Silva", "Carlos Souza", "Beatriz Lima", "João Pedro", "Mariana Costa", "Fernanda Alves", "Lucas Pereira"]
    categorias = ["Suporte Técnico", "Financeiro", "Vendas", "Reclamações", "Dúvidas"]
    atendentes = ["Gabriel Almeida", "Patricia Rocha", "Roberto Santos", "Camila Martins"]
    statuses = ["Concluído", "Em andamento", "Cancelado"]

    registros = []
    base_date = datetime.now() - timedelta(days=60)

    for i in range(50):  # Gera 50 atendimentos fictícios
        data_atendimento = base_date + timedelta(days=random.randint(0, 60), hours=random.randint(1, 8))
        registros.append(
            models.Atendimento(
                nome_cliente=random.choice(clientes),
                categoria=random.choice(categorias),
                atendente=random.choice(atendentes),
                data_atendimento=data_atendimento,
                status=random.choice(statuses),
                avaliacao=round(random.uniform(2.0, 5.0), 1),
                tempo_minutos=random.randint(5, 60),
                descricao=f"Atendimento referente à solicitação #{i+1}"
            )
        )

    db.add_all(registros)
    db.commit()
    print("50 registros de atendimentos criados com sucesso!")

if __name__ == "__main__":
    popular_banco()
    db.close()
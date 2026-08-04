# 🍄 MycoGuard — Sistema Inteligente para Classificação e Segurança Micológica

> **Aplicação de Machine Learning e Inteligência Artificial Explicável (Caixa-Branca) para a identificação preditiva da toxicidade em cogumelos.**

---

## 📌 Sobre o Projeto

O **MycoGuard** é um assistente preditivo desenvolvido como Projeto Integrador da disciplina de **Inteligência Artificial**. Seu principal objetivo é mitigar os riscos de envenenamento acidental por ingestão de cogumelos selvagens através de um modelo de aprendizado de máquina ágil, transparente e de alta precisão.

Distinguir espécimes comestíveis de venenosos a olho nu é uma tarefa ambígua e perigosa. A aplicação substitui regras empíricas por um cálculo probabilístico rigoroso, processando variáveis morfológicas e olfativas para emitir um diagnóstico instantâneo de segurança.

---

## 🎯 Principais Destaques e Diferenciais

- **IA Explicável (Modelo Caixa-Branca):** Utiliza o algoritmo *DecisionTreeClassifier* (Árvore de Decisão), permitindo auditabilidade total dos nós de decisão e transparência crítica em cenários de saúde.
- **Engenharia de UX e Seleção de Atributos:** Em vez de exigir o preenchimento de todas as 23 variáveis originais do dataset, o modelo foi otimizado para operar com as **5 variáveis preditoras estratégicas** de maior ganho de informação (*Information Gain*), reduzindo a fricção com o usuário no campo.
- **Independência Fotográfica:** Baseado em atributos estruturais e olfativos diretos, eliminando erros comuns de visão computacional provocados por fotos desfocadas ou má iluminação.
- **Risco Zero de Falsos Negativos:** Foco do treinamento voltado à eliminação rigorosa da classificação de espécimes venenosos como comestíveis.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

| Componente | Tecnologia / Biblioteca | Função |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.10+ | Linguagem base do projeto |
| **Engine de IA** | `Scikit-Learn` | Treinamento do *DecisionTreeClassifier* e encoding |
| **Manipulação de Dados**| `Pandas` / `NumPy` | Estruturação e tratamento de matrizes e DataFrames |
| **Interface Web** | `Streamlit` | Front-end interativo, reativo e responsivo |
| **Serialização** | `Joblib` | Exportação e carregamento dos modelos treinados (`.pkl`) |
| **Visualização (EDA)** | `Matplotlib` / `Seaborn` | Plotagem de matrizes de confusão e análises exploratórias |

---

## 🔬 Arquitetura e Fluxo do Sistema

1. **Entrada de Dados (Front-end):** O usuário escolhe 5 atributos observados (Odor, Cor das Brânquias, Cor dos Esporos, Habitat/Região e Cor do Chapéu) na interface do Streamlit.
2. **Pipeline de Encoding:** As variáveis categóricas em texto são transformadas dinamicamente em coleções numéricas com o `LabelEncoder`.
3. **Motor Preditivo:** O modelo treinado percorre as regras condicionais da Árvore de Decisão gerada pelo `Scikit-Learn`.
4. **Output & Explicabilidade:** O sistema retorna a classificação (*Comestível* vs. *Venenoso*), o percentual de confiança da previsão e o caminho lógico interno percorrido no nó folha.

---

## 📁 Estrutura de Pastas do Repositório

```text
MycoGuard/
├── .venv/                         # Ambiente virtual Python
├── app.py                         # Código-fonte da interface Web (Streamlit)
├── modelo_mycoguard.pkl           # Inteligência treinada da Árvore de Decisão
├── dicionario_encoders.pkl        # Encoders serializados para conversão de dados
├── dataset_cogumelos_traduzido.csv # Base de dados tratada (UCI Machine Learning)
├── requirements.txt               # Dependências do projeto para deploy
└── README.md                      # Documentação técnica do projeto
```

---

## 🗃️ Sobre a Base de Dados

- **Fonte:** UCI Machine Learning Repository (Audubon Society Field Guide).
- **Amostra:** 8.124 registros de espécimes da família Agaricaceae.
- **Divisão Amostral:** 70% para treino e 30% para teste com amostragem estratificada.

---

## 🚀 Como Executar o Projeto Localmente

### **Pré-requisitos**
- Ter o Python 3.10+ instalado em seu computador.

### **Passo a Passo**

1 - Clone o repositório:
```bash

```

2 - Crie e ative um ambiente virtual (recomendado):
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3 - Instale as dependências:
```bash
pip install -r requirements.txt
```

4 - Execute o aplicativo Streamlit:
```bash
streamlit run app.py
```

5 - O aplicativo será aberto automaticamente no seu navegador padrão em http://localhost:8501.

---

## 👥 Autores e Créditos

- **Desenvolvedor:** Bruno Gomes Silva
- **Disciplina:** Introdução à Inteligência Artificial
- **Instituição:** SENAI Cimatec
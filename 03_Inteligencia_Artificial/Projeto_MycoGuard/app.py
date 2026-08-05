# ==========================================
# FASE 3: APLICATIVO WEB INTERATIVO (app.py)
# ==========================================

import joblib
import pandas as pd
import streamlit as st

# 1. Configuração visual da página
st.set_page_config(
    page_title="MycoGuard — IA Micológica",
    page_icon="🍄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Estilização de cabeçalho
st.title("🍄 MycoGuard")
st.subheader("Sistema Inteligente de Triagem e Segurança Micológica")
st.markdown(
    "Insira as características morfológicas e olfativas do cogumelo para verificação de toxicidade baseada em **IA Explicável (Caixa-Branca)**."
)


# 2. Função para carregar os arquivos .pkl salvos na Fase 2
@st.cache_resource
def carregar_arquivos():
  modelo = joblib.load("modelo_mycoguard.pkl")
  encoders = joblib.load("dicionario_encoders.pkl")
  return modelo, encoders


# Tentativa de carregamento dos modelos
try:
  modelo, encoders = carregar_arquivos()
except Exception as e:
  st.error(
      "🚨 Erro ao carregar os arquivos `.pkl`. Certifique-se de que"
      " 'modelo_mycoguard.pkl' e 'dicionario_encoders.pkl' estão na mesma pasta"
      " do arquivo 'app.py'."
  )
  st.stop()

st.markdown("---")
st.markdown("### 📋 Formato de Entrada de Dados")

# 3. Formulário de seleção interativa
col1, col2 = st.columns(2)

with col1:
  odor = st.selectbox(
      "Odor do Cogumelo",
      encoders["odor"].classes_,
      help="Característica olfativa principal observada no espécime.",
  )
  cor_branquias = st.selectbox(
      "Cor das Brânquias",
      encoders["cor_branquias"].classes_,
      help="Coloração das lâminas sob o chapéu do cogumelo.",
  )
  cor_esporos = st.selectbox(
      "Cor dos Esporos",
      encoders["cor_esporos"].classes_,
      help="Cor da impressão de esporos extraída do cogumelo.",
  )

with col2:
  regiao = st.selectbox(
      "Região / Habitat",
      encoders["regiao"].classes_,
      help="Substrato ou ambiente onde o espécime foi coletado.",
  )
  cor_chapeu = st.selectbox(
      "Cor do Chapéu",
      encoders["cor_chapeu"].classes_,
      help="Coloração da superfície superior do píleo (chapéu).",
  )

# Botão de Ação
st.markdown("---")
if st.button(
    "🔍 Analisar Segurança com MycoGuard",
    type="primary",
    use_container_width=True,
):

  # 4. Processamento das Entradas (Encoding para o formato que a IA entende)
  dados_usuario = {
      "odor": encoders["odor"].transform([odor])[0],
      "cor_branquias": encoders["cor_branquias"].transform([cor_branquias])[0],
      "cor_esporos": encoders["cor_esporos"].transform([cor_esporos])[0],
      "regiao": encoders["regiao"].transform([regiao])[0],
      "cor_chapeu": encoders["cor_chapeu"].transform([cor_chapeu])[0],
  }

  df_input = pd.DataFrame([dados_usuario])

  # 5. Predição da Inteligência Artificial
  predicao_num = modelo.predict(df_input)[0]
  probabilidades = modelo.predict_proba(df_input)[0]

  # Decodificação do resultado de número para texto
  resultado_texto = encoders["tipo"].inverse_transform([predicao_num])[0]
  confianca = probabilidades[predicao_num] * 100

  # 6. Exibição do Diagnóstico de Saída (Output)
  st.markdown("### 📊 Diagnóstico do Sistema")

  if (
      resultado_texto.lower() == "comestivel"
      or resultado_texto.lower() == "comestível"
  ):
    st.success(
        f"✅ **DIAGNÓSTICO: APROVADO PARA CONSUMO ({resultado_texto.upper()})**"
    )
    st.info(f"Nível de Confiança do Modelo: **{confianca:.1f}%**")
  else:
    st.error(
        "🚨 **ALERTA MÁXIMO: ESPÉCIE ALTAMENTE VENENOSA / LETAL"
        f" ({resultado_texto.upper()})**"
    )
    st.warning(f"Risco Confirmado com **{confianca:.1f}%** de Certeza!")

  # 7. Motor de Explicabilidade Transparente (Caixa-Branca)
  st.markdown("---")
  with st.expander(
      "🔬 Ver Explicação Transparente da Decisão (Modelo Caixa-Branca)"
  ):
    st.write(
        "O modelo percorreu os seguintes nós lógicos da Árvore de Decisão para"
        " emitir este diagnóstico:"
    )
    st.code(
        f"""
[1] Variável Raiz: Odor selecionado = '{odor}'
[2] Cruzamento Secundário: Brânquias '{cor_branquias}' + Esporos '{cor_esporos}'
[3] Validação de Substrato/Habitat: Region = '{regiao}'
--------------------------------------------------------------
-> RESULTADO DO NÓ FOLHA: {resultado_texto.upper()} (Probabilidade: {confianca:.1f}%)
        """,
        language="yaml",
    )

# Rodapé institucional
st.caption(
    "MycoGuard v1.0 — Projeto Integrador para a disciplina de Inteligência"
    " Artificial | Feito por: [Bruno](https://github.com/dvbcknd)"
)
import streamlit as st

# ========== ESTILO CUSTOMIZADO ==========
st.markdown("""
    <style>
        body, .stApp {
            background-color: #eee5d2; /* Sua cor primária */
            color: #050835; /* Sua cor secundária para o texto */
        }

        h1, h2, h3, h4, label, p, div, input, button {
            color: #2d63b2 !important;
        }

        .stNumberInput input {
            background-color: #eaf1fc !important;
            color: #050835 !important;
        }

        .stMetric label, .stMetric div {
            color: #2d63b2 !important;
        }

        input[type="radio"] {
            accent-color: #2d63b2 !important;
        }

        div[data-baseweb="radio"] label p {
            color: #2d63b2 !important;
            font-weight: bold;
        }

        label[data-baseweb="radio"] {
            background: transparent !important;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)


# ========== TÍTULO ==========
st.title("📈 Calculadora Kelly Criterion")

# ========== CAMPOS ==========
st.markdown("Preencha os campos abaixo para calcular o fator de alocação baseado no Critério de Kelly.")

col1, col2 = st.columns(2)
with col1:
    win_rate = st.number_input("Assertividade (%)", min_value=0.0, max_value=100.0, value=55.0, step=0.1) / 100
with col2:
    payoff = st.number_input("Fator Lucrativo (Payoff)", min_value=0.1, value=1.5, step=0.1)

# ========== CÁLCULO ==========
kelly = win_rate - ((1 - win_rate) / payoff)
kelly = max(0, kelly)

st.markdown(f"### 🔢 Fator de Kelly Ideal: `{kelly:.2%}`")

# ========== ESCALAS ==========
st.markdown("#### 🧮 Frações do Kelly para controle de risco:")

fractions = {
    "1/4 Kelly": kelly * 0.25,
    "1/2 Kelly": kelly * 0.50,
    "3/4 Kelly": kelly * 0.75,
    "Full Kelly": kelly
}

col1, col2 = st.columns(2)
for i, (label, value) in enumerate(fractions.items()):
    with (col1 if i % 2 == 0 else col2):
        st.metric(label=label, value=f"{value:.2%}")



# Rodapé
st.markdown("---")
st.markdown("**Desenvolvido por Kauan Nunes - Trader QUANT**")

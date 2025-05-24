import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")
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




st.title("📊 Simulador de Resultados por Trade")

# === INPUTS ===
col1, col2, col3 = st.columns(3)
with col1:
    win_rate = st.number_input("Taxa de acerto (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.5)
with col2:
    rr_ratio = st.number_input("Ratio Recompensa/Risco", min_value=0.1, value=1.5, step=0.1)
with col3:
    risk_per_trade = st.number_input("Risco por Operação (%)", min_value=0.1, value=1.5, step=0.1)

col4, col5 = st.columns(2)
with col4:
    initial_balance = st.number_input("Saldo inicial $", min_value=100.0, value=1000.0, step=10.0)
with col5:
    num_trades = st.number_input("Total de Trades", min_value=1, max_value=1000, value=20)

simulate = st.button("🚀 Projetar")

# === SIMULAÇÃO ===
if simulate:
    results = []
    balance = initial_balance
    wins = 0
    losses = 0

    for i in range(1, int(num_trades) + 1):
        is_win = np.random.rand() < (win_rate / 100)
        amount = balance * (risk_per_trade / 100)

        if is_win:
            profit = amount * rr_ratio
            wins += 1
        else:
            profit = -amount
            losses += 1

        balance += profit
        retorno = ((balance / initial_balance) - 1) * 100
        results.append([i, f"${profit:.2f}", f"${balance:.2f}", f"{retorno:.2f}%"])

    df = pd.DataFrame(results, columns=["Trade #", "Resultado da operação", "Saldo Final", "Retorno"])

    def highlight(val):
        return "background-color: #c6efce" if "-" not in val else "background-color: #f4cccc"

    styled_df = df.style.applymap(highlight, subset=["Resultado da operação"])

    st.dataframe(styled_df, use_container_width=True)

    st.info(f"**Taxa de acerto real:** {wins/num_trades:.0%}. Ganhou: {wins} e perdeu: {losses} trades. "
            "Repare que com mais operações o 'real' tende a ficar mais próximo do planejado.")






# Rodapé
st.markdown("---")
st.markdown("**Desenvolvido por Kauan Nunes - Trader QUANT**")

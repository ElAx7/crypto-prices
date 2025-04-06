import streamlit as st
import matplotlib.pyplot as plt
from crypto import get_historical_data, get_crypto_price  

st.title('📊 Crypto Dashboard')
coin = st.selectbox("Elige una cripto", ["bitcoin", "ethereum", "solana", "cardano"])
days = st.slider("Días históricos", 1, 365, 30)

# Llama a la función importada
dates, prices = get_historical_data(coin, days)
fig, ax = plt.subplots()
ax.plot(dates, prices)
st.pyplot(fig)
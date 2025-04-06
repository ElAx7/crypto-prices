# Crypto Price Tracker
# 📈 Crypto Price Tracker

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/ElAx7/crypto-prices)
![License](https://img.shields.io/badge/License-MIT-green)

Aplicación Python para rastrear precios de criptomonedas en tiempo real usando la API de CoinGecko, con visualización de datos históricos y alertas personalizables.

![Screenshot de la App](/view.png)

## 🌟 Características

- ✅ Obtiene precios actuales de 100+ criptomonedas
- 📊 Gráficos interactivos de histórico (1 día a 1 año)
- 🔔 Alertas por email cuando los precios cambian (opcional)
- 🐳 Configuración con Docker para despliegue fácil
- 🧪 Tests automatizados con pytest

## 🛠 Tecnologías

- **Lenguaje**: Python 3.11
- **Librerías Principales**:
  - `requests` - Para llamadas a la API de CoinGecko
  - `matplotlib` - Visualización de datos
  - `pytest` - Testing
- **Herramientas**:
  - Git
  - Docker

## 🚀 Cómo Ejecutar

### Opción 1: Localmente
```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/crypto-prices.git
cd crypto-prices

# Instala dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
python3 crypto.py 

chmod +x start.sh && ./start.sh

#Añade logs: Para debuggear, ejecuta Streamlit en modo verbose
streamlit run app.py --logger.level=debug
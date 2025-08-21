

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Title ---
st.title("📈 Tweet-based Stock Price Predictor")

# --- Sidebar for inputs ---
st.sidebar.header("Prediction Settings")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol", "AAPL")
n_days = st.sidebar.number_input("Days to Predict", min_value=1, max_value=30, value=7)

# --- Predict Button ---
if st.sidebar.button("Predict"):
    st.subheader(f"Predicted Closing Prices for {stock_symbol} - Next {n_days} Days")

    # Dummy prediction logic (replace later with your ML model)
    last_price = 150  # placeholder
    predictions = [last_price + np.random.randn() * 2 for _ in range(n_days)]
    dates = pd.date_range(start=pd.Timestamp.today(), periods=n_days)

    # Create dataframe
    df_pred = pd.DataFrame({"Date": dates, "Predicted Close": predictions})

    # Show table
    st.dataframe(df_pred)

    # Show line chart
    fig, ax = plt.subplots()
    ax.plot(df_pred["Date"], df_pred["Predicted Close"], marker="o", linestyle="-", label="Prediction")
    ax.set_xlabel("Date")
    ax.set_ylabel("Predicted Close Price")
    ax.legend()
    st.pyplot(fig)

else:
    st.info("👈 Enter stock symbol and days, then click Predict.")

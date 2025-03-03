import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data (Pastikan data yang digunakan sudah disiapkan sebelumnya)
@st.cache_data
def load_data_orders():
    return orders_df

@st.cache_data
def load_data_orderitem():
    return orders_df

@st.cache_data
def load_data_customer():
    return orders_df

df = load_data()

# Judul Dashboard
st.title("Dashboard Analisis Data")

# **1. Visualisasi Tren Penjualan Bulanan**
st.subheader("Tren Penjualan Bulanan")
monthly_orders = df.groupby(df['order_purchase_timestamp'].dt.to_period("M")).size()
fig, ax = plt.subplots()
ax.plot(monthly_orders.index.astype(str), monthly_orders.values, marker='o', linestyle='-')
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Pesanan")
ax.set_title("Tren Penjualan Bulanan")
st.pyplot(fig)

# **2. Visualisasi Top 10 Pelanggan Berdasarkan Monetary Value**
st.subheader("Top 10 Pelanggan Berdasarkan Monetary Value")
top_customers = rfm_df.sort_values(by='Monetary', ascending=False).head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_customers.index, y=top_customers['Monetary'], palette='viridis', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_xlabel("Customer ID")
ax.set_ylabel("Total Monetary Value")
ax.set_title("Top 10 Pelanggan Berdasarkan Monetary Value")
st.pyplot(fig)

st.write("Dashboard ini menampilkan tren penjualan dan daftar pelanggan bernilai tinggi berdasarkan RFM Analysis.")

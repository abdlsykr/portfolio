import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data dari URL
@st.cache_data
def load_data():
    url_orders = "https://raw.githubusercontent.com/abdlsykr/portfolio/refs/heads/main/Dicoding/Belajar%20Analisis%20Data%20dengan%20Python/E-Commerce%20Public%20Dataset/data/orders_dataset.csv"
    url_order_items = "https://raw.githubusercontent.com/abdlsykr/portfolio/refs/heads/main/Dicoding/Belajar%20Analisis%20Data%20dengan%20Python/E-Commerce%20Public%20Dataset/data/order_items_dataset.csv"
    url_customers = "https://raw.githubusercontent.com/abdlsykr/portfolio/refs/heads/main/Dicoding/Belajar%20Analisis%20Data%20dengan%20Python/E-Commerce%20Public%20Dataset/data/customers_dataset.csv"
    
    orders_df = pd.read_csv(url_orders, parse_dates=['order_purchase_timestamp'])
    order_items_df = pd.read_csv(url_order_items)
    customers_df = pd.read_csv(url_customers)
    
    return orders_df, order_items_df, customers_df

orders_df, order_items_df, customers_df = load_data()

# Judul Dashboard
st.title("Dashboard Analisis Data E-Commerce Public")

st.write("Dashboard ini menampilkan tren penjualan dan daftar pelanggan high value berdasarkan RFM Analysis.")

# **1. Visualisasi Tren Penjualan Bulanan**
st.subheader("Tren Penjualan Bulanan")
monthly_orders = orders_df.groupby(orders_df['order_purchase_timestamp'].dt.to_period("M")).size()
fig, ax = plt.subplots()
ax.plot(monthly_orders.index.astype(str), monthly_orders.values, marker='o', linestyle='-')
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Pesanan")
ax.set_title("Tren Penjualan Bulanan")
plt.xticks(rotation=90)  # Menyesuaikan rotasi label sumbu x
st.pyplot(fig)

st.write("Tren penjualan menunjukkan peningkatan signifikan sejak awal hingga mencapai puncaknya pada akhir 2017. Namun, terdapat penurunan drastis setelah pertengahan 2018, yang mungkin disebabkan oleh faktor musiman atau perubahan strategi bisnis.")

# **2. Analisis RFM (Recency, Frequency, Monetary)**
latest_date = orders_df['order_purchase_timestamp'].max()
rfm_df = order_items_df.groupby('order_id').agg(
    {'price': 'sum'}
).reset_index()
rfm_df = rfm_df.merge(orders_df[['order_id', 'customer_id', 'order_purchase_timestamp']], on='order_id')
rfm_df['Recency'] = (latest_date - rfm_df['order_purchase_timestamp']).dt.days
rfm_df = rfm_df.groupby('customer_id').agg(
    {'Recency': 'min', 'order_id': 'count', 'price': 'sum'}
).rename(columns={'order_id': 'Frequency', 'price': 'Monetary'})

# **3. Visualisasi Top 10 Pelanggan Berdasarkan Monetary Value**
st.subheader("Top 10 Pelanggan Berdasarkan Monetary Value")
top_customers = rfm_df.sort_values(by='Monetary', ascending=False).head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_customers.index, y=top_customers['Monetary'], palette='viridis', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_xlabel("Customer ID")
ax.set_ylabel("Total Monetary Value")
ax.set_title("Top 10 Pelanggan Berdasarkan Monetary Value")
st.pyplot(fig)

st.write("Satu pelanggan memiliki nilai transaksi yang jauh lebih tinggi dibandingkan pelanggan lainnya, hampir dua kali lipat dari pelanggan di posisi kedua. Ini menunjukkan bahwa pelanggan ini berkontribusi secara signifikan terhadap pendapatan. Perusahaan dapat mempertimbangkan strategi khusus seperti program loyalitas, penawaran eksklusif, atau layanan premium untuk mempertahankan dan meningkatkan keterlibatan pelanggan bernilai tinggi ini.")

# **4. Visualisasi Distribusi Segmen Pelanggan**
st.subheader("Distribusi Segmen Pelanggan")
rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], q=4, labels=[4, 3, 2, 1])
rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'].rank(method='first'), q=4, labels=[1, 2, 3, 4])
rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'], q=4, labels=[1, 2, 3, 4])
rfm_df['RFM_Score'] = rfm_df[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)
seg_map = {
    r'[1-3]': 'Low Value',
    r'[4-6]': 'Mid Value',
    r'[7-9]': 'High Value',
    r'10|11|12': 'Best Customers'
}
rfm_df['Segment'] = rfm_df['RFM_Score'].astype(str).replace(seg_map, regex=True)
fig, ax = plt.subplots()
sns.countplot(x=rfm_df['Segment'], palette='coolwarm', order=rfm_df['Segment'].value_counts().index, ax=ax)
ax.set_xlabel("Segment")
ax.set_ylabel("Jumlah Pelanggan")
ax.set_title("Distribusi Segmen Pelanggan")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("Mayoritas pelanggan berada dalam kategori High Value, menunjukkan bahwa banyak pelanggan melakukan pembelian berulang dengan nilai transaksi yang tinggi. Terdapat segmen Low Value, yang mungkin mencerminkan pelanggan dengan transaksi sekali pakai atau pola pembelian yang tidak konsisten. Analisis lebih lanjut diperlukan untuk memahami apakah segmen ini bisa dikembangkan atau ditargetkan dengan strategi pemasaran tertentu.")
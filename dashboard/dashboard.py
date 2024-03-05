import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/day.csv')  # Mengubah path direktori file day.csv
    return df

df = load_data()

# Cetak nama kolom yang ada dalam DataFrame
st.write("dteday")
st.write(df["dteday"])

# Data Wrangling
pd.set_option('mode.use_inf_as_null', True)  # Menangani nilai infinitas
df['dteday'] = pd.to_datetime(df['dteday'])
df.drop(columns=['instant', 'temp', 'casual', 'registered'], inplace=True)
df.dropna(inplace=True)
df['mnth'] = df['mnth'].map({1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug",
                              9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"})
df['season'] = df['season'].map({1:"semi", 2:"panas", 3:"gugur", 4:"salju"})
df['weathersit'] = df['weathersit'].map({1:"cerah", 2:"berawan", 3:"hujan ringan", 4:"hujan deras"})

# Visualisasi Grafik
st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://www.kaggle.com/code/ramanchandra/bike-sharing-data-analysis)")


# VISUALIZATION


# yearly bike share count
# st.subheader("Hourly Bike Share Count")
yearly_count = data.groupby("yr")["cnt"].sum().reset_index()
fig_yearly_count = px.line(
    yearly_count, x="yr", y="cnt", title="Jumlah Jam Penyewaan Sepeda per Tahun")
st.plotly_chart(fig_yearly_count, use_container_width=True,
                height=400, width=600)

# daily bike share count
# st.subheader("Hourly Bike Share Count")
dteday_count = data.groupby("dteday")["cnt"].sum().reset_index()
fig_dteday_count = px.line(
    dteday_count, x="dteday", y="cnt", title="Jumlah Penyewaan Sepeda per Tanggal")
st.plotly_chart(fig_dteday_count, use_container_width=True,
                height=400, width=600)


# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. "
                "Dataset ini mengandung informasi mengenai penyewaan sepeda berdasarkan berbagai variabel seperti musim, suhu, kelembaban, dan faktor lainnya.")

# Main Function
def main():
    st.sidebar.title("Informasi Pengguna")
    st.sidebar.subheader("Data Diri")
    st.sidebar.write("- **Nama:** Akhtar Ramadhan Putra")
    st.sidebar.write("- **Email:** m295d4ky1879@bangkit.academy")
    st.sidebar.write("- **ID Dicoding:** https://www.dicoding.com/users/akhtar_ramadhan/")

if __name__ == '__main__':
    main()

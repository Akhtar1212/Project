import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/day.csv')
    return df

# Load the data
df = load_data()

# Sidebar
st.sidebar.title("Informasi Pengguna")
st.sidebar.subheader("Data Diri")
st.sidebar.write("- **Nama:** Akhtar Ramadhan Putra")
st.sidebar.write("- **Email:** m295d4ky1879@bangkit.academy")
st.sidebar.write("- **ID Dicoding:** https://www.dicoding.com/users/akhtar_ramadhan/")

# Main Content
st.title("Dashboard Analisis Data Bike Sharing")

# Data Wrangling
df['dteday'] = pd.to_datetime(df['dteday'])
df['mnth'] = df['mnth'].map({1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug",
                              9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"})
df['season'] = df['season'].map({1:"semi", 2:"panas", 3:"gugur", 4:"salju"})
df['weathersit'] = df['weathersit'].map({1:"cerah", 2:"berawan", 3:"hujan ringan", 4:"hujan deras"})

# Main Function
def main():
    st.header("Data Summary")
    st.write(df.head())

    st.header("Informasi Statistik Data")
    st.write(df.describe())

    st.header("Visualisasi Data")
    # Visualisasi: Distribusi Jumlah Sepeda yang Disewakan Berdasarkan Musim
    st.subheader("Distribusi Jumlah Sepeda yang Disewakan Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='season', y='cnt', ax=ax)
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Sepeda')
    plt.title('Distribusi Jumlah Sepeda yang Disewakan Berdasarkan Musim')
    plt.xticks([0, 1, 2, 3], ['Semi', 'Panas', 'Gugur', 'Salju'])
    st.pyplot(fig)

if __name__ == '__main__':
    main()

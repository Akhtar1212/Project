import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

    st.header("Data Visualization")

    # Visualisasi 1: Jumlah Sepeda yang Disewakan Berdasarkan Kondisi Cuaca
    st.subheader("Jumlah Sepeda yang Disewakan Berdasarkan Kondisi Cuaca")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x="dteday", y="cnt", hue="weathersit", ax=ax1)
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Sepeda")
    plt.title("Jumlah Sepeda yang Disewakan Berdasarkan Kondisi Cuaca")
    st.pyplot(fig1)

    # Visualisasi 2: Jumlah Sepeda yang Disewakan Berdasarkan Musim
    st.subheader("Jumlah Sepeda yang Disewakan Berdasarkan Musim")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x="season", y="cnt", hue="yr", palette="rocket", ci=None, ax=ax2)
    plt.ylabel("Jumlah Sepeda")
    plt.xlabel("Musim")
    plt.title("Jumlah Sepeda yang Disewakan Berdasarkan Musim")
    plt.xticks([0,1,2,3],['Semi', 'Panas', 'Gugur', 'Salju'])
    plt.legend(title='Tahun', loc='best', labels=['2011', '2012'], frameon=False)
    st.pyplot(fig2)

    # Visualisasi 3: Distribusi Total Sepeda yang Disewakan Berdasarkan Musim dan Hari Kerja
    st.subheader("Distribusi Total Sepeda yang Disewakan Berdasarkan Musim dan Hari Kerja")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='season', y='cnt', hue='workingday', ax=ax3)
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Sepeda')
    plt.title('Distribusi Total Sepeda yang Disewakan Berdasarkan Musim dan Hari Kerja')
    plt.legend(title='Hari Kerja', loc='best', labels=['Non-Working Day', 'Working Day'], frameon=False)
    plt.xticks([0,1,2,3],['Semi', 'Panas', 'Gugur', 'Salju'])
    st.pyplot(fig3)

if __name__ == '__main__':
    main()

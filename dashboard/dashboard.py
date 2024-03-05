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
st.write("weathersit")
st.write(df[["weathersit"]])

# Data Wrangling
df['dteday'] = pd.to_datetime(df['dteday'])
df.drop(columns=['instant', 'temp', 'casual', 'registered'], inplace=True)
df.dropna(inplace=True)
df['mnth'] = df['mnth'].map({1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug",
                              9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"})
df['season'] = df['season'].map({1:"semi", 2:"panas", 3:"gugur", 4:"salju"})
df['weathersit'] = df['weathersit'].map({1:"cerah", 2:"berawan", 3:"hujan ringan", 4:"hujan deras"})

# Main Function
def main():
    st.sidebar.title("Informasi Pengguna")
    st.sidebar.subheader("Data Diri")
    st.sidebar.write("- **Nama:** Akhtar Ramadhan Putra")
    st.sidebar.write("- **Email:** m295d4ky1879@bangkit.academy")
    st.sidebar.write("- **ID Dicoding:** https://www.dicoding.com/users/akhtar_ramadhan/")

if __name__ == '__main__':
    main()


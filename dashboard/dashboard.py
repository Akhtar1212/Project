import pandas as pd
pd.set_option('use_inf_as_na', False) # Set 'use_inf_as_na' to False to avoid using infinities as NaN values
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/day.csv')  # Load the 'day.csv' file into a DataFrame
    return df

df = load_data()

# Data Wrangling
df['dteday'] = pd.to_datetime(df['dteday']) # Convert 'dteday' column to datetime format
df.drop(columns=['instant', 'temp', 'casual', 'registered'], inplace=True) # Drop unnecessary columns
df.dropna(inplace=True) # Remove any rows with missing values

# Map categorical variables to more understandable strings
df['mnth'] = df['mnth'].map({1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug",
                                   9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"})
df['season'] = df['season'].map({1:"semi", 2:"panas", 3:"gugur", 4:"salju"})
df['weathersit'] = df['weathersit'].map({1:"cerah", 2:"berawan", 3:"hujan ringan", 4:"hujan deras"})

# Visualization & Explanatory Analysis
def visualize():
    st.sidebar.title("Informasi Pengguna")
    st.sidebar.subheader("Data Diri")
    st.sidebar.write("- **Nama:** Akhtar Ramadhan Putra")
    st.sidebar.write("- **Email:** m295d4ky1879@bangkit.academy")
    st.sidebar.write("- **ID Dicoding:** https://www.dicoding.com/users/akhtar_ramadhan/")

    st.title("Dashboard Visualisasi Data Bike Sharing")

    st.write("### Visualisasi 1: Jumlah Sepeda yang Disewakan Berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(14,5))
    sns.lineplot(data=df, x="dteday", y="cnt",hue="weathersit", ax=ax) # Plot the number of bikes rented per day with different weather conditions
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah")
    plt.title("Jumlah Sepeda yang Disewakan Berdasarkan Kondisi Cuaca")
    st.pyplot(fig)

    st.write("### Visualisasi 2: Jumlah Sepeda yang Disewakan Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(data=df,x="season",  y="cnt", hue="yr", palette="rocket",  ci=None, ax=ax) # Plot the number of bikes rented per season with different years
    plt.ylabel('Jumlah')
    plt.xlabel('Musim')
    plt.title("Jumlah Sepeda yang Dise

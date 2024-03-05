import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
@st.cache
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
st.write("### Visualisasi Data")
st.write("#### Grafik Jumlah Sepeda yang Disewakan Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=df, x="dteday", y="cnt", hue="weathersit", ax=ax)
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Sepeda")
plt.title("Jumlah Sepeda yang Disewakan Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

st.write("#### Grafik Jumlah Sepeda yang Disewakan Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x="season", y="cnt", hue="yr", palette="rocket", ci=None, ax=ax)
plt.ylabel("Jumlah Sepeda")
plt.xlabel("Musim")
plt.title("Jumlah Sepeda yang Disewakan Berdasarkan Musim")
plt.xticks([0,1,2,3],['Semi', 'Panas', 'Gugur', 'Salju'])
plt.legend(title='Tahun', loc='best', labels=['2011', '2012'], frameon=False)
st.pyplot(fig)

st.write("#### Distribusi Total Sepeda yang Disewakan Berdasarkan Musim dan Hari Kerja")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='season', y='cnt', hue='workingday', ax=ax)
plt.xlabel('Musim')
plt.ylabel('Jumlah Sepeda')
plt.title('Distribusi Total Sepeda yang Disewakan Berdasarkan Musim dan Hari Kerja')
plt.legend(title='Hari Kerja', loc='best', labels=['Non-Working Day', 'Working Day'], frameon=False)
plt.xticks([0,1,2,3],['Semi', 'Panas', 'Gugur', 'Salju'])
st.pyplot(fig)

# Main Function
def main():
    st.sidebar.title("Informasi Pengguna")
    st.sidebar.subheader("Data Diri")
    st.sidebar.write("- **Nama:** Akhtar Ramadhan Putra")
    st.sidebar.write("- **Email:** m295d4ky1879@bangkit.academy")
    st.sidebar.write("- **ID Dicoding:** https://www.dicoding.com/users/akhtar_ramadhan/")

if __name__ == '__main__':
    main()

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
st.write(df.columns)

# Main Function
def main():
    visualize()

if __name__ == '__main__':
    main()

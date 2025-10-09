import streamlit as st
import pandas as pd

def sidebar_menu():
    st.sidebar.subheader("Pilih Halaman")
    menu = st.sidebar.radio(
        "Menu:",
        options=("Data Overview", "Business Insight")
    )
    return menu

def date_filter(day_df, hour_df):
    st.sidebar.markdown("---")
    st.sidebar.subheader("Filter Rentang Tanggal")

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

    min_date = day_df['dteday'].min()
    max_date = day_df['dteday'].max()

    start_date, end_date = st.sidebar.date_input(
        "Pilih Rentang Tanggal:",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    filtered_day_df = day_df[
        (day_df['dteday'] >= pd.to_datetime(start_date)) & 
        (day_df['dteday'] <= pd.to_datetime(end_date))
    ]

    filtered_hour_df = hour_df[
        (hour_df['dteday'] >= pd.to_datetime(start_date)) & 
        (hour_df['dteday'] <= pd.to_datetime(end_date))
    ]

    return filtered_day_df, filtered_hour_df
import streamlit as st
from modules.data_loader import load_data
from modules.data_overview import show_overview
from modules.utils import sidebar_menu, date_filter
from modules.business_insight import show_business_insights

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide", initial_sidebar_state="expanded")

day_df, hour_df = load_data()
menu = sidebar_menu()
filtered_day_df, filtered_hour_df = date_filter(day_df, hour_df)

if menu == "Data Overview":
    show_overview(filtered_day_df, filtered_hour_df)
elif menu == "Business Insight":
    show_business_insights(filtered_day_df, filtered_hour_df)
import streamlit as st

def show_overview(day_df, hour_df):
    st.header("Data Overview")

    st.subheader("Day-level Dataset")
    st.dataframe(day_df.head(100))

    st.subheader("Hour-level Dataset")
    st.dataframe(hour_df.head(100))

    st.write("Shape of day_df: ", day_df.shape)
    st.write("Shape of hour_df: ", hour_df.shape)
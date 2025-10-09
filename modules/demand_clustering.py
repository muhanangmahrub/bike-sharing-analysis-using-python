import streamlit as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

def show_demand_clustering(day_df):
    st.header("Demand Clustering Analysis")
    
    features = ['temp', 'hum', 'windspeed', 'cnt']
    X = day_df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=123)
    day_df['cluster'] = kmeans.fit_predict(X_scaled)

    # st.write("Cluster Centers:")
    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(
        day_df['temp'], 
        day_df['cnt'], 
        c=day_df['cluster'], 
        cmap='viridis',
        alpha=0.6
    )
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Count of Rentals')
    ax.set_title('K-Means Clustering of Bike Rentals')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    st.pyplot(fig)

    st.divider()
    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(
        day_df['hum'], 
        day_df['cnt'], 
        c=day_df['cluster'], 
        cmap='viridis',
        alpha=0.6
    )
    ax.set_xlabel('Humidity')
    ax.set_ylabel('Count of Rentals')
    ax.set_title('K-Means Clustering of Bike Rentals')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    st.pyplot(fig)

    st.divider()
    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(
        day_df['windspeed'], 
        day_df['cnt'], 
        c=day_df['cluster'], 
        cmap='viridis',
        alpha=0.6
    )
    ax.set_xlabel('Wind Speed')
    ax.set_ylabel('Count of Rentals')
    ax.set_title('K-Means Clustering of Bike Rentals')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    st.pyplot(fig)
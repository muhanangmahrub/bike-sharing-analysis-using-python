import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_business_insights(day_df, hour_df):
    st.header("Business Insight")

    st.subheader("Rata-rata Penyewaan Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=day_df,
        x="season",
        y="cnt",
        estimator="mean",
        errorbar=None,
        hue="season",
        palette="Set2",
        ax=ax,
        legend=False
    )
    # ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim", fontsize=10)
    ax.set_xlabel("Musim (1:Spring, 2:Summer, 3:Fall, 4:Winter)", size=8)
    ax.set_ylabel("Rata-rata Penyewaan Sepeda", size=8)
    st.pyplot(fig)

    st.divider()

    st.subheader("Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(
        data=day_df,
        x="weathersit",
        y="cnt",
        hue="weathersit",
        legend=False,
        palette="coolwarm",
        ax=ax
    )
    # ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca", fontsize=10)
    ax.set_xlabel("Kondisi Cuaca (1:Clear, 2:Mist, 3:Light Snow/Rain, 4:Heavy Rain/Snow)", size=8)
    ax.set_ylabel("Jumlah Penyewaan Sepeda", size=8)
    st.pyplot(fig)

    st.divider()
    combined_insight = (
        day_df.groupby(['season', 'weathersit'])
        .agg(
            avg_rentals=("cnt", "mean"),
            total_rentals=("cnt", "sum")
        )
        .sort_values("avg_rentals", ascending=False)
    )

    st.subheader("Rata-rata Penyewaan Berdasarkan Musim dan Kondisi Cuaca")
    # st.dataframe(combined_insight)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        data=combined_insight.reset_index(),
        x="season",
        y="avg_rentals",
        hue="weathersit",
        palette="Set3",
        ax=ax
    )
    # ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim dan Kondisi Cuaca", fontsize=10)
    st.pyplot(fig)
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_business_insights(day_df, hour_df):
    st.header("Business Insight")

    st.subheader("Rata-Rata Penyewaan Berdasarkan Musim")
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

    st.subheader("Rata-Rata Penyewaan Berdasarkan Musim dan Kondisi Cuaca")
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

    st.divider()
    st.subheader("Pola Penyewaan Sepeda per Jam")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        data=hour_df,
        x="hr",
        y="cnt",
        estimator="mean",
        errorbar=None,
        color="green",
        ax=ax
    )
    ax.set_xticks(range(0, 24))
    ax.set_ylabel("Rata-rata Penyewaan Sepeda", size=8)
    ax.set_xlabel("Jam (0-23)", size=8)
    st.pyplot(fig)

    st.divider()
    st.subheader("Rata-Rata Penyewaan Sepeda per Hari dalam Seminggu")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(
        data=day_df,
        x="weekday",
        y="cnt",
        estimator="mean",
        errorbar=None,
        hue="weekday",
        legend=False,
        palette="Set3",
        ax=ax
    )
    ax.set_xlabel("Hari dalam Seminggu", size=8)
    ax.set_ylabel("Rata-rata Penyewaan Sepeda", size=8)
    st.pyplot(fig)

    st.divider()
    st.subheader("Perilaku Pengguna Terdaftar vs Pengguna Kasual per Jam")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.set_style("whitegrid")
    sns.lineplot(
        data=hour_df.melt(id_vars=['hr'], value_vars=['registered', 'casual'], var_name='user_type', value_name='count'),
        x='hr',
        y='count',
        hue='user_type',
        ax=ax
    )
    ax.set_xticks(range(0, 24))
    ax.set_xlabel("Jam (0-23)", size=8)
    ax.set_ylabel("Jumlah Penyewaan Sepeda", size=8)
    st.pyplot(fig)

    st.divider()
    st.subheader("Perbandingan Pengguna Casual dan Terdaftar per Hari")
    user_weekday = day_df.groupby("weekday")[["casual", "registered"]].mean().reset_index()
    nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    user_weekday["nama_hari"] = user_weekday["weekday"].apply(lambda x: nama_hari[x])

    fig, ax = plt.subplots(figsize=(10, 5))
    user_weekday.plot(
        x="nama_hari",
        y=["casual", "registered"],
        kind="bar",
        stacked=False,
        ax=ax,
        color=["orange", "skyblue"]
    )
    ax.set_xlabel("Hari dalam Seminggu", size=8)
    ax.set_ylabel("Rata-rata Penyewaan Sepeda", size=8)
    st.pyplot(fig)
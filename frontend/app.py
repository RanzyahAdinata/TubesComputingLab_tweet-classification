import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

API_URL = "http://backend:8000"

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Tweet Topic Classifier",
    page_icon="🐦",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom right, #020617, #0f172a);
}

/* TEXT */
h1, h2, h3, h4 {
    color: white;
}

p {
    color: #cbd5e1;
}

/* INPUT */
.stTextArea textarea {

    background-color: #111827;

    color: white;

    border-radius: 14px;

    border: 1px solid #334155;

    font-size: 16px;
}

/* BUTTON */
.stButton button {

    width: 100%;

    height: 52px;

    border-radius: 14px;

    border: none;

    color: white;

    font-size: 16px;

    font-weight: bold;

    background: linear-gradient(
        270deg,
        #2563eb,
        #7c3aed,
        #2563eb
    );

    background-size: 400% 400%;

    animation: gradientMove 8s ease infinite;

    transition: 0.3s ease;
}

.stButton button:hover {

    transform: scale(1.02);

    box-shadow:
        0 0 20px rgba(124,58,237,0.5);
}

/* PREDICTION CARD */
.prediction-card {

    background: linear-gradient(
        135deg,
        rgba(37,99,235,0.95),
        rgba(124,58,237,0.95)
    );

    padding: 35px;

    border-radius: 24px;

    text-align: center;

    margin-top: 25px;

    margin-bottom: 25px;

    box-shadow:
        0 0 30px rgba(124,58,237,0.3);

    animation: fadeIn 0.8s ease;
}

.prediction-label {

    color: rgba(255,255,255,0.8);

    font-size: 16px;

    margin-bottom: 10px;

    letter-spacing: 1px;
}

.prediction-value {

    color: white;

    font-size: 38px;

    font-weight: bold;

    animation: pulse 2s infinite;
}

/* CLOCK */
.clock-box {

    position: fixed;

    top: 20px;
    right: 25px;

    background: rgba(15,23,42,0.8);

    padding: 12px 18px;

    border-radius: 16px;

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(10px);

    z-index: 999;

    animation: floatClock 4s ease-in-out infinite;
}

.clock-time {

    color: white;

    font-size: 20px;

    font-weight: bold;
}

.clock-date {

    color: #cbd5e1;

    font-size: 12px;
}

/* TABLE */
[data-testid="stDataFrame"] {

    border-radius: 18px;

    overflow: hidden;

    border: 1px solid #334155;
}

/* ANIMATIONS */
@keyframes pulse {

    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.03);
    }

    100% {
        transform: scale(1);
    }
}

@keyframes gradientMove {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

@keyframes fadeIn {

    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floatClock {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-3px);
    }

    100% {
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# CLOCK
# =========================
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d %B %Y")

st.markdown(f"""
<div class="clock-box">
    <div class="clock-time">🕒 {current_time}</div>
    <div class="clock-date">{current_date}</div>
</div>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("🐦 Tweet Topic Classification")

st.write(
    "Klasifikasi topik tweet menggunakan "
    "Machine Learning dan Natural Language Processing"
)

st.divider()

# =========================
# INPUT
# =========================
st.header("✍️ Klasifikasi Tweet")

tweet_input = st.text_area(
    "Masukkan tweet:",
    height=180,
    placeholder="Contoh: I love playing football today"
)

# =========================
# PREDICT
# =========================
if st.button("🔍 Klasifikasikan Tweet"):

    if tweet_input.strip() == "":
        st.warning("Tweet tidak boleh kosong")

    else:

        with st.spinner("🧠 AI sedang menganalisis tweet..."):

            response = requests.post(
                f"{API_URL}/predict",
                json={"tweet": tweet_input}
            )

        if response.status_code == 200:

            result = response.json()

            prediction = result[
                "prediction_label"
            ].replace("_", " ").title()

            st.markdown(f"""
<div class="prediction-card">

    <div class="prediction-label">
        🤖 AI Prediction Result
    </div>

    <div class="prediction-value">
        {prediction}
    </div>

</div>
""", unsafe_allow_html=True)

        else:
            st.error("Terjadi kesalahan pada server")

st.divider()

# =========================
# DASHBOARD
# =========================
st.header("📊 Monitoring Dashboard")

stats_response = requests.get(f"{API_URL}/stats")
logs_response = requests.get(f"{API_URL}/logs")

col1, col2 = st.columns(2)

# =========================
# PIE CHART
# =========================
with col1:

    st.subheader("Distribusi Kategori")

    if stats_response.status_code == 200:

        data = stats_response.json()

        if len(data) > 0:

            labels = list(data.keys())
            values = list(data.values())

            fig, ax = plt.subplots(figsize=(5,5))

            ax.pie(
                values,
                labels=labels,
                autopct='%1.1f%%'
            )

            st.pyplot(fig)

        else:
            st.info("Belum ada data")

# =========================
# BAR CHART
# =========================
with col2:

    st.subheader("Jumlah Prediksi")

    if stats_response.status_code == 200:

        data = stats_response.json()

        if len(data) > 0:

            df_chart = pd.DataFrame({
                "Kategori": list(data.keys()),
                "Jumlah": list(data.values())
            })

            st.bar_chart(
                df_chart.set_index("Kategori")
            )

        else:
            st.info("Belum ada data")

st.divider()

# =========================
# DELETE HISTORY
# =========================
col3, col4 = st.columns([4,1])

with col4:

    if st.button("🗑️ Hapus Riwayat"):

        delete_response = requests.delete(
            f"{API_URL}/logs"
        )

        if delete_response.status_code == 200:

            st.success("Riwayat berhasil dihapus")

            st.rerun()

st.divider()

# =========================
# LOG TABLE
# =========================
st.subheader("📄 Riwayat Prediksi")

if logs_response.status_code == 200:

    logs = logs_response.json()

    if len(logs) > 0:

        df_logs = pd.DataFrame(logs)

        df_logs.columns = [
            "ID",
            "Tweet",
            "Prediction",
            "Created At"
        ]

        st.dataframe(
            df_logs,
            use_container_width=True
        )

    else:
        st.info("Belum ada riwayat")
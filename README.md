# 🐦 Tweet Topic Classification

Aplikasi klasifikasi topik tweet berbasis Machine Learning dan Natural Language Processing (NLP).

Project ini dibuat untuk memenuhi tugas besar AI Engineering dan Machine Learning dengan implementasi end-to-end mulai dari preprocessing data, training model, backend API, frontend dashboard, hingga deployment.

---

# 🚀 Features

✅ Tweet topic classification menggunakan Machine Learning  
✅ NLP preprocessing pipeline  
✅ FastAPI backend inference API  
✅ Streamlit interactive frontend  
✅ SQLite prediction logging  
✅ Real-time monitoring dashboard  
✅ Pie chart & bar chart analytics  
✅ Delete prediction history feature  
✅ Dockerized application  
✅ Ready for cloud deployment  

---

# 🧠 Machine Learning Pipeline

Model dibangun menggunakan:

- Python
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Natural Language Processing (NLP)

Tahapan pipeline:

1. Data Cleaning
2. Text Preprocessing
3. Feature Extraction (TF-IDF)
4. Model Training
5. Model Evaluation
6. API Deployment

---

# 📂 Project Structure

```text
tweet-classification/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── model.pkl
│   ├── tfidf.pkl
│   └── label_mapping.pkl
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── ml/
│   ├── notebook.ipynb
│   └── dataset/
│
├── docker-compose.yml
│
└── README.md
```

---

# ⚙️ Local Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/tweet-classification.git
```

---

## 2. Masuk ke Project

```bash
cd tweet-classification
```

---

# 🐍 Create Virtual Environment (venv)

## Mac/Linux

```bash
python3 -m venv venv
```

Aktifkan venv:

```bash
source venv/bin/activate
```

---

## Windows

```bash
python -m venv venv
```

Aktifkan venv:

```bash
venv\\Scripts\\activate
```

---

# 📦 Install Dependencies

## Backend

Masuk ke folder backend:

```bash
cd backend
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

## Frontend

Buka terminal baru lalu masuk ke folder frontend:

```bash
cd frontend
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application Manually

## Run Backend

Masuk ke folder backend:

```bash
cd backend
```

Jalankan FastAPI:

```bash
uvicorn main:app --reload
```

Backend akan berjalan di:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

## Run Frontend

Masuk ke folder frontend:

```bash
cd frontend
```

Jalankan Streamlit:

```bash
streamlit run app.py
```

Frontend akan berjalan di:

```text
http://localhost:8501
```

---

# 🐳 Run Using Docker

## Jalankan Application

Di root project:

```bash
docker compose up --build
```

---

# 🌐 Access Application

## Frontend

```text
http://localhost:8501
```

## Backend API Docs

```text
http://localhost:8000/docs
```

---

# 🧪 API Example

## POST /predict

### Request

```json
{
  "tweet": "I love football"
}
```

---

### Response

```json
{
  "tweet": "I love football",
  "prediction_label": "sports",
  "prediction_code": 2
}
```

---

# 📊 Dashboard Features

- Real-time prediction monitoring
- Pie chart distribution
- Bar chart analytics
- Prediction logs
- Delete history feature

---

# 🗄️ Database

Aplikasi menggunakan SQLite untuk menyimpan:

- Tweet input
- Prediction label
- Timestamp

Database digunakan untuk:

- Monitoring dashboard
- Prediction history
- Data analytics

---

# ☁️ Deployment

## Backend Deployment (Render)

1. Push project ke GitHub
2. Login ke Render
3. Create New Web Service
4. Connect GitHub repository
5. Set Root Directory menjadi:

```text
backend
```

6. Deploy

---

## Frontend Deployment (Streamlit Cloud)

1. Push project ke GitHub
2. Login ke Streamlit Community Cloud
3. Create New App
4. Pilih:

```text
frontend/app.py
```

5. Deploy

---

# 🛠️ Technologies Used

| Technology | Usage |
|---|---|
| Python | Main Programming Language |
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| Scikit-learn | Machine Learning |
| SQLite | Database |
| Docker | Containerization |
| GitHub | Version Control |

---

# 📈 Model Evaluation

Model berhasil mencapai accuracy sekitar:

```text
81%
```

menggunakan:
- TF-IDF Vectorization
- Logistic Regression
- NLP preprocessing pipeline

---

# 🔒 Error Handling

API telah menangani berbagai validasi input seperti:

✅ Empty string validation  
✅ Non-string validation  
✅ Maximum character validation  
✅ Graceful HTTP error response  

---

# 👨‍💻 Author

Nama: YOUR_NAME  
Project: Tweet Topic Classification  

---

# 📄 License

This project is for educational purposes.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from collections import Counter
import joblib
import re

from database import SessionLocal, TweetLog

app = FastAPI()

# Load Label Mapping
label_mapping = joblib.load("label_mapping.pkl")

# Load model
model = joblib.load("model.pkl")
tfidf = joblib.load("tfidf.pkl")

# Request schema
class TweetRequest(BaseModel):
    tweet: str

# Cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\{\{.*?\}\}", "", text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Root endpoint
@app.get("/")
def root():
    return {"message": "Tweet Classification API Running 🚀"}

# Predict endpoint
@app.post("/predict")
def predict(request: TweetRequest):

    # VALIDATION
    if not isinstance(request.tweet, str):
        raise HTTPException(status_code=400, detail="Tweet harus string")

    if request.tweet.strip() == "":
        raise HTTPException(status_code=400, detail="Tweet kosong")

    if len(request.tweet) > 10000:
        raise HTTPException(status_code=400, detail="Tweet terlalu panjang")

    # PREPROCESS
    clean = clean_text(request.tweet)
    vector = tfidf.transform([clean])

    # PREDICT
    prediction = model.predict(vector)[0]

    prediction_label = label_mapping[int(prediction)]

    # SAVE TO DB
    db = SessionLocal()

    log = TweetLog(
        text=request.tweet,
        prediction=prediction_label
    )

    db.add(log)
    db.commit()
    db.close()

    return {
        "tweet": request.tweet,
        "prediction_label": prediction_label,
        "prediction_code": int(prediction)
    }

# Get logs endpoint
@app.get("/logs")
def get_logs():

    db = SessionLocal()

    data = db.query(TweetLog)\
        .order_by(TweetLog.id.desc())\
        .limit(100)\
        .all()

    db.close()

    return [
        {
            "id": d.id,
            "tweet": d.text,
            "prediction": d.prediction,
            "created_at": d.created_at
        }
        for d in data
    ]

# Statistics endpoint
@app.get("/stats")
def get_stats():

    db = SessionLocal()

    data = db.query(TweetLog).all()

    db.close()

    labels = [d.prediction for d in data]

    counter = Counter(labels)

    return counter

# Delete history endpoint
@app.delete("/logs")
def delete_logs():

    db = SessionLocal()

    db.query(TweetLog).delete()

    db.commit()
    db.close()

    return {
        "message": "Semua riwayat berhasil dihapus"
    }
from fastapi import FastAPI

app = FastAPI(title="Log Intelligence & Anomaly Detection System")

@app.get("/")
def health_check():
    return {"status": "running"}

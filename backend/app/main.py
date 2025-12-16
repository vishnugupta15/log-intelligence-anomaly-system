from fastapi import FastAPI
from pydantic import BaseModel

from database import engine, SessionLocal, Base
from models import Log
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

class LogRequest(BaseModel):
    service: str
    level: str
    message: str

@app.post("/logs")
def ingest_log(log: LogRequest):
    db = SessionLocal()
    try:
        db_log = Log(
            service=log.service,
            level=log.level,
            message=log.message
        )
        db.add(db_log)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

    return {"status": "saved"}


@app.get("/logs")
def get_logs(limit: int = 10):
    db = SessionLocal()
    logs = db.query(Log).limit(limit).all()
    db.close()

    result = []
    for log in logs:
        result.append({
            "id": log.id,
            "service": log.service,
            "level": log.level,
            "message": log.message
        })

    return result
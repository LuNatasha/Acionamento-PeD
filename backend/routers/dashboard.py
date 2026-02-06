from fastapi import APIRouter
from sqlalchemy import func
from datetime import date
from database import SessionLocal, Resposta

router = APIRouter()

@router.get("/api/dashboard")
def dashboard():
    db = SessionLocal()
    try:
        total = db.query(Resposta).count()

        urgentes = db.query(Resposta)\
            .filter(Resposta.prioridade == "URGENTE (LINHA PARADA)")\
            .count()

        normais = db.query(Resposta)\
            .filter(Resposta.prioridade == "NORMAL")\
            .count()

        ultimo = db.query(Resposta)\
            .order_by(Resposta.id.desc())\
            .first()

        return {
            "total": total,
            "urgentes": urgentes,
            "normais": normais,
            "ultimo_chamado": {
                "motivo": ultimo.motivo if ultimo else None
            }
        }
    finally:
        db.close()
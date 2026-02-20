from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.database import SessionLocal, Resposta
from datetime import datetime

router = APIRouter()

@router.get("/api/dashboard")
def obter_dashboard():
    db: Session = SessionLocal()

    hoje = datetime.now().strftime("%d/%m/%Y")

    # totais GERAL
    total = db.query(Resposta).count()
    urgentes = db.query(Resposta).filter(Resposta.prioridade == "URGENTE (LINHA PARADA)").count()
    normais = db.query(Resposta).filter(Resposta.prioridade == "NORMAL").count()

    # ultimo chamado
    ultimo = db.query(Resposta).order_by(Resposta.id.desc()).first()

    if ultimo:
        ultimo_chamado = {
            "segmento": ultimo.segmento or "-",
            "motivo": ultimo.motivo or "-",
            "data_hora": ultimo.data_abertura or "-"
        }
    else:
        ultimo_chamado = {"segmento": "-", "motivo": "-", "data_hora": "-"}

    # Filtra por HOJE usando LIKE no campo data_abertura (formato dd/mm/yyyy HH:MM)
    registros_hoje = db.query(Resposta).filter(
        Resposta.data_abertura.like(f"{hoje}%")
    ).all()

    # SEGMENTO hoje
    segmentos = {}
    for r in registros_hoje:
        if r.segmento:
            segmentos[r.segmento] = segmentos.get(r.segmento, 0) + 1

    # MOTIVO hoje
    motivos = {}
    for r in registros_hoje:
        if r.motivo:
            motivos[r.motivo] = motivos.get(r.motivo, 0) + 1

    # TURNO hoje
    turnos = {}
    for r in registros_hoje:
        if r.turno:
            turnos[r.turno] = turnos.get(r.turno, 0) + 1

    db.close()

    return {
        "total": total,
        "urgentes": urgentes,
        "normais": normais,
        "ultimo_chamado": ultimo_chamado,
        "segmentos": segmentos,
        "motivos": motivos,
        "turnos": turnos
    }
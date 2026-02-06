from fastapi import APIRouter
from pydantic import BaseModel
from database import SessionLocal, Resposta

router = APIRouter()

class RespostaSchema(BaseModel):
    segmento: str
    linha: str
    posto: str
    manutencao: str
    motivo: str
    descricao: str
    prioridade: str
    turno: str
    executor: str

@router.post("/api/respostas")
def receber_resposta(resposta: RespostaSchema):
    db = SessionLocal()
    try:
        novo = Resposta(
            segmento=resposta.segmento,
            linha=resposta.linha,
            posto=resposta.posto,
            manutencao=resposta.manutencao,
            motivo=resposta.motivo,
            descricao=resposta.descricao,
            prioridade=resposta.prioridade,
            turno=resposta.turno,
            executor=resposta.executor
        )
        db.add(novo)
        db.commit()
        return {"status": "ok", "mensagem": "Resposta salva com sucesso"}
    finally:
        db.close()
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Resposta(Base):
    __tablename__ = "respostas"

    id = Column(Integer, primary_key=True, index=True)
    segmento = Column(String)
    linha = Column(String)
    posto = Column(String)
    manutencao = Column(String)
    motivo = Column(String)
    descricao = Column(String)
    prioridade = Column(String)
    turno = Column(String)
    executor = Column(String)

Base.metadata.create_all(bind=engine)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import respostas, dashboard

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# registrar rotas
app.include_router(respostas.router)
app.include_router(dashboard.router)
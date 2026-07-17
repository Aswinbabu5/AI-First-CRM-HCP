from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import agent, hcp, interaction

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ai Powered CRM_HCP_Module",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
    "https://ai-first-crm-hcp-nlb1.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent.router)
app.include_router(hcp.router)
app.include_router(interaction.router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
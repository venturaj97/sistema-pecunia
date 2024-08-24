from fastapi import FastAPI
from app.api.routes import router 

app = FastAPI()

# Incluindo o router com as rotas
app.include_router(router)

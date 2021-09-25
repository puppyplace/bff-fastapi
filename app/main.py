from fastapi import FastAPI

from src.routers.router import router

# instancia do fastapi
app = FastAPI()

#inicio das rotas
router(app)

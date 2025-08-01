from fastapi import FastAPI
from .routes import propiedades, users
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(propiedades.router)
app.include_router(users.router)

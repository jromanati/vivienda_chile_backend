from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database
from .users import get_current_user

router = APIRouter(
    prefix="/propiedades",
    tags=["propiedades"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Propiedad)
def crear_propiedad(
    propiedad: schemas.PropiedadCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    return crud.crear_propiedad(db, propiedad)

@router.get("/", response_model=list[schemas.Propiedad])
def listar_propiedades(
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    return crud.obtener_propiedades(db)

@router.delete("/{propiedad_id}")
def eliminar_propiedad(
    propiedad_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(get_current_user)
):
    crud.eliminar_propiedad(db, propiedad_id)
    return {"ok": True}

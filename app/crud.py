from sqlalchemy.orm import Session
from . import models, schemas, auth

def crear_propiedad(db: Session, propiedad: schemas.PropiedadCreate):
    db_propiedad = models.Propiedad(**propiedad.dict())
    db.add(db_propiedad)
    db.commit()
    db.refresh(db_propiedad)
    return db_propiedad

def obtener_propiedades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Propiedad).offset(skip).limit(limit).all()

def obtener_propiedad(db: Session, propiedad_id: int):
    return db.query(models.Propiedad).filter(models.Propiedad.id == propiedad_id).first()

def eliminar_propiedad(db: Session, propiedad_id: int):
    db.query(models.Propiedad).filter(models.Propiedad.id == propiedad_id).delete()
    db.commit()

# ---- Usuario ----
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not auth.verify_password(password, user.hashed_password):
        return None
    return user

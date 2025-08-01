from pydantic import BaseModel, EmailStr
from typing import Optional

class PropiedadBase(BaseModel):
    titulo: str
    descripcion: str
    imagen_url: str
    video_url: str | None = None
    activa: bool = True

class PropiedadCreate(PropiedadBase):
    pass

class Propiedad(PropiedadBase):
    id: int

    class Config:
        orm_mode = True

# ------ Usuarios ------
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    class Config:
        orm_mode = True

# ------ Autenticación ------
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# create_superuser.py
from app.database import SessionLocal
from app.crud import get_user_by_email, create_user
from app.schemas import UserCreate

db = SessionLocal()
email = "admin_jose@ejemplo.com"
pw = "tu_password_segura"

# Si no existe, lo creamos
user = get_user_by_email(db, email)
if not user:
    user = create_user(db, UserCreate(email=email, password=pw))

# Lo promovemos
user.is_superuser = True
db.commit()
print(f"Superuser creado/promovido: {user.email}")

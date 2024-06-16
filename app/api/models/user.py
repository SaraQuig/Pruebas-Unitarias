from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)

# Crear una nueva instancia de usuario SQLAlchemy
db_user = UserModel(username=user.username, email=user.email, age=user.age)
db.add(db_user) # Añadir el usuario a la sesión
db.commit() # Confirmar la sesión para guardar el usuario en la base de datos

# Eliminar un usuario por id
db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
if db_user is None: raise APIException(status_code=404, detail="User not found")
db.delete(db_user) # Eliminar el usuario de la sesión
db.commit() # Confirmar la sesión para eliminar el usuario de la base de datos

# Actualizar el usuario por id
db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
if db_user is None: raise APIException(status_code=404, detail="User not found")
# Actualizar los campos que necesite actualizar, por ejemplo:
db_user.username = "some_new_username"
# Confirmar la sesión para guardar los cambios en la base de datos
db.commit()

# Obtener todos los usuarios con más de 18 años de edad
users = db.query(UserModel).filter(UserModel.age > 18).all()
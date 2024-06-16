from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .models import User as UserModel
from .database import get_db
from .utils import APIException
from pydantic import BaseModel, EmailStr

router = APIRouter()

# Los serializadores se utilizan para validar el cuerpo de la solicitud entrante
# Aquí se determina qué campos son obligatorios y sus tipos
class CreateSerializer(BaseModel):
    password: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    is_active: bool

# Los serializadores también se utilizan para dar formato al cuerpo de la respuesta saliente
class UserSmallSerializer(BaseModel):
    email: str
    is_active: bool

    class Config:
        from_attributes = True

@router.get("/users/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(UserModel).offset(skip).limit(limit).all()
    return [UserSmallSerializer.model_validate(user) for user in users]

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise APIException(status_code=404, detail="User not found")
    return UserSmallSerializer.model_validate(user)

@router.post("/users/")
def create_user(user: CreateSerializer, db: Session = Depends(get_db)):
    db_user = UserModel(username=user.username, email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserSmallSerializer.model_validate(db_user)

@router.put("/users/{user_id}", response_model=UserSmallSerializer)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise APIException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return UserSmallSerializer.model_validate(db_user)

@router.delete("/users/{user_id}", response_model=UserSmallSerializer)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise APIException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return UserSmallSerializer.model_validate(db_user)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from app.database import get_db
from app.models import Product as ProductModel

router = APIRouter()

# Serializadores
class ProductCreateSerializer(BaseModel):
    name_pro: str
    descrip_pro: str
    cant: int
    precio: float
    oferta: bool

class ProductUpdateSerializer(BaseModel):
    name_pro: str = None
    descrip_pro: str = None
    cant: int = None
    precio: float = None
    oferta: bool = None

class ProductSmallSerializer(BaseModel):
    id_pro: int
    name_pro: str
    descrip_pro: str
    cant: int
    precio: float
    oferta: bool

    class Config:
        orm_mode = True

# Endpoints
@router.get("/products/", response_model=List[ProductSmallSerializer])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(ProductModel).offset(skip).limit(limit).all()
    return products

@router.get("/products/{product_id}", response_model=ProductSmallSerializer)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id_pro == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=ProductSmallSerializer)
def create_product(product: ProductCreateSerializer, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.put("/products/{product_id}", response_model=ProductSmallSerializer)
def update_product(product_id: int, product: ProductUpdateSerializer, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id_pro == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/products/{product_id}", response_model=ProductSmallSerializer)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id_pro == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return db_product

from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id_pro = Column(Integer, primary_key=True, index=True)
    name_pro = Column(String, index=True)
    descrip_pro = Column(String)
    cant = Column(Integer)
    precio = Column(Float)
    oferta = Column(Boolean)

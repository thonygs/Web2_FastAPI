from sqlalchemy import Column, Integer, String
from db.database import Base

# Modelo do banco de dados
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
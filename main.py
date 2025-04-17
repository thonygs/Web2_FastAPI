from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from db.database import criar_banco, get_db
from db.models import Item

criar_banco()

# Instância do FastAPI
app = FastAPI()

# Rota para criar um novo item
@app.post("/items/")
def criar_item(nome: str, descricao: str, db: Session = Depends(get_db)):
    new_item = Item(nome=nome, descricao=descricao)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Item criado com sucesso!", "item": {"id": new_item.id, "nome": new_item.nome, "descricao": new_item.descricao}}

# Rota para obter todos os itens
@app.get("/items/")
def listar_itens(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return {"items": items}

# Rota para obter um item pelo ID
@app.get("/items/{item_id}")
def buscar_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"id": item.id, "nome": item.nome, "descricao": item.descricao}
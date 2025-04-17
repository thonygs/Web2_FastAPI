# Guia de Configuração e Execução do Projeto

## Criação de Ambiente Virtual
```bash
python -m venv .venv
```

## Instalar FastAPI e Uvicorn
```bash
pip install fastapi uvicorn
```

## Instalar ORM
```bash
pip install sqlalchemy
```

## Ativar o Ambiente Virtual
### Windows
```bash
.venv\Scripts\activate
```

### Linux
```bash
source .venv/bin/activate
```

## Executar Código
```bash
uvicorn main:app --reload
```

---

**Autor:** Anthony Silva

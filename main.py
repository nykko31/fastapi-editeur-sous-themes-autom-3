from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modèle de données pour recevoir la liste des sous-thèmes
class SousThemesInput(BaseModel):
    items: list[str]

# 1) Endpoint pour recevoir la liste des sous-thèmes depuis n8n
@app.post("/edit")
def edit_sous_themes(payload: SousThemesInput):
    return {
        "status": "received",
        "count": len(payload.items),
        "items": payload.items
    }

# 2) Endpoint pour vérifier que l’API fonctionne
@app.get("/")
def ping():
    return {"status": "ok", "message": "FastAPI ready"}

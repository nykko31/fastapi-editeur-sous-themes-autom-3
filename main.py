from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modèle de données pour recevoir la liste des sous-thèmes
class SousThemesInput(BaseModel):
    items: list[str]

# 1) Endpoint pour recevoir la liste des sous-thèmes depuis n8n
@app.post("/edit")
def edit_sous_themes(payload: SousThemesInput):
    # ICI tu modifies les sous-thèmes comme tu veux
    edited_items = [item.upper() for item in payload.items]  # exemple : transformation de chaque sous-thème en majuscule

    return {
        "status": "edited",
        "original_count": len(payload.items),
        "new_items": edited_items
    }

# 2) Endpoint pour vérifier que l’API fonctionne
@app.get("/")
def ping():
    return {"status": "ok", "message": "FastAPI ready"}

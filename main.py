from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Correcteur CP1-Terminale", version="1.0")

# Autorise les requêtes depuis ton app mobile/web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/corriger")
async def corriger(
    niveau: str = Form(...),  # Ex: CP1, CE2, 6eme, Terminale C, D, A
    matiere: str = Form(...), # Ex: Maths, Français, Physique, SVT
    file: UploadFile = None   # Photo ou PDF de la copie
):
    """
    K(p)=1 : Corrige une copie du CP1 à la Terminale.
    Tu mettras ton vrai algo IA ici plus tard.
    """
    # TODO: Remplacer par ton vrai calcul de note
    note = 14.5
    commentaire = f"Copie {niveau} en {matiere}. K(p)=1. Bonne démarche. Revoir calcul Q3."
    
    return {ss
        "niveau": niveau,
        "matiere": matiere,
        "note": f"{note}/20",
        "commentaire": commentaire,
        "K(p)": 1
    }

@app.get("/")
def home():
    return {"status": "Correcteur CP1-Terminale Live", "K(p)": 1}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
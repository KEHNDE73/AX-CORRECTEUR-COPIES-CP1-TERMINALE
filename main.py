from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import PyPDF2
import io

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
BAREME_CP1_MATHS = ["théorème", "démonstration", "hypothèse", "conclusion", "donc"]

@app.get("/", response_class=HTMLResponse)
def page_accueil():
    html = "<html><head><title>Ax-KEHNDE - Arbitre Numerique Instantane CP1-Terminale CI</title>"
    html += "<meta name='description' content='Correction automatique CP1-Terminale. Note instantanee K(p)=1. Par Dr KEHNDE73.'></head>"
    html += "<body><h1>Ax-KEHNDE Arbitre Numerique K(p)=1</h1>"
    html += "<p>API correction instantanee education ivoirienne.</p>"
    html += "<p>Endpoint: POST /arbitrer - Upload PDF pour note immediate</p></body></html>"
    return html

@app.get("/status")
def read_status():
    return {"message": "Ax-KEHNDE ARBITRE NUMERIQUE V1", "K(p)": 1}

@app.post("/arbitrer")
async def arbitrer_copie(file: UploadFile = File(...)):
    content = await file.read()
    texte = ""
    try:
        pdf = PyPDF2.PdfReader(io.BytesIO(content))
        for page in pdf.pages:
            texte += page.extract_text()
    except:
        return {"erreur": "PDF illisible", "K(p)": 0}
    score = 0
    mots_trouves = []
    for mot in BAREME_CP1_MATHS:
        if mot.lower() in texte.lower():
            score += 4
            mots_trouves.append(mot)
    note = min(20, score)
    kp = 1 if note >= 10 else 0
    commentaire = f"Copie {file.filename}: {len(mots_trouves)}/5 mots-cles. "
    commentaire += "Raisonnement structure K(p)=1." if kp == 1 else "Structure a renforcer K(p)=0."
    return {"filename": file.filename, "note": f"{note}/20", "K(p)": kp, "mots_cles_detectes": mots_trouves, "commentaire": commentaire, "arbitre": "Ax-KEHNDE V1"}

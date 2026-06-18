from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
import json
from typing import Optional

from app.nlp import recognize_intent


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    intent: str
    confidence: float


app = FastAPI(title="University Chatbot")

# Allow the simple static UI to call the API during local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static UI from / (optional)
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/", StaticFiles(directory=str(static_dir), html=True), name="static")

INTENTS_PATH = Path(__file__).parent / "intents.json"
with open(INTENTS_PATH, "r", encoding="utf-8") as fh:
    INTENTS = json.load(fh)

DB_PATH = Path(__file__).parent / 'data' / 'university_db.json'
with open(DB_PATH, 'r', encoding='utf-8') as fh:
    UNIVERSITY_DB = json.load(fh)

# Simple in-memory session store for demo purposes (resume-friendly feature)
SESSIONS: dict[str, list[dict]] = {}


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    intent, confidence = recognize_intent(req.message)
    intent_def = INTENTS.get(intent) or INTENTS.get("fallback")
    reply = intent_def["responses"][0]

    # save short history for session-aware responses (demo only)
    if req.session_id:
        hist = SESSIONS.setdefault(req.session_id, [])
        hist.append({"message": req.message, "intent": intent})

    resp = {"reply": reply, "intent": intent, "confidence": confidence}
    if intent == 'admissions':
        resp['data'] = {'university': UNIVERSITY_DB}

    return resp

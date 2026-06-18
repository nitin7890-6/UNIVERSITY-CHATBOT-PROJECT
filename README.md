
# AI-Powered Chandigarh University Chatbot

An intelligent chatbot tailored for Chandigarh University to automate student queries regarding admissions, examinations, fees, and academics.

Features
- Intent recognition (NLP-based, pluggable)
- Context-aware responses (session-aware placeholder)
- Simple FastAPI backend for integration

Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the API server:

```bash
uvicorn app.main:app --reload --port 8000
```

3. Send a POST to `/chat` with JSON `{ "message": "your question", "session_id": "optional" }`.

Examples
- Admissions: "How do I apply to Chandigarh University?"
- Exams: "When are final exams scheduled at CU?"
- Fees: "How can I pay my Chandigarh University tuition?"
- Academics: "What courses are required for B.Tech Computer Science at CU?"

Next steps
- Replace the rule-based recognizer with a trained model (spaCy / transformers / Rasa)
- Add conversational memory and a small DB for sessions
- Add a web UI or integrate with messaging platforms (MS Teams, Slack, WhatsApp)
 
Containerized

Build and run with Docker:

```bash
docker build -t university-chatbot .
docker run -p 8000:8000 university-chatbot
```

Or with docker-compose:

```bash
docker-compose up --build
```

Demo UI

Open http://localhost:8000/ to use the simple demo UI.

Resume-ready summary

Implemented an AI-powered Chandigarh University Chatbot with:

- A FastAPI backend (Flask fallback for compatibility) and REST `/chat` endpoint.
- A pluggable NLP recognizer (keyword-based; easy to replace with spaCy/transformers).
- Branded Bootstrap demo UI with session demo and intent/confidence display.
- Optional Redis-backed session persistence for production-like deployments.
- Containerization via `Dockerfile` and `docker-compose` (includes Redis service).
- CI workflow (GitHub Actions) that runs tests on push/PR.

This repo is resume-ready: easy to deploy, test, and extend.

┌───────────────────────────────────────────────────────────────────────────────────┐
│                                1. CLIENT LAYER                                    │
│                                                                                   │
│    Web Browser / Mobile Device                                                    │
│    └─► Loads HTML5/CSS3/JavaScript UI from GitHub Pages                           │
│        [https://krishnegowda9.github.io/spacy-chatbot/]                           │
└────────────────────────────────────────┬──────────────────────────────────────────┘
│
│  HTTP POST /chat
│  Payload: {"message": "hi"}
▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                                2. BACKEND API LAYER                               │
│                                                                                   │
│    Render Cloud Infrastructure (Docker Container)                                 │
│    └─► FastAPI Application + CORS Middleware                                      │
│        [https://spacy-chatbot-app-latest.onrender.com]                            │
└────────────────────────────────────────┬──────────────────────────────────────────┘
│
│  Process Raw Text
▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                                3. NLP & INTENT ENGINE                             │
│                                                                                   │
│    spaCy Pipeline (en_core_web_sm)                                                │
│    ├─► Tokenization & Lemmatization                                               │
│    ├─► Stop-word Filtering                                                        │
│    └─► Pattern Matching & Entity Extraction                                       │
│                                                                                   │
│    Intent Matcher                                                                 │
│    ├─► Match found ──► Return specific response (e.g. "Hi there!")                │
│    └─► No match   ──► Return fallback response                                    │
└────────────────────────────────────────┬──────────────────────────────────────────┘
│
│  JSON Response: {"response": "Hi there!"}
▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                                4. USER INTERFACE                                  │
│                                                                                   │
│    JavaScript Fetch API receives payload and appends response to chat UI          │
└───────────────────────────────────────────────────────────────────────────────────┘

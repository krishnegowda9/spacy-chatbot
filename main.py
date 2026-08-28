import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy

app = FastAPI(title="spaCy Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp = spacy.load("en_core_web_sm")

intents = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "greetings"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    },
    "damodar_info": {
        "keywords": [
            "damodar",
            "dhamodhar",
            "damodar sir",
            "dhamodhar sir",
            "who is damodar sir",
            "who is dhamodhar sir",
            "who is damodar",
        ],
        "responses": ["He is a great teacher."],
    },
    "uta_query": {
        "keywords": ["uta aytha", "uta ayta", "uta", "oota aytha"],
        "responses": ["Hu aythu Nimdu"],
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see", "later", "exit", "quit"],
        "responses": ["Goodbye!", "See you later!", "Bye! Take care."],
    },
    "thanks": {
        "keywords": ["thank", "thanks", "appreciate"],
        "responses": [
            "You're welcome!",
            "No problem!",
            "Glad I could help!",
        ],
    },
}

fallback_responses = [
    "I'm not sure I understand. Can you rephrase that?",
    "I didn't quite catch that.",
]


class ChatRequest(BaseModel):
    message: str


def process_text(text: str):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    lemmas = [
        token.lemma_.lower()
        for token in doc
        if not token.is_punct and not token.is_space
    ]
    pos_tags = [(token.text, token.pos_) for token in doc]
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return tokens, lemmas, pos_tags, entities


def get_intent(user_message: str, lemmas: list):
    clean_message = user_message.lower().strip()

    for intent, data in intents.items():
        for keyword in data["keywords"]:
            kw = keyword.lower().strip()
            # Direct phrase match for multi-word queries
            if kw in clean_message:
                return intent
            # Keyword match against spaCy lemmas
            if kw in [l.lower() for l in lemmas]:
                return intent
    return None


@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    tokens, lemmas, pos_tags, entities = process_text(request.message)
    intent = get_intent(request.message, lemmas)

    if intent and intent in intents:
        bot_response = random.choice(intents[intent]["responses"])
    else:
        bot_response = random.choice(fallback_responses)

    return {
        "user_message": request.message,
        "response": bot_response,
        "intent": intent,
        "tokens": tokens,
        "lemmas": lemmas,
        "pos_tags": pos_tags,
        "entities": entities,
    }
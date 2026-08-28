import random
import spacy

nlp = spacy.load("en_core_web_sm")

# Store conversation state
user_data = {}

intents = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "greetings"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"],
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


def process_text(text):
    """Process text using spaCy for tokens, lemmas, POS tags, and entities."""
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


def chatbot_response(user_input):
    tokens, lemmas, pos_tags, entities = process_text(user_input)

    # 1. Extract Person Name using NER
    for ent_text, ent_label in entities:
        if ent_label == "PERSON":
            user_data["name"] = ent_text
            return f"SpacyBot: Nice to meet you, {ent_text}!"

    # 2. Check for Intent Keywords
    for intent, data in intents.items():
        for keyword in data["keywords"]:
            if keyword in lemmas:
                # Personalize greeting if name is known
                if intent == "greeting" and "name" in user_data:
                    return f"SpacyBot: Hello again, {user_data['name']}!"
                return f"SpacyBot: {random.choice(data['responses'])}"

    return "SpacyBot: I didn't quite catch that. Can you rephrase?"


def run_chat():
    print(
        "SpacyBot: Hi! I'm a chatbot powered by spaCy. Type 'bye' to exit.\n"
    )
    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue

        response = chatbot_response(user_input)
        print(f"{response}\n")

        # Check for exit commands
        doc = nlp(user_input)
        lemmas = [token.lemma_.lower() for token in doc]
        if any(word in lemmas for word in ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    run_chat()
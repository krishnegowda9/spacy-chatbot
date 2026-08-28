# 🤖 spaCy Conversational AI Chatbot

A lightweight, end-to-end web application that leverages **spaCy Natural Language Processing (NLP)** to classify user intents and return real-time responses through a **FastAPI** REST interface. The application is containerized with **Docker**, hosted on **Render**, and served globally via **GitHub Pages**.

---

## 🌐 Live Application Links

- **Frontend Interface (Live Chatbot):** [https://krishnegowda9.github.io/spacy-chatbot/](https://krishnegowda9.github.io/spacy-chatbot/)
- **Backend API Service:** [https://spacy-chatbot-app-latest.onrender.com](https://spacy-chatbot-app-latest.onrender.com)
- **Source Code Repository:** [https://github.com/krishnegowda9/spacy-chatbot](https://github.com/krishnegowda9/spacy-chatbot)

---

## 🏗️ System Architecture & Workflow
---

## 🔄 End-to-End Processing Flow

1. **User Input:** A user enters a query (e.g., *"Who is damodar sir"*) into the web client hosted on GitHub Pages.
2. **API Request:** The client triggers an asynchronous `fetch()` POST request carrying the user message in JSON format to the FastAPI endpoint on Render.
3. **NLP Processing:** 
   - FastAPI receives the payload and passes the raw text into the **spaCy NLP model** (`en_core_web_sm`).
   - Text is normalized (converted to lowercase, cleaned, and tokenized).
   - The engine checks tokens against predefined intent patterns.
4. **Response Generation:** The matched response string is wrapped inside a JSON dictionary and returned across the HTTP channel.
5. **UI Rendering:** The frontend JavaScript parses the JSON response and updates the chat interface dynamically.

---

## 🛠️ Tech Stack & Key Components

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **NLP Framework** | **spaCy** (`en_core_web_sm`) | Text processing, tokenization, intent matching |
| **Backend Framework** | **FastAPI** + **Uvicorn** | High-performance asynchronous REST API |
| **Frontend** | **HTML5**, **CSS3**, **JavaScript** | Responsive user interface using asynchronous Fetch API |
| **Containerization** | **Docker** & **Docker Hub** | Packaging application dependencies into an immutable image |
| **Cloud Hosting** | **Render Platform** | Running the Dockerized FastAPI service in the cloud |
| **Static Hosting** | **GitHub Pages** | Serving the global user frontend |

---

## 🚀 Local Development Setup

### 1. Clone Repository
```bash
git clone [https://github.com/krishnegowda9/spacy-chatbot.git](https://github.com/krishnegowda9/spacy-chatbot.git)
cd spacy-chatbot
2. Set Up Virtual Environment
PowerShell
python -m venv venv
.\venv\Scripts\Activate
3. Install Dependencies & spaCy Model
PowerShell
pip install -r requirements.txt
python -m spacy download en_core_web_sm
4. Run API Backend
PowerShell
uvicorn main:app --reload
The local API server will launch at http://127.0.0.1:8000.

5. Launch Frontend
Open index.html directly in your browser or run a simple local web server.

🐳 Docker Deployment Commands
To containerize and test locally using Docker:

PowerShell
# Build Docker Image
docker build -t krishnegowda2005/spacy-chatbot-app:latest .

# Run Container Locally
docker run -p 8000:8000 krishnegowda2005/spacy-chatbot-app:latest

# Push Image to Docker Hub
docker push krishnegowda2005/spacy-chatbot-app:latest


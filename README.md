# 🤖 spaCy AI Chatbot

A lightweight, high-performance web-based conversational AI application built using **spaCy NLP**, **FastAPI**, **Docker**, and deployed live on **Render** and **GitHub Pages**.

This project was developed as part of the college training program led by **Akshay Sir** and **Damodar Sir**.

---

## 🏗️ System Architecture

The project follows a decoupled, cloud-ready microservice architecture:
+-------------------------------------------------------------------------+
|                              FRONTEND                                   |
|                                                                         |
|  GitHub Pages (HTML5 / CSS3 / JavaScript)                               |
|  https://krishnegowda9.github.io/spacy-chatbot/                         |
+-------------------------------------------------------------------------+
|
| HTTP / REST API Request
| (JSON Payload: {"message": "..."})
v
+-------------------------------------------------------------------------+
|                              BACKEND                                    |
|                                                                         |
|  Render Cloud Platform (Dockerized Container)                           |
|  FastAPI + Uvicorn + spaCy NLP Engine                                   |
|  https://spacy-chatbot-app-latest.onrender.com                         |
+-------------------------------------------------------------------------+
### **Architecture Breakdown:**
1. **Frontend Layer:** Hosted on **GitHub Pages**, providing a responsive UI for user input and rendering real-time chat responses.
2. **REST API Layer:** Built with **FastAPI** to receive user requests asynchronously and return JSON responses.
3. **NLP Engine:** Powered by **spaCy** (`en_core_web_sm`) to process natural language input, match intents, and extract named entities.
4. **Containerization & Deployment:** Packaged into a lightweight **Docker image** (`krishnegowda2005/spacy-chatbot-app:latest`) and automatically hosted on **Render**.

5. ## ✨ Features

- **Intent Recognition:** Uses spaCy NLP tokenization and text analysis to detect user intents (e.g., greetings, info requests, farewells).
- **Live Cloud Deployment:** Accessible globally without local setup.
- **Cross-Origin Resource Sharing (CORS):** Fully configured to allow requests from external web environments.
- **Dockerized:** Ensures consistent runtime execution across local development and production environments.

---
## 🛠️ Tech Stack

- **NLP Framework:** [spaCy](https://spacy.io/)
- **Backend API:** [FastAPI](https://fastapi.tiangolo.com/) + Uvicorn
- **Frontend UI:** HTML5, CSS3, JavaScript (Fetch API)
- **Containerization:** Docker & Docker Hub
- **Cloud Hosting:** Render (Backend API) & GitHub Pages (Frontend UI)

## 🚀 Getting Started Locally

### **1. Clone the Repository**
```bash
git clone [https://github.com/krishnegowda9/spacy-chatbot.git](https://github.com/krishnegowda9/spacy-chatbot.git)
cd spacy-chatbot

2. Set Up Virtual Environment & Install Dependencies
PowerShell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
3. Run Backend API Locally
PowerShell
uvicorn main:app --reload
The API server will run at http://127.0.0.1:8000.

4. Open Frontend
Open index.html in your browser to interact with the chatbot locally.

🐳 Docker Deployment
To build and run using Docker:

PowerShell
# Build image
docker build -t spacy-chatbot-app .

# Run container locally
docker run -p 8000:8000 spacy-chatbot-app

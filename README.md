📘 Wiki Quiz Generator (LLM-Powered)
🚀 Overview
Wiki Quiz Generator is a full‑stack application that accepts a Wikipedia article URL and automatically generates a quiz using a Large Language Model (LLM).

The system:

 Scrapes Wikipedia articles (HTML only, no Wikipedia API)

 Generates quizzes (5–10 MCQs) using Gemini via LangChain

 Stores results in PostgreSQL

 Provides history and quiz replay

 Includes bonus features like Take Quiz mode, URL preview, section‑wise grouping, and caching indicator

✨ Features
Core Features
 Accepts Wikipedia article URL

 Scrapes and cleans article content using BeautifulSoup

 Generates quiz using Gemini (LangChain)

 Each question includes:

Question text

4 options

Correct answer

Difficulty (easy / medium / hard)

Explanation

 Suggests related Wikipedia topics

 Stores all data in PostgreSQL

 History tab to view past quizzes

 Modal view for quiz details

Bonus Features
 Take Quiz mode with scoring and feedback

 URL preview (auto‑fetch article title before generation)

 Section‑wise question grouping

 Caching indicator (detects reused URLs)

 Fully Dockerized backend + database

🏗️ Tech Stack
Backend

FastAPI

SQLAlchemy

PostgreSQL

LangChain

Gemini Pro (Free Tier)

BeautifulSoup

Docker

Frontend

React

Vite

TypeScript

Tailwind CSS

📂 Project Structure
Code
wiki-quiz/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── scraper.py
│   │   ├── llm.py
│   │   ├── prompts.py
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   └── wiki-quiz-frontend/
│
├── sample_data/
│   ├── urls.txt
│   └── alan_turing.json
│
├── docker-compose.yml
└── README.md
⚙️ Setup Instructions
1️⃣ Prerequisites
Docker & Docker Compose

Node.js  (v18+)

Gemini API Key

2️⃣ Environment Variables
Create a .env file at project root:

Code
GOOGLE_API_KEY=your_gemini_api_key_here
3️⃣ Run Backend + Database
bash
docker-compose up --build
Backend runs at: http://localhost:8000

Swagger docs: http://localhost:8000/docs

4️⃣ Run Frontend
bash
cd frontend/wiki-quiz-frontend
npm install
npm run dev
Frontend runs at: http://localhost:5173

🔌 API Endpoints
Generate Quiz
http
POST /quiz/generate
Body:

json
{
  "url": "https://en.wikipedia.org/wiki/India"
}
Preview Article Title
http
GET /quiz/preview?url=<wikipedia_url>
History
http
GET /history
Quiz Details
http
GET /quiz/{id}

## 🧠 Prompt Templates Used
The following prompt templates are used to ensure structured, grounded,
and hallucination-minimized LLM outputs.


QUIZ_PROMPT = """
You are an expert quiz creator.

Using ONLY the information from the Wikipedia article below,
generate 5 to 10 multiple-choice questions.

Rules:
- Each question must belong to ONE section from the article
- Section must be chosen from the article headings
- Each question must have exactly 4 options
- Only ONE correct answer
- Difficulty: easy, medium, hard
- Explanation grounded in article text
- Output MUST be valid JSON
- DO NOT add extra text

Wikipedia Article:
{article_text}

Return JSON strictly in this format:
[
  {{
    "section": "",
    "question": "",
    "options": ["", "", "", ""],
    "answer": "",
    "difficulty": "",
    "explanation": ""
  }}
]
"""

RELATED_TOPICS_PROMPT = """
Based ONLY on the Wikipedia article below,
suggest 5 related Wikipedia topics for further reading.

Rules:
- Topics must be relevant
- No explanations
- Output ONLY a JSON array of strings

Wikipedia Article:
{article_text}
"""

🧪 Sample Data
Located in sample_data/:

urls.txt — tested Wikipedia URLs

alan_turing.json — sample API response

## 📸 Screenshots

### Generate Quiz Page
![Generate Quiz Screenshot](docs/generate_quiz.png)

### History Page
![History Screenshot](docs/history_tab.png)
![History Modal Screenshot](docs/history_modal.png)

### Take Quiz Mode
![Take Quiz Screenshot](docs/quiz_score.png)



🙌 Final Note
This project demonstrates:

Full‑stack development

LLM integration

API design

Clean architecture

Product‑oriented thinking
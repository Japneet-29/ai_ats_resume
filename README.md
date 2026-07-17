# ATS Resume Scorer

A web application that analyzes how well a resume matches a job description and provides an ATS score along with actionable feedback. Built with FastAPI and Streamlit, using spaCy for NLP, Jina Embeddings for semantic similarity, and the Groq API for AI-generated recommendations.

## Features

- Upload resumes in **PDF**, **DOC**, or **DOCX** format.
- Compare resumes against any job description.
- Semantic matching between resume content and job requirements using **Jina Embeddings**.
- ATS score with category-wise breakdown:
  - Resume Formatting
  - Keyword Match
  - Content Quality
  - Skill Validation
  - ATS Compatibility
- AI-generated suggestions using **Groq (Llama 3)**.
- User authentication with **Supabase** (Email/Password and Google OAuth).
- Save previous analyses to your account.
- Export analysis reports as PDF.

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI (Python)
- **NLP:** spaCy (`en_core_web_sm`)
- **Semantic Embeddings:** Jina Embeddings API (`jina-embeddings-v3`)
- **LLM:** Groq API (Llama 3)
- **Authentication & Database:** Supabase
- **PDF Report Generation:** WeasyPrint + Jinja2

---

## Project Structure

```text
ATS_SCORER/
├── backend/              FastAPI backend, NLP pipeline, API routes
├── frontend/             Streamlit frontend
├── ml model/             Supporting ML artifacts (if required)
├── requirements.txt      Project dependencies
├── .env.example          Environment variable template
└── README.md
```

> **Note:** The `jupyter notebooks/` directory contains research and experimentation notebooks and is **not required** for running the application. It can be excluded from production deployments.

---

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd ATS_SCORER
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Linux Dependencies (WeasyPrint)

**Ubuntu/Debian**

```bash
sudo apt install -y libcairo2 libpango-1.0-0 libpangoft2-1.0-0 libffi-dev
```

**Fedora**

```bash
sudo dnf install -y cairo pango gdk-pixbuf2 libffi
```

---

### 4. Configure Environment Variables

Copy:

```bash
cp .env.example .env
```

Fill in the following:

- **SUPABASE_URL**
- **SUPABASE_KEY**
- **SUPABASE_ANON_KEY**
- **GROQ_API_KEY**
- **JINA_API_KEY**

If using Google Sign-In, configure Google OAuth in the Supabase Dashboard.

For the Streamlit frontend, create:

```text
frontend/.streamlit/secrets.toml
```

using the provided example and add your Supabase credentials.

---

### 5. Run the Backend

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Backend:

```
http://localhost:8000
```

Swagger Docs:

```
http://localhost:8000/docs
```

---

### 6. Run the Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend:

```
http://localhost:8501
```

---

## Architecture

```
Resume
   │
   ▼
Resume Parser (spaCy)
   │
   ▼
Skill & Experience Extraction
   │
   ▼
Jina Embeddings API
   │
   ▼
Semantic Similarity Scoring
   │
   ▼
ATS Scoring Engine
   │
   ▼
Groq (Llama 3)
   │
   ▼
Personalized Resume Suggestions
```

---

## Deployment

- **Frontend:** Streamlit Community Cloud
- **Backend:** Render
- **Database & Authentication:** Supabase
- **Embedding Service:** Jina AI
- **LLM:** Groq

---

## License

This project is intended for educational and portfolio purposes.
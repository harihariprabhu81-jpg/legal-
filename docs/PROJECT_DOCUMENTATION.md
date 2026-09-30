# LegalEase Project Documentation

## 1. Project Overview
LegalEase is an AI-powered legal document generation application that helps users generate professional legal documents such as employment contracts, NDAs, and lease agreements. The system combines a FastAPI backend with a Streamlit frontend and uses the Gemini API for generation.

## 2. Project Goals
- Generate legal documents from user input
- Offer easy document preview and editing
- Support export to TXT, DOCX, and PDF
- Provide a modern user interface for legal drafting

## 3. Architecture
### Frontend
- Framework: Streamlit
- File: `frontend/app.py`
- Purpose: Collect legal details, submit them to the backend, preview generated output, and download files.

### Backend
- Framework: FastAPI
- File: `legalaseAPI/main.py`
- File: `legalaseAPI/routes.py`
- Purpose: Expose `/generate` endpoint and handle incoming legal document requests.

### AI layer
- File: `ai_core/gemini_generator.py`
- Purpose: Uses Gemini via the Google GenAI client to create legal content from prompt data.

### Configuration
- File: `.env`
- Variable: `GEMINI_API_KEY`

## 4. How It Works
1. The user fills in the document type, parties, terms, and date.
2. The Streamlit app sends a POST request to the FastAPI backend.
3. The backend calls the Gemini generator.
4. The AI generates a legal document.
5. The user can preview, edit, and export the final result.

## 5. File Structure
- `.env` – environment configuration
- `requirements.txt` – Python dependencies
- `ai_core/gemini_generator.py` – AI generation logic
- `legalaseAPI/main.py` – FastAPI app entry point
- `legalaseAPI/routes.py` – API route definitions
- `frontend/app.py` – Streamlit interface
- `docs/` – documentation and output examples

## 6. Setup Instructions
### Install dependencies
```bash
pip install -r requirements.txt
```

### Create environment file
```env
GEMINI_API_KEY=your_api_key_here
```

### Run backend
```bash
python -m uvicorn legalaseAPI.main:app --host 127.0.0.1 --port 8001
```

### Run frontend
```bash
streamlit run frontend/app.py --server.address 127.0.0.1 --server.port 8501
```

## 7. Features
- AI-generated legal document text
- Editable preview panel
- Download as TXT
- Download as DOCX
- Download as PDF
- Dark premium UI theme

## 8. Real Project Notes
- The earlier API key issue was caused by a duplicated value in `.env`.
- The PDF export issue was resolved by wrapping long content before sending it to FPDF.
- The app was successfully running locally on:
  - Frontend: http://127.0.0.1:8503
  - Backend: http://127.0.0.1:8001

## 9. Sample Use Case
This project is ideal for creating quick legal draft documents for:
- employment agreements
- non-disclosure agreements
- freelancer contracts
- rental agreements

## 10. Future Improvements
- add user authentication
- save previous documents in a database
- support multiple languages
- add clause templates and legal review workflow
- improve PDF formatting and styling

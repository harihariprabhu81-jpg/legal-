# LegalEase

LegalEase is an AI-powered legal document generator built with FastAPI and Streamlit. It helps users create professional documents such as employment contracts, NDAs, freelance agreements, and lease agreements using Gemini AI.

## Demo

- Local demo: http://127.0.0.1:8503
- Public demo: deploy using the Render Blueprint below; Render provides the public URL after deployment.

## Project Overview

LegalEase provides a clean interface for entering legal details and generating a structured draft. Users can preview the generated text, make adjustments, and export the result as TXT, DOCX, or PDF.

## Features

- AI-generated legal documents
- Document type selection
- Parties and terms input
- Date entry for contract creation
- Editable preview
- Export to TXT, DOCX, and PDF
- Dark premium UI

## Tech Stack

- Python
- FastAPI
- Streamlit
- Google Gemini API
- FPDF
- python-docx

## Project Structure

```text
LegalEase/
├── .env
├── requirements.txt
├── README.md
├── ai_core/
│   └── gemini_generator.py
├── legalaseAPI/
│   ├── __init__.py
│   ├── main.py
│   └── routes.py
├── frontend/
│   └── app.py
├── render.yaml
├── requirements-render.txt
├── docs/
│   ├── PROJECT_DOCUMENTATION.md
│   └── sample_output.txt
├── 1. Brainstorming & Ideation/
├── 2. Requirement Analysis/
├── 3. Project Design Phase/
├── 4. Project Planning Phase/
├── 5. Project Development Phase/
├── 6. Project Testing/
├── 7. Project Documentation/
├── 8. Project Demonstration/
└── .gitignore
```

## Setup

1. Create a virtual environment
2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Add your Gemini API key in `.env`:

```env
GEMINI_API_KEY=your_key_here
```

4. Run backend:

```bash
python -m uvicorn legalaseAPI.main:app --host 127.0.0.1 --port 8001
```

5. Run frontend:

```bash
streamlit run frontend/app.py --server.address 127.0.0.1 --server.port 8501
```

## Public Deployment (Render)

1. Push this repository to GitHub. Confirm `.env` is not committed; if an API key was ever committed, revoke it and create a new one.
2. In Render, choose **New > Blueprint** and connect this GitHub repository. Render will read `render.yaml` and create the API and Streamlit services.
3. Enter `GEMINI_API_KEY` when prompted for the API service's secret environment variable, then deploy both services.
4. Open the Streamlit service's `onrender.com` URL. The Blueprint configures its API URL from the API service automatically.

The public demo is not live until these deployment steps are completed. Keep API credentials in Render's environment settings, not in source files or GitHub.

## Usage

1. Open the Streamlit app in the browser.
2. Select the document type.
3. Enter parties, terms, and date.
4. Click Generate Legal Document.
5. Preview and export the document.

## Documentation

The project documentation and sample output are available in the `docs` folder.

## Important Notes

- This app requires a valid Gemini API key.
- The project was tested locally and verified to generate documents successfully.

## License

This project is intended for educational and prototype use.

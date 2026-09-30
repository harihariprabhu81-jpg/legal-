import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = (
    os.getenv("GEMINI_API_KEY")
    or os.getenv("GOOGLE_API_KEY")
    or ""
).strip()

if api_key.startswith("GEMINI_API_KEY="):
    api_key = api_key.split("=", 1)[1].strip()

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is missing or empty. Add a valid Google AI Studio API key to the .env file."
    )

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
client = genai.Client(api_key=api_key)


def generate_legal_document(document_type, parties, terms, dates):
    prompt = f"""
You are a legal document drafting assistant.

Generate a professional {document_type}.

Parties:
{parties}

Terms and Conditions:
{terms}

Dates:
{dates}

Create a clear and well-structured document.
Use appropriate headings and clauses.
Do not invent important facts that were not provided.
"""

    try:
        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt,
        )
        return response.text
    except Exception as exc:  # pragma: no cover - runtime API integration error path
        message = str(exc)
        if "401" in message or "UNAUTHENTICATED" in message or "API key" in message.lower():
            raise RuntimeError(
                "Invalid or expired Gemini API key. Update GEMINI_API_KEY in the .env file with a valid Google AI Studio key."
            ) from exc
        if "404" in message or "not found" in message.lower():
            raise RuntimeError(
                f"Unsupported Gemini model '{DEFAULT_MODEL}'. Update GEMINI_MODEL to a valid Gemini model name."
            ) from exc
        raise RuntimeError(f"Gemini generation failed: {message}") from exc
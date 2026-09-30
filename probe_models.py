import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
models = [
    'gemini-1.5-flash',
    'gemini-1.5-pro',
    'gemini-2.0-flash',
    'gemini-2.0-flash-lite',
    'gemini-2.5-flash',
    'gemini-2.5-flash-lite',
    'gemini-2.0-flash-001',
    'gemini-2.0-flash-lite-001',
]

for m in models:
    try:
        resp = client.models.generate_content(model=m, contents='Say hello in one word.')
        text = getattr(resp, 'text', None)
        print('OK', m, '->', text[:80] if text else 'NO_TEXT')
    except Exception as e:
        print('ERR', m, '->', type(e).__name__, str(e)[:600])

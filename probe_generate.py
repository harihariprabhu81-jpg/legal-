import requests

payload = {
    'document_type': 'Employment Contract',
    'parties': 'Acme LLC and Jane Doe',
    'terms': 'Payment of 1000 USD and 30-day review period',
    'dates': '2026-09-30',
}

r = requests.post('http://127.0.0.1:8001/generate', json=payload, timeout=120)
print(r.status_code)
print(r.text[:1500])

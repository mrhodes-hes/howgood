import hashlib, hmac, json, requests

secret = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "",
    "email": "",
    "resume": "",       # URL to your resume
    "location": "",     # e.g. "New York, NY"
    "linkedin": "",
    "codeLink": "",     # URL to the repo/gist containing THIS script
    "yearsPython": 0,
    "yearsDjango": 0,
    "notes": "Hi! First off, I love this application step--it seems like a quick and easy way to get to know potential developers. I'm writing this email as I eat a Chipotle burrito and work on my ",
    "repos": [""]
}

body = json.dumps(payload)
signature = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()

resp = requests.post(
    endpoint,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-HMAC-Signature": signature,
    },
)
print(resp.status_code, resp.json())
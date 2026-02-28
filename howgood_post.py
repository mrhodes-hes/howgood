import hashlib, hmac, json, requests

secret = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "Michael Rhodes",
    "email": "mir333@g.harvard.edu",
    "resume": "https://drive.google.com/file/d/13QNFJFYSAu-9lbBU46lnRht6IXK2p-de/view?usp=sharing",       # URL to your resume
    "location": "Westminster, CO",     # e.g. "New York, NY"
    "linkedin": "https://www.linkedin.com/in/5743rhodesm/",
    "codeLink": "https://github.com/mrhodes-hes/howgood",     # URL to the repo/gist containing THIS script
    "yearsPython": 15,
    "yearsDjango": 10,
    "notes": """Hi! First off, I love this application step--it seems like a quick and easy way to get to know potential developers. 
    I'm writing this note as I eat a Chipotle burrito and am working on one of my assignments for my corporate responsibility course, 
    which made coming across your company's environmental impact report for said burrito feel very apropos. Throughout my career as a software developer 
    and data scientist, I have continually looked for ways to leverage my experience help businesses and organizations become more sustainable. 
    To this end, I would love to learn more about your organization's mission/work, and if there is the potential for us to work together. I look forward 
    to hearing from you!
    
    Additionally, the repo attached to the payload was for a job board project I started many years ago and is not currently active. While it is not the most 
    organized project that I've done, I think it shows my ability to translate business needs into solutions. Please reach to to me at mir333@g.harvard.edu so 
    I can grant you access.""",
    "repos": ["https://github.com/rhodestechnologies/job_board_project"]
}

body = json.dumps(payload)
signature = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()

try:
    resp = requests.post(
        endpoint,
        data=body,
        headers={
            "Content-Type": "application/json",
            "X-HMAC-Signature": signature,
        },
    )
except Exception as e:
    print(e)

print(resp.status_code, resp.json())
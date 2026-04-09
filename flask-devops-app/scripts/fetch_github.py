import requests
repo = "VSUBASHRAJ/CI-CD-Pipeline-for-Flask-Application"
url = f"https://api.github.com/repos/{repo}/commits"
resp = requests.get(url)
commits = resp.json()[:5]
for c in commits:
    print(f"{c['sha'][:7]} - {c['commit']['message']}")
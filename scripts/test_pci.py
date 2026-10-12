import urllib.request, ssl, re, sys
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.pciconcursos.com.br/'
}
url = 'https://www.pciconcursos.com.br/provas/download/agente-administrativo-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

# Procura qualquer coisa com "baixar" ou "download" ou "arquivo"
for line in html.splitlines():
    if any(k in line.lower() for k in ['baixar', 'download', 'pdf', 'arquivo', 'action=', 'form']):
        print(line.strip()[:150])

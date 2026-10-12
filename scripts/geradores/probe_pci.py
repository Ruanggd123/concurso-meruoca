import urllib.request
import ssl
import re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://www.pciconcursos.com.br/provas/download/agente-administrativo-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    
    # Procura trecho ao redor de "Download da Prova" ou "Baixar"
    trechos = re.findall(r'.{0,100}(?:download|baixar|prova|gabarito|arquivo).{0,100}', html, re.IGNORECASE)
    for t in trechos[:10]:
        print("Trecho:", t.strip().replace('\n', ' '))
        
    # Procura scripts JS
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
    for s in scripts:
        if any(w in s for w in ['pdf', 'download', 'location', 'window']):
            print("Script relevante:", s[:200].strip())

import urllib.request
import ssl
import re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://www.inbrasp.org/', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Status: {resp.status}, Tamanho do HTML: {len(html)} bytes")
        links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
        print(f"Total de links na home: {len(links)}")
        for l in set(links):
            if any(k in l.lower() for k in ['meruoca', 'concurso', 'edital', 'pdf', 'arquivo', 'download']):
                print(" -> Link relevante:", l)
except Exception as e:
    print(f"Erro: {e}")

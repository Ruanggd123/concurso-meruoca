import urllib.request, ssl, re, urllib.parse, sys
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.9'
}

paginas = [
    "https://www.inbrasp.org/index.php?menu=concursos",
    "https://www.inbrasp.org/index.php?menu=concursos&acao=concursos1",
    "https://www.inbrasp.org/index.php?menu=concursos&acao=encerrados",
    "https://www.inbrasp.org/"
]

concursos = {}
for pag in paginas:
    try:
        req = urllib.request.Request(pag, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            items = re.findall(r'<a[^>]+href=[\'"]([^\'"]*id=(\d+)[^\'"]*)[\'"][^>]*>(.*?)</a>', html, re.DOTALL)
            for href, cid, text in items:
                clean_text = re.sub(r'<[^>]+>', '', text).strip()
                if clean_text and len(clean_text) > 3:
                    concursos[cid] = clean_text
    except Exception as e:
        print(f"Erro em {pag}: {e}")

print(f"Total de concursos encontrados: {len(concursos)}")
for cid, titulo in sorted(concursos.items(), key=lambda x: int(x[0]), reverse=True):
    print(f"ID {cid}: {titulo}")

print("\nVerificando se há provas/gabaritos dentro de cada certame...")
arquivos_encontrados = []
for cid, titulo in sorted(concursos.items(), key=lambda x: int(x[0]), reverse=True):
    url_concurso = f"https://www.inbrasp.org/index.php?menu=concursos&acao=ver&id={cid}"
    try:
        req = urllib.request.Request(url_concurso, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Busca links para pdfs ou arquivos
            links = re.findall(r'href=[\'"]([^\'"]+[\.a-zA-Z0-9_\-\/% ]+)[\'"]', html)
            for l in set(links):
                l_lower = l.lower()
                if any(k in l_lower for k in ['.pdf', 'prova', 'gabarito', 'caderno']):
                    arquivos_encontrados.append((cid, titulo, l))
                    print(f"  [ID {cid}] {titulo[:30]} -> {l}")
    except Exception as e:
        pass

print(f"\nTotal de arquivos relevantes encontrados: {len(arquivos_encontrados)}")

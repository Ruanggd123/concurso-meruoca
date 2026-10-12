import os
import sys
import re
import urllib.request
import urllib.parse
import urllib.error
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "originais_pdf")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

ssl_context = ssl._create_unverified_context()

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.9',
}

def sanitizar_url(url):
    parsed = urllib.parse.urlsplit(url)
    encoded_path = urllib.parse.quote(parsed.path, safe='/')
    encoded_query = urllib.parse.quote(parsed.query, safe='=&?/')
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, encoded_path, encoded_query, parsed.fragment))

def sanitizar_nome_arquivo(nome):
    # Remove caracteres inválidos no Windows
    return re.sub(r'[\\/*?:"<>|]', '_', nome).strip()

def baixar_arquivo(url, destino):
    url_limpa = sanitizar_url(url)
    req = urllib.request.Request(url_limpa, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=25) as response:
            if response.status == 200:
                conteudo = response.read()
                if conteudo.startswith(b'%PDF') or b'PDF' in conteudo[:200] or len(conteudo) > 1000:
                    with open(destino, 'wb') as f:
                        f.write(conteudo)
                    tamanho_kb = len(conteudo) / 1024
                    print(f"    [SUCESSO] ({tamanho_kb:.1f} KB) -> {os.path.basename(destino)}")
                    return True
                else:
                    return False
    except Exception as e:
        print(f"    [FALHA] {os.path.basename(destino)} -> {e}")
        return False

def crawler_completo_inbrasp():
    print("="*75)
    print(" CRAWLER OFICIAL INBRASP (V2): Baixando TODOS os arquivos com URLs sanitizadas...")
    print("="*75)

    # 1. Obter todos os IDs de concursos
    paginas = [
        "https://www.inbrasp.org/index.php?menu=concursos",
        "https://www.inbrasp.org/index.php?menu=concursos&acao=concursos1",
        "https://www.inbrasp.org/"
    ]
    
    concursos_ids = set()
    for pag in paginas:
        try:
            req = urllib.request.Request(pag, headers=HEADERS)
            with urllib.request.urlopen(req, context=ssl_context, timeout=15) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                ids = re.findall(r'id=(\d+)', html)
                concursos_ids.update(ids)
        except Exception as e:
            print(f"[-] Erro ao listar {pag}: {e}")
            
    print(f"[*] Total de certames identificados: {len(concursos_ids)} concursos.")

    # 2. Varrer cada certame
    arquivos_alvo = {}
    for cid in sorted(concursos_ids, key=int, reverse=True):
        url_concurso = f"https://www.inbrasp.org/index.php?menu=concursos&acao=ver&id={cid}"
        try:
            req = urllib.request.Request(url_concurso, headers=HEADERS)
            with urllib.request.urlopen(req, context=ssl_context, timeout=15) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                
                # Pega todos os links que apontam para arquivos/documentos
                links = re.findall(r'href=[\'"]([^\'"]+[\.a-zA-Z0-9_\-\/% ]+)[\'"]', html)
                for l in links:
                    if any(ext in l.lower() for ext in ['.pdf', 'arquivos/', 'download', 'upload']):
                        if not l.startswith('http'):
                            full_url = "https://www.inbrasp.org/" + l.lstrip('/')
                        else:
                            full_url = l
                            
                        if 'inbrasp.org' in full_url:
                            nome_cru = urllib.parse.unquote(full_url.split('/')[-1].split('?')[0])
                            if not nome_cru.lower().endswith('.pdf'):
                                nome_cru += ".pdf"
                            nome_salvar = sanitizar_nome_arquivo(f"ID_{cid}_{nome_cru}")
                            arquivos_alvo[full_url] = nome_salvar
        except Exception:
            pass

    print(f"\n[*] Total de documentos únicos encontrados no portal: {len(arquivos_alvo)}")
    print("="*75)

    baixados_novos = 0
    ja_existentes = 0

    for url, nome_arquivo in arquivos_alvo.items():
        destino = os.path.join(DOWNLOAD_DIR, nome_arquivo)
        if os.path.exists(destino) and os.path.getsize(destino) > 1000:
            ja_existentes += 1
            continue

        print(f"\n[+] Baixando: {nome_arquivo}")
        if baixar_arquivo(url, destino):
            baixados_novos += 1
        time.sleep(0.2)

    total_final = len([f for f in os.listdir(DOWNLOAD_DIR) if f.lower().endswith('.pdf')])
    print("\n" + "="*75)
    print(f" CONCLUÍDO COM SUCESSO!")
    print(f" • Novos arquivos baixados nesta rodada: {baixados_novos}")
    print(f" • Arquivos já existentes na pasta: {ja_existentes}")
    print(f" • TOTAL DE PDFs OFICIAIS NA PASTA: {total_final}")
    print(f" • Diretório: {DOWNLOAD_DIR}")
    print("="*75)

if __name__ == "__main__":
    crawler_completo_inbrasp()

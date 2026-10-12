import os
import sys
import re
import urllib.request
import urllib.parse
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "originais_pdf", "ibrasp_pci")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

ssl_context = ssl._create_unverified_context()

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://www.pciconcursos.com.br/'
}

URLS_PCI = [
    # Rianápolis 2023
    ("Agente_Administrativo_Rianapolis_2023", "https://www.pciconcursos.com.br/provas/download/agente-administrativo-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023"),
    ("Vigia_Rianapolis_2023", "https://www.pciconcursos.com.br/provas/download/vigia-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023"),
    ("Fiscal_Postura_Rianapolis_2023", "https://www.pciconcursos.com.br/provas/download/fiscal-de-postura-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023"),
    ("Auxiliar_Servicos_Gerais_Rianapolis_2023", "https://www.pciconcursos.com.br/provas/download/auxiliar-de-servicos-gerais-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023"),
    ("Motorista_II_Rianapolis_2023", "https://www.pciconcursos.com.br/provas/download/motorista-ii-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023"),
    ("Fiscal_Meio_Ambiente_Rianapolis_2023", "https://www.pciconcursos.com.br/provas/download/fiscal-de-meio-ambiente-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023"),
    ("Fiscal_Vigilancia_Sanitaria_Rianapolis_2023", "https://www.pciconcursos.com.br/provas/download/fiscal-de-vigilancia-sanitaria-prefeitura-rianapolis-go-ibrasp-consultoria-e-concursos-2023"),
    # Itapaci 2022
    ("Executor_Administrativo_Itapaci_2022", "https://www.pciconcursos.com.br/provas/download/executor-administrativo-prefeitura-itapaci-go-ibrasp-consultoria-e-concursos-2022"),
    ("Porteiro_Servente_Itapaci_2022", "https://www.pciconcursos.com.br/provas/download/porteiro-servente-prefeitura-itapaci-go-ibrasp-consultoria-e-concursos-2022"),
    ("Coletor_Municipal_Itapaci_2022", "https://www.pciconcursos.com.br/provas/download/coletor-municipal-prefeitura-itapaci-go-ibrasp-consultoria-e-concursos-2022"),
    # Ipameri 2021
    ("Auxiliar_Administracao_Ipameri_2021", "https://www.pciconcursos.com.br/provas/download/auxiliar-de-administracao-prefeitura-ipameri-go-ibrasp-consultoria-e-concursos-2021"),
    ("Fiscal_Posturas_Ipameri_2021", "https://www.pciconcursos.com.br/provas/download/fiscal-de-posturas-prefeitura-ipameri-go-ibrasp-consultoria-e-concursos-2021"),
    ("Fiscal_Meio_Ambiente_Ipameri_2021", "https://www.pciconcursos.com.br/provas/download/fiscal-de-meio-ambiente-prefeitura-ipameri-go-ibrasp-consultoria-e-concursos-2021"),
    ("Zelador_Ipameri_2021", "https://www.pciconcursos.com.br/provas/download/zelador-prefeitura-ipameri-go-ibrasp-consultoria-e-concursos-2021"),
    # Água Fria 2018
    ("Fiscal_Ambiental_Agua_Fria_2018", "https://www.pciconcursos.com.br/provas/download/fiscal-ambiental-prefeitura-agua-fria-de-goias-go-ibrasp-consultoria-e-concursos-2018"),
    ("Fiscal_Sanitario_Agua_Fria_2018", "https://www.pciconcursos.com.br/provas/download/fiscal-sanitario-prefeitura-agua-fria-de-goias-go-ibrasp-consultoria-e-concursos-2018"),
    ("Fiscal_Tributos_Agua_Fria_2018", "https://www.pciconcursos.com.br/provas/download/fiscal-de-tributos-prefeitura-agua-fria-de-goias-go-ibrasp-consultoria-e-concursos-2018"),
    ("Vigia_Agua_Fria_2018", "https://www.pciconcursos.com.br/provas/download/vigia-prefeitura-agua-fria-de-goias-go-ibrasp-consultoria-e-concursos-2018")
]

def baixar_pci(nome_prefixo, url_pagina):
    print(f"\n[*] Acessando página PCI: {nome_prefixo}")
    req = urllib.request.Request(url_pagina, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # Encontra links diretos para arquivos de download (PDFs ou ZIPs)
            links = re.findall(r'href=[\'"]([^\'"]+\.(?:pdf|zip))[\'"]', html, re.IGNORECASE)
            # Também procura links com /download/arquivo ou links de CDN
            links_extra = re.findall(r'href=[\'"](https?://[^\'"]*(?:arquivos|provas|download)[^\'"]*)[\'"]', html, re.IGNORECASE)
            
            todos_links = set(links + links_extra)
            print(f"    -> Encontrados {len(todos_links)} links candidatos a download.")
            
            sucesso = False
            for link in todos_links:
                if any(ext in link.lower() for ext in ['.pdf', '.zip']):
                    if not link.startswith('http'):
                        link = urllib.parse.urljoin(url_pagina, link)
                    
                    extensao = ".pdf" if ".pdf" in link.lower() else ".zip"
                    nome_salvar = f"{nome_prefixo}_{os.path.basename(link.split('?')[0])}"
                    if not nome_salvar.lower().endswith(('.pdf', '.zip')):
                        nome_salvar += extensao
                        
                    caminho_final = os.path.join(DOWNLOAD_DIR, nome_salvar)
                    
                    print(f"    [+] Baixando arquivo: {link}")
                    req_dl = urllib.request.Request(link, headers=HEADERS)
                    try:
                        with urllib.request.urlopen(req_dl, context=ssl_context, timeout=20) as resp_dl:
                            conteudo = resp_dl.read()
                            if len(conteudo) > 1000:
                                with open(caminho_final, 'wb') as f:
                                    f.write(conteudo)
                                print(f"    [SUCESSO] Salvo ({len(conteudo)/1024:.1f} KB): {nome_salvar}")
                                sucesso = True
                    except Exception as e:
                        print(f"    [-] Falha ao baixar arquivo {link}: {e}")
            return sucesso
    except Exception as e:
        print(f"[-] Erro ao acessar página {url_pagina}: {e}")
        return False

def main():
    print("="*75)
    print(" DOWNLOADER DE PROVAS REAIS IBRASP / INBRASP (PCI CONCURSOS)")
    print(f" Diretório de Destino: {DOWNLOAD_DIR}")
    print("="*75)
    
    baixados = 0
    for nome, url in URLS_PCI:
        if baixar_pci(nome, url):
            baixados += 1
        time.sleep(0.5)
        
    print("\n" + "="*75)
    print(f" FINALIZADO! Total de {baixados} concursos processados.")
    print(f" Arquivos em: {DOWNLOAD_DIR}")
    print("="*75)

if __name__ == "__main__":
    main()

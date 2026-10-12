import re, os, sys, ssl, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

LOG = r"C:\Users\Ruan Gomes\.gemini\antigravity\brain\654a9279-1604-4c92-9ace-2a4b6b3f73a7\.system_generated\tasks\task-843.log"
OUT = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas\provas_reais_inbrasp\_candidatos"
os.makedirs(OUT, exist_ok=True)
ctx = ssl._create_unverified_context()
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0 Safari/537.36'}

EXCL = ['resultado','edital','aditivo','convoca','homolog','isen','recurso','local','titulo','título','nomea',
        'comunicado','retific','divulga','inscri','aprovados','orienta','portaria','nota','hetero','biopsic',
        'psicos','entrevista','cronograma','classifica','gabarito','resposta','concorr','diário','diario','minuta',
        'conv.','result','definitivo','pre ','ind.quil','hom.pdf','rf.pdf','kkkk','scan']

lines = open(LOG, encoding='utf-8', errors='ignore').read().splitlines()
seen = set()
cands = []
for l in lines:
    m = re.match(r'\s*\[ID (\d+)\] (.*?) -> (arquivos/.+\.pdf)', l)
    if not m:
        continue
    cid, org, path = m.groups()
    low = path.lower()
    if any(k in low for k in EXCL):
        continue
    if re.search(r'arquivos/\d{8}_\d{6}_[A-Za-z0-9]{40}\.pdf', path):
        continue  # nomes aleatórios (portarias/atos)
    if path in seen:
        continue
    seen.add(path)
    cands.append((cid, org.strip(), path))

print(f"Candidatos: {len(cands)}")
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None
    print("pypdf ausente")

for cid, org, path in cands:
    url = "https://www.inbrasp.org/" + urllib.parse.quote(path, safe='/')
    nome = f"ID{cid}_" + re.sub(r'[\\/*?:"<>|]', '_', path.split('/')[-1])
    dest = os.path.join(OUT, nome)
    try:
        if not os.path.exists(dest):
            with urllib.request.urlopen(urllib.request.Request(url, headers=H), context=ctx, timeout=30) as r:
                open(dest, 'wb').write(r.read())
        info = ""
        if PdfReader:
            rd = PdfReader(dest)
            txt = ""
            for p in rd.pages[:4]:
                txt += (p.extract_text() or "")
            nq = len(re.findall(r'QUEST[ÃA]O\s*\d+|\n\s*\d{1,2}\s*[\.\)-]\s', txt, re.I))
            alt = len(re.findall(r'\(?\b[A-D]\)\s', txt))
            info = f"pags={len(rd.pages)} questoes~{nq} alts~{alt} | {txt[:90].strip()!r}"
        print(f"[ID {cid}] {org[:28]:28} {nome[:60]:60} {info}")
    except Exception as e:
        print(f"[ID {cid}] ERRO {nome}: {e}")

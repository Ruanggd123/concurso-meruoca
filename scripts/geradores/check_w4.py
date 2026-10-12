import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

pat = re.compile(r'\{\"id\":\s*(\d+),\s*\"category\":\s*\"[^\"]+\",\s*\"day\":\s*\"w4_d3\",\s*\"discipline\":\s*\"([^\"]+)\",\s*\"topic\":\s*\"([^\"]+)\",\s*\"question\":\s*\"([^\"]+)\",\s*\"options\":\s*(\[[^\]]+\]),\s*\"correctAnswer\":\s*(\d+)')
matches = list(pat.finditer(code))
print(f"Total w4_d3 encontradas: {len(matches)}")
for m in matches:
    qid = m.group(1)
    opts = json.loads(m.group(5))
    cor = int(m.group(6))
    lens = [len(o) for o in opts]
    is_max = (lens.index(max(lens)) == cor)
    max_len = max(lens)
    min_len = min(lens)
    ratio = max_len / (min_len if min_len > 0 else 1)
    print(f"Q{qid}: Cor={chr(65+cor)} | Lens={lens} | Ratio={ratio:.1f} | CorIsLongest={is_max}")
    if ratio > 1.8 and is_max:
        print(f"   [ALERTA DESTACADA] Resposta correta ({chr(65+cor)}) muito maior que as outras!")
        print(f"   Correta: {opts[cor]}")

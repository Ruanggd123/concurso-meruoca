import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

pat = re.compile(r'\{\"id\":\s*(\d+),\s*\"category\":\s*\"[^\"]+\",\s*\"day\":\s*\"(w[45]_d[1-4])\",\s*\"discipline\":\s*\"([^\"]+)\",\s*\"topic\":\s*\"([^\"]+)\",\s*\"question\":\s*\"([^\"]+)\",\s*\"options\":\s*(\[[^\]]+\]),\s*\"correctAnswer\":\s*(\d+)')
matches = list(pat.finditer(code))
print(f"Total questoes encontradas em w4 e w5: {len(matches)}")

alertas = 0
for m in matches:
    qid = m.group(1)
    day = m.group(2)
    opts = json.loads(m.group(6))
    cor = int(m.group(7))
    lens = [len(o) for o in opts]
    ratio = max(lens) / min(lens)
    if ratio > 1.25:
        print(f"[ALERTA] Q{qid} ({day}): Ratio={ratio:.2f} | Lens={lens}")
        alertas += 1

if alertas == 0:
    print("[SUCESSO TOTAL] Nenhuma questão em w4 ou w5 tem opções desproporcionais! Todas têm alternativas perfeitamente equilibradas (Ratio <= 1.25)!")

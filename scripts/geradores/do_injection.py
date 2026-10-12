import sys, json, re
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

from define_w4_d3 import W4_D3_QUESTIONS
from define_w4_d4 import W4_D4_QUESTIONS

# Rebalancear letras de w4_d3: 5A, 5B, 4C, 4D
target_keys_d3 = [1, 0, 3, 1, 2, 0, 3, 2, 0, 2, 3, 2, 1, 0, 3, 1, 0, 1]
for i, q in enumerate(W4_D3_QUESTIONS):
    cur_cor = q['correctAnswer']
    target_cor = target_keys_d3[i]
    if cur_cor != target_cor:
        opts = list(q['options'])
        cor_text = opts[cur_cor]
        other_text = opts[target_cor]
        opts[target_cor] = cor_text
        opts[cur_cor] = other_text
        q['options'] = opts
        q['correctAnswer'] = target_cor
        letra = chr(65 + target_cor)
        com = q['commentary']
        if com.startswith('Gabarito: '):
            q['commentary'] = f'Gabarito: {letra}.' + com[11:]

# Rebalancear letras de w4_d4: 5A, 5B, 4C, 4D
target_keys_d4 = [0, 1, 3, 0, 2, 3, 0, 1, 2, 3, 0, 1, 3, 1, 2, 0, 2, 1]
for i, q in enumerate(W4_D4_QUESTIONS):
    cur_cor = q['correctAnswer']
    target_cor = target_keys_d4[i]
    if cur_cor != target_cor:
        opts = list(q['options'])
        cor_text = opts[cur_cor]
        other_text = opts[target_cor]
        opts[target_cor] = cor_text
        opts[cur_cor] = other_text
        q['options'] = opts
        q['correctAnswer'] = target_cor
        letra = chr(65 + target_cor)
        com = q['commentary']
        if com.startswith('Gabarito: '):
            q['commentary'] = f'Gabarito: {letra}.' + com[11:]

print("w4_d3 gabarito:", Counter([chr(65+q['correctAnswer']) for q in W4_D3_QUESTIONS]))
print("w4_d4 gabarito:", Counter([chr(65+q['correctAnswer']) for q in W4_D4_QUESTIONS]))

# Ler app.js
with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Achar a linha com '{"id": 613,' e a linha com '{"id": 630,'
idx_start = -1
idx_end = -1
for i, l in enumerate(lines):
    if '{"id": 613,' in l:
        idx_start = i
    if '{"id": 630,' in l:
        idx_end = i

print(f"Linhas alvo das questoes: {idx_start+1} a {idx_end+1}")
if idx_start == -1 or idx_end == -1:
    print("ERRO ao localizar linhas!")
    sys.exit(1)

# Gerar linhas JSON das novas questoes
novas_linhas = []
todas = W4_D3_QUESTIONS + W4_D4_QUESTIONS
for idx, q in enumerate(todas):
    novas_linhas.append("  " + json.dumps(q, ensure_ascii=False) + (",\n" if idx < len(todas)-1 else "\n"))

# Substituir o bloco em lines
lines = lines[:idx_start] + novas_linhas + lines[idx_end+1:]

app_content = "".join(lines)

# Atualizar QUIZ_DAYS_CONFIG
# Vamos verificar o inicio de QUIZ_DAYS_CONFIG
novo_config_dias = """const QUIZ_DAYS_CONFIG = {
  w4_d4: {
    title: "⭐ Semana 4 • Dia 4 — Quinta-feira (24/09/2026 - HOJE): LRF & Colocação Pronominal (18 Questões)",
    desc: "10 questões de LRF (LC 101/2000: limites de pessoal no Legislativo, vedações no fim de mandato, RGF e RREO) + 8 questões de Língua Portuguesa (Colocação Pronominal: próclise, ênclise, mesóclise e locuções). Formato enxuto, padrão fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_04_DIA_04_24_09_2026.html",
    bookletLabel: "Abrir Caderno Hoje Impresso (PDF)"
  },
  w4_d3: {
    title: "📅 Semana 4 • Dia 3 — Quarta-feira (23/09/2026 - Ontem): Orçamento Público & Informática (18 Questões)",
    desc: "10 questões de Orçamento Público (PPA, LDO, LOA, princípios orçamentários e créditos adicionais) + 8 questões de Informática (E-mail, Thunderbird, SMTP/IMAP/POP, colaboração digital). Formato enxuto, padrão fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_04_DIA_03_23_09_2026.html",
    bookletLabel: "Abrir Caderno Ontem Impresso (PDF)"
  },
  w4_d2: {
    title: "📅 Semana 4 • Dia 2 — Terça-feira (22/09/2026): Regimento & RLM (18 Questões)",
    desc: "10 questões de Regimento Interno (moções, espécies, plenário e comissões) + 8 questões de RLM (silogismos, categóricas, De Morgan e Venn). Formato enxuto, padrão réplica fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_04_DIA_02_22_09_2026.html",
    bookletLabel: "Abrir Caderno Impresso (PDF)"
  },
  w4_d1: {
    title: "📅 Semana 4 • Dia 1 — Segunda-feira (21/09/2026): Regimento & Regência (18 Questões)",
    desc: "12 questões de Regimento Interno (Mesa, Presidente, sessões e comissões) + 6 questões de Língua Portuguesa (Regência Verbal & Nominal). Formato enxuto, padrão réplica fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_04_DIA_01_21_09_2026.html",
    bookletLabel: "Abrir Caderno Impresso (PDF)"
  },"""

# Substituir o topo de QUIZ_DAYS_CONFIG ate w4_d1
pattern_cfg = r'const QUIZ_DAYS_CONFIG\s*=\s*\{(?:\s*w4_d[1-4]:\s*\{.*?\},\s*)+'
app_content = re.sub(pattern_cfg, novo_config_dias + "\n", app_content, flags=re.DOTALL)

# Atualizar default de dia no appState
app_content = re.sub(r"quizCategoryFilter:\s*'w4_d[1-3]'", "quizCategoryFilter: 'w4_d4'", app_content)
app_content = re.sub(r"lastSeenDay:\s*'w4_d[1-3]'", "lastSeenDay: 'w4_d4'", app_content)
app_content = re.sub(r"dayKey\s*=\s*'w4_d[1-3]';", "dayKey = 'w4_d4';", app_content)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_content)

print("app.js atualizado com sucesso!")

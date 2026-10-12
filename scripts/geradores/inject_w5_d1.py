import sys, json, re
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

from define_w5_d1 import W5_D1_QUESTIONS

# 1. Rebalancear letras para 5 A, 5 B, 4 C, 4 D
target_keys = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
letters = ['A', 'B', 'C', 'D']

for i, q in enumerate(W5_D1_QUESTIONS):
    cur_cor = q['correctAnswer']
    target_cor = target_keys[i]
    if cur_cor != target_cor:
        opts = list(q['options'])
        cor_text = opts[cur_cor]
        other_text = opts[target_cor]
        opts[target_cor] = cor_text
        opts[cur_cor] = other_text
        q['options'] = opts
        q['correctAnswer'] = target_cor
        letra = letters[target_cor]
        com = q['commentary']
        if com.startswith('Gabarito: '):
            q['commentary'] = f'Gabarito: {letra}.' + com[11:]

print("Distribuição de gabarito w5_d1:", Counter([letters[q['correctAnswer']] for q in W5_D1_QUESTIONS]))

# 2. Ler app.js e localizar o ponto de insercao
with open('app.js', 'r', encoding='utf-8') as f:
    app_code = f.read()

# Localizar o fechamento da Q648: {"id": 648, ...}
idx_q648 = app_code.find('{"id": 648,')
if idx_q648 == -1:
    print("ERRO: Q648 nao encontrada em app.js!")
    sys.exit(1)

# Achar onde termina a Q648 (proxima quebra com fecho de array)
idx_end_q648 = app_code.find('},\n', idx_q648)
if idx_end_q648 == -1:
    idx_end_q648 = app_code.find('}\n', idx_q648)
idx_end_q648 += 1 # logo apos a chave '}'

# Achar onde fecha o array QUIZ_QUESTIONS_DATA: `];\n\n// Metadados` ou similar
idx_array_end = app_code.find('];\n\n// =========================================================================', idx_end_q648)
if idx_array_end == -1:
    idx_array_end = app_code.find('];\n\n// Metadados', idx_end_q648)
if idx_array_end == -1:
    idx_array_end = app_code.find('];\n//', idx_end_q648)

# Montar JSON para as 18 questoes de w5_d1
json_blocos = []
for q in W5_D1_QUESTIONS:
    json_blocos.append("  " + json.dumps(q, ensure_ascii=False))

novo_trecho = ",\n" + ",\n".join(json_blocos) + "\n"

app_code = app_code[:idx_end_q648] + novo_trecho + app_code[idx_array_end:]
print(f"Questoes Q649 a Q666 inseridas em app.js (Total agora: 657).")

# 3. Atualizar QUIZ_DAYS_CONFIG em app.js
novo_config_topo = """const QUIZ_DAYS_CONFIG = {
  w5_d1: {
    title: "⭐ Semana 5 • Dia 1 — Segunda-feira (28/09/2026 - HOJE): Controle da Administração Pública & Semântica (18 Questões)",
    desc: "10 questões de Controle da Administração (CF/88 Art. 31, parecer prévio do TCE 2/3, STF Temas 157/835, controle interno e autotutela) + 8 questões de Língua Portuguesa (Semântica: sinonímia, antonímia, parônimos ratificar/retificar, deferir/diferir, sessão/seção/cessão e denotação). Padrão fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_05_DIA_01_28_09_2026.html",
    bookletLabel: "Abrir Caderno Hoje Impresso (PDF)"
  },
  w4_d4: {
    title: "📅 Semana 4 • Dia 4 — Quinta-feira (24/09/2026): LRF & Colocação Pronominal (18 Questões)",
    desc: "10 questões de LRF (LC 101/2000: limites de pessoal no Legislativo, vedações no fim de mandato, RGF e RREO) + 8 questões de Língua Portuguesa (Colocação Pronominal: próclise, ênclise, mesóclise e locuções). Formato enxuto, padrão fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_04_DIA_04_24_09_2026.html",
    bookletLabel: "Abrir Caderno Impresso (PDF)"
  },"""

pattern_cfg = r'const QUIZ_DAYS_CONFIG\s*=\s*\{(?:\s*w[45]_d[1-4]:\s*\{.*?\},\s*)+'
app_code = re.sub(pattern_cfg, novo_config_topo + "\n", app_code, flags=re.DOTALL)

# Atualizar default de dia no appState
app_code = re.sub(r"quizCategoryFilter:\s*'w[45]_d[1-4]'", "quizCategoryFilter: 'w5_d1'", app_code)
app_code = re.sub(r"lastSeenDay:\s*'w[45]_d[1-4]'", "lastSeenDay: 'w5_d1'", app_code)
app_code = re.sub(r"dayKey\s*=\s*'w[45]_d[1-4]';", "dayKey = 'w5_d1';", app_code)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("app.js atualizado com sucesso!")

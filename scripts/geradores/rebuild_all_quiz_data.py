import os, sys, json, re
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

# Adicionar caminhos de import
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'geradores'))
sys.path.insert(0, BASE_DIR)

from gerar_questoes_semana4_dia2 import QUESTOES_S4_D2
from define_w4_d3 import W4_D3_QUESTIONS
from define_w4_d4 import W4_D4_QUESTIONS
from define_w5_d1 import W5_D1_QUESTIONS

letters = ['A', 'B', 'C', 'D']

print(f"S4_D2: {len(QUESTOES_S4_D2)} questoes (IDs {QUESTOES_S4_D2[0]['id']} a {QUESTOES_S4_D2[-1]['id']})")
print(f"S4_D3: {len(W4_D3_QUESTIONS)} questoes (IDs {W4_D3_QUESTIONS[0]['id']} a {W4_D3_QUESTIONS[-1]['id']})")
print(f"S4_D4: {len(W4_D4_QUESTIONS)} questoes (IDs {W4_D4_QUESTIONS[0]['id']} a {W4_D4_QUESTIONS[-1]['id']})")
print(f"S5_D1: {len(W5_D1_QUESTIONS)} questoes (IDs {W5_D1_QUESTIONS[0]['id']} a {W5_D1_QUESTIONS[-1]['id']})")

# 1. Rebalancear letras de w4_d3 para 5A, 5B, 4C, 4D
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
        letra = letters[target_cor]
        com = q['commentary']
        if com.startswith('Gabarito: '):
            q['commentary'] = f'Gabarito: {letra}.' + com[11:]

# 2. Rebalancear letras de w4_d4 para 5A, 5B, 4C, 4D
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
        letra = letters[target_cor]
        com = q['commentary']
        if com.startswith('Gabarito: '):
            q['commentary'] = f'Gabarito: {letra}.' + com[11:]

# 3. w5_d1 ja esta perfeitamente balanceado em define_w5_d1.py (5A, 5B, 4C, 4D)
print("Distribuicao S5_D1:", Counter([letters[q['correctAnswer']] for q in W5_D1_QUESTIONS]))

# Juntar todas as 72 novas questoes (595 a 666)
todas_novas = QUESTOES_S4_D2 + W4_D3_QUESTIONS + W4_D4_QUESTIONS + W5_D1_QUESTIONS
print(f"Total de novas questoes a inserir: {len(todas_novas)} (IDs {todas_novas[0]['id']} a {todas_novas[-1]['id']})")

# Ler app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_code = f.read()

# Localizar o fechamento da Q594:
pos_q594 = app_code.find('{"id": 594,')
if pos_q594 == -1:
    pos_q594 = app_code.find('"id": 594,')
if pos_q594 == -1:
    print("ERRO: Q594 nao encontrada em app.js!")
    sys.exit(1)

# Achar onde fecha o bloco da Q594
pos_end_q594 = app_code.find('}\n];\n\n//', pos_q594)
if pos_end_q594 == -1:
    pos_end_q594 = app_code.find('}\n];\n', pos_q594)
if pos_end_q594 == -1:
    pos_end_q594 = app_code.find('}\n];', pos_q594)

if pos_end_q594 == -1:
    print("ERRO ao localizar fechamento da Q594 e ];")
    sys.exit(1)

pos_insert = pos_end_q594 + 1 # logo depois da '}'

# Gerar trecho formatado
novas_linhas = []
for q in todas_novas:
    novas_linhas.append("  " + json.dumps(q, ensure_ascii=False))

bloco_json = ",\n" + ",\n".join(novas_linhas)

# Inserir no array QUIZ_QUESTIONS_DATA
app_code = app_code[:pos_insert] + bloco_json + app_code[pos_insert:]
print("Array QUIZ_QUESTIONS_DATA atualizado com sucesso!")

# Atualizar QUIZ_DAYS_CONFIG
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
  },
  w4_d3: {
    title: "📅 Semana 4 • Dia 3 — Quarta-feira (23/09/2026): Orçamento Público & Informática (18 Questões)",
    desc: "10 questões de Orçamento Público (PPA, LDO, LOA, princípios orçamentários e créditos adicionais) + 8 questões de Informática (E-mail, Thunderbird, SMTP/IMAP/POP, colaboração digital). Formato enxuto, padrão fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_04_DIA_03_23_09_2026.html",
    bookletLabel: "Abrir Caderno Impresso (PDF)"
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

pattern_cfg = r'const QUIZ_DAYS_CONFIG\s*=\s*\{(?:\s*w[45]_d[1-4]:\s*\{.*?\},\s*)+'
app_code = re.sub(pattern_cfg, novo_config_topo + "\n", app_code, flags=re.DOTALL)

# Atualizar default de dia no appState
app_code = re.sub(r"quizCategoryFilter:\s*'w[45]_d[1-4]'", "quizCategoryFilter: 'w5_d1'", app_code)
app_code = re.sub(r"lastSeenDay:\s*'w[45]_d[1-4]'", "lastSeenDay: 'w5_d1'", app_code)
app_code = re.sub(r"dayKey\s*=\s*'w[45]_d[1-4]';", "dayKey = 'w5_d1';", app_code)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("app.js reconstruído e atualizado com sucesso!")

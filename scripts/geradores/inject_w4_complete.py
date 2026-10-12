import sys, re, json
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

from define_w4_d3 import W4_D3_QUESTIONS
from define_w4_d4 import W4_D4_QUESTIONS

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
        letra = chr(65 + target_cor)
        com = q['commentary']
        if com.startswith('Gabarito: '):
            q['commentary'] = f'Gabarito: {letra}.' + com[11:]

print("w4_d3 gabarito:", Counter([chr(65+q['correctAnswer']) for q in W4_D3_QUESTIONS]))

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
        letra = chr(65 + target_cor)
        com = q['commentary']
        if com.startswith('Gabarito: '):
            q['commentary'] = f'Gabarito: {letra}.' + com[11:]

print("w4_d4 gabarito:", Counter([chr(65+q['correctAnswer']) for q in W4_D4_QUESTIONS]))

# 3. Ler app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_code = f.read()

# Remover quaisquer questoes antigas de w4_d3 e w4_d4
# A lista de questoes comeca em `const QUIZ_QUESTIONS_DATA = [`
# Vamos extrair ate a Q612
idx_q612 = app_code.find('{"id": 612,')
if idx_q612 == -1:
    print("ERRO: Q612 nao encontrada em app.js!")
    sys.exit(1)

# Achar o final da Q612
idx_end_q612 = app_code.find('},\n', idx_q612)
if idx_end_q612 == -1:
    idx_end_q612 = app_code.find('}\n', idx_q612)
idx_end_q612 += 1  # depois da chave '}'

# Achar onde fecha o array QUIZ_QUESTIONS_DATA: `];\n\n// Metadados`
idx_array_end = app_code.find('];\n\n// Metadados', idx_end_q612)
if idx_array_end == -1:
    idx_array_end = app_code.find('];\n// Metadados', idx_end_q612)

# Montar JSON para todas as 36 questoes (18 de w4_d3 + 18 de w4_d4)
todas_novas = W4_D3_QUESTIONS + W4_D4_QUESTIONS
json_blocos = []
for q in todas_novas:
    json_blocos.append("  " + json.dumps(q, ensure_ascii=False))

novo_trecho_questoes = ",\n" + ",\n".join(json_blocos) + "\n"

app_code = app_code[:idx_end_q612] + novo_trecho_questoes + app_code[idx_array_end:]
print(f"Questoes Q613 a Q648 inseridas em app.js (Total agora: 648).")

# 4. Atualizar QUIZ_DAYS_CONFIG em app.js
# Inserir w4_d4 e atualizar w4_d3
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
  },"""

# Substituir inicio de QUIZ_DAYS_CONFIG
pattern_days = r'const QUIZ_DAYS_CONFIG\s*=\s*\{(?:\s*w4_d[34]:\s*\{.*?\},\s*)*'
app_code = re.sub(r'const QUIZ_DAYS_CONFIG\s*=\s*\{(?:\s*w4_d[34]:\s*\{.*?\},\s*)+', novo_config_dias + "\n", app_code)

# 5. Atualizar default dayKey para w4_d4 em app.js
app_code = app_code.replace("quizCategoryFilter: 'w4_d3'", "quizCategoryFilter: 'w4_d4'")
app_code = app_code.replace("quizCategoryFilter: 'w4_d2'", "quizCategoryFilter: 'w4_d4'")
app_code = app_code.replace("lastSeenDay: 'w4_d3'", "lastSeenDay: 'w4_d4'")
app_code = app_code.replace("lastSeenDay: 'w4_d2'", "lastSeenDay: 'w4_d4'")
app_code = app_code.replace("dayKey = 'w4_d2';", "dayKey = 'w4_d4';")
app_code = app_code.replace("dayKey = 'w4_d3';", "dayKey = 'w4_d4';")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("app.js atualizado com sucesso!")

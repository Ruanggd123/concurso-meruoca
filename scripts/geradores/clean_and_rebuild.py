import re, sys, json, os
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'geradores'))
sys.path.insert(0, BASE_DIR)

from gerar_questoes_semana4_dia2 import QUESTOES_S4_D2
from define_w4_d3 import W4_D3_QUESTIONS
from define_w4_d4 import W4_D4_QUESTIONS
from define_w5_d1 import W5_D1_QUESTIONS

letters = ['A', 'B', 'C', 'D']

# 1. w4_d3
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

# 2. w4_d4
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

# 3. w5_d1 is already balanced in define_w5_d1.py: {'A': 5, 'B': 5, 'C': 4, 'D': 4}
print("Distribuicao S5_D1:", Counter([letters[q['correctAnswer']] for q in W5_D1_QUESTIONS]))

todas_novas = QUESTOES_S4_D2 + W4_D3_QUESTIONS + W4_D4_QUESTIONS + W5_D1_QUESTIONS
print(f"Total de novas questoes (595-666): {len(todas_novas)}")

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find start of QUIZ_QUESTIONS_DATA
start_marker = "const QUIZ_QUESTIONS_DATA = ["
pos_start = content.find(start_marker)
if pos_start == -1:
    print("ERRO: start_marker not found")
    sys.exit(1)

# Find where QUIZ_QUESTIONS_DATA ends, which is before WEEKS_DATA
weeks_marker = "// =========================================================================\n// DADOS COMPLETOS DO CRONOGRAMA DE 5 SEMANAS (30 DIAS)\n// =========================================================================\nconst WEEKS_DATA ="
pos_weeks = content.find(weeks_marker)
if pos_weeks == -1:
    # Try finding const WEEKS_DATA
    pos_weeks = content.find("const WEEKS_DATA =")
    if pos_weeks == -1:
        print("ERRO: WEEKS_DATA not found")
        sys.exit(1)

# Between pos_start and pos_weeks, find Q594
pos_q594 = content.find('"id": 594,', pos_start)
if pos_q594 == -1:
    pos_q594 = content.find('{"id": 594,', pos_start)
if pos_q594 == -1 or pos_q594 > pos_weeks:
    print("ERRO: Q594 not found before WEEKS_DATA")
    sys.exit(1)

# Find end of Q594 object (closing brace of Q594)
# In app.js, each question is usually on a single line or ends with "}"
pos_end_q594_obj = content.find("}", pos_q594)
# After this '}', we want to cut everything until the closing '];' of QUIZ_QUESTIONS_DATA
pos_end_array = content.rfind("];", pos_start, pos_weeks)
if pos_end_array == -1:
    print("ERRO: closing ]; not found before WEEKS_DATA")
    sys.exit(1)

print(f"Cutting from {pos_end_q594_obj + 1} to {pos_end_array}")

novas_linhas = []
for q in todas_novas:
    novas_linhas.append("  " + json.dumps(q, ensure_ascii=False))

bloco_novas = ",\n" + ",\n".join(novas_linhas) + "\n"

new_content = content[:pos_end_q594_obj + 1] + bloco_novas + content[pos_end_array:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("app.js reescrito com sucesso!")

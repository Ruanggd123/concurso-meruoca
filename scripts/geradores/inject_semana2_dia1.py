import json
from gerar_questoes_semana2_dia1 import QUESTOES_S2_D1

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# 1. Localizar final de QUIZ_QUESTIONS_DATA
pos_q180 = app_js.find('"id": 180')
if pos_q180 == -1:
    pos_q180 = app_js.find('id: 180')

pos_end_array = app_js.find('];', pos_q180)

js_add = ",\n" + ",\n".join([json.dumps(q, ensure_ascii=False, indent=2) for q in QUESTOES_S2_D1])

app_js = app_js[:pos_end_array] + js_add + "\n" + app_js[pos_end_array:]
print(f"[+] Injetadas {len(QUESTOES_S2_D1)} questões em QUIZ_QUESTIONS_DATA! Total agora: 220 questões.")

# 2. Atualizar getFilteredBaseQuestions() para filtrar w2_d1
filtro_antigo = """function getFilteredBaseQuestions(filterKey) {
  let questions = QUIZ_QUESTIONS_DATA;
  if (filterKey === 'dia6') {"""

filtro_novo = """function getFilteredBaseQuestions(filterKey) {
  let questions = QUIZ_QUESTIONS_DATA;
  if (filterKey === 'w2_d1') {
    questions = questions.filter(q => q.id >= 181 && q.id <= 220);
  } else if (filterKey === 'dia6') {"""

app_js = app_js.replace(filtro_antigo, filtro_novo)

# 3. Atualizar selectQuizDay()
nav_antigo = """  const btn6 = document.getElementById('btnDayTab6');
  const btn5 = document.getElementById('btnDayTab5');"""

nav_novo = """  const btnS2D1 = document.getElementById('btnDayTabS2D1');
  const btn6 = document.getElementById('btnDayTab6');
  const btn5 = document.getElementById('btnDayTab5');"""

app_js = app_js.replace(nav_antigo, nav_novo)

toggle_antigo = """  if (btn6) btn6.classList.toggle('active', dayKey === 'dia6');
  if (btn5) btn5.classList.toggle('active', dayKey === 'dia5');"""

toggle_novo = """  if (btnS2D1) btnS2D1.classList.toggle('active', dayKey === 'w2_d1');
  if (btn6) btn6.classList.toggle('active', dayKey === 'dia6');
  if (btn5) btn5.classList.toggle('active', dayKey === 'dia5');"""

app_js = app_js.replace(toggle_antigo, toggle_novo)

# Atualizar textos de títulos do selectQuizDay
textos_antigos = """  if (dayKey === 'dia6') {
    if (titleEl) titleEl.innerText = "⭐ Dia 6 — Sábado (05/09/2026 - HOJE): SIMULADO 01 OFICIAL (40 Questões)";
    if (descEl) descEl.innerText = "Prova Completa 40Q no Padrão Oficial da Banca INBRASP (10 Português + 5 Informática + 5 RLM + 20 Específicas). Treino de cronometragem de 3 horas.";
  } else if (dayKey === 'dia5') {"""

textos_novos = """  if (dayKey === 'w2_d1') {
    if (titleEl) titleEl.innerText = "⭐ Semana 2 • Dia 1 — Segunda-feira (07/09/2026 - HOJE): Organização do Estado & Formação de Palavras (40 Questões)";
    if (descEl) descEl.innerText = "20 questões de D. Constitucional (CF/88 Arts. 18 a 31: Competências, Municípios e Controle) + 20 de Português (Estrutura e Processos de Formação de Palavras). Padrão Oficial INBRASP.";
  } else if (dayKey === 'dia6') {
    if (titleEl) titleEl.innerText = "📅 Dia 6 — Sábado (05/09/2026): SIMULADO 01 OFICIAL (40 Questões)";
    if (descEl) descEl.innerText = "Prova Completa 40Q no Padrão Oficial da Banca INBRASP (10 Português + 5 Informática + 5 RLM + 20 Específicas). Treino de cronometragem de 3 horas.";
  } else if (dayKey === 'dia5') {"""

app_js = app_js.replace(textos_antigos, textos_novos)

# Atualizar textos de todas as questões
app_js = app_js.replace(
    "Todas as Questões do Banco de Provas da Semana 1 (180 Questões)",
    "Todas as Questões do Banco de Provas (220 Questões)"
)
app_js = app_js.replace(
    "todas as 180 questões da Semana 1 (Dias 2, 3, 4, 5 e Simulado 1) para treino de alta resistência.",
    "todas as 220 questões ativas (Semana 1 completa + Semana 2 Dia 1) para treino de alta performance."
)

# Atualizar appState inicial para 'w2_d1' (Hoje, 07/09/2026)
app_js = app_js.replace("quizCategoryFilter: 'dia6'", "quizCategoryFilter: 'w2_d1'")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("[+] app.js atualizado com sucesso com suporte a Semana 2 / Dia 1!")

import json
from build_questoes_dia5 import QUESTOES_DIA5

with open('questoes_dia6_simulado1.json', 'r', encoding='utf-8') as f:
    QUESTOES_DIA6 = json.load(f)

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# 1. Localizar final de QUIZ_QUESTIONS_DATA
pos_q100 = app_js.find('"id": 100')
if pos_q100 == -1:
    pos_q100 = app_js.find('id: 100')

pos_end_array = app_js.find('];', pos_q100)

novas_questoes = QUESTOES_DIA5 + QUESTOES_DIA6
js_add = ",\n" + ",\n".join([json.dumps(q, ensure_ascii=False, indent=2) for q in novas_questoes])

app_js = app_js[:pos_end_array] + js_add + "\n" + app_js[pos_end_array:]
print(f"[+] Injetadas {len(novas_questoes)} novas questões em QUIZ_QUESTIONS_DATA! Total agora: 180 questões.")

# 2. Atualizar renderQuiz() para filtrar dia5 e dia6
# Buscar filtro no renderQuiz
filtro_antigo = """  if (appState.quizCategoryFilter === 'dia4') {
    questions = questions.filter(q => q.id >= 61 && q.id <= 100);
  } else if (appState.quizCategoryFilter === 'dia2') {"""

filtro_novo = """  if (appState.quizCategoryFilter === 'dia6') {
    questions = questions.filter(q => q.id >= 141 && q.id <= 180);
  } else if (appState.quizCategoryFilter === 'dia5') {
    questions = questions.filter(q => q.id >= 101 && q.id <= 140);
  } else if (appState.quizCategoryFilter === 'dia4') {
    questions = questions.filter(q => q.id >= 61 && q.id <= 100);
  } else if (appState.quizCategoryFilter === 'dia2') {"""

app_js = app_js.replace(filtro_antigo, filtro_novo)

# 3. Atualizar selectQuizDay()
nav_antigo = """  const btn4 = document.getElementById('btnDayTab4');
  const btn3 = document.getElementById('btnDayTab3');
  const btn2 = document.getElementById('btnDayTab2');
  const btnAll = document.getElementById('btnDayTabAll');
  if (btn4) btn4.classList.toggle('active', dayKey === 'dia4');
  if (btn3) btn3.classList.toggle('active', dayKey === 'dia3');
  if (btn2) btn2.classList.toggle('active', dayKey === 'dia2');
  if (btnAll) btnAll.classList.toggle('active', dayKey === 'all');"""

nav_novo = """  const btn6 = document.getElementById('btnDayTab6');
  const btn5 = document.getElementById('btnDayTab5');
  const btn4 = document.getElementById('btnDayTab4');
  const btn3 = document.getElementById('btnDayTab3');
  const btn2 = document.getElementById('btnDayTab2');
  const btnAll = document.getElementById('btnDayTabAll');
  if (btn6) btn6.classList.toggle('active', dayKey === 'dia6');
  if (btn5) btn5.classList.toggle('active', dayKey === 'dia5');
  if (btn4) btn4.classList.toggle('active', dayKey === 'dia4');
  if (btn3) btn3.classList.toggle('active', dayKey === 'dia3');
  if (btn2) btn2.classList.toggle('active', dayKey === 'dia2');
  if (btnAll) btnAll.classList.toggle('active', dayKey === 'all');"""

app_js = app_js.replace(nav_antigo, nav_novo)

# Atualizar textos de títulos do selectQuizDay
textos_antigos = """  if (dayKey === 'dia4') {
    if (titleEl) titleEl.innerText = "⭐ Dia 4 — Quinta-feira (03/09/2026): Português, Constitucional & Lei Orgânica de Meruoca (40 Questões)";
    if (descEl) descEl.innerText = "15 questões de Português (Fonologia, Acentuação e Crase) + 15 de Constitucional (Direitos Sociais Arts. 6º ao 11) + 10 de Lei Orgânica de Meruoca (Arts. 1º ao 15).";
  } else if (dayKey === 'dia3') {"""

textos_novos = """  if (dayKey === 'dia6') {
    if (titleEl) titleEl.innerText = "⭐ Dia 6 — Sábado (05/09/2026 - HOJE): SIMULADO 01 OFICIAL (40 Questões)";
    if (descEl) descEl.innerText = "Prova Completa 40Q no Padrão Oficial da Banca INBRASP (10 Português + 5 Informática + 5 RLM + 20 Específicas). Treino de cronometragem de 3 horas.";
  } else if (dayKey === 'dia5') {
    if (titleEl) titleEl.innerText = "📅 Dia 5 — Sexta-feira (04/09/2026): D. Administrativo, Python & Lei Orgânica (40 Questões)";
    if (descEl) descEl.innerText = "15 questões de D. Administrativo (Poderes & Atributos PATI) + 15 de Informática (Algoritmos, Fluxogramas & Python) + 10 de Lei Orgânica de Meruoca (Arts. 16 ao 30).";
  } else if (dayKey === 'dia4') {
    if (titleEl) titleEl.innerText = "📅 Dia 4 — Quinta-feira (03/09/2026): Português, Constitucional & Lei Orgânica (40 Questões)";
    if (descEl) descEl.innerText = "15 questões de Português (Fonologia, Acentuação e Crase) + 15 de Constitucional (Direitos Sociais Arts. 6º ao 11) + 10 de Lei Orgânica de Meruoca (Arts. 1º ao 15).";
  } else if (dayKey === 'dia3') {"""

app_js = app_js.replace(textos_antigos, textos_novos)

# Atualizar texto de "todas as questões"
app_js = app_js.replace("Todas as Questões do Banco de Provas (100 Questões)", "Todas as Questões do Banco de Provas da Semana 1 (180 Questões)")
app_js = app_js.replace("todas as questões dos dias 2, 3 e 4 para revisão ampla e treino de resistência.", "todas as 180 questões da Semana 1 (Dias 2, 3, 4, 5 e Simulado 1) para treino de alta resistência.")

# Atualizar appState inicial para 'dia6' (Hoje, Sábado 05/09/2026)
app_js = app_js.replace("quizCategoryFilter: 'dia4'", "quizCategoryFilter: 'dia6'")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("[+] app.js atualizado com sucesso com suporte total a Dia 5 e Dia 6 (Simulado 1)!")

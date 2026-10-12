import json
import re
from gerar_questoes_dia4 import QUESTOES_DIA4

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Injetar as 40 questões no QUIZ_QUESTIONS_DATA
# Localizar o fim de QUIZ_QUESTIONS_DATA
# Procura id: 60
pos_q60 = content.find('id: 60,')
if pos_q60 != -1:
    pos_end_array = content.find('];', pos_q60)
    if pos_end_array != -1:
        # Converter as novas questões para formato JS
        js_questions = ",\n" + ",\n".join([json.dumps(q, ensure_ascii=False, indent=2) for q in QUESTOES_DIA4])
        content = content[:pos_end_array] + js_questions + "\n" + content[pos_end_array:]
        print("[+] Injetadas 40 questões em QUIZ_QUESTIONS_DATA com sucesso!")
    else:
        print("[-] Não encontrou final do array QUIZ_QUESTIONS_DATA")
else:
    print("[-] Não encontrou q60 em app.js")

# 2. Injetar flashcards do Dia 4 em FLASHCARDS_DATA
FLASHCARDS_DIA4 = [
  {
    "id": 31,
    "category": "portugues",
    "day": "dia4",
    "tag": "Português — Proparoxítonas",
    "question": "Qual é a regra geral de acentuação gráfica das palavras PROPAROXÍTONAS na Língua Portuguesa?",
    "answer": "TODAS as palavras proparoxítonas são acentuadas graficamente.",
    "explanation": "Exemplos clássicos da INBRASP: po-LÍ-ti-ca, CÔM-pu-to, TÉC-ni-co, CÂ-ma-ra, DÉ-fi-cit."
  },
  {
    "id": 32,
    "category": "portugues",
    "day": "dia4",
    "tag": "Português — Crase Proibida",
    "question": "Quais são os 3 casos mais cobrados em concursos em que a CRASE é expressamente PROIBIDA?",
    "answer": "1. Antes de palavras masculinas;\n2. Antes de verbos no infinitivo;\n3. Antes de pronomes que não aceitam artigo (esta, essa, quem, alguém, todos).",
    "explanation": "Crase é a fusão de preposição 'a' + artigo 'a'. Se a palavra seguinte não aceita artigo feminino, a crase não pode ocorrer."
  },
  {
    "id": 33,
    "category": "portugues",
    "day": "dia4",
    "tag": "Português — Crase Facultativa",
    "question": "Quais são os 3 casos clássicos em que a CRASE é FACULTATIVA (opcional)? (Mnemônico)",
    "answer": "Mnemônico: ATÉ, NOME DE MULHER, POSSESSIVO\n1. Depois da palavra 'até';\n2. Antes de nomes próprios femininos sem qualificativo;\n3. Antes de pronome possessivo feminino singular (minha, sua, tua).",
    "explanation": "Exemplos: 'Fui até a/à praça'; 'Entreguei o ofício a/à Maria'; 'Dirigi-me a/à sua sala'."
  },
  {
    "id": 34,
    "category": "portugues",
    "day": "dia4",
    "tag": "Português — Hiatos Tônicos",
    "question": "Por que 'SAÍDA' e 'BAÚ' têm acento gráfico, mas 'RAINHA' e 'JUIZ' não têm?",
    "answer": "'I' e 'U' tônicos em hiato recebem acento quando sozinhos na sílaba (ou com 's'). Não recebem acento se seguidos de 'nh' (ra-i-nha) ou de outra consoante como 'z' (ju-iz).",
    "explanation": "Sa-í-da (acentua); Ba-ú (acentua); Ju-iz (não acentua, mas 'ju-í-zes' acentua porque o 'i' fica sozinho com a divisão silábica)."
  },
  {
    "id": 35,
    "category": "constitucional",
    "day": "dia4",
    "tag": "Constitucional — Direitos Sociais",
    "question": "Quais são os limites constitucionais de jornada de trabalho para empregados urbanos e rurais (Art. 7º, XIII)?",
    "answer": "Até 8 HORAS diárias e até 44 HORAS semanais.",
    "explanation": "É facultada a compensação de horários e a redução de jornada mediante acordo ou convenção coletiva de trabalho."
  },
  {
    "id": 36,
    "category": "constitucional",
    "day": "dia4",
    "tag": "Constitucional — Menores de Idade",
    "question": "Quais são as 3 idades-chave para o trabalho de menores segundo a CF/88 (Art. 7º, XXXIII)?",
    "answer": "• 18 anos: Proibido trabalho noturno, perigoso ou insalubre.\n• 16 anos: Proibido qualquer trabalho em geral.\n• 14 anos: Permitido exclusivamente na condição de APRENDIZ.",
    "explanation": "Atenção: A INBRASP adora tentar colocar aprendiz a partir de 12 anos ou trocar 16 por 14 anos na regra geral!"
  },
  {
    "id": 37,
    "category": "constitucional",
    "day": "dia4",
    "tag": "Constitucional — Horas Extras e Férias",
    "question": "Qual o percentual MÍNIMO de adicional de horas extras e o acréscimo de férias na CF/88?",
    "answer": "• Hora extra: no mínimo 50% superior à hora normal.\n• Férias: acréscimo de pelo menos 1/3 (um terço) a mais do salário normal.",
    "explanation": "Art. 7º, XVI e XVII da CF/88."
  },
  {
    "id": 38,
    "category": "constitucional",
    "day": "dia4",
    "tag": "Constitucional — Estabilidade Sindical",
    "question": "Qual o período da estabilidade provisória do dirigente sindical (Art. 8º, VIII da CF)?",
    "answer": "A partir do registro da candidatura e, se eleito (mesmo suplente), até 1 ANO após o término do mandato.",
    "explanation": "Salvo se cometer falta grave devidamente apurada nos termos da lei."
  },
  {
    "id": 39,
    "category": "legislacao",
    "day": "dia4",
    "tag": "Lei Orgânica de Meruoca",
    "question": "Quem são os únicos detentores dos Poderes Políticos no âmbito do Município de Meruoca?",
    "answer": "O Poder Legislativo (Câmara Municipal) e o Poder Executivo (Prefeitura).",
    "explanation": "Município NÃO possui Poder Judiciário nem Ministério Público local. O Judiciário é estadual."
  },
  {
    "id": 40,
    "category": "legislacao",
    "day": "dia4",
    "tag": "Lei Orgânica de Meruoca",
    "question": "Qual a diferença essencial entre Competência Privativa e Competência Comum do Município de Meruoca?",
    "answer": "• Privativa: Assuntos de interesse estritamente local, tributos municipais, fixação de tarifas e zoneamento urbano.\n• Comum: Saúde, proteção ao meio ambiente, educação e assistência pública (exercida em cooperação com Estado e União).",
    "explanation": "Competência privativa = só o município faz; comum = município, Estado e União atuam juntos."
  }
]

pos_fc30 = content.find('id: 30,')
if pos_fc30 != -1:
    pos_end_fc = content.find('];', pos_fc30)
    if pos_end_fc != -1:
        js_flashcards = ",\n" + ",\n".join([json.dumps(fc, ensure_ascii=False, indent=2) for fc in FLASHCARDS_DIA4])
        content = content[:pos_end_fc] + js_flashcards + "\n" + content[pos_end_fc:]
        print("[+] Injetados 10 flashcards do Dia 4 com sucesso!")

# 3. Atualizar renderQuiz() e selectQuizDay() em app.js para suporte a 'dia4'
content = content.replace(
    "if (appState.quizCategoryFilter === 'dia2') {",
    "if (appState.quizCategoryFilter === 'dia4') {\n    questions = questions.filter(q => q.id >= 61 && q.id <= 100);\n  } else if (appState.quizCategoryFilter === 'dia2') {"
)

content = content.replace(
    "const btn3 = document.getElementById('btnDayTab3');",
    "const btn4 = document.getElementById('btnDayTab4');\n  const btn3 = document.getElementById('btnDayTab3');"
)
content = content.replace(
    "if (btn3) btn3.classList.toggle('active', dayKey === 'dia3');",
    "if (btn4) btn4.classList.toggle('active', dayKey === 'dia4');\n  if (btn3) btn3.classList.toggle('active', dayKey === 'dia3');"
)

# Atualizar as descrições no selectQuizDay()
antigo_bloco_textos = """  if (dayKey === 'dia3') {
    if (titleEl) titleEl.innerText = "⭐ Dia 3 — Quarta-feira (02/09/2026): D. Administrativo & Informática";
    if (descEl) descEl.innerText = "15 questões de Direito Administrativo (Princípios LIMPE e Organização) + 15 questões de Informática (Windows 11, Linux, Hardware e Backup).";
  } else if (dayKey === 'dia2') {"""

novo_bloco_textos = """  if (dayKey === 'dia4') {
    if (titleEl) titleEl.innerText = "⭐ Dia 4 — Quinta-feira (03/09/2026): Português, Constitucional & Lei Orgânica de Meruoca (40 Questões)";
    if (descEl) descEl.innerText = "15 questões de Português (Fonologia, Acentuação e Crase) + 15 de Constitucional (Direitos Sociais Arts. 6º ao 11) + 10 de Lei Orgânica de Meruoca (Arts. 1º ao 15).";
  } else if (dayKey === 'dia3') {
    if (titleEl) titleEl.innerText = "📅 Dia 3 — Quarta-feira (02/09/2026): D. Administrativo & Informática";
    if (descEl) descEl.innerText = "15 questões de Direito Administrativo (Princípios LIMPE e Organização) + 15 questões de Informática (Windows 11, Linux, Hardware e Backup).";
  } else if (dayKey === 'dia2') {"""

content = content.replace(antigo_bloco_textos, novo_bloco_textos)

# Atualizar texto de "todas as questões"
content = content.replace(
    "Todas as Questões do Banco de Provas (60 Questões)",
    "Todas as Questões do Banco de Provas (100 Questões)"
)
content = content.replace(
    "todas as questões dos dias 2 e 3 para revisão ampla.",
    "todas as questões dos dias 2, 3 e 4 para revisão ampla e treino de resistência."
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("[+] app.js atualizado com sucesso!")

# -*- coding: utf-8 -*-
import json
import re
from gerar_questoes_semana4_dia3 import QUESTOES_S4_D3

letters = ['A', 'B', 'C', 'D']
ORC = [q for q in QUESTOES_S4_D3 if q['discipline'] == 'Orçamento Público']
INF = [q for q in QUESTOES_S4_D3 if q['discipline'] == 'Informática']
assert len(ORC) == 10 and len(INF) == 8, (len(ORC), len(INF))

def bloco(q):
    h = f"""
    <div class="question-block">
      <div class="question-meta">
        <span class="q-badge">QUESTÃO {q['id']}</span>
        <span class="q-topic">{q['discipline']} • {q['topic']}</span>
      </div>
      <div class="question-text">{q['question']}</div>
      <ul class="options-list">
    """
    for idx, opt in enumerate(q['options']):
        h += f"""
        <li class="option-item">
          <span class="option-letter">{letters[idx]}</span>
          <span>{opt}</span>
        </li>
        """
    return h + """
      </ul>
    </div>
    """

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>CADERNO OFICIAL DE QUESTÕES — SEMANA 4 / DIA 3 (23/09/2026) | INBRASP</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @page { size: A4; margin: 15mm 18mm; }
    :root { --primary: #1e3a8a; --primary-dark: #0f172a; --accent: #dc2626; --border: #cbd5e1; --bg: #ffffff; --text: #0f172a; --text-muted: #475569; }
    body { font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Arial, sans-serif; color: var(--text); background: #f8fafc; margin: 0; padding: 24px; font-size: 10.5pt; line-height: 1.45; }
    .container { max-width: 960px; margin: 0 auto; background: white; padding: 36px 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); }
    .header-box { border: 2px solid var(--primary); border-radius: 8px; padding: 16px 20px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; }
    .header-titles h1 { margin: 0 0 4px 0; font-size: 1.35rem; color: var(--primary); font-weight: 800; text-transform: uppercase; }
    .header-titles h2 { margin: 0 0 4px 0; font-size: 1rem; color: var(--text); font-weight: 700; }
    .header-titles p { margin: 0; font-size: 0.85rem; color: var(--text-muted); }
    .badge-banca { background: #fee2e2; color: #991b1b; font-weight: 800; padding: 6px 14px; border-radius: 6px; font-size: 0.85rem; text-transform: uppercase; border: 1px solid #fecaca; }
    .no-print { display: flex; gap: 12px; margin-bottom: 24px; }
    .btn-action { background: var(--primary); color: white; border: none; padding: 10px 18px; border-radius: 6px; font-weight: 700; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; font-size: 0.9rem; }
    .btn-action:hover { background: var(--primary-dark); }
    .section-title { background: #e0e7ff; color: #1e3a8a; padding: 10px 16px; border-left: 5px solid #2563eb; font-weight: 800; font-size: 1rem; margin: 26px 0 16px 0; border-radius: 0 6px 6px 0; display: flex; justify-content: space-between; align-items: center; }
    .section-title.informatica { background: #fef3c7; color: #92400e; border-left-color: #f59e0b; }
    .question-block { border: 1px solid var(--border); border-radius: 8px; padding: 16px 18px; margin-bottom: 16px; background: #ffffff; page-break-inside: avoid; }
    .question-meta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 0.78rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px; }
    .q-badge { background: #1e3a8a; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 800; }
    .q-topic { color: var(--text-muted); font-weight: 600; text-transform: uppercase; }
    .question-text { font-size: 0.96rem; font-weight: 600; margin-bottom: 12px; line-height: 1.5; }
    .options-list { list-style: none; padding: 0; margin: 0; }
    .option-item { display: flex; align-items: flex-start; gap: 10px; padding: 8px 10px; border-radius: 6px; margin-bottom: 6px; border: 1px solid transparent; font-size: 0.92rem; }
    .option-item:hover { background: #f8fafc; border-color: #e2e8f0; }
    .option-letter { width: 22px; height: 22px; border-radius: 50%; background: #e2e8f0; color: #334155; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.78rem; flex-shrink: 0; }
    .folha-respostas-box { background: #f8fafc; border: 2px dashed #94a3b8; border-radius: 8px; padding: 16px 20px; margin: 30px 0; page-break-before: always; }
    .folha-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 8px; margin-top: 12px; }
    .folha-row { display: flex; align-items: center; gap: 6px; font-size: 0.85rem; font-weight: 700; }
    .folha-num { width: 24px; text-align: right; color: #475569; }
    .folha-circle { width: 20px; height: 20px; border: 1.5px solid #64748b; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; color: #475569; }
    .gabarito-section { margin-top: 36px; border-top: 2px solid #cbd5e1; padding-top: 24px; page-break-before: always; }
    .gabarito-item { border-left: 3px solid #10b981; background: #f0fdf4; padding: 10px 14px; border-radius: 0 6px 6px 0; margin-bottom: 10px; font-size: 0.9rem; }
    .gabarito-letra { font-weight: 800; color: #047857; margin-right: 6px; font-size: 1rem; }
    @media print {
      body { background: white; padding: 0; }
      .container { box-shadow: none; padding: 0; }
      .no-print { display: none; }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="no-print">
      <a href="../index.html" class="btn-action" style="background: #475569;"><i class="fas fa-arrow-left"></i> Voltar ao Gerenciador</a>
      <button onclick="window.print()" class="btn-action"><i class="fas fa-print"></i> Imprimir Caderno A4</button>
    </div>

    <div class="header-box">
      <div class="header-titles">
        <h1>Câmara Municipal de Meruoca — Concurso 2026</h1>
        <h2>Técnico Legislativo • Caderno de Questões — Semana 4 / Dia 3 (23/09/2026)</h2>
        <p>18 Questões Inéditas em Estilo Banca: 10 Orçamento Público + 8 Informática (Comunicação & E-mail)</p>
      </div>
      <div style="text-align: right;">
        <span class="badge-banca">Banca INBRASP</span>
        <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">4 Alternativas (A, B, C, D)</div>
      </div>
    </div>

    <div class="section-title">
      <span><i class="fas fa-coins"></i> PARTE 1: ORÇAMENTO PÚBLICO — PPA, LDO E LOA (QUESTÕES 613 A 622)</span>
      <span style="font-size: 0.8rem; font-weight: normal;">CF/88 Art. 165 a 167 • Lei 4.320/64 • Princípios</span>
    </div>
"""

for q in ORC:
    html_template += bloco(q)

html_template += """
    <div class="section-title informatica">
      <span><i class="fas fa-envelope-open-text"></i> PARTE 2: INFORMÁTICA — COMUNICAÇÃO DIGITAL & E-MAIL (QUESTÕES 623 A 630)</span>
      <span style="font-size: 0.8rem; font-weight: normal;">Thunderbird • Webmail • SMTP/IMAP/POP3 • WhatsApp/Telegram/Discord</span>
    </div>
"""

for q in INF:
    html_template += bloco(q)

html_template += """
    <div class="folha-respostas-box">
      <div style="text-align: center; border-bottom: 1px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 10px;">
        <strong style="font-size: 1.1rem; text-transform: uppercase; color: var(--primary);">Folha de Respostas Óptica — Simulação Real (18 Questões)</strong>
        <p style="margin: 4px 0 0 0; font-size: 0.8rem; color: #64748b;">Preencha a bolha correspondente à alternativa escolhida para treino de agilidade.</p>
      </div>
      <div class="folha-grid">
"""

for q in QUESTOES_S4_D3:
    html_template += f"""
        <div class="folha-row">
          <span class="folha-num">{q['id']}</span>
          <span class="folha-circle">A</span>
          <span class="folha-circle">B</span>
          <span class="folha-circle">C</span>
          <span class="folha-circle">D</span>
        </div>
    """

html_template += """
      </div>
    </div>
    <div class="gabarito-section">
      <div style="background: var(--primary); color: white; padding: 10px 16px; border-radius: 6px; font-weight: 800; font-size: 1.1rem; margin-bottom: 16px;">
        <i class="fas fa-check-double"></i> GABARITO OFICIAL FUNDAMENTADO
      </div>
"""

for q in QUESTOES_S4_D3:
    letra = letters[q['correctAnswer']]
    html_template += f"""
      <div class="gabarito-item">
        <span class="gabarito-letra">{letra}</span>
        <strong>Questão {q['id']} ({q['discipline']} - {q['topic']}):</strong>
        <p style="margin: 4px 0 0 0; color: #334155; font-size: 0.85rem;">{q['commentary']}</p>
      </div>
    """

html_template += """
    </div>
  </div>
</body>
</html>
"""

# Salva o arquivo HTML
with open('provas/CADERNO_QUESTOES_SEMANA_04_DIA_03_23_09_2026.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
print("[+] Caderno S4D3 HTML gerado com sucesso em provas/CADERNO_QUESTOES_SEMANA_04_DIA_03_23_09_2026.html")

# Injeta em app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_text = f.read()

# Verifica se ID 613 já existe
if '"id": 613' in app_text or "'id': 613" in app_text:
    print("[!] Questão 613 já presente em app.js, pulando injeção.")
else:
    # Localiza o final do array QUIZ_QUESTIONS_DATA
    # A última questão é o ID 612
    idx_612 = app_text.find('"id": 612')
    if idx_612 == -1:
        idx_612 = app_text.find("'id': 612")
    assert idx_612 != -1, "ID 612 não encontrado em app.js"
    
    # Encontra o fecha chaves da questão 612
    end_q612 = app_text.find('}', idx_612)
    assert end_q612 != -1, "Fim da questão 612 não encontrado"
    
    # Prepara JSON das 18 questões
    qs_json = ",\n" + ",\n".join(["  " + json.dumps(q, ensure_ascii=False) for q in QUESTOES_S4_D3])
    
    app_text = app_text[:end_q612+1] + qs_json + app_text[end_q612+1:]
    
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(app_text)
    print(f"[+] 18 questões injetadas em app.js (Total agora: 621 questões).")

# Atualiza index.html badges
with open('index.html', 'r', encoding='utf-8') as f:
    idx_text = f.read()

idx_text_updated = re.sub(r'(id="sidebarQuizBadge">)\d+(</span>)', r'\g<1>621\g<2>', idx_text)
idx_text_updated = re.sub(r'(id="mobileQuizBadge">)\d+(</span>)', r'\g<1>621\g<2>', idx_text_updated)

if idx_text != idx_text_updated:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_text_updated)
    print("[+] Badges atualizados para 621 em index.html.")

print("[+] Concluído com sucesso!")

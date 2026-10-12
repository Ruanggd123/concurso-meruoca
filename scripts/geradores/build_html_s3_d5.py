from gerar_questoes_semana3_dia5 import QUESTOES_S3_D5

letters = ['A', 'B', 'C', 'D']

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>CADERNO OFICIAL DE QUESTÕES — SEMANA 3 / DIA 5 (18/09/2026) | INBRASP</title>
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
    .btn-action:hover { background: #1d4ed8; }
    .section-title { background: #1e3a8a; color: white; padding: 8px 14px; border-radius: 6px; font-size: 1.05rem; font-weight: 800; margin: 28px 0 16px 0; display: flex; justify-content: space-between; align-items: center; }
    .section-title.matematica { background: #0284c7; }
    .question-block { border: 1px solid var(--border); border-radius: 8px; padding: 16px 18px; margin-bottom: 16px; background: #ffffff; page-break-inside: avoid; }
    .question-meta { display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.8rem; }
    .q-badge { font-weight: 800; color: var(--primary); }
    .q-topic { color: var(--text-muted); font-weight: 600; }
    .question-text { font-weight: 700; color: var(--primary-dark); margin-bottom: 12px; line-height: 1.45; white-space: pre-line; }
    .options-list { list-style: none; padding: 0; margin: 0; }
    .option-item { display: flex; align-items: flex-start; gap: 10px; padding: 6px 8px; margin-bottom: 4px; border-radius: 4px; font-size: 0.92rem; }
    .option-letter { width: 24px; height: 24px; border: 1.5px solid #94a3b8; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.8rem; color: #334155; flex-shrink: 0; }
    .folha-respostas-box { border: 2px dashed var(--primary); border-radius: 8px; padding: 20px; margin: 30px 0; background: #f8fafc; page-break-before: always; }
    .folha-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; font-size: 0.82rem; margin-top: 14px; }
    .folha-row { display: flex; align-items: center; gap: 6px; padding: 4px 6px; background: white; border: 1px solid var(--border); border-radius: 4px; }
    .folha-num { width: 28px; font-weight: 800; color: var(--primary); }
    .folha-circle { width: 16px; height: 16px; border: 1px solid #64748b; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.65rem; font-weight: 700; color: #475569; }
    .gabarito-section { page-break-before: always; margin-top: 30px; }
    .gabarito-item { background: #f1f5f9; border-left: 4px solid var(--primary); padding: 10px 14px; margin-bottom: 10px; border-radius: 0 6px 6px 0; font-size: 0.88rem; }
    .gabarito-letra { background: #16a34a; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 800; margin-right: 6px; }
    @media print { body { background: white; padding: 0; } .container { padding: 0; box-shadow: none; max-width: 100%; } .no-print { display: none !important; } }
  </style>
</head>
<body>
  <div class="container">
    <div class="no-print">
      <button class="btn-action" onclick="window.print()"><i class="fas fa-print"></i> Imprimir Caderno (PDF)</button>
      <a href="../index.html" class="btn-action" style="background: #e2e8f0; color: #334155;"><i class="fas fa-arrow-left"></i> Voltar ao Gerenciador de Estudos</a>
    </div>
    <div class="header-box">
      <div class="header-titles">
        <span style="font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: #dc2626;">Caderno de Treino Diário Oficial • Semana 3</span>
        <h1>Câmara Municipal de Meruoca / CE</h1>
        <h2>Concurso Público nº 001/2026 — Cargo: Técnico Legislativo</h2>
        <p><strong>Semana 3 • Dia 5 (18/09/2026):</strong> Lei Orgânica — Processo Legislativo Municipal (10Q) • Matemática — Geometria Básica (8Q)</p>
      </div>
      <div style="text-align: right;">
        <div class="badge-banca">Banca INBRASP</div>
        <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 6px;">18 Questões (A, B, C, D)</div>
      </div>
    </div>
    <div class="section-title">
      <span><i class="fas fa-landmark"></i> PARTE 1: LEI ORGÂNICA — PROCESSO LEGISLATIVO (QUESTÕES 521 A 530)</span>
      <span style="font-size: 0.8rem; font-weight: normal;">Iniciativa, Tramitação, Sanção, Veto e Fiscalização</span>
    </div>
"""

for q in QUESTOES_S3_D5[:10]:
    html_template += f"""
    <div class="question-block">
      <div class="question-meta">
        <span class="q-badge">QUESTÃO {q['id']}</span>
        <span class="q-topic">{q['discipline']} • {q['topic']}</span>
      </div>
      <div class="question-text">{q['question']}</div>
      <ul class="options-list">
    """
    for idx, opt in enumerate(q['options']):
        html_template += f"""
        <li class="option-item">
          <span class="option-letter">{letters[idx]}</span>
          <span>{opt}</span>
        </li>
        """
    html_template += """
      </ul>
    </div>
    """

html_template += """
    <div class="section-title matematica">
      <span><i class="fas fa-shapes"></i> PARTE 2: MATEMÁTICA — GEOMETRIA BÁSICA (QUESTÕES 531 A 538)</span>
      <span style="font-size: 0.8rem; font-weight: normal;">Áreas, Perímetro e Volume</span>
    </div>
"""

for q in QUESTOES_S3_D5[10:]:
    html_template += f"""
    <div class="question-block">
      <div class="question-meta">
        <span class="q-badge">QUESTÃO {q['id']}</span>
        <span class="q-topic">{q['discipline']} • {q['topic']}</span>
      </div>
      <div class="question-text">{q['question']}</div>
      <ul class="options-list">
    """
    for idx, opt in enumerate(q['options']):
        html_template += f"""
        <li class="option-item">
          <span class="option-letter">{letters[idx]}</span>
          <span>{opt}</span>
        </li>
        """
    html_template += """
      </ul>
    </div>
    """

html_template += """
    <div class="folha-respostas-box">
      <div style="text-align: center; border-bottom: 1px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 10px;">
        <strong style="font-size: 1.1rem; text-transform: uppercase; color: var(--primary);">Folha de Respostas Óptica — Simulação Real (18 Questões)</strong>
        <p style="margin: 4px 0 0 0; font-size: 0.8rem; color: #64748b;">Preencha a bolha correspondente à alternativa escolhida para treino de agilidade.</p>
      </div>
      <div class="folha-grid">
"""

for q in QUESTOES_S3_D5:
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
        <i class="fas fa-check-double"></i> GABARITO OFICIAL FUNDAMENTADO (QUESTÕES 521 A 538)
      </div>
"""

for q in QUESTOES_S3_D5:
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

with open('provas/CADERNO_QUESTOES_SEMANA_03_DIA_05_18_09_2026.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("[+] Caderno CADERNO_QUESTOES_SEMANA_03_DIA_05_18_09_2026.html gerado com sucesso!")

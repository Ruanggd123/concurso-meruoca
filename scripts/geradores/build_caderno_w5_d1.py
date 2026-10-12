import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

from define_w5_d1 import W5_D1_QUESTIONS

letters = ['A', 'B', 'C', 'D']

def render_options(opts):
    res = ""
    for idx, opt in enumerate(opts):
        res += f"""
        <li class="option-item">
          <span class="option-letter">{letters[idx]}</span>
          <span>{opt}</span>
        </li>
        """
    return res

def render_folha(questions):
    res = ""
    for q in questions:
        res += f"""
        <div class="folha-row">
          <span class="folha-num">{q['id']}</span>
          <span class="folha-circle">A</span>
          <span class="folha-circle">B</span>
          <span class="folha-circle">C</span>
          <span class="folha-circle">D</span>
        </div>
        """
    return res

def render_gabaritos(questions):
    res = ""
    for q in questions:
        letra = letters[q['correctAnswer']]
        res += f"""
        <div class="gabarito-item">
          <strong>Questão {q['id']}:</strong> <span class="gabarito-letra">({letra})</span> {q['commentary']}
        </div>
        """
    return res

def gerar_caderno(dia_str, data_str, subtitulo, parte1_title, parte1_sub, parte2_title, parte2_sub, questions, parte1_filter, out_path):
    p1_qs = [q for q in questions if parte1_filter(q)]
    p2_qs = [q for q in questions if not parte1_filter(q)]

    def bloco_q(q):
        return f"""
    <div class="question-block">
      <div class="question-meta">
        <span class="q-badge">QUESTÃO {q['id']}</span>
        <span class="q-topic">{q['discipline']} • {q['topic']}</span>
      </div>
      <div class="question-text">{q['question']}</div>
      <ul class="options-list">
        {render_options(q['options'])}
      </ul>
    </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>CADERNO OFICIAL DE QUESTÕES — SEMANA 5 / {dia_str.upper()} ({data_str}) | INBRASP</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @page {{ size: A4; margin: 15mm 18mm; }}
    :root {{ --primary: #1e3a8a; --primary-dark: #0f172a; --accent: #dc2626; --border: #cbd5e1; --bg: #ffffff; --text: #0f172a; --text-muted: #475569; }}
    body {{ font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Arial, sans-serif; color: var(--text); background: #f8fafc; margin: 0; padding: 24px; font-size: 10.5pt; line-height: 1.45; }}
    .container {{ max-width: 960px; margin: 0 auto; background: white; padding: 36px 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); }}
    .header-box {{ border: 2px solid var(--primary); border-radius: 8px; padding: 16px 20px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; }}
    .header-titles h1 {{ margin: 0 0 4px 0; font-size: 1.35rem; color: var(--primary); font-weight: 800; text-transform: uppercase; }}
    .header-titles h2 {{ margin: 0 0 4px 0; font-size: 1rem; color: var(--text); font-weight: 700; }}
    .header-titles p {{ margin: 0; font-size: 0.85rem; color: var(--text-muted); }}
    .badge-banca {{ background: #fee2e2; color: #991b1b; font-weight: 800; padding: 6px 14px; border-radius: 6px; font-size: 0.85rem; text-transform: uppercase; border: 1px solid #fecaca; }}
    .no-print {{ display: flex; gap: 12px; margin-bottom: 24px; }}
    .btn-action {{ background: var(--primary); color: white; border: none; padding: 10px 18px; border-radius: 6px; font-weight: 700; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; font-size: 0.9rem; }}
    .btn-action:hover {{ background: var(--primary-dark); }}
    .section-title {{ background: #e0e7ff; color: #1e3a8a; padding: 10px 16px; border-left: 5px solid #2563eb; font-weight: 800; font-size: 1rem; margin: 26px 0 16px 0; border-radius: 0 6px 6px 0; display: flex; justify-content: space-between; align-items: center; }}
    .section-title.secundario {{ background: #fef3c7; color: #92400e; border-left-color: #f59e0b; }}
    .question-block {{ border: 1px solid var(--border); border-radius: 8px; padding: 16px 18px; margin-bottom: 16px; background: #ffffff; page-break-inside: avoid; }}
    .question-meta {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 0.78rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 6px; }}
    .q-badge {{ background: #1e3a8a; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 800; }}
    .q-topic {{ color: var(--text-muted); font-weight: 600; text-transform: uppercase; }}
    .question-text {{ font-size: 0.96rem; font-weight: 600; margin-bottom: 12px; line-height: 1.5; }}
    .options-list {{ list-style: none; padding: 0; margin: 0; }}
    .option-item {{ display: flex; align-items: flex-start; gap: 10px; padding: 8px 10px; border-radius: 6px; margin-bottom: 6px; border: 1px solid transparent; font-size: 0.92rem; }}
    .option-item:hover {{ background: #f8fafc; border-color: #e2e8f0; }}
    .option-letter {{ width: 22px; height: 22px; border-radius: 50%; background: #e2e8f0; color: #334155; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.78rem; flex-shrink: 0; }}
    .folha-respostas-box {{ background: #f8fafc; border: 2px dashed #94a3b8; border-radius: 8px; padding: 16px 20px; margin: 30px 0; page-break-before: always; }}
    .folha-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 8px; margin-top: 12px; }}
    .folha-row {{ display: flex; align-items: center; gap: 6px; font-size: 0.85rem; font-weight: 700; }}
    .folha-num {{ width: 24px; text-align: right; color: #475569; }}
    .folha-circle {{ width: 20px; height: 20px; border: 1.5px solid #64748b; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; color: #475569; }}
    .gabarito-section {{ margin-top: 36px; border-top: 2px solid #cbd5e1; padding-top: 24px; page-break-before: always; }}
    .gabarito-item {{ border-left: 3px solid #10b981; background: #f0fdf4; padding: 10px 14px; border-radius: 0 6px 6px 0; margin-bottom: 10px; font-size: 0.9rem; }}
    .gabarito-letra {{ font-weight: 800; color: #047857; margin-right: 6px; font-size: 1rem; }}
    @media print {{
      body {{ background: white; padding: 0; }}
      .container {{ box-shadow: none; padding: 0; }}
      .no-print {{ display: none; }}
    }}
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
        <h2>Técnico Legislativo • Caderno de Questões — Semana 5 / {dia_str.title()} ({data_str})</h2>
        <p>{subtitulo}</p>
      </div>
      <div style="text-align: right;">
        <span class="badge-banca">Banca INBRASP</span>
        <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">4 Alternativas (A, B, C, D)</div>
      </div>
    </div>

    <div class="section-title">
      <span><i class="fas fa-balance-scale"></i> {parte1_title}</span>
      <span style="font-size: 0.8rem; font-weight: normal;">{parte1_sub}</span>
    </div>

    {"".join([bloco_q(q) for q in p1_qs])}

    <div class="section-title secundario">
      <span><i class="fas fa-book-reader"></i> {parte2_title}</span>
      <span style="font-size: 0.8rem; font-weight: normal;">{parte2_sub}</span>
    </div>

    {"".join([bloco_q(q) for q in p2_qs])}

    <div class="folha-respostas-box">
      <div style="font-weight: 800; font-size: 1rem; color: var(--primary); text-transform: uppercase;">
        <i class="fas fa-edit"></i> Folha Óptica de Respostas (Simulado Pré-Prova)
      </div>
      <p style="font-size: 0.82rem; color: var(--text-muted); margin: 4px 0 12px 0;">Preencha os círculos correspondentes às suas respostas antes de conferir o gabarito comentado.</p>
      <div class="folha-grid">
        {render_folha(questions)}
      </div>
    </div>

    <div class="gabarito-section">
      <div style="font-weight: 800; font-size: 1.15rem; color: #047857; margin-bottom: 16px;">
        <i class="fas fa-check-double"></i> Gabarito Oficial Fundamentado (Banca INBRASP)
      </div>
      {render_gabaritos(questions)}
    </div>

  </div>
</body>
</html>
"""
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Caderno gerado: {out_path}")

# Gerar caderno w5_d1
gerar_caderno(
    dia_str="Dia 1",
    data_str="28/09/2026",
    subtitulo="18 Questões Inéditas em Estilo Banca: 10 Controle da Administração Pública + 8 Língua Portuguesa (Semântica & Vocábulos)",
    parte1_title="PARTE 1: CONTROLE DA ADMINISTRAÇÃO PÚBLICA (QUESTÕES 649 A 658)",
    parte1_sub="CF/88 Art. 31 e 74 • Controle Externo Municipal (TCE/Câmara) • Parecer Prévio (2/3) • Autotutela e Remédios",
    parte2_title="PARTE 2: LÍNGUA PORTUGUESA — SEMÂNTICA & SIGNIFICADOS (QUESTÕES 659 A 666)",
    parte2_sub="Sinonímia, Antonímia, Polissemia, Homonímia, Parônimos e Significação dos Vocábulos",
    questions=W5_D1_QUESTIONS,
    parte1_filter=lambda q: q['discipline'] == 'Controle da Administração Pública',
    out_path=r"c:\Users\Ruan Gomes\Downloads\Meruoca\provas\CADERNO_QUESTOES_SEMANA_05_DIA_01_28_09_2026.html"
)

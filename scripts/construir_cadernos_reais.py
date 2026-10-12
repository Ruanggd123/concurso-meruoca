import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROVAS_DIR = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas"
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def render_html(titulo, badge, orgao, certame, cargo, fonte, questoes):
    """
    questoes: lista de dicts com:
      - numero: int
      - header: str
      - enunciado: str
      - options: list of 4 strs
      - gabarito: str ('A', 'B', 'C' ou 'D')
      - comentario: str
    """
    conteudo_questoes = []
    folha_bolhas = []
    conteudo_gabarito = []
    
    current_sec = ""
    for q in questoes:
        sec = q.get('secao', '')
        if sec and sec != current_sec:
            current_sec = sec
            conteudo_questoes.append(f'<div class="section-title">{current_sec}</div>')
            
        num = q['numero']
        h = q['header']
        enunc = q['enunciado']
        opts = q['options']
        gab = q['gabarito']
        com = q['comentario']
        
        # HTML questão
        opts_html = "".join([f"<li>({letra}) {texto}</li>" for letra, texto in zip(['A', 'B', 'C', 'D'], opts)])
        q_html = f"""
        <div class="question-box">
          <div class="question-header">QUESTÃO {num:02d} • {h}</div>
          <div class="question-title">{enunc}</div>
          <ul class="options-list">
            {opts_html}
          </ul>
        </div>
        """
        conteudo_questoes.append(q_html)
        
        # Folha de bolhas
        bolhas = "".join([f'<span class="bubble">{l}</span>' for l in ['A', 'B', 'C', 'D']])
        folha_bolhas.append(f'<div class="answer-row"><span>{num:02d}.</span> {bolhas}</div>')
        
        # Gabarito fundamentado
        g_html = f"""
        <div class="question-box">
          <div class="question-header">QUESTÃO {num:02d} • Gabarito Oficial: <strong>({gab})</strong></div>
          <div class="comentario-box">
            <strong>Resolução / Fundamentação:</strong> {com}
          </div>
        </div>
        """
        conteudo_gabarito.append(g_html)
        
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{titulo}</title>
  <style>
    @media print {{
      body {{ font-size: 10pt; }}
      .no-print {{ display: none; }}
      .page-break {{ page-break-before: always; }}
    }}
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.45;
      color: #111;
      max-width: 900px;
      margin: 0 auto;
      padding: 24px;
      background: #fff;
    }}
    .header-box {{
      border: 3px solid #1e3a8a;
      background: #f0fdf4;
      padding: 16px;
      text-align: center;
      margin-bottom: 20px;
      border-radius: 6px;
    }}
    .header-box h1 {{ font-size: 14pt; margin: 0 0 6px 0; color: #1e3a8a; text-transform: uppercase; }}
    .header-box h2 {{ font-size: 11.5pt; margin: 0 0 4px 0; color: #15803d; }}
    .header-box p {{ font-size: 9pt; margin: 2px 0; color: #333; }}
    .badge-real {{
      display: inline-block;
      background: #dc2626;
      color: white;
      font-weight: bold;
      padding: 3px 10px;
      border-radius: 4px;
      font-size: 9pt;
      margin-bottom: 6px;
      text-transform: uppercase;
    }}
    .instructions-box {{
      border: 1px solid #333;
      background: #f9f9f9;
      padding: 12px 16px;
      font-size: 8.5pt;
      margin-bottom: 24px;
    }}
    .instructions-box ul {{ margin: 4px 0; padding-left: 20px; }}
    .section-title {{
      background: #1e3a8a;
      color: #fff;
      padding: 6px 12px;
      font-size: 10pt;
      font-weight: bold;
      text-transform: uppercase;
      margin: 22px 0 14px 0;
      border-radius: 3px;
    }}
    .question-box {{
      margin-bottom: 18px;
      padding-bottom: 12px;
      border-bottom: 1px dashed #ccc;
      page-break-inside: avoid;
    }}
    .question-header {{
      font-size: 8.5pt;
      color: #64748b;
      font-weight: bold;
      margin-bottom: 4px;
    }}
    .question-title {{ font-weight: bold; margin-bottom: 6px; font-size: 9.5pt; color: #0f172a; }}
    .options-list {{ list-style: none; padding-left: 0; margin: 6px 0; }}
    .options-list li {{ margin-bottom: 5px; font-size: 9pt; }}
    .answer-card {{
      border: 2px solid #000;
      padding: 16px;
      margin-top: 30px;
      page-break-before: always;
    }}
    .answer-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-top: 14px;
    }}
    .answer-row {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 9pt;
      font-weight: bold;
    }}
    .bubble {{
      width: 18px;
      height: 18px;
      border: 1px solid #000;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 7.5pt;
    }}
    .comentario-box {{
      background: #f8fafc;
      border-left: 3px solid #2563eb;
      padding: 8px 12px;
      font-size: 8.5pt;
      margin-top: 8px;
      color: #334155;
    }}
    .comentario-box strong {{ color: #1e3a8a; }}
  </style>
</head>
<body>

  <div class="header-box">
    <span class="badge-real">{badge}</span>
    <h1>{orgao}</h1>
    <h2>{certame}</h2>
    <p><strong>CARGO:</strong> {cargo}</p>
    <p><strong>FONTE:</strong> {fonte}</p>
  </div>

  <div class="instructions-box">
    <strong>INFORMAÇÕES OFICIAIS DO CADERNO:</strong>
    <ul>
      <li>Este caderno é composto exclusivamente por <strong>questões reais de concursos oficiais</strong> de Câmaras Municipais e Prefeituras do Ceará e região.</li>
      <li>Formato de 4 alternativas (A, B, C e D) exatamente no modelo adotado pela banca INBRASP no Edital de Meruoca.</li>
      <li>Tempo recomendado para resolução contínua: 3 horas (simulação estrita de prova física).</li>
      <li>Ao concluir a resolução, marque o gabarito na Folha Óptica e confira com as fundamentações oficiais ao final.</li>
    </ul>
  </div>

  {"".join(conteudo_questoes)}

  <div class="answer-card">
    <h3 style="margin: 0 0 8px 0; text-align: center; text-transform: uppercase;">Folha Óptica de Respostas (Treino de Simulação)</h3>
    <p style="text-align: center; font-size: 8.5pt; margin: 0 0 12px 0;">Preencha a bolha da alternativa correta conforme o cartão de respostas oficial:</p>
    <div class="answer-grid">
      {"".join(folha_bolhas)}
    </div>
  </div>

  <div class="page-break"></div>
  <div class="section-title">GABARITO OFICIAL FUNDAMENTADO & RESOLUÇÃO TÉCNICA</div>
  {"".join(conteudo_gabarito)}

</body>
</html>
"""
    return html

def compilar_para_pdf(html_path, pdf_path):
    normalized_url = "file:///" + html_path.replace("\\", "/")
    cmd = [
        EDGE_PATH,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        normalized_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"[OK] {os.path.basename(pdf_path)} ({size_kb:.1f} KB)")
        return True
    else:
        print(f"[FALHA] {os.path.basename(pdf_path)}")
        return False

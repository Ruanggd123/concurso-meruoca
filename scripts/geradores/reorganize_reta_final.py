import sys
sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>CRONOGRAMA DE RETA FINAL & PROVAS OFICIAIS — CÂMARA DE MERUOCA 2026</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --primary: #1e3a8a;
      --primary-dark: #0f172a;
      --accent: #dc2626;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #475569;
      --border: #e2e8f0;
      --success: #059669;
      --radius: 12px;
      --shadow: 0 4px 15px rgba(0,0,0,0.06);
    }
    body {
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      margin: 0;
      padding: 24px 16px;
      line-height: 1.5;
    }
    .container {
      max-width: 1050px;
      margin: 0 auto;
    }
    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 20px;
    }
    .btn-nav {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 16px;
      background: #e2e8f0;
      color: #334155;
      text-decoration: none;
      font-weight: 700;
      border-radius: 8px;
      font-size: 0.88rem;
      transition: background 0.2s;
    }
    .btn-nav:hover { background: #cbd5e1; }
    .btn-nav.primary { background: var(--primary); color: white; }
    .btn-nav.primary:hover { background: var(--primary-dark); }

    /* Header Reta Final */
    .header-box {
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      color: white;
      border-radius: var(--radius);
      padding: 28px 30px;
      margin-bottom: 24px;
      border: 1px solid #3b82f6;
      box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.25);
    }
    .header-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--accent);
      color: white;
      font-weight: 800;
      font-size: 0.78rem;
      padding: 4px 12px;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
    }
    .header-box h1 {
      margin: 0 0 8px 0;
      font-size: 1.85rem;
      font-weight: 800;
    }
    .header-box p {
      margin: 0;
      font-size: 0.96rem;
      color: #cbd5e1;
      max-width: 800px;
    }

    /* Card Meta de Hoje */
    .hoje-card {
      background: #fff;
      border: 2px solid var(--accent);
      border-radius: var(--radius);
      padding: 22px 24px;
      margin-bottom: 30px;
      box-shadow: var(--shadow);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    .hoje-info h2 {
      margin: 0 0 6px 0;
      font-size: 1.25rem;
      color: var(--accent);
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .hoje-info p {
      margin: 0;
      font-size: 0.92rem;
      color: var(--text-muted);
    }
    .btn-hoje {
      background: var(--accent);
      color: white;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 800;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3);
      transition: transform 0.2s, background 0.2s;
    }
    .btn-hoje:hover {
      background: #b91c1c;
      transform: translateY(-2px);
    }

    /* Seções */
    .section-title {
      font-size: 1.28rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin: 32px 0 14px 0;
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 2px solid var(--border);
      padding-bottom: 8px;
    }

    /* Tabela do Cronograma Dia a Dia */
    .cronograma-table {
      width: 100%;
      border-collapse: collapse;
      background: white;
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 30px;
      font-size: 0.9rem;
    }
    .cronograma-table th {
      background: #f1f5f9;
      color: var(--text);
      font-weight: 800;
      padding: 12px 16px;
      text-align: left;
      border-bottom: 2px solid var(--border);
    }
    .cronograma-table td {
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
    }
    .cronograma-table tr:hover td {
      background: #f8fafc;
    }
    .cronograma-table tr.hoje-row td {
      background: #fff1f2;
      border-left: 4px solid var(--accent);
    }
    .cronograma-table tr.prova-row td {
      background: #ecfdf5;
      border-left: 4px solid var(--success);
      font-weight: 700;
    }
    .dia-badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 0.78rem;
      text-transform: uppercase;
    }
    .badge-hoje { background: #fee2e2; color: #991b1b; }
    .badge-normal { background: #e2e8f0; color: #334155; }
    .badge-prova { background: #d1fae5; color: #065f46; }

    .btn-pdf {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      background: var(--primary);
      color: white;
      border-radius: 6px;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.82rem;
      white-space: nowrap;
      transition: background 0.2s;
    }
    .btn-pdf:hover { background: var(--primary-dark); }
    .btn-pdf.green { background: var(--success); }
    .btn-pdf.green:hover { background: #047857; }
    .btn-pdf.red { background: var(--accent); }
    .btn-pdf.red:hover { background: #b91c1c; }

    /* Grid de Provas em Destaque */
    .provas-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
      gap: 18px;
      margin-bottom: 30px;
    }
    .prova-card {
      background: white;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .prova-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }
    .prova-tag {
      font-size: 0.75rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      display: inline-block;
      margin-bottom: 8px;
    }
    .tag-real { background: #d1fae5; color: #065f46; }
    .tag-meruoca { background: #fee2e2; color: #991b1b; }
    .tag-simulado { background: #dbeafe; color: #1e40af; }
    .tag-revisao { background: #fef3c7; color: #92400e; }

    .prova-title {
      font-size: 1.1rem;
      font-weight: 800;
      margin: 0 0 6px 0;
      color: var(--text);
    }
    .prova-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 14px;
    }

    /* Documentos Oficiais */
    .docs-box {
      background: white;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow);
    }
    .doc-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 0;
      border-bottom: 1px solid var(--border);
      font-size: 0.88rem;
    }
    .doc-row:last-child { border-bottom: none; }
  </style>
</head>
<body>

  <div class="container">
    
    <div class="top-bar">
      <a href="../index.html" class="btn-nav"><i class="fas fa-arrow-left"></i> Voltar ao Gerenciador de Estudos</a>
      <a href="BANCO_ESTRATEGICO_INBRASP_GCM.html" class="btn-nav primary"><i class="fas fa-chart-line"></i> Raio-X da Banca INBRASP</a>
    </div>

    <!-- Header Reta Final -->
    <div class="header-box">
      <span class="header-tag"><i class="fas fa-flag-checkered"></i> Reta Final • 13 Dias Para a Prova</span>
      <h1>Cronograma Oficial de Provas & Treinos (05/10 a 18/10)</h1>
      <p>Todos os arquivos foram limpos e convertidos em <strong>PDFs reais</strong> para você focar apenas em resolver provas oficiais da banca e simulados idênticos ao edital de Meruoca.</p>
    </div>

    <!-- META DE HOJE -->
    <div class="hoje-card">
      <div class="hoje-info">
        <h2><i class="fas fa-crosshairs"></i> O QUE VOCÊ DEVE FAZER HOJE (Segunda-feira, 05/10):</h2>
        <p>Resolver a <strong>Prova Real Aplicada pela Banca INBRASP em 2026</strong> (Câmara de Ipaporanga — 29 Questões Reais).</p>
      </div>
      <a href="PROVA_REAL_INBRASP_2026_IPAPORANGA.pdf" target="_blank" class="btn-hoje">
        <i class="fas fa-file-pdf"></i> ABRIR PROVA REAL DE HOJE (PDF)
      </a>
    </div>

    <!-- SEÇÃO 1: CRONOGRAMA DIA A DIA -->
    <h2 class="section-title"><i class="fas fa-calendar-check" style="color: var(--primary);"></i> 1. Roteiro Dia a Dia até a Prova (05/10 a 18/10)</h2>
    <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: -6px; margin-bottom: 16px;">
      Siga esta sequência diária. Basta clicar em <strong>"Abrir PDF"</strong> no dia correspondente para praticar:
    </p>

    <table class="cronograma-table">
      <thead>
        <tr>
          <th style="width: 140px;">Data</th>
          <th>Missão do Dia (Prova / Caderno)</th>
          <th style="width: 130px;">Qtd. Questões</th>
          <th style="width: 130px; text-align: center;">Arquivo Oficial</th>
        </tr>
      </thead>
      <tbody>
        <!-- 05/10 - HOJE -->
        <tr class="hoje-row">
          <td><span class="dia-badge badge-hoje">05/10 • HOJE</span></td>
          <td><strong>Prova Real da Banca INBRASP (2026)</strong> — Prova física oficial da Câmara de Ipaporanga/CE (Português, Info, Admin e CF/88).</td>
          <td>29 Questões</td>
          <td style="text-align: center;">
            <a href="PROVA_REAL_INBRASP_2026_IPAPORANGA.pdf" target="_blank" class="btn-pdf red"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 06/10 - TER -->
        <tr>
          <td><span class="dia-badge badge-normal">06/10 • Terça</span></td>
          <td><strong>Simulado Oficial Câmara de Meruoca</strong> — Focado 100% no Edital 001/2026: Lei Orgânica de Meruoca, Regimento Interno e LIMPE.</td>
          <td>40 Questões</td>
          <td style="text-align: center;">
            <a href="SIMULADO_01_CAMARA_MERUOCA.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 07/10 - QUA -->
        <tr>
          <td><span class="dia-badge badge-normal">07/10 • Quarta</span></td>
          <td><strong>Simulado Câmara de Pires Ferreira (INBRASP)</strong> — Ênfase em Concordância, Crase, Excel e Nova Lei de Licitações (14.133).</td>
          <td>40 Questões</td>
          <td style="text-align: center;">
            <a href="SIMULADO_02_CAMARA_PIRES_FERREIRA.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 08/10 - QUI -->
        <tr>
          <td><span class="dia-badge badge-normal">08/10 • Quinta</span></td>
          <td><strong>Simulado Câmara de Ipaporanga (INBRASP)</strong> — Orações Concessivas, Regra do Hiato, Segurança, Redes e LRF.</td>
          <td>40 Questões</td>
          <td style="text-align: center;">
            <a href="SIMULADO_03_CAMARA_IPAPORANGA.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 09/10 - SEX -->
        <tr>
          <td><span class="dia-badge badge-normal">09/10 • Sexta</span></td>
          <td><strong>Simulado Câmara de Hidrolândia (INBRASP)</strong> — Crase Proibida, Art. 59 CF (Espécies Normativas), CPI e Transparência.</td>
          <td>40 Questões</td>
          <td style="text-align: center;">
            <a href="SIMULADO_04_CAMARA_HIDROLANDIA.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 10/10 - SÁB -->
        <tr>
          <td><span class="dia-badge badge-normal">10/10 • Sábado</span></td>
          <td><strong>Simulado Câmara de Pedra Branca (INBRASP)</strong> — Regência de Obedecer, Verbo Haver, Linux e Registro de Preços.</td>
          <td>40 Questões</td>
          <td style="text-align: center;">
            <a href="SIMULADO_05_CAMARA_PEDRA_BRANCA.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 11/10 - DOM -->
        <tr>
          <td><span class="dia-badge badge-normal">11/10 • Domingo</span></td>
          <td><strong>Revisão de Erros e Descanso Estratégico</strong> — Rever as questões que errou nos simulados da semana.</td>
          <td>—</td>
          <td style="text-align: center; color: var(--text-muted); font-size: 0.8rem; font-weight: 700;">Revisão</td>
        </tr>

        <!-- 12/10 - SEG -->
        <tr>
          <td><span class="dia-badge badge-normal">12/10 • Segunda</span></td>
          <td><strong>Essencial Ouro (Parte 1: Português & Administrativo)</strong> — As questões de maior incidência da banca.</td>
          <td>45 Questões</td>
          <td style="text-align: center;">
            <a href="CADERNO_ESSENCIAL_OURO_89Q.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 13/10 - TER -->
        <tr>
          <td><span class="dia-badge badge-normal">13/10 • Terça</span></td>
          <td><strong>Essencial Ouro (Parte 2: Licitações 14.133, Matemática & Redes)</strong> — Fechamento do conteúdo de ouro.</td>
          <td>44 Questões</td>
          <td style="text-align: center;">
            <a href="CADERNO_ESSENCIAL_OURO_89Q.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 14/10 - QUA -->
        <tr>
          <td><span class="dia-badge badge-normal">14/10 • Quarta</span></td>
          <td><strong>Reforço Específico: Sintaxe da Oração & Período Composto</strong> — O assunto que mais reprova em concurso.</td>
          <td>40 Questões</td>
          <td style="text-align: center;">
            <a href="CADERNO_REFORCO_PORTUGUES_40Q.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 15/10 - QUI -->
        <tr>
          <td><span class="dia-badge badge-normal">15/10 • Quinta</span></td>
          <td><strong>Treino Rápido: Controle da Administração Pública & Semântica</strong> — CF/88 Art. 31, Parecer TCE (2/3) e Parônimos.</td>
          <td>18 Questões</td>
          <td style="text-align: center;">
            <a href="CADERNO_HOJE_SEMANA_05_DIA_01.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 16/10 - SEX -->
        <tr>
          <td><span class="dia-badge badge-normal">16/10 • Sexta</span></td>
          <td><strong>Treino Rápido: Lei de Responsabilidade Fiscal (LRF) & Colocação</strong> — Despesa com pessoal no Legislativo e Próclise.</td>
          <td>18 Questões</td>
          <td style="text-align: center;">
            <a href="CADERNO_QUESTOES_SEMANA_04_DIA_04.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir PDF</a>
          </td>
        </tr>

        <!-- 17/10 - SÁB -->
        <tr>
          <td><span class="dia-badge badge-normal">17/10 • Sábado</span></td>
          <td><strong>Véspera da Prova</strong> — Leitura leve dos artigos da Lei Orgânica de Meruoca, preparar caneta preta e descansar cedo.</td>
          <td>—</td>
          <td style="text-align: center; color: var(--text-muted); font-size: 0.8rem; font-weight: 700;">Descanso</td>
        </tr>

        <!-- 18/10 - DOMINGO -->
        <tr class="prova-row">
          <td><span class="dia-badge badge-prova">18/10 • DOMINGO</span></td>
          <td><strong>🎯 DIA DA PROVA OFICIAL — CÂMARA MUNICIPAL DE MERUOCA / CE</strong></td>
          <td>40 Questões</td>
          <td style="text-align: center; color: var(--success); font-weight: 800;">APROVAÇÃO</td>
        </tr>
      </tbody>
    </table>

    <!-- SEÇÃO 2: PAINEL DIRETO DAS PROVAS EM PDF -->
    <h2 class="section-title"><i class="fas fa-folder-open" style="color: var(--primary);"></i> 2. Acesso Direto aos PDFs das Provas Oficiais & Simulados</h2>
    <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: -6px; margin-bottom: 16px;">
      Todos os arquivos estão baixados no seu computador. Clique para abrir o PDF:
    </p>

    <div class="provas-grid">
      
      <!-- CARD 1: PROVA REAL 2026 -->
      <div class="prova-card" style="border: 2px solid var(--success); background: #f0fdf4;">
        <div>
          <span class="prova-tag tag-real">⭐ 100% Real Aplicada (2026)</span>
          <h3 class="prova-title">Câmara de Ipaporanga / CE</h3>
          <p class="prova-desc">Prova oficial da banca INBRASP aplicada em 2026 com 29 questões reais de concurso de Câmara.</p>
        </div>
        <a href="PROVA_REAL_INBRASP_2026_IPAPORANGA.pdf" target="_blank" class="btn-pdf green" style="padding: 10px; justify-content: center; font-size: 0.9rem;">
          <i class="fas fa-file-pdf"></i> Abrir Prova Real (PDF)
        </a>
      </div>

      <!-- CARD 2: SIMULADO MERUOCA -->
      <div class="prova-card" style="border: 2px solid var(--accent); background: #fffcfc;">
        <div>
          <span class="prova-tag tag-meruoca">Oficial Meruoca 2026</span>
          <h3 class="prova-title">Câmara de Meruoca / CE</h3>
          <p class="prova-desc">Simulado direto no Edital 001/2026: 40 questões com Lei Orgânica de Meruoca e Regimento Interno.</p>
        </div>
        <a href="SIMULADO_01_CAMARA_MERUOCA.pdf" target="_blank" class="btn-pdf red" style="padding: 10px; justify-content: center; font-size: 0.9rem;">
          <i class="fas fa-file-pdf"></i> Abrir Simulado Meruoca (PDF)
        </a>
      </div>

      <!-- CARD 3: ESSENCIAL OURO -->
      <div class="prova-card" style="border: 2px solid #f59e0b; background: #fffdf5;">
        <div>
          <span class="prova-tag tag-revisao">Caderno de Ouro • 89Q</span>
          <h3 class="prova-title">Essencial Ouro (Reta Final)</h3>
          <p class="prova-desc">As 89 questões dos temas mais frequentes da banca (Sintaxe, Licitações 14.133, Concordância e RLM).</p>
        </div>
        <a href="CADERNO_ESSENCIAL_OURO_89Q.pdf" target="_blank" class="btn-pdf" style="background: #b45309; padding: 10px; justify-content: center; font-size: 0.9rem;">
          <i class="fas fa-file-pdf"></i> Abrir Essencial Ouro (PDF)
        </a>
      </div>

      <!-- CARD 4: PIRES FERREIRA -->
      <div class="prova-card">
        <div>
          <span class="prova-tag tag-simulado">Câmara Municipal • 40Q</span>
          <h3 class="prova-title">Câmara de Pires Ferreira / CE</h3>
          <p class="prova-desc">40 questões padrão banca: Português, Informática, RLM, Licitações e Direito Administrativo.</p>
        </div>
        <a href="SIMULADO_02_CAMARA_PIRES_FERREIRA.pdf" target="_blank" class="btn-pdf" style="padding: 10px; justify-content: center;">
          <i class="fas fa-file-pdf"></i> Abrir Simulado Pires Ferreira (PDF)
        </a>
      </div>

      <!-- CARD 5: IPAPORANGA COMPLETA -->
      <div class="prova-card">
        <div>
          <span class="prova-tag tag-simulado">Câmara Municipal • 40Q</span>
          <h3 class="prova-title">Câmara de Ipaporanga / CE</h3>
          <p class="prova-desc">40 questões padrão banca: LRF, Orçamento, Redes de Computadores e Gramática.</p>
        </div>
        <a href="SIMULADO_03_CAMARA_IPAPORANGA.pdf" target="_blank" class="btn-pdf" style="padding: 10px; justify-content: center;">
          <i class="fas fa-file-pdf"></i> Abrir Simulado Ipaporanga (PDF)
        </a>
      </div>

      <!-- CARD 6: HIDROLÂNDIA -->
      <div class="prova-card">
        <div>
          <span class="prova-tag tag-simulado">Câmara Municipal • 40Q</span>
          <h3 class="prova-title">Câmara de Hidrolândia / CE</h3>
          <p class="prova-desc">40 questões padrão banca: Processo Legislativo, CPI, Transparência e Crase.</p>
        </div>
        <a href="SIMULADO_04_CAMARA_HIDROLANDIA.pdf" target="_blank" class="btn-pdf" style="padding: 10px; justify-content: center;">
          <i class="fas fa-file-pdf"></i> Abrir Simulado Hidrolândia (PDF)
        </a>
      </div>

    </div>

    <!-- SEÇÃO 3: DOCUMENTOS OFICIAIS DO CONCURSO DE MERUOCA -->
    <h2 class="section-title"><i class="fas fa-file-contract" style="color: var(--primary);"></i> 3. Documentos Oficiais da Banca INBRASP (PDFs Originais)</h2>
    <div class="docs-box">
      <div class="doc-row">
        <div>
          <strong>Edital de Abertura nº 001/2026 — Câmara de Meruoca / CE</strong>
          <div style="font-size: 0.78rem; color: var(--text-muted);">Conteúdo programático e regras oficiais do seu concurso</div>
        </div>
        <a href="originais_pdf/ID_726_20260828_133904_EDITAL%20001.2026%20-%20CAMARA%20DE%20MERUOCA%20-%2028.08.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir Edital</a>
      </div>
      <div class="doc-row">
        <div>
          <strong>Cronograma Oficial de Atividades — Câmara de Meruoca</strong>
          <div style="font-size: 0.78rem; color: var(--text-muted);">Datas de prova, gabarito e recursos confirmadas pela banca</div>
        </div>
        <a href="originais_pdf/ID_726_20260828_144712_CRONOGRAMA%20DE%20ATIVIDADES%20-%20CAMARA%20DE%20MERUOCA.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir Cronograma</a>
      </div>
      <div class="doc-row">
        <div>
          <strong>Resultado dos Pedidos de Isenção da Taxa de Inscrição</strong>
          <div style="font-size: 0.78rem; color: var(--text-muted);">Publicação oficial homologada da banca</div>
        </div>
        <a href="originais_pdf/ID_726_20260916_155456_MERUOCA%20DEFINITIVO%20ISEN%C7AO.pdf" target="_blank" class="btn-pdf"><i class="fas fa-file-pdf"></i> Abrir Documento</a>
      </div>
    </div>

  </div>

</body>
</html>
"""

with open(r'c:\Users\Ruan Gomes\Downloads\Meruoca\provas\CENTRAL_DE_PROVAS.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("CENTRAL_DE_PROVAS.html limpo e reestruturado como Cronograma de Reta Final!")

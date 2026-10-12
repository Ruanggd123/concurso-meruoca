import sys
sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>CENTRAL DE PROVAS & DOCUMENTOS OFICIAIS — BANCA INBRASP (MERUOCA 2026)</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --success: #10b981;
      --purple: #8b5cf6;
      --orange: #f59e0b;
      --danger: #ef4444;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    }
    body {
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      margin: 0;
      padding: 30px 20px;
    }
    .container {
      max-width: 1150px;
      margin: 0 auto;
    }
    .header {
      text-align: center;
      margin-bottom: 24px;
    }
    .header h1 {
      font-size: 2.1rem;
      font-weight: 800;
      color: #1e3a8a;
      margin-bottom: 8px;
    }
    .header p {
      font-size: 1rem;
      color: var(--text-muted);
      max-width: 820px;
      margin: 0 auto;
    }
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }
    .stat-card {
      background: var(--card-bg);
      padding: 16px 18px;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .stat-icon {
      width: 46px;
      height: 46px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
    }
    .stat-icon.blue { background: #dbeafe; color: #1d4ed8; }
    .stat-icon.green { background: #d1fae5; color: #047857; }
    .stat-icon.purple { background: #ede9fe; color: #6d28d9; }
    .stat-icon.orange { background: #fef3c7; color: #b45309; }
    .stat-val { font-size: 1.35rem; font-weight: 800; }
    .stat-lbl { font-size: 0.78rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase; }

    /* Guia de Início Rápido */
    .guia-box {
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      color: white;
      border-radius: var(--radius);
      padding: 24px 26px;
      margin-bottom: 30px;
      box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.3);
      border: 1px solid #3b82f6;
    }
    .guia-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #dc2626;
      color: white;
      font-weight: 800;
      font-size: 0.75rem;
      padding: 4px 12px;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
    }
    .guia-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-top: 18px;
    }
    .guia-step {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.18);
      border-radius: 10px;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .guia-step:hover {
      background: rgba(255, 255, 255, 0.14);
    }
    .guia-step-num {
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .guia-step-title {
      font-size: 1.05rem;
      font-weight: 800;
      margin-bottom: 8px;
      color: #ffffff;
    }
    .guia-step-desc {
      font-size: 0.85rem;
      color: #cbd5e1;
      line-height: 1.45;
      margin-bottom: 14px;
    }

    /* Menu de atalhos rápidos */
    .quick-nav {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 24px;
      padding: 10px 14px;
      background: white;
      border: 1px solid var(--border);
      border-radius: 10px;
    }
    .quick-nav a {
      font-size: 0.82rem;
      font-weight: 700;
      color: #334155;
      text-decoration: none;
      padding: 6px 12px;
      border-radius: 6px;
      background: #f1f5f9;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .quick-nav a:hover {
      background: #e2e8f0;
      color: var(--primary);
    }
    .quick-nav a.active-link {
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #fecaca;
    }

    .section-heading {
      font-size: 1.3rem;
      font-weight: 800;
      color: #0f172a;
      margin: 34px 0 14px 0;
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 2px solid var(--border);
      padding-bottom: 8px;
    }
    .section-desc {
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-top: -6px;
      margin-bottom: 16px;
      line-height: 1.45;
    }

    .exams-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
      margin-bottom: 20px;
    }
    .exam-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .exam-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1);
    }
    .exam-badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 10px;
    }
    .badge-blue { background: #dbeafe; color: #1e40af; }
    .badge-green { background: #d1fae5; color: #065f46; }
    .badge-purple { background: #ede9fe; color: #5b21b6; }
    .badge-orange { background: #fef3c7; color: #92400e; }
    .badge-red { background: #fee2e2; color: #991b1b; }

    .exam-title {
      font-size: 1.12rem;
      font-weight: 800;
      margin: 0 0 8px 0;
      color: var(--text-main);
    }
    .exam-desc {
      font-size: 0.84rem;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 14px;
    }
    .exam-features {
      list-style: none;
      padding: 0;
      margin: 0 0 16px 0;
      font-size: 0.82rem;
      color: var(--text-main);
    }
    .exam-features li {
      margin-bottom: 5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .exam-features li i {
      color: var(--success);
    }
    .btn-action {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      padding: 10px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.88rem;
      color: white;
      background: var(--primary);
      transition: background 0.2s;
      box-sizing: border-box;
    }
    .btn-action:hover {
      background: var(--primary-dark);
    }
    .back-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 16px;
      background: #e2e8f0;
      color: #334155;
      text-decoration: none;
      font-weight: 700;
      border-radius: 8px;
      font-size: 0.9rem;
      transition: background 0.2s;
    }
    .back-btn:hover {
      background: #cbd5e1;
    }

    /* Repositório de Documentos Baixados */
    .download-repo-box {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow);
      margin-top: 20px;
    }
    .files-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }
    .files-table th {
      background: #f1f5f9;
      padding: 10px 14px;
      text-align: left;
      font-weight: 700;
      color: #475569;
      border-bottom: 2px solid var(--border);
    }
    .files-table td {
      padding: 10px 14px;
      border-bottom: 1px solid var(--border);
    }
    .files-table tr:hover td {
      background: #f8fafc;
    }
    .file-badge {
      font-size: 0.75rem;
      padding: 2px 6px;
      background: #fee2e2;
      color: #b91c1c;
      border-radius: 4px;
      font-weight: 700;
    }

    details.archive-group {
      background: white;
      border: 1px solid var(--border);
      border-radius: 10px;
      margin-bottom: 14px;
      padding: 12px 18px;
    }
    details.archive-group summary {
      font-weight: 800;
      font-size: 1rem;
      color: #1e3a8a;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
    }
    details.archive-group[open] summary {
      margin-bottom: 16px;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 8px;
    }
  </style>
</head>
<body>

  <div class="container">
    <div style="display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px;">
      <a href="../index.html" class="back-btn"><i class="fas fa-arrow-left"></i> Voltar ao Gerenciador Principal</a>
      <a href="BANCO_ESTRATEGICO_INBRASP_GCM.html" class="back-btn" style="background: #1e3a8a; color: white;">
        <i class="fas fa-chart-line"></i> Ver Raio-X & Análise da Banca (INBRASP)
      </a>
    </div>

    <div class="header">
      <h1>🏛️ Central de Provas & Treinos INBRASP</h1>
      <p>Material completo organizado para a Câmara de Meruoca 2026: Prova Real da banca, Cadernos Diários de 18Q, Simulados de Câmaras e Documentos Oficiais.</p>
    </div>

    <!-- Estatísticas Globais -->
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-icon blue"><i class="fas fa-file-signature"></i></div>
        <div>
          <div class="stat-val">Prova Real</div>
          <div class="stat-lbl">INBRASP 2026 (Ipaporanga)</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon green"><i class="fas fa-tasks"></i></div>
        <div>
          <div class="stat-val">657</div>
          <div class="stat-lbl">Questões de Treino (A, B, C, D)</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon purple"><i class="fas fa-layer-group"></i></div>
        <div>
          <div class="stat-val">5 Simulados</div>
          <div class="stat-lbl">Completos de 40Q (200Q)</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon orange"><i class="fas fa-print"></i></div>
        <div>
          <div class="stat-val">15+ Cadernos</div>
          <div class="stat-lbl">Prontos p/ Impressão (PDF)</div>
        </div>
      </div>
    </div>

    <!-- GUIA PRÁTICO: POR ONDE COMEÇAR -->
    <div class="guia-box" id="guiaInicio">
      <span class="guia-badge"><i class="fas fa-compass"></i> Guia Rápido de Estudos</span>
      <h2 style="margin: 0; font-size: 1.45rem; font-weight: 800;">🧭 Não sabe por onde começar? Siga este roteiro em 3 passos:</h2>
      <p style="margin: 6px 0 0 0; font-size: 0.92rem; color: #cbd5e1;">
        Não tente fazer todos os cadernos de uma vez. Vá direto ao que mais importa hoje:
      </p>

      <div class="guia-grid">
        
        <!-- PASSO 1 -->
        <div class="guia-step" style="border-top: 4px solid #ef4444;">
          <div>
            <div class="guia-step-num" style="color: #fca5a5;">
              <i class="fas fa-fire"></i> PASSO 1 • HOJE (Meta Diária)
            </div>
            <div class="guia-step-title">Fazer o Caderno de Hoje</div>
            <div class="guia-step-desc">
              Apenas <strong>18 questões</strong> focadas: 10 de Controle da Administração Pública + 8 de Português (Semântica). Curto e sem sobrecarga.
            </div>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_05_DIA_01_28_09_2026.html" target="_blank" class="btn-action" style="background: #dc2626;">
            <i class="fas fa-play"></i> Abrir Caderno de Hoje (18Q)
          </a>
        </div>

        <!-- PASSO 2 -->
        <div class="guia-step" style="border-top: 4px solid #10b981;">
          <div>
            <div class="guia-step-num" style="color: #6ee7b7;">
              <i class="fas fa-trophy"></i> PASSO 2 • FIM DE SEMANA (Simulação Real)
            </div>
            <div class="guia-step-title">Prova Real de Ipaporanga 2026</div>
            <div class="guia-step-desc">
              As <strong>29 questões reais</strong> aplicadas pela banca INBRASP este ano. Faça com cronômetro para medir sua pontuação real.
            </div>
          </div>
          <a href="PROVA_REAL_INBRASP_2026_IPAPORANGA.html" target="_blank" class="btn-action" style="background: #059669;">
            <i class="fas fa-file-signature"></i> Abrir Prova Real 2026
          </a>
        </div>

        <!-- PASSO 3 -->
        <div class="guia-step" style="border-top: 4px solid #3b82f6;">
          <div>
            <div class="guia-step-num" style="color: #93c5fd;">
              <i class="fas fa-star"></i> PASSO 3 • REVISÃO (Quando tiver tempo)
            </div>
            <div class="guia-step-title">Caderno Essencial Ouro (89Q)</div>
            <div class="guia-step-desc">
              O melhor resumo das semanas anteriores: o que mais cai de Sintaxe, Concordância, Licitações 14.133 e Matemática.
            </div>
          </div>
          <a href="CADERNO_ESSENCIAL_OURO_89Q.html" target="_blank" class="btn-action" style="background: #2563eb;">
            <i class="fas fa-gem"></i> Abrir Essencial Ouro (89Q)
          </a>
        </div>

      </div>
    </div>

    <!-- Menu de Navegação Rápida entre Seções -->
    <div class="quick-nav">
      <span style="font-size: 0.8rem; font-weight: 800; color: #64748b; display: flex; align-items: center; gap: 4px; padding: 4px 6px;">
        <i class="fas fa-bars"></i> Pular para:
      </span>
      <a href="#secHoje" class="active-link"><i class="fas fa-calendar-day"></i> 1. Caderno de Hoje (S5 D1)</a>
      <a href="#secSemana4"><i class="fas fa-clock-rotate-left"></i> 2. Treinos Recentes (Semana 4)</a>
      <a href="#secProvaReal"><i class="fas fa-trophy"></i> 3. Prova Real 2026</a>
      <a href="#secResumo"><i class="fas fa-star"></i> 4. Revisão & Resgate</a>
      <a href="#secSimulados"><i class="fas fa-landmark"></i> 5. Simulados 40Q</a>
      <a href="#secArquivo"><i class="fas fa-box-archive"></i> 6. Arquivo Histórico</a>
      <a href="#secDocs"><i class="fas fa-file-pdf"></i> 7. Documentos Oficiais</a>
    </div>

    <!-- SEÇÃO 1: CADERNO DE HOJE -->
    <div id="secHoje"></div>
    <h2 class="section-heading"><i class="fas fa-fire" style="color: #dc2626;"></i> 1. Meta Diária de Hoje (Semana 5 • Dia 1)</h2>
    <p class="section-desc">
      O treino do dia de hoje (<strong>28/09/2026</strong>). São 18 questões objetivas com alternativas de tamanho rigorosamente balanceadas:
    </p>

    <div class="exams-grid">
      <!-- CADERNO SEMANA 5 / DIA 1 (28/09/2026 - HOJE) -->
      <div class="exam-card" style="border: 2px solid #dc2626; background: #fffcfc;">
        <div>
          <span class="exam-badge" style="background: #fee2e2; color: #b91c1c; font-weight: 800;">⭐ CADERNO HOJE (28/09/2026) • 18 QUESTÕES</span>
          <h3 class="exam-title" style="color: #b91c1c;">Semana 5 • Dia 1 — 18 Questões</h3>
          <p class="exam-desc">Treino oficial de hoje: <strong>10 Controle da Administração Pública</strong> (CF/88 Art. 31 e 74, controle externo e interno, parecer do TCE com quórum de 2/3, STF Temas 157/835, autotutela) + <strong>8 Português</strong> (Semântica: sinonímia, antonímia, parônimos ratificar/retificar, deferir/diferir, eminente/iminente, homônimos homófonos).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle" style="color: #dc2626;"></i> 18 Questões (A, B, C, D) com alternativas equilibradas</li>
            <li><i class="fas fa-check-circle" style="color: #dc2626;"></i> Gabarito com distribuição equilibrada (5 A, 5 B, 4 C, 4 D)</li>
            <li><i class="fas fa-check-circle" style="color: #dc2626;"></i> Folha Óptica de Respostas (Simulado Pré-Prova)</li>
            <li><i class="fas fa-check-circle" style="color: #dc2626;"></i> Gabarito Oficial Fundamentado (CF/88, STF e Gramática Normativa)</li>
          </ul>
        </div>
        <a href="CADERNO_QUESTOES_SEMANA_05_DIA_01_28_09_2026.html" target="_blank" class="btn-action" style="background: #dc2626;">
          <i class="fas fa-print"></i> Abrir Caderno de Hoje (PDF)
        </a>
      </div>
    </div>

    <!-- SEÇÃO 2: TREINOS RECENTES DA SEMANA 4 -->
    <div id="secSemana4"></div>
    <h2 class="section-heading"><i class="fas fa-calendar-week" style="color: #2563eb;"></i> 2. Treinos Recentes (Semana 4 — Formato Enxuto 18Q)</h2>
    <p class="section-desc">
      Cadernos aplicados nos últimos dias da Semana 4 para você manter a regularidade:
    </p>

    <div class="exams-grid">
      <!-- CADERNO SEMANA 4 / DIA 4 (24/09/2026) -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-blue">📅 CADERNO (24/09/2026)</span>
          <h3 class="exam-title" style="color: #1e40af;">Semana 4 • Dia 4 — 18 Questões</h3>
          <p class="exam-desc">Treino em formato enxuto: <strong>10 LRF</strong> (LC 101/2000: limites de pessoal no Legislativo, vedações no fim de mandato, RGF e RREO) + <strong>8 Português</strong> (Colocação Pronominal: próclise, ênclise e mesóclise).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 18 Questões (A, B, C, D) com alternativas equilibradas</li>
            <li><i class="fas fa-check-circle"></i> Proporção oficial de matérias com distratores refinados</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica de Respostas</li>
            <li><i class="fas fa-check-circle"></i> Gabarito Oficial Fundamentado (LC 101/00)</li>
          </ul>
        </div>
        <a href="CADERNO_QUESTOES_SEMANA_04_DIA_04_24_09_2026.html" target="_blank" class="btn-action">
          <i class="fas fa-print"></i> Abrir Caderno Semana 4 Dia 4 (PDF)
        </a>
      </div>

      <!-- CADERNO SEMANA 4 / DIA 3 (23/09/2026) -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-blue">📅 CADERNO (23/09/2026)</span>
          <h3 class="exam-title" style="color: #1e40af;">Semana 4 • Dia 3 — 18 Questões</h3>
          <p class="exam-desc">Treino em formato enxuto: <strong>10 Orçamento Público</strong> (PPA, LDO, LOA, princípios e créditos) + <strong>8 Informática</strong> (E-mail, Thunderbird, SMTP/IMAP/POP, colaboração digital).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 18 Questões (A, B, C, D) sem pegadinhas-dica</li>
            <li><i class="fas fa-check-circle"></i> Proporção oficial de matérias</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica de Respostas</li>
            <li><i class="fas fa-check-circle"></i> Gabarito Oficial Fundamentado (CF/88 e Lei 4.320/64)</li>
          </ul>
        </div>
        <a href="CADERNO_QUESTOES_SEMANA_04_DIA_03_23_09_2026.html" target="_blank" class="btn-action">
          <i class="fas fa-print"></i> Abrir Caderno Semana 4 Dia 3 (PDF)
        </a>
      </div>

      <!-- CADERNO SEMANA 4 / DIA 2 (22/09/2026) -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-blue">📅 CADERNO (22/09/2026)</span>
          <h3 class="exam-title" style="color: #1e40af;">Semana 4 • Dia 2 — 18 Questões</h3>
          <p class="exam-desc">Treino em formato enxuto: <strong>10 Regimento Interno</strong> (moções, espécies, plenário e comissões) + <strong>8 RLM</strong> (silogismos, categóricas, De Morgan e Venn).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 18 Questões (A, B, C, D)</li>
            <li><i class="fas fa-check-circle"></i> Distratores plausíveis + gabarito natural</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica de Respostas</li>
            <li><i class="fas fa-check-circle"></i> Gabarito Oficial Fundamentado</li>
          </ul>
        </div>
        <a href="CADERNO_QUESTOES_SEMANA_04_DIA_02_22_09_2026.html" target="_blank" class="btn-action">
          <i class="fas fa-print"></i> Abrir Caderno Semana 4 Dia 2 (PDF)
        </a>
      </div>

      <!-- CADERNO SEMANA 4 / DIA 1 (21/09/2026) -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-blue">📅 CADERNO (21/09/2026)</span>
          <h3 class="exam-title" style="color: #1e40af;">Semana 4 • Dia 1 — 18 Questões</h3>
          <p class="exam-desc">Treino em formato enxuto: <strong>12 Regimento Interno</strong> (Mesa, Presidente, sessões e comissões) + <strong>6 Língua Portuguesa</strong> (Regência Verbal & Nominal).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 18 Questões (A, B, C, D)</li>
            <li><i class="fas fa-check-circle"></i> Foco no Regimento da Câmara de Meruoca</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica de Respostas</li>
            <li><i class="fas fa-check-circle"></i> Gabarito Oficial Fundamentado</li>
          </ul>
        </div>
        <a href="CADERNO_QUESTOES_SEMANA_04_DIA_01_21_09_2026.html" target="_blank" class="btn-action">
          <i class="fas fa-print"></i> Abrir Caderno Semana 4 Dia 1 (PDF)
        </a>
      </div>
    </div>

    <!-- SEÇÃO 3: PROVA REAL APLICADA PELA BANCA -->
    <div id="secProvaReal"></div>
    <h2 class="section-heading"><i class="fas fa-trophy" style="color: #059669;"></i> 3. Prova Real Aplicada pela Banca (INBRASP 2026)</h2>
    <p class="section-desc">
      Esta é a <strong>única prova real física transcrita na íntegra</strong> com número do QConcursos. Guarde para o seu simulado de fim de semana:
    </p>

    <div class="exams-grid">
      <!-- PROVA REAL 2026: IPAPORANGA -->
      <div class="exam-card" style="border: 2px solid #059669; background: #f0fdf4;">
        <div>
          <span class="exam-badge" style="background: #d1fae5; color: #065f46; font-weight: 800;">⭐ PROVA 100% REAL APLICADA (2026)</span>
          <h3 class="exam-title" style="color: #065f46;">Câmara de Ipaporanga / CE — 2026</h3>
          <p class="exam-desc">Caderno Oficial com as <strong>29 questões reais de 2026 da Banca INBRASP</strong> (Direito Administrativo 14.133, CF/88, Atos, Arquivologia, Administração, Word/Excel, Matemática e Português).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle" style="color: #059669;"></i> Questões Reais da Banca INBRASP (2026)</li>
            <li><i class="fas fa-check-circle" style="color: #059669;"></i> Padrão Oficial de 4 Alternativas (A, B, C, D)</li>
            <li><i class="fas fa-check-circle" style="color: #059669;"></i> Folha Óptica de Respostas (Simulação de 3 horas)</li>
            <li><i class="fas fa-check-circle" style="color: #059669;"></i> Gabarito Oficial Comentado com Artigos de Lei</li>
          </ul>
        </div>
        <a href="PROVA_REAL_INBRASP_2026_IPAPORANGA.html" target="_blank" class="btn-action" style="background: #059669;">
          <i class="fas fa-file-signature"></i> Abrir Prova Real 2026 (PDF)
        </a>
      </div>
    </div>

    <!-- SEÇÃO 4: CADERNOS ESPECIAIS DE REVISÃO E RESGATE -->
    <div id="secResumo"></div>
    <h2 class="section-heading"><i class="fas fa-gem" style="color: #b45309;"></i> 4. Cadernos Especiais de Revisão & Resgate</h2>
    <p class="section-desc">
      Use estes cadernos quando quiser revisar pontos fracos ou recuperar matérias acumuladas sem precisar fazer tudo do zero:
    </p>

    <div class="exams-grid">
      <!-- ESSENCIAL OURO 89Q -->
      <div class="exam-card" style="border: 2px solid #f59e0b; background: #fffdf5;">
        <div>
          <span class="exam-badge" style="background: #fef3c7; color: #b45309; font-weight: 800;">⭐ ESSENCIAL OURO — 89Q</span>
          <h3 class="exam-title" style="color: #b45309;">Essencial Ouro — O Que Mais Cai</h3>
          <p class="exam-desc">As 89 questões de maior incidência: <strong>Sintaxe (10)</strong> + <strong>Período (12)</strong> + <strong>Concordância (10)</strong> + <strong>Admin (11)</strong> + <strong>Matemática (12)</strong> + <strong>14.133 Licitações (9)</strong> + <strong>Contratos (20)</strong> + <strong>Redes (5)</strong>.</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle" style="color: #d97706;"></i> 89 Questões Modelo INBRASP (A, B, C, D)</li>
            <li><i class="fas fa-check-circle" style="color: #d97706;"></i> Organizado em 8 partes para fazer em 3 sessões</li>
            <li><i class="fas fa-check-circle" style="color: #d97706;"></i> Folha Óptica + Gabarito Fundamentado</li>
          </ul>
        </div>
        <a href="CADERNO_ESSENCIAL_OURO_89Q.html" target="_blank" class="btn-action" style="background: #b45309;">
          <i class="fas fa-gem"></i> Abrir Essencial OURO (PDF)
        </a>
      </div>

      <!-- PROVÃO DE RESGATE — 137Q -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-purple">⭐ PROVÃO DE RESGATE — 137Q</span>
          <h3 class="exam-title" style="color: #5b21b6;">Provão de Resgate — Dias 11 a 17</h3>
          <p class="exam-desc">Compilado completo de pendências: PT Sintaxe (20), PT Período (20), Admin Extinção (17), Matemática (20), Lei 14.133 (20), Redes (10) e Contratos/Concordância (30).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 137 Questões Modelo INBRASP (A, B, C, D)</li>
            <li><i class="fas fa-check-circle"></i> Dividido em 7 partes com plano sugerido</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica + Gabarito Fundamentado</li>
          </ul>
        </div>
        <a href="CADERNO_PROVAO_RESGATE_137Q.html" target="_blank" class="btn-action" style="background: #6d28d9;">
          <i class="fas fa-layer-group"></i> Abrir Provão de Resgate (PDF)
        </a>
      </div>

      <!-- REFORÇO PORTUGUÊS SINTAXE E PERÍODO 40Q -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-blue">🎯 REFORÇO ESPECÍFICO — 40Q</span>
          <h3 class="exam-title" style="color: #1e40af;">Reforço: Sintaxe da Oração & Período</h3>
          <p class="exam-desc">Caderno focado no calcanhar de Aquiles dos concursos: 20 questões de termos da oração (sujeito, complementos) + 20 questões de período composto (substantivas, adjetivas e adverbiais).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 40 Questões com macetes da banca</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica + Gabarito Passo a Passo</li>
          </ul>
        </div>
        <a href="CADERNO_REFORCO_PORTUGUES_SINTAXE_PERIODO_40Q.html" target="_blank" class="btn-action">
          <i class="fas fa-book-reader"></i> Abrir Reforço Português (PDF)
        </a>
      </div>
    </div>

    <!-- SEÇÃO 5: SIMULADOS COMPLETOS DE CÂMARAS (40Q CADA) -->
    <div id="secSimulados"></div>
    <h2 class="section-heading"><i class="fas fa-landmark" style="color: #1e3a8a;"></i> 5. Simulados Completos de 40 Questões (Estilo Câmara Municipal)</h2>
    <p class="section-desc">
      Simulados fechados de 40 questões (10 Português + 5 Informática + 5 RLM + 20 Específicas) modelados a partir dos editais oficiais da banca:
    </p>

    <div class="exams-grid">
      <!-- PROVA 01: MERUOCA -->
      <div class="exam-card" style="border: 2px solid #2563eb;">
        <div>
          <span class="exam-badge badge-blue">Simulado Mestre 01 • Oficial</span>
          <h3 class="exam-title">Câmara de Meruoca / CE</h3>
          <p class="exam-desc">Simulado direto no Edital nº 001/2026: Lei Orgânica de Meruoca, Regimento, LIMPE, Mandado de Segurança e disciplinas básicas.</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 40 Questões no Modelo Oficial</li>
            <li><i class="fas fa-check-circle"></i> 10 PT + 5 Info + 5 RLM + 20 Específicas</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica + Gabarito Comentado</li>
          </ul>
        </div>
        <a href="PROVA_OFICIAL_SIMULADO_01_INBRASP.html" target="_blank" class="btn-action">
          <i class="fas fa-print"></i> Abrir Simulado Meruoca (PDF)
        </a>
      </div>

      <!-- PROVA 02: PIRES FERREIRA -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-green">Simulado 02 • Câmara</span>
          <h3 class="exam-title">Câmara de Pires Ferreira / CE</h3>
          <p class="exam-desc">Ênfase em Concordância, Crase, Excel (fórmulas e referências), Juros Simples, Estabilidade e Pregão na 14.133.</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 40 Questões (A, B, C, D)</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica + Gabarito Comentado</li>
          </ul>
        </div>
        <a href="PROVA_02_CAMARA_PIRES_FERREIRA_INBRASP.html" target="_blank" class="btn-action" style="background: #047857;">
          <i class="fas fa-print"></i> Abrir Prova 02 (PDF)
        </a>
      </div>

      <!-- PROVA 03: IPAPORANGA -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-purple">Simulado 03 • Câmara</span>
          <h3 class="exam-title">Câmara de Ipaporanga / CE</h3>
          <p class="exam-desc">Questões sobre Orações Concessivas, Regra do Hiato, Criptografia Assimétrica, Firewall, Regra de 3 e PPA.</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 40 Questões (A, B, C, D)</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica + Gabarito Comentado</li>
          </ul>
        </div>
        <a href="PROVA_03_CAMARA_IPAPORANGA_INBRASP.html" target="_blank" class="btn-action" style="background: #6d28d9;">
          <i class="fas fa-print"></i> Abrir Prova 03 (PDF)
        </a>
      </div>

      <!-- PROVA 04: HIDROLÂNDIA -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-orange">Simulado 04 • Câmara</span>
          <h3 class="exam-title">Câmara de Hidrolândia / CE</h3>
          <p class="exam-desc">Foco em Crase Proibida, Catáfora, Redes LAN/WAN, HTTPS, DNS, Sistemas Lineares, Art. 59 CF e CPI.</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 40 Questões (A, B, C, D)</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica + Gabarito Comentado</li>
          </ul>
        </div>
        <a href="PROVA_04_CAMARA_HIDROLANDIA_INBRASP.html" target="_blank" class="btn-action" style="background: #9333ea;">
          <i class="fas fa-print"></i> Abrir Prova 04 (PDF)
        </a>
      </div>

      <!-- PROVA 05: PEDRA BRANCA -->
      <div class="exam-card">
        <div>
          <span class="exam-badge badge-red">Simulado 05 • Câmara</span>
          <h3 class="exam-title">Câmara de Pedra Branca / CE</h3>
          <p class="exam-desc">Cobrança de Regência de Obedecer, Verbo Haver, Linux chmod, Python básico, De Morgan e Registro de Preços (SRP).</p>
          <ul class="exam-features">
            <li><i class="fas fa-check-circle"></i> 40 Questões (A, B, C, D)</li>
            <li><i class="fas fa-check-circle"></i> Folha Óptica + Gabarito Comentado</li>
          </ul>
        </div>
        <a href="PROVA_05_CAMARA_PEDRA_BRANCA_INBRASP.html" target="_blank" class="btn-action" style="background: #b45309;">
          <i class="fas fa-print"></i> Abrir Prova 05 (PDF)
        </a>
      </div>
    </div>

    <!-- SEÇÃO 6: ARQUIVO HISTÓRICO DE CADERNOS ANTERIORES -->
    <div id="secArquivo"></div>
    <h2 class="section-heading"><i class="fas fa-box-archive" style="color: #64748b;"></i> 6. Arquivo Histórico de Cadernos Diários (Semanas 1, 2 e 3)</h2>
    <p class="section-desc">
      Todos os cadernos das semanas anteriores ficam guardados aqui em blocos sanfonados. Você só precisa abrir caso queira treinar um assunto específico do passado:
    </p>

    <!-- SEMANA 3 -->
    <details class="archive-group" open>
      <summary>
        <span><i class="fas fa-folder-open" style="color: #2563eb; margin-right: 8px;"></i> Semana 3 (14/09 a 18/09) — 5 Cadernos</span>
        <span style="font-size: 0.8rem; color: #64748b; font-weight: normal;">Clique para recolher/expandir</span>
      </summary>
      <div class="exams-grid" style="margin-top: 14px;">
        <!-- S3 D5 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">18/09/2026 • 18Q</span>
            <h4 class="exam-title">Semana 3 • Dia 5</h4>
            <p class="exam-desc">10 Lei Orgânica (Processo Legislativo) + 8 Geometria Básica.</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_03_DIA_05_18_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S3 D5</a>
        </div>
        <!-- S3 D4 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">17/09/2026 • 30Q</span>
            <h4 class="exam-title">Semana 3 • Dia 4</h4>
            <p class="exam-desc">20 Lei 14.133 (Contratos e Sanções) + 10 Português (Concordância).</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_03_DIA_04_17_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S3 D4</a>
        </div>
        <!-- S3 D3 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">16/09/2026 • 30Q</span>
            <h4 class="exam-title">Semana 3 • Dia 3</h4>
            <p class="exam-desc">20 Lei 14.133 (Princípios e Planejamento) + 10 Informática (Internet/Navegadores).</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_03_DIA_03_16_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S3 D3</a>
        </div>
        <!-- S3 D2 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">15/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 3 • Dia 2</h4>
            <p class="exam-desc">20 Direito Administrativo (Atos e Invalidação) + 20 Matemática & RLM.</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_03_DIA_02_15_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S3 D2</a>
        </div>
        <!-- S3 D1 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">14/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 3 • Dia 1</h4>
            <p class="exam-desc">20 Direito Administrativo (Requisitos e Atributos) + 20 Português (Período Composto).</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_03_DIA_01_14_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S3 D1</a>
        </div>
      </div>
    </details>

    <!-- SEMANA 2 -->
    <details class="archive-group">
      <summary>
        <span><i class="fas fa-folder" style="color: #2563eb; margin-right: 8px;"></i> Semana 2 (07/09 a 11/09) — 5 Cadernos</span>
        <span style="font-size: 0.8rem; color: #64748b; font-weight: normal;">Clique para expandir</span>
      </summary>
      <div class="exams-grid" style="margin-top: 14px;">
        <!-- S2 D5 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">11/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 2 • Dia 5</h4>
            <p class="exam-desc">20 Técnica Legislativa (LC 95/98) + 20 Português (Sintaxe da Oração).</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_02_DIA_05_11_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S2 D5</a>
        </div>
        <!-- S2 D4 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">10/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 2 • Dia 4</h4>
            <p class="exam-desc">20 Técnico Legislativo (Sessões Plenárias) + 20 Matemática/RLM.</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_02_DIA_04_10_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S2 D4</a>
        </div>
        <!-- S2 D3 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">09/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 2 • Dia 3</h4>
            <p class="exam-desc">20 Processo Legislativo (CF art. 59) + 20 Informática (Word e Excel).</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_02_DIA_03_09_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S2 D3</a>
        </div>
        <!-- S2 D2 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">08/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 2 • Dia 2</h4>
            <p class="exam-desc">20 Técnico Legislativo (Mesa Diretora) + 20 Português (Morfologia e Verbos).</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_02_DIA_02_08_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S2 D2</a>
        </div>
        <!-- S2 D1 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">07/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 2 • Dia 1</h4>
            <p class="exam-desc">20 D. Constitucional (CF Arts. 18 a 31) + 20 Português (Formação de Palavras).</p>
          </div>
          <a href="CADERNO_QUESTOES_SEMANA_02_DIA_01_07_09_2026.html" target="_blank" class="btn-action">Abrir Caderno S2 D1</a>
        </div>
      </div>
    </details>

    <!-- SEMANA 1 -->
    <details class="archive-group">
      <summary>
        <span><i class="fas fa-folder" style="color: #2563eb; margin-right: 8px;"></i> Semana 1 (03/09 e 04/09) — 2 Cadernos</span>
        <span style="font-size: 0.8rem; color: #64748b; font-weight: normal;">Clique para expandir</span>
      </summary>
      <div class="exams-grid" style="margin-top: 14px;">
        <!-- S1 D5 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-green">04/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 1 • Dia 5</h4>
            <p class="exam-desc">15 D. Administrativo + 15 Informática (Algoritmos/Python) + 10 Lei Orgânica (Arts. 16 ao 30).</p>
          </div>
          <a href="CADERNO_QUESTOES_DIA_05_04_09_2026.html" target="_blank" class="btn-action" style="background: #059669;">Abrir Caderno Dia 5</a>
        </div>
        <!-- S1 D4 -->
        <div class="exam-card">
          <div>
            <span class="exam-badge badge-blue">03/09/2026 • 40Q</span>
            <h4 class="exam-title">Semana 1 • Dia 4</h4>
            <p class="exam-desc">15 Português (Fonologia e Acentuação) + 15 D. Constitucional + 10 Lei Orgânica (Arts. 1º a 15).</p>
          </div>
          <a href="CADERNO_QUESTOES_DIA_04_03_09_2026.html" target="_blank" class="btn-action">Abrir Caderno Dia 4</a>
        </div>
      </div>
    </details>

    <!-- SEÇÃO 7: DOCUMENTOS OFICIAIS DE MERUOCA 2026 -->
    <div id="secDocs"></div>
    <h2 class="section-heading"><i class="fas fa-file-contract" style="color: var(--primary);"></i> 7. Documentos Oficiais do Concurso — Câmara de Meruoca 2026</h2>
    <div class="download-repo-box">
      <p style="margin: 0 0 16px 0; color: var(--text-muted); font-size: 0.9rem;">
        Editais e cronogramas oficiais publicados pela banca INBRASP para o certame da Câmara Municipal de Meruoca/CE:
      </p>

      <div style="border: 1px solid var(--border); border-radius: 8px; overflow: hidden;">
        <table class="files-table">
          <thead>
            <tr>
              <th style="width: 50px;">Tipo</th>
              <th>Documento Oficial</th>
              <th style="width: 110px; text-align: right;">Tamanho</th>
              <th style="width: 120px; text-align: center;">Ação</th>
            </tr>
          </thead>
          <tbody id="filesTableBody">
            <!-- Inserido dinamicamente pelo JavaScript -->
          </tbody>
        </table>
      </div>
      <div id="searchCounter" style="margin-top: 10px; font-size: 0.85rem; color: var(--text-muted); text-align: right;">
        Mostrando documentos oficiais de Meruoca
      </div>
    </div>

  </div>

  <script>
    let todosArquivos = [];

    // Carrega o manifesto de arquivos
    fetch('arquivos_manifest.json')
      .then(res => res.json())
      .then(data => {
        todosArquivos = data;
        renderizarTabela(todosArquivos);
      })
      .catch(err => {
        console.error('Erro ao carregar manifesto:', err);
      });

    const NOMES_AMIGAVEIS = {
      "ID_726_20260828_133904_EDITAL 001.2026 - CAMARA DE MERUOCA - 28.08.pdf": "Edital Oficial nº 001/2026 — Concurso Câmara de Meruoca/CE",
      "ID_726_20260828_144712_CRONOGRAMA DE ATIVIDADES - CAMARA DE MERUOCA.pdf": "Cronograma Oficial de Atividades — Câmara de Meruoca/CE",
      "ID_726_20260904_163326_ISE\u00c7AO MERUOCA INBRASP.pdf": "Resultado Preliminar dos Pedidos de Isenção de Taxa",
      "ID_726_20260916_155456_MERUOCA DEFINITIVO ISEN\u00c7AO.pdf": "Resultado Definitivo dos Pedidos de Isenção de Taxa"
    };

    function renderizarTabela(lista) {
      const tbody = document.getElementById('filesTableBody');
      const counter = document.getElementById('searchCounter');
      
      if (!tbody) return;
      if (counter) counter.innerText = `${lista.length} documentos oficiais de Meruoca disponíveis na pasta local`;

      if (lista.length === 0) {
        tbody.innerHTML = `<tr><td colspan="4" style="text-align: center; padding: 20px; color: var(--text-muted);">Nenhum documento encontrado.</td></tr>`;
        return;
      }

      tbody.innerHTML = lista.map(item => {
        const tituloAmigavel = NOMES_AMIGAVEIS[item.nome] || item.nome;
        return `
        <tr>
          <td><span class="file-badge">PDF</span></td>
          <td>
            <strong>${tituloAmigavel}</strong>
            <div style="font-size: 0.78rem; color: #64748b; font-family: monospace;">${item.nome}</div>
          </td>
          <td style="text-align: right; color: var(--text-muted);">${item.tamanho_kb} KB</td>
          <td style="text-align: center;">
            <a href="originais_pdf/${encodeURIComponent(item.nome)}" target="_blank" style="display: inline-flex; align-items: center; gap: 5px; background: #2563eb; color: white; padding: 6px 12px; border-radius: 6px; text-decoration: none; font-weight: 700; font-size: 0.8rem;">
              <i class="fas fa-file-pdf"></i> Abrir PDF
            </a>
          </td>
        </tr>
      `;
      }).join('');
    }
  </script>

</body>
</html>
"""

with open(r'c:\Users\Ruan Gomes\Downloads\Meruoca\provas\CENTRAL_DE_PROVAS.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("CENTRAL_DE_PROVAS.html reorganizado com sucesso!")

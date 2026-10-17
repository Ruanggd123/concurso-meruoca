import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>🔥 TUDO OU NADA (RODADA 1 & 2) — Câmara de Meruoca 2026</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --primary: #1e3a8a;
      --primary-dark: #0f172a;
      --accent: #dc2626;
      --gold: #eab308;
      --success: #16a34a;
      --bg: #f1f5f9;
      --card: #ffffff;
      --text: #0f172a;
      --muted: #475569;
      --border: #cbd5e1;
      --radius: 14px;
    }

    * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }

    body {
      margin: 0;
      padding: 0 0 80px 0;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.55;
    }

    /* BARRA FIXA NO TOPO */
    .sticky-top {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      color: white;
      padding: 10px 14px;
      box-shadow: 0 4px 18px rgba(0,0,0,0.25);
      border-bottom: 3px solid var(--gold);
    }

    .sticky-row {
      max-width: 960px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }

    .brand-title {
      font-size: 1rem;
      font-weight: 900;
      display: flex;
      align-items: center;
      gap: 8px;
      color: #fef08a;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }

    .timer-box {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .countdown-pill {
      background: #dc2626;
      color: white;
      font-weight: 900;
      font-size: 0.95rem;
      padding: 5px 12px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 0 12px rgba(220, 38, 38, 0.6);
      font-variant-numeric: tabular-nums;
      cursor: pointer;
    }

    .score-pill {
      background: rgba(255,255,255,0.15);
      color: #fff;
      font-weight: 800;
      font-size: 0.85rem;
      padding: 5px 11px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.25);
    }

    .nav-tabs {
      max-width: 960px;
      margin: 8px auto 0 auto;
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 2px;
    }

    .tab-jump {
      flex: 1;
      text-align: center;
      background: rgba(255,255,255,0.12);
      color: #e2e8f0;
      border: 1px solid rgba(255,255,255,0.2);
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 800;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .tab-jump.active, .tab-jump:hover {
      background: var(--gold);
      color: #0f172a;
      border-color: var(--gold);
    }

    .container {
      max-width: 960px;
      margin: 16px auto;
      padding: 0 12px;
    }

    /* SELETOR GIGANTE DE RODADA (RODADA 1 vs RODADA 2 NOVA) */
    .round-switcher {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 18px;
    }

    .round-btn {
      padding: 14px 16px;
      border-radius: 12px;
      border: 2px solid #cbd5e1;
      background: white;
      color: #1e293b;
      font-weight: 900;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 4px;
      text-align: center;
      transition: all 0.2s;
      box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    }
    .round-btn span {
      font-size: 0.78rem;
      font-weight: 600;
      color: #64748b;
    }
    .round-btn.active {
      background: linear-gradient(135deg, #16a34a 0%, #15803d 100%);
      color: white;
      border-color: #14532d;
      box-shadow: 0 6px 18px rgba(22, 163, 74, 0.35);
    }
    .round-btn.active span {
      color: #dcfce7;
    }

    /* SEÇÃO BANNER */
    .section-banner {
      background: var(--primary-dark);
      color: white;
      padding: 14px 18px;
      border-radius: 12px;
      margin: 20px 0 14px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      border-left: 6px solid var(--gold);
    }

    .section-banner h2 {
      margin: 0;
      font-size: 1.12rem;
      font-weight: 900;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .section-banner span {
      background: var(--gold);
      color: #0f172a;
      font-size: 0.78rem;
      font-weight: 900;
      padding: 4px 10px;
      border-radius: 6px;
    }

    /* CARDS DE RESUMO */
    .resumo-card {
      background: var(--card);
      border: 2px solid var(--border);
      border-radius: var(--radius);
      padding: 18px;
      margin-bottom: 16px;
      box-shadow: 0 3px 10px rgba(0,0,0,0.04);
      transition: border-color 0.2s, background 0.2s;
    }
    .resumo-card.checked-card {
      border-color: var(--success);
      background: #f0fdf4;
    }

    .resumo-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 10px;
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 10px;
      margin-bottom: 12px;
    }

    .resumo-title {
      font-size: 1.06rem;
      font-weight: 900;
      color: var(--primary);
      margin: 0;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .check-read-lbl {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #dcfce7;
      color: #166534;
      padding: 5px 10px;
      border-radius: 8px;
      font-size: 0.78rem;
      font-weight: 800;
      cursor: pointer;
      white-space: nowrap;
      user-select: none;
      border: 1px solid #86efac;
    }
    .check-read-lbl input {
      width: 16px;
      height: 16px;
      accent-color: #16a34a;
      cursor: pointer;
    }

    .mini-table {
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
      font-size: 0.89rem;
    }
    .mini-table th {
      background: #eff6ff;
      color: #1e3a8a;
      text-align: left;
      padding: 8px 10px;
      border: 1px solid #bfdbfe;
      font-weight: 800;
    }
    .mini-table td {
      padding: 8px 10px;
      border: 1px solid #e2e8f0;
      vertical-align: top;
    }
    .mini-table tr:nth-child(even) td {
      background: #f8fafc;
    }

    .bullet-list {
      margin: 0;
      padding-left: 18px;
      font-size: 0.93rem;
    }
    .bullet-list li {
      margin-bottom: 9px;
    }

    .step-flow {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 6px;
      margin: 8px 0;
      background: #f8fafc;
      padding: 10px 12px;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
      font-size: 0.86rem;
      font-weight: 700;
    }
    .step-box {
      background: #e2e8f0;
      color: #1e293b;
      padding: 4px 9px;
      border-radius: 6px;
    }
    .step-box.gold {
      background: #fef08a;
      color: #713f12;
      border: 1px solid #eab308;
      font-weight: 900;
    }
    .step-arrow {
      color: #dc2626;
      font-weight: 900;
      font-size: 1rem;
    }

    .tag-hot {
      background: #fee2e2;
      color: #991b1b;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.8rem;
    }
    .tag-ok {
      background: #dcfce7;
      color: #166534;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.8rem;
    }
    .tag-num {
      background: #fef08a;
      color: #713f12;
      font-weight: 900;
      padding: 2px 6px;
      border-radius: 4px;
    }

    /* FILTROS DO SIMULADO */
    .quiz-controls {
      background: white;
      border: 2px solid var(--primary);
      border-radius: var(--radius);
      padding: 14px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .f-pill {
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 800;
      cursor: pointer;
    }
    .f-pill.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }

    .btn-apostila {
      background: #16a34a;
      color: white;
      border: none;
      padding: 9px 14px;
      border-radius: 8px;
      font-size: 0.84rem;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .btn-apostila:hover { background: #15803d; }

    /* QUESTÕES INTERATIVAS */
    .q-card {
      background: white;
      border: 1.5px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      margin-bottom: 14px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .q-card.correct-card {
      border: 2px solid #16a34a;
      background: #f0fdf4;
    }
    .q-card.wrong-card {
      border: 2px solid #dc2626;
      background: #fff1f2;
    }

    .q-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 8px;
    }

    .q-badge {
      background: var(--primary);
      color: white;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: 6px;
    }

    .q-mat {
      background: #e0e7ff;
      color: #1e40af;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: 6px;
    }

    .q-enun {
      font-size: 0.98rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 12px;
      line-height: 1.45;
    }

    .q-opts {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .opt-btn {
      width: 100%;
      text-align: left;
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: 10px;
      padding: 11px 13px;
      font-size: 0.92rem;
      color: #1e293b;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      transition: all 0.15s;
    }
    .opt-btn:hover {
      background: #eff6ff;
      border-color: #93c5fd;
    }

    .opt-let {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #e2e8f0;
      color: #334155;
      font-weight: 900;
      font-size: 0.8rem;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .opt-btn.is-correct {
      background: #dcfce7 !important;
      border-color: #16a34a !important;
      color: #14532d !important;
      font-weight: 700;
    }
    .opt-btn.is-correct .opt-let {
      background: #16a34a !important;
      color: white !important;
    }

    .opt-btn.is-wrong {
      background: #fee2e2 !important;
      border-color: #dc2626 !important;
      color: #7f1d1d !important;
    }
    .opt-btn.is-wrong .opt-let {
      background: #dc2626 !important;
      color: white !important;
    }

    .q-exp {
      display: none;
      margin-top: 10px;
      padding: 10px 12px;
      background: #ffffff;
      border-left: 4px solid var(--primary);
      border-radius: 6px;
      font-size: 0.86rem;
      color: #334155;
    }
    .q-exp.visible {
      display: block;
    }
  </style>
</head>
<body>

  <!-- BARRA FIXA DE 1 HORA -->
  <header class="sticky-top">
    <div class="sticky-row">
      <div class="brand-title">
        <i class="fas fa-fire"></i> TUDO OU NADA • MERUOCA
      </div>
      <div class="timer-box">
        <div class="score-pill">
          Acertos: <strong id="hitsCount">0</strong>/<span id="ansCount">0</span> (<span id="pctCount">0%</span>)
        </div>
        <div class="countdown-pill" onclick="resetOneHourTimer()" title="Clique para reiniciar os 60 minutos">
          <i class="fas fa-stopwatch"></i> <span id="timerDisplay">60:00</span>
        </div>
      </div>
    </div>
    <div class="nav-tabs">
      <button class="tab-jump active" id="tabBtnR2" onclick="switchRound(2)">
        🚀 RODADA 2 NOVA (Blocos 7 a 12 + 40 Questões Inéditas)
      </button>
      <button class="tab-jump" id="tabBtnR1" onclick="switchRound(1)">
        🔥 RODADA 1 (Blocos 1 a 6 + 40 Questões Base)
      </button>
      <button class="tab-jump" onclick="scrollToSection('sec-questoes')">
        🎯 Ir p/ Questões
      </button>
      <button class="tab-jump" onclick="revealAllCurrentRound()">
        ⚡ Marcar Todas Certas
      </button>
    </div>
  </header>

  <div class="container">

    <!-- SELETOR DE RODADA -->
    <div class="round-switcher">
      <button type="button" class="round-btn active" id="bigBtnR2" onclick="switchRound(2)">
        <div>🚀 RODADA 2 INÉDITA (PARTE 2)</div>
        <span>6 Novos Blocos de Resumo + 40 Questões Novas</span>
      </button>
      <button type="button" class="round-btn" id="bigBtnR1" onclick="switchRound(1)">
        <div>🔥 RODADA 1 (PARTE 1 LIMPA)</div>
        <span>Blocos 1 a 6 (Sem códigos) + 40 Questões Base</span>
      </button>
    </div>

    <!-- =========================================================
         CONTEÚDO DA RODADA 2 (NOVA — BLOCOS 7 A 12)
         ========================================================= -->
    <div id="round2Content">
      <div class="section-banner">
        <h2><i class="fas fa-rocket"></i> RODADA 2 — 6 NOVOS BLOCOS DE OURO (TEXTO LIMPO E DIRETO)</h2>
        <span>LEITURA: 25 MINUTOS</span>
      </div>

      <!-- BLOCO 7 -->
      <div class="resumo-card" id="rc7">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-user-tie"></i> BLOCO 7: Lei Orgânica de Meruoca — Prefeito, Vereadores, Posse e Vedações</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc7', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Posse do Prefeito, Vice e Vereadores:</strong> No dia <span class="tag-num">1º de janeiro</span> do ano seguinte ao da eleição, em Sessão Solene de Instalação na Câmara Municipal.</li>
          <li><strong>E se o Prefeito não tomar posse?</strong> Se decorridos <span class="tag-num">10 dias</span> da data fixada para a posse o Prefeito ou o Vice-Prefeito, salvo motivo de força maior aceito pela Câmara, não tiver assumido o cargo, este será declarado <strong>VAGO</strong>!</li>
          <li><strong>Licença para sair do Município ou do País:</strong> O Prefeito e o Vice-Prefeito não poderão, sem licença da Câmara Municipal, ausentar-se do Município por período superior a <span class="tag-num">15 dias consecutivos</span> (ou do País por qualquer tempo), sob pena de <strong>perda do cargo</strong>.</li>
          <li><strong>Inviolabilidade dos Vereadores (Art. 29, VIII CF / LOM):</strong> Os Vereadores são invioláveis por suas opiniões, palavras e votos no exercício do mandato e <span class="tag-hot">NA CIRCUNSCRIÇÃO DO MUNICÍPIO</span> (não vale em todo o território nacional!).</li>
          <li><strong>Vereador que assume cargo de Secretário Municipal:</strong> <span class="tag-ok">NÃO PERDE O MANDATO!</span> Ele fica automaticamente licenciado da Câmara (convoca-se o suplente) e pode optar pela remuneração de Vereador ou de Secretário.</li>
          <li><strong>Quando o Suplente de Vereador é convocado?</strong> Nos casos de <strong>vaga</strong> (morte, renúncia ou cassação), de <strong>investidura em cargo de Secretário</strong> ou de <strong>licença superior a 120 dias</strong>.</li>
        </ul>
      </div>

      <!-- BLOCO 8 -->
      <div class="resumo-card" id="rc8">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-gavel"></i> BLOCO 8: Regimento Interno da Câmara — Sessões, Mesa Diretora e Comissões</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc8', this.checked)"> Já li e gravei!
          </label>
        </div>
        <table class="mini-table">
          <thead>
            <tr>
              <th style="width:28%;">Órgão / Sessão</th>
              <th>Regra Exata Cobrada em Provas de Câmara</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Partes da Sessão Ordinária</strong></td>
              <td>1º <strong>Pequeno Expediente:</strong> Leitura da ata anterior e correspondências recebidas.<br>
              2º <strong>Grande Expediente:</strong> Uso da palavra pelos vereadores inscritos na Tribuna.<br>
              3º <strong>Ordem do Dia:</strong> Discussão e <strong>votação</strong> dos projetos em pauta (exige presença da <span class="tag-num">Maioria Absoluta</span> da Câmara para iniciar votações!).</td>
            </tr>
            <tr>
              <td><strong>Sessão Extraordinária</strong><br>(No Recesso)</td>
              <td>• Quem pode convocar? <strong>Prefeito Municipal</strong>, <strong>Presidente da Câmara</strong> ou a <strong>Maioria dos Vereadores</strong>.<br>
              • Na sessão extraordinária, a Câmara <strong>SÓ pode deliberar sobre a matéria objeto da convocação</strong> (é proibido pagar verba indenizatória extra por sessão extraordinária!).</td>
            </tr>
            <tr>
              <td><strong>Presidente da Câmara vs. 1º Secretário</strong></td>
              <td>• <strong>Presidente:</strong> Representa a Câmara em juízo, dirige o Plenário, promulga Resoluções e Decretos Legislativos. Na votação de maioria simples, só vota para <strong>desempatar</strong> (voto de qualidade/minerva). Já nas votações de <strong>Maioria Absoluta</strong>, <strong>2/3</strong> ou escrutínio secreto, o Presidente vota normalmente!<br>
              • <strong>1º Secretário:</strong> Faz a chamada nominal dos vereadores, lê o expediente/ata e supervisiona a Secretaria Administrativa.</td>
            </tr>
            <tr>
              <td><strong>Comissões Permanentes vs. Temporárias</strong></td>
              <td>• <strong>Permanentes:</strong> Subsistem através das legislaturas (ex: <em>Comissão de Constituição e Justiça - CCJ</em>; <em>Comissão de Finanças e Orçamento - CFO</em>).<br>
              • <strong>Temporárias (Especiais):</strong> Extinguem-se ao final do prazo ou quando cumprem seu objetivo (ex: <strong>CPI</strong>, Comissão Processante, Comissão de Representação).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- BLOCO 9 -->
      <div class="resumo-card" id="rc9">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-shield-alt"></i> BLOCO 9: Poderes da Administração & Nova Lei de Improbidade (Lei 14.230/21)</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc9', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Diferença entre os 4 Poderes Administrativos (Cai em TODA prova da INBRASP!):</strong>
            <ul>
              <li><strong>Poder Hierárquico:</strong> Escalonar, dar ordens, fiscalizar, rever atos, <strong>delegar</strong> e <strong>avocar</strong> atribuições dentro da mesma estrutura. <span class="tag-hot">O que NÃO pode ser delegado? (CE-NO-RE):</span> <strong>CE</strong> = Competência Exclusiva; <strong>NO</strong> = Edição de atos de caráter Normativo; <strong>RE</strong> = Decisão de Recursos administrativos.</li>
              <li><strong>Poder Disciplinar:</strong> Aplicar penalidades às pessoas sujeitas à disciplina interna da Administração (<strong>servidores públicos</strong> após PAD e <strong>empresas contratadas</strong> pela Câmara/Prefeitura).</li>
              <li><strong>Poder de Polícia:</strong> Restringir e fiscalizar bens, atividades e direitos de particulares em geral em benefício da coletividade (ex: interdição sanitária, alvará de funcionamento, multa de trânsito). Atributos: <strong>D-A-C</strong> (<strong>D</strong>iscricionariedade, <strong>A</strong>utoexecutoriedade e <strong>C</strong>oercibilidade).</li>
              <li><strong>Poder Regulamentar:</strong> Privativo do Chefe do Executivo para editar Decretos regulamentando leis.</li>
            </ul>
          </li>
          <li><strong>Nova Lei de Improbidade Administrativa (Lei nº 8.429/92 atualizada pela Lei 14.230/2021):</strong>
            <ul>
              <li><span class="tag-hot">REGRA Nº 1:</span> <strong>NÃO EXISTE MAIS IMPROBIDADE CULPOSA!</strong> Todo ato de improbidade exige <strong>DOLO ESPECÍFICO</strong> (vontade livre e consciente de alcançar o resultado ilícito).</li>
              <li><strong>Enriquecimento Ilícito (Art. 9º):</strong> Suspensão dos direitos políticos e proibição de contratar por até <span class="tag-num">14 anos</span>.</li>
              <li><strong>Lesão ao Erário (Art. 10):</strong> Suspensão dos direitos políticos e proibição de contratar por até <span class="tag-num">12 anos</span>.</li>
              <li><strong>Atentado contra os Princípios (Art. 11 — Rol Taxativo):</strong> <span class="tag-ok">NÃO tem suspensão de direitos políticos!</span> Proibição de contratar por até <span class="tag-num">4 anos</span> + multa de até 24x a remuneração.</li>
              <li><strong>Prescrição da ação de improbidade:</strong> <span class="tag-num">8 anos</span> contados a partir da ocorrência do fato.</li>
            </ul>
          </li>
        </ul>
      </div>

      <!-- BLOCO 10 -->
      <div class="resumo-card" id="rc10">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-pen-fancy"></i> BLOCO 10: Língua Portuguesa — Os 4 Porquês, Onde/Aonde, Mau/Mal e Concordância</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc10', this.checked)"> Já li e gravei!
          </label>
        </div>
        <table class="mini-table">
          <thead>
            <tr>
              <th>Dúvida Clássica</th>
              <th>Macete Direto para Acertar em 5 Segundos</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>POR QUE</strong><br>(Separado sem acento)</td>
              <td>Usado no <strong>início de perguntas</strong> (diretas ou indiretas) ou quando puder trocar por <strong>"pelo qual / por qual razão"</strong>.<br>Ex: <em>"<u>Por que</u> a votação atrasou?"</em> / <em>"Os ideais <u>por que</u> lutamos."</em></td>
            </tr>
            <tr>
              <td><strong>POR QUÊ</strong><br>(Separado com acento)</td>
              <td>Usado <strong>NO FIM DA FRASE</strong> (antes de ponto final, interrogação ou exclamação).<br>Ex: <em>"O projeto foi retirado de pauta, mas ninguém sabe <u>por quê</u>."</em></td>
            </tr>
            <tr>
              <td><strong>PORQUE</strong><br>(Junto sem acento)</td>
              <td>Usado em <strong>RESPOSTAS, explicações ou causas</strong> (troque por <strong>"pois / já que"</strong>).<br>Ex: <em>"Não houve sessão <u>porque</u> faltou quórum."</em></td>
            </tr>
            <tr>
              <td><strong>PORQUÊ</strong><br>(Junto com acento)</td>
              <td>É um <strong>SUBSTANTIVO</strong> (= <em>o motivo, a razão</em>). Sempre vem depois de <strong>"o / este / um"</strong>.<br>Ex: <em>"Quero entender <u>o porquê</u> desta decisão."</em></td>
            </tr>
            <tr>
              <td><strong>ONDE vs. AONDE</strong></td>
              <td>• <strong>ONDE:</strong> Lugar fixo / parado (quem mora, mora <em>em</em> ➔ <em>"A cidade <u>onde</u> moro"</em>).<br>
              • <strong>AONDE:</strong> Movimento / destino (quem vai, vai <em>a</em> ➔ <em>"A Câmara <u>aonde</u> iremos amanhã"</em>).</td>
            </tr>
            <tr>
              <td><strong>MAU vs. MAL</strong></td>
              <td>• <strong>MAU</strong> = oposto de <strong>BOM</strong> (<em>"Um mau exemplo" = "Um bom exemplo"</em>).<br>
              • <strong>MAL</strong> = oposto de <strong>BEM</strong> (<em>"Passou mal" = "Passou bem"</em>) ou igual a <strong>"assim que"</strong> (<em>"Mal chegou, a sessão começou"</em>).</td>
            </tr>
            <tr>
              <td><strong>ANEXO vs. EM ANEXO</strong></td>
              <td>• <strong>Anexo / Obrigado / Mesmo / Próprio:</strong> Concordam em gênero e número (<em>"Seguem <u>anexas</u> as atas"</em>, <em>"Elas <u>mesmas</u> assinaram"</em>).<br>
              • Já a expressão <strong>"Em anexo"</strong> é invariável (<em>"Seguem <u>em anexo</u> as atas"</em>).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- BLOCO 11 -->
      <div class="resumo-card" id="rc11">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-square-root-alt"></i> BLOCO 11: Matemática & RLM — Equivalências Lógicas, MMC/MDC e Juros Simples</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc11', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Equivalência do "SE P, ENTÃO Q" (Muito cobrado junto com Negação!):</strong>
            <br>Cuidado para não confundir <strong>Negação</strong> (MANÉ) com <strong>Equivalência</strong>! Se a questão pedir uma frase <strong>EQUIVALENTE</strong> a <em>"Se é vereador, então vota"</em>, existem 2 respostas certas:
            <div class="step-flow">
              <span class="step-box gold">1ª Equivalência (Inverte e Nega as Duas):</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">"Se NÃO vota, então NÃO é vereador"</span>
            </div>
            <div class="step-flow">
              <span class="step-box gold">2ª Equivalência (Regra do NEYMAR — Nega a 1ª OU Mantém a 2ª):</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">"NÃO é vereador OU vota"</span>
            </div>
          </li>
          <li><strong>MMC vs. MDC (Como identificar na hora na prova):</strong>
            <br>• Problema de <strong>encontro no futuro / ciclos que coincidem</strong> (Ex: <em>"Um ônibus passa de 4 em 4 horas e outro de 6 em 6 horas. Se saíram juntos agora, daqui a quantas horas sairão juntos de novo?"</em>) ➔ Calcule o <strong>MMC</strong>! MMC de 4 e 6 = <span class="tag-num">12 horas</span>.
            <br>• Problema de <strong>dividir em pacotes iguais do MAIOR tamanho possível sem sobra</strong> (Ex: <em>"Dividir 24 processos de compras e 36 processos de pessoal em lotes iguais com a maior quantidade possível"</em>) ➔ Calcule o <strong>MDC</strong>! MDC de 24 e 36 = <span class="tag-num">12 processos por lote</span>.</li>
          <li><strong>Juros Simples (Fórmula: Juros = Capital × Taxa × Tempo):</strong>
            <br>• Exemplo prático: Um capital de <strong>R$ 2.000,00</strong> aplicado a juros simples de <strong>3% ao mês</strong> durante <strong>5 meses</strong>:
            <br>1º Calcule 1% de 2.000 (basta cortar dois zeros) = R$ 20,00.
            <br>2º Logo, 3% ao mês = 3 × 20 = <strong>R$ 60,00 por mês</strong>.
            <br>3º Em 5 meses: 5 × 60 = <span class="tag-ok">R$ 300,00 de juros</span> (Montante final = R$ 2.300,00).</li>
        </ul>
      </div>

      <!-- BLOCO 12 -->
      <div class="resumo-card" id="rc12">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-archive"></i> BLOCO 12: Arquivologia, Atendimento e Redes (Conhecimentos do Cargo + Informática)</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc12', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Teoria das 3 Idades do Arquivo (Ciclo Vital dos Documentos — Cai muito para Técnico/Agente!):</strong>
            <div class="step-flow">
              <span class="step-box gold">1ª Idade: CORRENTE</span>
              <span>Uso frequente no setor</span>
              <span class="step-arrow">➔</span>
              <span class="step-box gold">2ª Idade: INTERMEDIÁRIO</span>
              <span>Aguarda prazo na Tabela</span>
              <span class="step-arrow">➔</span>
              <span class="step-box gold">3ª Idade: PERMANENTE</span>
              <span>Valor Histórico (NUNCA é eliminado!)</span>
            </div>
          </li>
          <li><strong>Tabela de Temporalidade Documental:</strong> É o instrumento arquivístico que define os <strong>prazos de guarda</strong> nas fases corrente e intermediária e determina a <strong>destinação final</strong> do documento (eliminação ou recolhimento para guarda permanente).</li>
          <li><strong>Protocolo vs. Expedição:</strong> O setor de <strong>Protocolo</strong> recebe, registra, autua (forma o processo) e distribui os documentos que chegam à Câmara.</li>
          <li><strong>Informática — Correio Eletrônico (E-mail) e Redes:</strong>
            <br>• <strong>Campo Para (To) e CC (Com Cópia):</strong> Todos os destinatários conseguem ver os e-mails uns dos outros.
            <br>• <strong>Campo CCo (Com Cópia Oculta / Bcc):</strong> Os destinatários principais <strong>NÃO veem</strong> quem foi colocado em CCo!
            <br>• <strong>Intranet vs. Extranet:</strong> A <strong>Intranet</strong> é uma rede privada de uso exclusivo dos servidores internos da Câmara/Prefeitura; a <strong>Extranet</strong> estende parte desse acesso de forma controlada a usuários externos autorizados (fornecedores, contadores, cidadãos).
            <br>• <strong>Protocolos Web:</strong> <strong>HTTPS</strong> usa criptografia (SSL/TLS) para proteger os dados trafegados; <strong>SMTP</strong> envia e-mails (<em>"Sua Mensagem Tá Partindo"</em>); <strong>IMAP / POP3</strong> recebem e-mails.</li>
        </ul>
      </div>
    </div>


    <!-- =========================================================
         CONTEÚDO DA RODADA 1 (BLOCOS 1 A 6 — 100% LIMPO SEM LATEX)
         ========================================================= -->
    <div id="round1Content" style="display: none;">
      <div class="section-banner">
        <h2><i class="fas fa-bolt"></i> RODADA 1 — OS 6 BLOCOS FUNDAMENTAIS (TEXTO 100% LIMPO)</h2>
        <span>LEITURA: 25 MINUTOS</span>
      </div>

      <!-- BLOCO 1 -->
      <div class="resumo-card" id="rc1">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-landmark"></i> BLOCO 1: Lei Orgânica de Meruoca & Quóruns da Câmara</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc1', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Autonomia do Município (Art. 18 e 29 CF / LOM):</strong> <span class="tag-ok">Política, Administrativa e Financeira</span>. O Município <strong>NÃO tem soberania</strong> e seus únicos Poderes são o <strong>Legislativo</strong> e o <strong>Executivo</strong> (não existe Judiciário nem MP municipal).</li>
          <li><strong>Símbolos Oficiais de Meruoca:</strong> <span class="tag-num">Bandeira, Brasão e Hino</span>.</li>
          <li><strong>Iniciativa Popular de Lei Municipal:</strong> Exige assinatura de no mínimo <span class="tag-num">5% do eleitorado</span> do Município (Art. 29, XIII CF).</li>
        </ul>
        <table class="mini-table">
          <thead>
            <tr>
              <th style="width: 28%;">Quórum de Votação</th>
              <th>Quando a Câmara Municipal exige? (DECORE!)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="tag-hot">DOIS TERÇOS (2/3)</span></td>
              <td>• <strong>Rejeitar o Parecer Prévio do Tribunal de Contas (TCE)</strong> sobre as contas do Prefeito (Art. 31, § 2º CF).<br>
              • <strong>Aprovar ou Emendar a Lei Orgânica (LOM)</strong> (votada em <strong>2 turnos</strong> com intervalo mínimo de <strong>10 dias</strong>).<br>
              • <strong>Cassar mandato</strong> do Prefeito ou de Vereador e <strong>destituir membro da Mesa</strong>.</td>
            </tr>
            <tr>
              <td><span class="tag-num">MAIORIA ABSOLUTA</span><br><small>Mais da metade do TOTAL da Casa</small></td>
              <td>• Aprovar <strong>Lei Complementar</strong> e o <strong>Regimento Interno</strong>.<br>
              • <strong>Rejeitar (derrubar) o Veto do Prefeito</strong> (prazo de 30 dias).<br>
              • <strong>Renovar projeto de lei rejeitado</strong> na mesma sessão legislativa (Art. 67 CF).</td>
            </tr>
            <tr>
              <td><span class="tag-ok">MAIORIA SIMPLES</span><br><small>Maioria dos PRESENTES</small></td>
              <td>• Aprovar <strong>Lei Ordinária</strong> e requerimentos comuns (presente a maioria absoluta dos vereadores).</td>
            </tr>
          </tbody>
        </table>
        <ul class="bullet-list">
          <li><strong>Números Sagrados:</strong> <span class="tag-num">60 dias</span> (contas à disposição do contribuinte); <span class="tag-num">70%</span> (máximo da receita da Câmara com folha de pagamento); <span class="tag-num">6% da RCL</span> (limite de gasto com pessoal do Legislativo na LRF); <span class="tag-num">1/3 dos vereadores</span> (criar CPI); <span class="tag-num">15 dias úteis</span> (prazo para o Prefeito sancionar ou vetar; silêncio = sanção tácita).</li>
        </ul>
      </div>

      <!-- BLOCO 2 -->
      <div class="resumo-card" id="rc2">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-file-signature"></i> BLOCO 2: Nova Lei de Licitações — Lei nº 14.133/2021</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc2', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>As 5 Modalidades Existentes:</strong> <span class="tag-ok">Pregão, Concorrência, Concurso, Leilão e Diálogo Competitivo</span>. <span class="tag-hot">Foram EXTINTAS: Tomada de Preços, Convite e RDC!</span></li>
          <li><strong>Pregão:</strong> Bens e serviços <strong>COMUNS</strong> | <strong>Concorrência:</strong> Bens e serviços <strong>ESPECIAIS</strong> e obras/engenharia | <strong>Leilão:</strong> Venda de bens móveis OU <strong>imóveis</strong> (Art. 76).</li>
          <li><strong>Ordem Padrão das Fases (Art. 17):</strong>
            <div class="step-flow">
              <span class="step-box">1. Preparatória</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">2. Edital</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">3. Propostas</span>
              <span class="step-arrow">➔</span>
              <span class="step-box gold">4. JULGAMENTO</span>
              <span class="step-arrow">➔</span>
              <span class="step-box gold">5. HABILITAÇÃO</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">6. Recursos</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">7. Homologação</span>
            </div>
            <em>(Regra geral: primeiro julga a proposta, depois confere a habilitação só do vencedor!).</em>
          </li>
          <li><strong>Inexigibilidade (Art. 74):</strong> Competição inviável: fornecedor exclusivo (vedada preferência de marca), artista consagrado, serviços técnicos intelectuais com notória especialização (<span class="tag-hot">PROIBIDA para publicidade e divulgação!</span>), credenciamento e locação/compra de imóvel específico.</li>
        </ul>
      </div>

      <!-- BLOCO 3 -->
      <div class="resumo-card" id="rc3">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-balance-scale"></i> BLOCO 3: Direito Administrativo & Constitucional (Art. 5º e 37)</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc3', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>LIMPE (Art. 37):</strong> Legalidade, Impessoalidade (proíbe promoção pessoal com foto/nome em obras e proíbe nepotismo até o 3º grau), Moralidade, Publicidade e Eficiência.</li>
          <li><strong>DesCOncentração vs. DesCEntralização:</strong> Des<strong>CO</strong>ncentração cria <strong>Órgão</strong> (mesma pessoa jurídica, tem subordinação). Des<strong>CE</strong>ntralização cria <strong>Entidade</strong> da Adm. Indireta (Autarquia, Fundação, Empresa Pública 100% pública, Sociedade de Economia Mista S/A — não há subordinação, só controle finalístico).</li>
          <li><strong>Anulação vs. Revogação (Súmula 473 STF):</strong>
            <br>• <strong>Anulação:</strong> Ato <strong>ILEGAL</strong> ➔ efeito <em>ex tunc</em> (retroage). Fazem Administração e Judiciário.
            <br>• <strong>Revogação:</strong> Ato <strong>LEGAL</strong> inconveniente/inoportuno ➔ efeito <em>ex nunc</em> (não retroage). <strong>Só a Administração pode revogar!</strong></li>
          <li><strong>Art. 5º e Servidores:</strong> Crimes inafiançáveis e <strong>imprescritíveis</strong> = <strong>RAÇÃO</strong> (Racismo e Ação de grupos armados). Estabilidade = <strong>3 anos</strong> de efetivo exercício em cargo efetivo. Concurso válido por até <strong>2 anos</strong> (prorrogável uma vez por igual período).</li>
        </ul>
      </div>

      <!-- BLOCO 4 -->
      <div class="resumo-card" id="rc4">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-spell-check"></i> BLOCO 4: Língua Portuguesa — Os 6 Macetes Principais</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc4', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Haver (existir) e Fazer (tempo):</strong> Ficam <strong>SEMPRE no singular</strong> (<em>"Houve muitas dúvidas"</em>, <em>"Deve haver soluções"</em>, <em>"Faz dez anos"</em>).</li>
          <li><strong>Crase Proibida:</strong> Antes de verbo (<em>a partir</em>), palavra masculina (<em>a prazo</em>), pronomes (<em>a ela, a todos, a Vossa Excelência</em>) e palavras repetidas (<em>cara a cara</em>). <strong>Crase Obrigatória:</strong> locuções femininas (<em>às pressas, às vezes, à noite, à medida que</em>).</li>
          <li><strong>Conjunções Concessivas (= mesmo que):</strong> <span class="tag-num">Embora, conquanto, ainda que, mesmo que, posto que, apesar de que</span>.</li>
          <li><strong>Pronome CUJO:</strong> Nunca aceita artigo depois dele (<em>"cujo projeto"</em> = certo; <em>"cujo o projeto"</em> = errado).</li>
          <li><strong>Voz Passiva (SE):</strong> Sem preposição concorda no plural (<em>"Aprovaram-se os projetos"</em>); com preposição fica no singular (<em>"Precisa-se de servidores"</em>).</li>
          <li><strong>Parônimos:</strong> <strong>Retificar</strong> = corrigir | <strong>Ratificar</strong> = confirmar | <strong>Deferir</strong> = aprovar | <strong>Diferir</strong> = adiar.</li>
        </ul>
      </div>

      <!-- BLOCO 5 -->
      <div class="resumo-card" id="rc5">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-calculator"></i> BLOCO 5: Matemática & RLM — Negações e Proporção</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc5', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Negação do "E":</strong> Troca por <strong>OU</strong> e nega tudo (<em>"Não A ou Não B"</em>).</li>
          <li><strong>Negação do "OU":</strong> Troca por <strong>E</strong> e nega tudo (<em>"Não A e Não B"</em>).</li>
          <li><strong>Negação do "SE... ENTÃO" (Regra do MANÉ):</strong> <strong>MA</strong>ntém a primeira <strong>E</strong> <strong>NE</strong>ga a segunda (Ex: Negação de <em>"Se estuda, então passa"</em> ➔ <strong>"Estuda E não passa"</strong>).</li>
          <li><strong>Negação de "TODO":</strong> <strong>"Algum... não"</strong> / <strong>"Pelo menos um não"</strong> (Nunca negue Todo com Nenhum!).</li>
          <li><strong>Divisão Proporcional:</strong> Para dividir 360 em partes proporcionais a 2, 3 e 4 ➔ Soma as partes (2 + 3 + 4 = 9), divide o total (360 ÷ 9 = 40) e multiplica pela parte pedida (menor: 2 × 40 = 80).</li>
        </ul>
      </div>

      <!-- BLOCO 6 -->
      <div class="resumo-card" id="rc6">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-laptop-code"></i> BLOCO 6: Informática — Word, Excel e Segurança</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc6', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Atalhos do Word (Português):</strong> <span class="tag-num">Ctrl + B</span> = Salvar | <span class="tag-num">Ctrl + L</span> = Localizar | <span class="tag-num">Ctrl + U</span> = Substituir | <span class="tag-num">Ctrl + T</span> = Selecionar Tudo.</li>
          <li><strong>Excel:</strong> Dois-pontos (<strong>:</strong>) = ATÉ (<code>=SOMA(A1:A5)</code> soma de A1 até A5); Ponto e vírgula (<strong>;</strong>) = E (<code>=SOMA(A1;A5)</code> soma só A1 e A5). <code>=CONT.VALORES</code> conta células não vazias; <code>=CONT.NÚM</code> conta só números.</li>
          <li><strong>Navegadores e Windows:</strong> <span class="tag-num">Ctrl + Shift + T</span> reabre a última aba fechada; <span class="tag-num">Shift + Delete</span> exclui arquivo sem passar pela Lixeira; <strong>Ransomware</strong> sequestra dados com criptografia e pede resgate.</li>
        </ul>
      </div>
    </div>


    <!-- =========================================================
         SEÇÃO DE QUESTÕES (ALTERNA ENTRE AS 40 DA RODADA 2 E AS 40 DA RODADA 1)
         ========================================================= -->
    <div id="sec-questoes" class="section-banner">
      <h2 id="quizSectionTitle"><i class="fas fa-crosshairs"></i> SIMULADO RODADA 2 — 40 NOVAS QUESTÕES INÉDITAS</h2>
      <span>10 PT • 5 MAT/RLM • 5 INFO • 20 ESPECÍFICAS</span>
    </div>

    <div class="quiz-controls">
      <div class="filter-pills">
        <button class="f-pill active" onclick="filterQuestions('all', this)">Todas (40Q)</button>
        <button class="f-pill" onclick="filterQuestions('pt', this)">Português (10Q)</button>
        <button class="f-pill" onclick="filterQuestions('mat', this)">Mat & RLM (5Q)</button>
        <button class="f-pill" onclick="filterQuestions('info', this)">Informática (5Q)</button>
        <button class="f-pill" onclick="filterQuestions('esp', this)">Específicas & LOM (20Q)</button>
        <button class="f-pill" onclick="filterQuestions('wrong', this)" style="color:#dc2626; border-color:#fca5a5;">Apenas Erradas</button>
      </div>
      <div style="display:flex; gap:8px; flex-wrap:wrap;">
        <button class="btn-apostila" onclick="revealAllCurrentRound()">
          <i class="fas fa-check-double"></i> Marcar Todas as 40 Certas
        </button>
        <button class="f-pill" onclick="resetCurrentRoundQuiz()">
          <i class="fas fa-redo"></i> Limpar Marcações
        </button>
      </div>
    </div>

    <div id="questionsContainer"></div>

  </div>

  <script>
    // CRONÔMETRO DE 60 MINUTOS
    let remainingSecs = 60 * 60;
    setInterval(() => {
      if (remainingSecs > 0) {
        remainingSecs--;
        const m = String(Math.floor(remainingSecs / 60)).padStart(2, '0');
        const s = String(remainingSecs % 60).padStart(2, '0');
        document.getElementById('timerDisplay').innerText = `${m}:${s}`;
      }
    }, 1000);

    function resetOneHourTimer() {
      remainingSecs = 60 * 60;
      document.getElementById('timerDisplay').innerText = '60:00';
    }

    function scrollToSection(id) {
      const el = document.getElementById(id);
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 95;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }

    function toggleCardRead(cardId, checked) {
      const c = document.getElementById(cardId);
      if (c) c.classList.toggle('checked-card', checked);
    }

    // =========================================================================
    // RODADA 2: 40 QUESTÕES INÉDITAS (BASEADAS NOS BLOCOS 7 A 12 + EDITAL)
    // =========================================================================
    const QUESTIONS_R2 = [
      // 1 a 10: Português (Rodada 2)
      {
        num: 1, cat: 'pt', mat: 'Língua Portuguesa • Uso dos Porquês',
        q: 'Assinale a alternativa em que o emprego do "porquê" está CORRETO de acordo com a norma-padrão:',
        opts: [
          'Os vereadores queriam saber o porquê do adiamento da votação.',
          'Porque você não protocolou o requerimento ontem pela manhã?',
          'O parecer foi aprovado por que estava muito bem fundamentado.',
          'Eles discordaram da emenda, mas não explicaram por que.'
        ],
        ans: 0,
        exp: 'Gabarito A. "O porquê" (junto e com acento) é substantivo (= o motivo, a razão) e vem precedido de artigo ("o"). Na B deveria ser "Por que" (início de pergunta); na C "porque" (causa/explicação); na D "por quê" (final de frase).'
      },
      {
        num: 2, cat: 'pt', mat: 'Língua Portuguesa • Onde vs. Aonde',
        q: 'Complete corretamente as lacunas: "A Câmara Municipal de Meruoca, ________ trabalham os servidores do Legislativo, é o local ________ os cidadãos se dirigirão amanhã para acompanhar a sessão."',
        opts: [
          'aonde — onde',
          'onde — aonde',
          'onde — onde',
          'aonde — aonde'
        ],
        ans: 1,
        exp: 'Gabarito B. "Onde" indica lugar fixo/permanência (quem trabalha, trabalha EM algum lugar -> onde trabalham). "Aonde" indica movimento/destino com verbos que pedem a preposição "a" (quem se dirige, dirige-se A algum lugar -> aonde se dirigirão).'
      },
      {
        num: 3, cat: 'pt', mat: 'Língua Portuguesa • Mau vs. Mal',
        q: 'Assinale a alternativa em que os vocábulos "MAU" e "MAL" foram empregados CORRETAMENTE:',
        opts: [
          'O servidor não é um mal profissional, apenas passou mau ontem.',
          'Mal começou a sessão ordinária, o mau tempo provocou queda de energia.',
          'O projeto foi mau redigido e causou um grande mau ao Município.',
          'Mau chegou ao plenário, o relator leu o parecer.'
        ],
        ans: 1,
        exp: 'Gabarito B. No início da frase, "Mal começou a sessão" equivale a "Assim que começou a sessão" (conjunção temporal = MAL com L). Já em "mau tempo", "mau" é adjetivo oposto de "bom" (bom tempo -> mau tempo).'
      },
      {
        num: 4, cat: 'pt', mat: 'Língua Portuguesa • Concordância Nominal (Anexo)',
        q: 'Assinale a frase que respeita integralmente as regras de concordância nominal da norma culta:',
        opts: [
          'Seguem anexo as planilhas orçamentárias da Câmara Municipal.',
          'As servidoras mesmo conferiram os protocolos do dia.',
          'Seguem anexas as certidões solicitadas pela Comissão de Finanças.',
          'É proibido a entrada de pessoas estranhas no arquivo sem autorização.'
        ],
        ans: 2,
        exp: 'Gabarito C. O adjetivo "anexo" concorda em gênero e número com o substantivo a que se refere ("Seguem anexas as certidões"). Na B seria "Elas mesmas"; na D "É proibida a entrada" (pois tem artigo "a").'
      },
      {
        num: 5, cat: 'pt', mat: 'Língua Portuguesa • Conjunções Adversativas',
        q: 'Na frase "O projeto de lei recebeu parecer favorável da comissão, CONTUDO precisará de ajustes na redação final", o conectivo destacado expressa ideia de:',
        opts: [
          'Adição, equivalendo a "ademais".',
          'Oposição / Adversidade, podendo ser substituído por "todavia", "entretanto" ou "no entanto".',
          'Conclusão, podendo ser substituído por "portanto".',
          'Finalidade, equivalendo a "a fim de que".'
        ],
        ans: 1,
        exp: 'Gabarito B. "Contudo" é conjunção coordenativa adversativa (indica oposição/ressalva), sendo sinônima de "mas, porém, todavia, entretanto, no entanto".'
      },
      {
        num: 6, cat: 'pt', mat: 'Língua Portuguesa • Colocação Pronominal (Próclise)',
        q: 'De acordo com a gramática normativa, palavras negativas ("não, nunca, jamais, ninguém") atraem o pronome oblíquo átono para antes do verbo (próclise). Assinale a frase CORRETA:',
        opts: [
          'Não informou-se o horário da reunião aos suplentes.',
          'Jamais afastar-nos-emos dos princípios da legalidade.',
          'Nunca se viu tamanha participação popular na Câmara de Meruoca.',
          'Me entregaram o ofício antes da abertura do expediente.'
        ],
        ans: 2,
        exp: 'Gabarito C. O advérbio negativo "Nunca" exige próclise obrigatória ("Nunca se viu"). Além disso, na letra D há erro pois não se inicia frase com pronome oblíquo átono ("Me entregaram").'
      },
      {
        num: 7, cat: 'pt', mat: 'Língua Portuguesa • Regência Verbal (Implicar e Obedecer)',
        q: 'Assinale a alternativa CORRETA quanto à regência verbal padrão:',
        opts: [
          'Todos os vereadores devem obedecer o Regimento Interno da Casa.',
          'Todos os vereadores devem obedecer ao Regimento Interno da Casa.',
          'O atraso na entrega das contas implicará em multa imediata.',
          'Prefiro mais estudar por questões do que ler doutrinas longas.'
        ],
        ans: 1,
        exp: 'Gabarito B. Os verbos "obedecer" e "desobedecer" são transitivos indiretos e exigem a preposição "A" ("obedecer AO Regimento"). Nota: "implicar" no sentido de acarretar é direto (sem "em"), e "preferir" é "preferir X a Y" (sem "mais" e sem "do que").'
      },
      {
        num: 8, cat: 'pt', mat: 'Língua Portuguesa • Formação de Palavras',
        q: 'O vocábulo "DESLEALDADE", formado pelo acréscimo simultâneo ou sucessivo do prefixo "des-" e do sufixo "-dade" ao radical "leal", exemplifica o processo de:',
        opts: [
          'Composição por justaposição.',
          'Derivação prefixal e sufixal (pois existem as palavras "desleal" e "lealdade" separadamente).',
          'Derivação regressiva.',
          'Hibridismo morfológico.'
        ],
        ans: 1,
        exp: 'Gabarito B. Em "des-leal-dade", se retirarmos o prefixo sobra "lealdade" (que existe), e se retirarmos o sufixo sobra "desleal" (que também existe). Logo, trata-se de derivação prefixal e sufixal!'
      },
      {
        num: 9, cat: 'pt', mat: 'Língua Portuguesa • Figuras de Linguagem',
        q: 'Na expressão "A Casa do Povo aprovou ontem o novo orçamento municipal de Meruoca", o emprego de "A Casa do Povo" no lugar de "A Câmara Municipal" e dos "Vereadores" caracteriza:',
        opts: [
          'Antítese.',
          'Metonímia / Perífrase (substituição de um termo por outro com o qual mantém relação de proximidade ou característica marcante).',
          'Pleonasmo vicioso.',
          'Onomatopeia.'
        ],
        ans: 1,
        exp: 'Gabarito B. Usar o continente pelo conteúdo ("A Câmara aprovou" no lugar de "Os vereadores aprovaram") é Metonímia, e usar um epíteto consagrado ("Casa do Povo") é Perífrase/Antonomásia.'
      },
      {
        num: 10, cat: 'pt', mat: 'Língua Portuguesa • Uso do Hífen (Novo Acordo Ortográfico)',
        q: 'Segundo o Novo Acordo Ortográfico da Língua Portuguesa, assinale a alternativa em que TODAS as palavras estão grafadas CORRETAMENTE:',
        opts: [
          'Auto-escola, anti-sala e micro-ondas.',
          'Autoescola, antessala e micro-ondas.',
          'Auto escola, ante-sala e microondas.',
          'Contra-regra, infra-estrutura e sub-chefe.'
        ],
        ans: 1,
        exp: 'Gabarito B. Vogais diferentes juntam-se sem hífen (autoescola, infraestrutura); quando o prefixo termina em vogal e a palavra seguinte começa com R ou S, dobra-se a consoante (antessala, contrarregra); vogais iguais separam-se com hífen (micro-ondas).'
      },

      // 11 a 15: Matemática & RLM (Rodada 2)
      {
        num: 11, cat: 'mat', mat: 'Raciocínio Lógico • Equivalência da Condicional',
        q: 'Considere a proposição verdadeira: "Se o projeto é de Lei Complementar, então exige maioria absoluta". Uma proposição logicamente EQUIVALENTE a essa afirmação é:',
        opts: [
          'Se o projeto não é de Lei Complementar, então não exige maioria absoluta.',
          'Se exige maioria absoluta, então o projeto é de Lei Complementar.',
          'Se não exige maioria absoluta, então o projeto não é de Lei Complementar.',
          'O projeto é de Lei Complementar e não exige maioria absoluta.'
        ],
        ans: 2,
        exp: 'Gabarito C. A equivalência contrapositiva de "Se P, então Q" é obtida INVERTENDO a ordem e NEGANDO as duas partes ("Se NÃO Q, então NÃO P"): "Se não exige maioria absoluta, então o projeto não é de Lei Complementar".'
      },
      {
        num: 12, cat: 'mat', mat: 'Matemática • Mínimo Múltiplo Comum (MMC)',
        q: 'Na Câmara Municipal, a Comissão de Justiça reúne-se a cada 4 dias e a Comissão de Finanças reúne-se a cada 6 dias. Se hoje ambas realizaram reunião juntas, daqui a quantos dias voltarão a se reunir no mesmo dia?',
        opts: [
          '8 dias.',
          '10 dias.',
          '12 dias.',
          '24 dias.'
        ],
        ans: 2,
        exp: 'Gabarito C. Problemas de coincidência de ciclos no futuro resolvem-se pelo MMC. O menor múltiplo comum entre 4 e 6 é 12 (múltiplos de 4: 4, 8, 12...; múltiplos de 6: 6, 12...). Logo, em 12 dias!'
      },
      {
        num: 13, cat: 'mat', mat: 'Matemática • Máximo Divisor Comum (MDC)',
        q: 'O setor de arquivo precisa organizar 24 pastas de projetos de lei e 36 pastas de decretos legislativos em caixas-arquivo, de modo que todas as caixas tenham a mesma quantidade de pastas, contenham apenas pastas do mesmo tipo e tenham a MAIOR quantidade possível por caixa. Quantas pastas terá cada caixa?',
        opts: [
          '6 pastas.',
          '8 pastas.',
          '12 pastas.',
          '18 pastas.'
        ],
        ans: 2,
        exp: 'Gabarito C. Dividir em partes iguais do maior tamanho possível é problema clássico de MDC. O Máximo Divisor Comum entre 24 e 36 é 12 (24 ÷ 12 = 2 caixas; 36 ÷ 12 = 3 caixas).'
      },
      {
        num: 14, cat: 'mat', mat: 'Matemática • Juros Simples',
        q: 'Um capital de R$ 2.000,00 foi aplicado sob o regime de juros simples à taxa de 3% ao mês durante 5 meses. Qual é o valor dos JUROS produzidos e o MONTANTE final ao término desse período?',
        opts: [
          'Juros de R$ 150,00 e Montante de R$ 2.150,00.',
          'Juros de R$ 300,00 e Montante de R$ 2.300,00.',
          'Juros de R$ 250,00 e Montante de R$ 2.250,00.',
          'Juros de R$ 60,00 e Montante de R$ 2.060,00.'
        ],
        ans: 1,
        exp: 'Gabarito B. 3% de R$ 2.000,00 = R$ 60,00 por mês. Em 5 meses: 5 × 60 = R$ 300,00 de juros. Somando ao capital inicial de R$ 2.000,00, o montante é R$ 2.300,00.'
      },
      {
        num: 15, cat: 'mat', mat: 'Matemática • Regra de Três Simples',
        q: 'Se 4 digitadores da Secretaria da Câmara conseguem digitalizar 120 atas em 3 horas de trabalho, quantas atas serão digitalizadas por 6 digitadores, no mesmo ritmo, também em 3 horas?',
        opts: [
          '150 atas.',
          '160 atas.',
          '180 atas.',
          '200 atas.'
        ],
        ans: 2,
        exp: 'Gabarito C. Como o tempo é o mesmo (3 horas), cada digitador digitaliza 120 ÷ 4 = 30 atas. Portanto, 6 digitadores digitalizarão 6 × 30 = 180 atas.'
      },

      // 16 a 20: Informática (Rodada 2)
      {
        num: 16, cat: 'info', mat: 'Informática • Microsoft Excel (Dois-pontos vs. Ponto e vírgula)',
        q: 'Em uma planilha do Excel, os valores das células são: A1=10, A2=20, A3=30 e A4=40. Qual será o resultado exato da fórmula =SOMA(A1;A4) comparada à fórmula =SOMA(A1:A4)?',
        opts: [
          'Ambas retornam 100.',
          '=SOMA(A1;A4) retorna 50 (soma apenas A1 e A4), enquanto =SOMA(A1:A4) retorna 100 (soma de A1 até A4).',
          '=SOMA(A1;A4) retorna 100, enquanto =SOMA(A1:A4) retorna 50.',
          '=SOMA(A1;A4) apresenta erro de sintaxe.'
        ],
        ans: 1,
        exp: 'Gabarito B. Ponto e vírgula (;) significa "E" -> soma apenas A1 (10) + A4 (40) = 50. Dois-pontos (:) significa "ATÉ" -> soma todo o intervalo A1+A2+A3+A4 = 100.'
      },
      {
        num: 17, cat: 'info', mat: 'Informática • Correio Eletrônico (CC vs. CCo)',
        q: 'Ao enviar um e-mail institucional pela Secretaria da Câmara para vários destinatários, o servidor deseja que um dos destinatários receba a mensagem SEM que os demais saibam que ele a recebeu. Para isso, o endereço desse destinatário deve ser inserido no campo:',
        opts: [
          'Para (To).',
          'CC (Com Cópia).',
          'CCo (Com Cópia Oculta / Bcc).',
          'Assunto (Subject).'
        ],
        ans: 2,
        exp: 'Gabarito C. O campo CCo (Com Cópia Oculta) oculta os endereços ali listados para os demais destinatários da mensagem.'
      },
      {
        num: 18, cat: 'info', mat: 'Informática • Redes (Intranet vs. Extranet)',
        q: 'A rede corporativa interna de uma Câmara Municipal, baseada nos mesmos protocolos da Internet (TCP/IP), mas de acesso restrito exclusivamente aos servidores e vereadores autenticados no órgão, denomina-se:',
        opts: [
          'Intranet.',
          'Deep Web.',
          'ARPANET.',
          'Bluetooth.'
        ],
        ans: 0,
        exp: 'Gabarito A. Intranet é a rede privada interna de uma instituição. Quando parte desse acesso é liberada para parceiros externos autorizados, chama-se Extranet.'
      },
      {
        num: 19, cat: 'info', mat: 'Informática • Segurança da Informação (Phishing)',
        q: 'Um servidor recebeu um e-mail falso que imitava perfeitamente a página do banco oficial da Câmara, solicitando que clicasse em um link urgente para recadastrar sua senha e token. Esse tipo de golpe de engenharia social para "pescar" dados confidenciais é denominado:',
        opts: [
          'Phishing.',
          'Defacement.',
          'Overclocking.',
          'Spooling.'
        ],
        ans: 0,
        exp: 'Gabarito A. Phishing ("pescaria" digital) utiliza mensagens e páginas falsas idênticas às legítimas para induzir o usuário a entregar senhas, cartões e credenciais.'
      },
      {
        num: 20, cat: 'info', mat: 'Informática • Atalhos do Windows 10/11',
        q: 'No sistema operacional Windows, caso o servidor precise se afastar rapidamente de sua mesa de trabalho na Câmara e queira BLOQUEAR a tela do computador imediatamente por segurança, deve pressionar o atalho:',
        opts: [
          'Tecla Windows + L',
          'Tecla Windows + E',
          'Alt + F4',
          'Ctrl + Alt + P'
        ],
        ans: 0,
        exp: 'Gabarito A. Tecla Windows + L (de Lock = bloquear) bloqueia imediatamente a sessão do usuário no Windows. Já Windows + E abre o Explorador de Arquivos.'
      },

      // 21 a 40: Conhecimentos Específicos — LOM, Regimento, Arquivologia, Admin e CF (Rodada 2)
      {
        num: 21, cat: 'esp', mat: 'Lei Orgânica de Meruoca • Posse e Vacância do Cargo de Prefeito',
        q: 'De acordo com a Lei Orgânica do Município de Meruoca, o Prefeito e o Vice-Prefeito tomam posse no dia 1º de janeiro em sessão solene na Câmara Municipal. Se, decorrido o prazo legal da data fixada para a posse, o Prefeito ou o Vice-Prefeito (salvo motivo de força maior aceito pela Câmara) não tiver assumido o cargo, este será declarado vago. Qual é esse prazo?',
        opts: [
          '48 (quarenta e oito) horas.',
          '5 (cinco) dias úteis.',
          '10 (dez) dias.',
          '60 (sessenta) dias.'
        ],
        ans: 2,
        exp: 'Gabarito C. Se decorridos 10 (dez) dias da data fixada para a posse o Prefeito ou Vice-Prefeito não assumir o cargo (salvo justo motivo aceito pela Câmara), o cargo será declarado vago.'
      },
      {
        num: 22, cat: 'esp', mat: 'Lei Orgânica de Meruoca • Ausência do Prefeito do Município',
        q: 'O Prefeito de Meruoca não poderá ausentar-se do Município, sem licença prévia da Câmara Municipal, sob pena de perda do cargo, por período superior a:',
        opts: [
          '5 (cinco) dias.',
          '15 (quinze) dias consecutivos.',
          '30 (trinta) dias.',
          '45 (quarenta e cinco) dias.'
        ],
        ans: 1,
        exp: 'Gabarito B. Conforme a Lei Orgânica e o modelo constitucional (Art. 83 da CF por simetria), o Prefeito não pode ausentar-se do Município por mais de 15 (quinze) dias consecutivos sem licença da Câmara Municipal, sob pena de perda do cargo.'
      },
      {
        num: 23, cat: 'esp', mat: 'Lei Orgânica & CF/88 • Inviolabilidade Parlamentar do Vereador',
        q: 'Nos termos do Art. 29, VIII da Constituição Federal e da Lei Orgânica de Meruoca, os Vereadores gozam de inviolabilidade (imunidade material) por suas opiniões, palavras e votos no exercício do mandato:',
        opts: [
          'Em todo o território nacional.',
          'Em todo o território do Estado do Ceará.',
          'Na circunscrição do Município.',
          'Apenas quando autorizados previamente pelo Poder Judiciário.'
        ],
        ans: 2,
        exp: 'Gabarito C. Art. 29, VIII da CF/88: "inviolabilidade dos Vereadores por suas opiniões, palavras e votos no exercício do mandato e NA CIRCUNSCRIÇÃO DO MUNICÍPIO".'
      },
      {
        num: 24, cat: 'esp', mat: 'Lei Orgânica & Regimento • Vereador Nomeado Secretário Municipal',
        q: 'Caso um Vereador da Câmara Municipal de Meruoca seja nomeado pelo Prefeito para ocupar o cargo de Secretário Municipal, o que ocorre com o seu mandato parlamentar?',
        opts: [
          'Ele perde definitivamente o mandato de Vereador, assumindo o suplente em caráter efetivo.',
          'Ele NÃO perde o mandato: fica automaticamente licenciado durante o exercício do cargo de Secretário, podendo optar pela remuneração do mandato.',
          'Ele acumula o exercício simultâneo nas sessões da Câmara e na Secretaria, recebendo as duas remunerações.',
          'A nomeação é nula, pois é proibido a qualquer Vereador assumir Secretaria Municipal.'
        ],
        ans: 1,
        exp: 'Gabarito B. Em simetria com o Art. 56, I e § 3º da CF/88 e a Lei Orgânica, o Vereador investido no cargo de Secretário Municipal NÃO perde o mandato; ele se licencia automaticamente e pode optar pela remuneração do mandato.'
      },
      {
        num: 25, cat: 'esp', mat: 'Regimento Interno • Sessões Ordinárias e Ordem do Dia',
        q: 'Nas Sessões Ordinárias da Câmara Municipal, a fase destinada especificamente à discussão e VOTAÇÃO das proposições e projetos constantes da pauta denomina-se:',
        opts: [
          'Pequeno Expediente.',
          'Ordem do Dia.',
          'Explicação Pessoal.',
          'Tribuna Livre.'
        ],
        ans: 1,
        exp: 'Gabarito B. A Ordem do Dia é a fase central da sessão ordinária em que se discutem e votam os projetos de lei, resoluções, decretos legislativos e pareceres.'
      },
      {
        num: 26, cat: 'esp', mat: 'Regimento Interno • Voto do Presidente da Câmara',
        q: 'De acordo com as normas regimentais das Câmaras Municipais, o Presidente da Câmara dirige os trabalhos em Plenário e, nas votações ostensivas de maioria simples (relativa), exerce o direito de voto:',
        opts: [
          'Sempre em primeiro lugar, tendo seu voto peso duplo em todas as sessões.',
          'Apenas quando ocorrer empate (voto de qualidade ou de minerva), votando normalmente nas matérias que exigem maioria absoluta ou 2/3 e na eleição da Mesa.',
          'Nunca, sendo proibido ao Presidente votar mesmo em caso de empate ou emenda à Lei Orgânica.',
          'Somente quando o Prefeito comparecer pessoalmente ao Plenário.'
        ],
        ans: 1,
        exp: 'Gabarito B. Regra clássica dos Regimentos Internos: o Presidente só vota nas deliberações de maioria simples para desempatar; porém, vota normalmente quando a matéria exige quórum qualificado (maioria absoluta ou 2/3) e nas eleições da Mesa.'
      },
      {
        num: 27, cat: 'esp', mat: 'Regimento Interno • Decreto Legislativo vs. Resolução',
        q: 'Qual é a espécie normativa elaborada exclusivamente pela Câmara Municipal (sem sanção do Prefeito) utilizada para julgar as contas anuais do Prefeito após o parecer prévio do TCE e para conceder Título de Cidadão Honorário?',
        opts: [
          'Decreto Legislativo.',
          'Medida Provisória.',
          'Portaria de Gabinete.',
          'Lei Delegada.'
        ],
        ans: 0,
        exp: 'Gabarito A. O Decreto Legislativo regula matérias de competência exclusiva da Câmara que produzem efeitos EXTERNOS (julgamento das contas do Executivo, concessão de títulos honoríficos, licença ao Prefeito).'
      },
      {
        num: 28, cat: 'esp', mat: 'Arquivologia & Rotinas Legislativas • Teoria das Três Idades',
        q: 'No gerenciamento de arquivos da Câmara Municipal, os documentos que perderam seu valor administrativo imediato, mas que já possuem valor histórico, probatório e cultural definitivo para a memória do Município, integram o:',
        opts: [
          'Arquivo Corrente (1ª Idade), podendo ser descartados após 30 dias.',
          'Arquivo Intermediário (2ª Idade), sujeito à fragmentação anual.',
          'Arquivo Permanente (3ª Idade), cujos documentos são inalienáveis, imprescritíveis e jamais podem ser eliminados.',
          'Arquivo Morto Descartável.'
        ],
        ans: 2,
        exp: 'Gabarito C. Os documentos de 3ª idade (Arquivo Permanente) possuem valor histórico/cultural definitivo e NUNCA podem ser eliminados.'
      },
      {
        num: 29, cat: 'esp', mat: 'Arquivologia & Rotinas • Tabela de Temporalidade',
        q: 'O instrumento arquivístico aprovado pela instituição que determina os prazos de guarda dos documentos nos arquivos corrente e intermediário e fixa sua destinação final (eliminação ou recolhimento ao arquivo permanente) é chamado de:',
        opts: [
          'Tabela de Temporalidade Documental.',
          'Livro de Ponto de Protocolo.',
          'Ata de Sessão Solene.',
          'Catálogo de Compras.'
        ],
        ans: 0,
        exp: 'Gabarito A. A Tabela de Temporalidade é o instrumento que define exatamente quanto tempo cada documento fica no arquivo corrente, quanto tempo fica no intermediário e qual será sua destinação final.'
      },
      {
        num: 30, cat: 'esp', mat: 'Direito Administrativo • Poderes (Delegação e Avocação)',
        q: 'De acordo com a doutrina e a Lei do Processo Administrativo (Lei nº 9.784/99), decorrem do Poder Hierárquico a delegação e a avocação de competências. Contudo, NÃO podem ser objeto de delegação:',
        opts: [
          'A prática de atos de expediente e rotinas de protocolo.',
          'A edição de atos de caráter normativo, a decisão de recursos administrativos e as matérias de competência exclusiva do órgão ou autoridade (CE-NO-RE).',
          'A instrução de processos licitatórios comuns.',
          'A assinatura de certidões de tempo de serviço.'
        ],
        ans: 1,
        exp: 'Gabarito B. Mnemônico CE-NO-RE (Art. 13 da Lei 9.784/99): são indelegáveis as matérias de Competência Exclusiva, a edição de atos de caráter Normativo e a decisão de Recursos administrativos.'
      },
      {
        num: 31, cat: 'esp', mat: 'Direito Administrativo • Poder Disciplinar vs. Poder de Polícia',
        q: 'Quando a Presidência da Câmara Municipal aplica a penalidade de suspensão a um servidor efetivo da Casa, após regular Processo Administrativo Disciplinar (PAD), por infração funcional, a Administração atua no exercício direto do:',
        opts: [
          'Poder de Polícia Administrativa.',
          'Poder Disciplinar.',
          'Poder Regulamentar Autônomo.',
          'Poder Constituinte Originário.'
        ],
        ans: 1,
        exp: 'Gabarito B. Punir servidor público ou particular que possui vínculo jurídico específico (contrato) com a Administração é exercício do PODER DISCIPLINAR.'
      },
      {
        num: 32, cat: 'esp', mat: 'Direito Administrativo • Nova Lei de Improbidade (Lei 14.230/2021)',
        q: 'Com as alterações promovidas pela Lei nº 14.230/2021 na Lei de Improbidade Administrativa (Lei nº 8.429/92), para que um agente público seja condenado por ato de improbidade administrativa (seja por enriquecimento ilícito, lesão ao erário ou violação a princípios), exige-se comprovadamente:',
        opts: [
          'Apenas culpa leve ou falta de atenção do servidor.',
          'Conduta obrigatoriamente DOLOSA (dolo específico: vontade livre e consciente de alcançar o resultado ilícito tipificado na lei), tendo sido extinta a improbidade meramente culposa.',
          'Mera irregularidade formal sem intenção desonesta.',
          'Responsabilidade objetiva automática do chefe do setor.'
        ],
        ans: 1,
        exp: 'Gabarito B. A reforma da Lei de Improbidade (Lei 14.230/2021) extinguiu a modalidade culposa! Hoje, qualquer ato de improbidade exige DOLO ESPECÍFICO.'
      },
      {
        num: 33, cat: 'esp', mat: 'Nova Lei de Licitações (Lei 14.133/2021) • Pregão vs. Concorrência',
        q: 'Nos termos da Lei nº 14.133/2021, a modalidade de licitação obrigatória para aquisição de bens e serviços COMUNS (cujos padrões de desempenho e qualidade podem ser objetivamente definidos pelo edital, por meio de especificações usuais de mercado), adotando-se o critério de menor preço ou maior desconto, é o(a):',
        opts: [
          'Diálogo Competitivo.',
          'Concurso.',
          'Pregão.',
          'Leilão.'
        ],
        ans: 2,
        exp: 'Gabarito C. Art. 6º, XLI e Art. 29 da Lei 14.133/2021: O PREGÃO é a modalidade obrigatória para aquisição de bens e serviços comuns (critérios: menor preço ou maior desconto).'
      },
      {
        num: 34, cat: 'esp', mat: 'Nova Lei de Licitações (Lei 14.133/2021) • Ordem das Fases',
        q: 'De acordo com o Art. 17 da Lei nº 14.133/2021, no rito procedimental comum das licitações (Pregão e Concorrência), a fase de HABILITAÇÃO ocorre, como regra geral:',
        opts: [
          'Antes da publicação do edital.',
          'APÓS a fase de apresentação de propostas/lances e de JULGAMENTO (verificando-se os documentos de habilitação apenas do licitante mais bem classificado), salvo inversão motivada prevista no edital.',
          'Apenas após a assinatura e execução total do contrato.',
          'Simultaneamente à elaboração do estudo técnico preliminar.'
        ],
        ans: 1,
        exp: 'Gabarito B. Regra geral do Art. 17 da Lei 14.133/2021: 1º Preparatória -> 2º Edital -> 3º Propostas e Lances -> 4º JULGAMENTO -> 5º HABILITAÇÃO -> 6º Recursal -> 7º Homologação.'
      },
      {
        num: 35, cat: 'esp', mat: 'Direito Administrativo • Nepotismo (Súmula Vinculante 13)',
        q: 'Segundo a Súmula Vinculante nº 13 do Supremo Tribunal Federal, a nomeação de cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, da autoridade nomeante ou de servidor da mesma pessoa jurídica investido em cargo de direção, chefia ou assessoramento, para o exercício de cargo em comissão ou de confiança na Administração Pública, é vedada até o:',
        opts: [
          '1º grau apenas (pais e filhos).',
          '2º grau apenas (irmãos e avós).',
          '3º grau (incluindo tios e sobrinhos).',
          '4º grau (incluindo primos).'
        ],
        ans: 2,
        exp: 'Gabarito C. A Súmula Vinculante 13 veda o nepotismo até o TERCEIRO GRAU (1º grau: pais/filhos; 2º grau: avós/netos/irmãos; 3º grau: bisavós/bisnetos/tios/sobrinhos). Primos são 4º grau!'
      },
      {
        num: 36, cat: 'esp', mat: 'Direito Constitucional • Art. 5º (Mandado de Segurança vs. Habeas Data)',
        q: 'Para proteger direito líquido e certo, não amparado por Habeas Corpus ou Habeas Data, quando o responsável pela ilegalidade ou abuso de poder for autoridade pública, cabe a impetração de Mandado de Segurança, cujo prazo decadencial previsto em lei é de:',
        opts: [
          '30 (trinta) dias.',
          '60 (sessenta) dias.',
          '120 (cento e vinte) dias, contados da ciência, pelo interessado, do ato impugnado.',
          '5 (cinco) anos.'
        ],
        ans: 2,
        exp: 'Gabarito C. Conforme o Art. 23 da Lei nº 12.016/2009, o direito de requerer Mandado de Segurança extinguir-se-á decorridos 120 (cento e vinte) dias, contados da ciência do ato impugnado.'
      },
      {
        num: 37, cat: 'esp', mat: 'Direito Constitucional • Art. 5º, XI (Inviolabilidade Domiciliar)',
        q: 'Nos termos do Art. 5º, XI da Constituição Federal, a casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, SALVO:',
        opts: [
          'A qualquer hora da noite mediante simples mandado de citação judicial.',
          'Em caso de flagrante delito ou desastre, ou para prestar socorro (a qualquer hora do dia ou da noite), ou, DURANTE O DIA, por determinação judicial.',
          'Por ordem verbal de fiscal da Prefeitura durante a madrugada.',
          'Por requisição de qualquer comissão da Câmara Municipal.'
        ],
        ans: 1,
        exp: 'Gabarito B. Flagrante delito, desastre ou para prestar socorro permitem entrada a qualquer hora (dia ou noite). Já por DETERMINAÇÃO JUDICIAL, somente DURANTE O DIA!'
      },
      {
        num: 38, cat: 'esp', mat: 'Direito Constitucional • Acumulação de Cargos Públicos (Art. 37, XVI)',
        q: 'Conforme o Art. 37, XVI da Constituição Federal, é vedada a acumulação remunerada de cargos públicos, EXCETO quando houver compatibilidade de horários, observado o teto remuneratório, para os seguintes casos:',
        opts: [
          'Dois cargos de Técnico Legislativo em Câmaras vizinhas.',
          'Dois cargos de professor; a de um cargo de professor com outro técnico ou científico; ou a de dois cargos ou empregos privativos de profissionais de saúde, com profissões regulamentadas.',
          'Três cargos de médico ou enfermeiro na rede municipal.',
          'Um cargo administrativo com outro de policial militar.'
        ],
        ans: 1,
        exp: 'Gabarito B. As 3 únicas exceções constitucionais do Art. 37, XVI são: 1) dois cargos de professor; 2) um de professor + um técnico ou científico; 3) dois privativos de profissionais de saúde com profissões regulamentadas (sempre com compatibilidade de horários).'
      },
      {
        num: 39, cat: 'esp', mat: 'Direito Constitucional • Teto Remuneratório Municipal (Art. 37, XI)',
        q: 'De acordo com o Art. 37, XI da Constituição Federal de 1988, o limite máximo (teto remuneratório geral) aplicável à remuneração e ao subsídio dos ocupantes de cargos, funções e empregos públicos da Administração Direta e Indireta no âmbito do MUNICÍPIO é o subsídio mensal do:',
        opts: [
          'Presidente da Câmara Municipal.',
          'Governador do Estado.',
          'Prefeito Municipal.',
          'Juiz de Direito da Comarca.'
        ],
        ans: 2,
        exp: 'Gabarito C. Art. 37, XI da CF/88: Nos Municípios, o teto remuneratório geral dos servidores públicos (do Executivo e do Legislativo) é o subsídio do PREFEITO MUNICIPAL.'
      },
      {
        num: 40, cat: 'esp', mat: 'Lei de Responsabilidade Fiscal • Limite de Fim de Mandato',
        q: 'Nos termos do Art. 21, II da Lei de Responsabilidade Fiscal (LC nº 101/2000), é NULO de pleno direito o ato de que resulte aumento da despesa com pessoal expedido pelo titular de Poder (Prefeito ou Presidente da Câmara) nos últimos:',
        opts: [
          '30 (trinta) dias do seu mandato.',
          '60 (sessenta) dias do seu mandato.',
          '180 (cento e oitenta) dias anteriores ao final do seu mandato.',
          '2 (dois) anos de mandato.'
        ],
        ans: 2,
        exp: 'Gabarito C. Art. 21, II da LRF: É nulo de pleno direito o ato de que resulte aumento da despesa com pessoal expedido nos 180 (cento e oitenta) dias anteriores ao final do mandato do titular do respectivo Poder.'
      }
    ];

    // =========================================================================
    // RODADA 1: AS 40 QUESTÕES BASE (1 A 40)
    // =========================================================================
    const QUESTIONS_R1 = [
      {
        num: 1, cat: 'pt', mat: 'Língua Portuguesa • Verbos Impessoais',
        q: 'Assinale a alternativa em que a concordância verbal está em total conformidade com a norma-padrão da Língua Portuguesa:',
        opts: [
          'Houveram diversas manifestações favoráveis ao projeto na Câmara.',
          'Fazem três anos que o novo Regimento Interno foi promulgado.',
          'Devem haver soluções imediatas para o atendimento ao público.',
          'Houve intensos debates durante a sessão extraordinária de ontem.'
        ],
        ans: 3,
        exp: 'Gabarito D. O verbo HAVER no sentido de existir/ocorrer é impessoal e fica SEMPRE na 3ª pessoa do singular ("Houve intensos debates", "Deve haver soluções"). O verbo FAZER indicando tempo decorrido também é impessoal ("Faz três anos").'
      },
      {
        num: 2, cat: 'pt', mat: 'Língua Portuguesa • Emprego da Crase',
        q: 'Assinale a alternativa em que o acento grave indicativo de crase foi empregado CORRETAMENTE:',
        opts: [
          'A comissão reuniu-se às pressas para emitir o parecer antes da votação.',
          'O requerimento foi encaminhado à Vossa Excelência na manhã de hoje.',
          'A secretaria da Câmara funcionará em regime especial à partir de segunda-feira.',
          'Os vereadores ficaram cara à cara com os representantes do bairro.'
        ],
        ans: 0,
        exp: 'Gabarito A. Usa-se crase obrigatoriamente nas locuções adverbiais femininas ("às pressas", "às vezes", "à noite"). Não há crase antes de pronomes de tratamento ("a Vossa Excelência"), antes de verbo ("a partir") nem entre palavras repetidas ("cara a cara").'
      },
      {
        num: 3, cat: 'pt', mat: 'Língua Portuguesa • Conjunções Subordinativas',
        q: 'No período "EMBORA as emendas tenham sido apresentadas no prazo, o plenário decidiu pelo arquivamento", a conjunção destacada estabelece relação de:',
        opts: [
          'Causa, podendo ser substituída por "já que".',
          'Concessão, podendo ser substituída por "conquanto" ou "ainda que" sem alteração de sentido.',
          'Condição, podendo ser substituída por "caso".',
          'Proporcionalidade, equivalendo a "à medida que".'
        ],
        ans: 1,
        exp: 'Gabarito B. "Embora" é a principal conjunção concessiva (indica um fato contrário que não impede a ação principal) e equivale a "conquanto", "ainda que", "mesmo que", "posto que".'
      },
      {
        num: 4, cat: 'pt', mat: 'Língua Portuguesa • Pronome Relativo CUJO',
        q: 'De acordo com a gramática normativa, assinale a frase em que o pronome relativo foi empregado CORRETAMENTE:',
        opts: [
          'O vereador cujo o projeto foi aprovado agradeceu aos colegas.',
          'A lei municipal a cuja leitura procedemos ontem entrou em vigor.',
          'O parecer cujo teor foi discutido na comissão recebeu aprovação unânime.',
          'A sessão que o presidente encerrou ela mais cedo será retomada.'
        ],
        ans: 2,
        exp: 'Gabarito C. O pronome "cujo" indica posse, concorda com o substantivo seguinte ("cujo teor") e JAMAIS admite artigo posposto ("cujo o" é sempre incorreto).'
      },
      {
        num: 5, cat: 'pt', mat: 'Língua Portuguesa • Voz Passiva & Partícula SE',
        q: 'Assinale a alternativa em que a partícula "SE" atua como pronome apassivador (voz passiva pronominal):',
        opts: [
          'Precisa-se de novos servidores efetivos na Câmara Municipal.',
          'Trata-se de matérias urgentes de interesse do Município.',
          'Aprovaram-se os projetos de lei complementar na sessão de ontem.',
          'Trabalha-se com dedicação no setor legislativo.'
        ],
        ans: 2,
        exp: 'Gabarito C. "Aprovaram-se os projetos" = "Os projetos foram aprovados" (Verbo Transitivo Direto sem preposição + SE apassivador, concordando no plural com o sujeito paciente).'
      },
      {
        num: 6, cat: 'pt', mat: 'Língua Portuguesa • Conjunção Integrante x Pronome Relativo',
        q: 'Assinale a opção em que o vocábulo destacado "QUE" classifica-se morfologicamente como CONJUNÇÃO INTEGRANTE:',
        opts: [
          'O presidente da Mesa comunicou QUE a ordem do dia seria prorrogada.',
          'O decreto legislativo QUE foi publicado hoje aprova as contas.',
          'A pauta a QUE fizemos referência já está disponível.',
          'Os documentos QUE chegaram da Prefeitura foram protocolados.'
        ],
        ans: 0,
        exp: 'Gabarito A. Em "comunicou QUE a ordem do dia seria prorrogada" (comunicou ISSO), a palavra "que" introduz oração subordinada substantiva objetiva direta, sendo conjunção integrante.'
      },
      {
        num: 7, cat: 'pt', mat: 'Língua Portuguesa • Ortografia & Parônimos',
        q: 'Para preencher corretamente as lacunas da frase: "A Mesa Diretora resolveu ________ (corrigir) o erro material da ata e ________ (confirmar) a votação anterior", utilizam-se, respectivamente:',
        opts: [
          'ratificar — retificar',
          'retificar — ratificar',
          'deferir — infringir',
          'infligir — diferir'
        ],
        ans: 1,
        exp: 'Gabarito B. RETIFICAR = corrigir, consertar. RATIFICAR = confirmar, validar.'
      },
      {
        num: 8, cat: 'pt', mat: 'Língua Portuguesa • Regras de Acentuação',
        q: 'As palavras "público", "caráter" e "também" são acentuadas graficamente, respectivamente, por serem:',
        opts: [
          'Proparoxítona, paroxítona terminada em -r e oxítona terminada em -em.',
          'Paroxítona, proparoxítona e oxítona terminada em -m.',
          'Proparoxítona, oxítona terminada em -r e paroxítona.',
          'Oxítona, paroxítona e proparoxítona.'
        ],
        ans: 0,
        exp: 'Gabarito A. Pú-bli-co (proparoxítona: todas são acentuadas); ca-rá-ter (paroxítona terminada em -r); tam-bém (oxítona terminada em -em).'
      },
      {
        num: 9, cat: 'pt', mat: 'Língua Portuguesa • Pontuação',
        q: 'Assinale a alternativa em que o emprego da(s) vírgula(s) está INCORRETO por violar regra básica de sintaxe:',
        opts: [
          'Meruoca, 18 de outubro de 2026.',
          'Os cidadãos, que acompanharam a sessão, aplaudiram a iniciativa.',
          'O Presidente da Câmara Municipal, convocou todos os vereadores para a sessão.',
          'Senhor Presidente, solicito a palavra pela ordem.'
        ],
        ans: 2,
        exp: 'Gabarito C. Jamais se separa o sujeito ("O Presidente da Câmara Municipal") do seu verbo ("convocou") por uma única vírgula!'
      },
      {
        num: 10, cat: 'pt', mat: 'Língua Portuguesa • Regência Verbal',
        q: 'Segundo a norma-padrão, o verbo "assistir" no sentido de "ver / presenciar" é transitivo indireto. Assinale a frase correta:',
        opts: [
          'Os moradores assistiram a sessão solene pela internet sem preposição.',
          'Os moradores assistiram à sessão solene de posse dos vereadores.',
          'A população assistiu o debate político na praça.',
          'Todos assistiram no julgamento das contas.'
        ],
        ans: 1,
        exp: 'Gabarito B. "Assistir" no sentido de ver/presenciar exige a preposição "a" -> "assistiram à sessão".'
      },
      {
        num: 11, cat: 'mat', mat: 'Raciocínio Lógico • Lei de De Morgan (Negação do E)',
        q: 'A negação lógica correta da proposição composta "O projeto foi votado E a sessão foi encerrada" é:',
        opts: [
          'O projeto não foi votado E a sessão não foi encerrada.',
          'Se o projeto não foi votado, então a sessão não foi encerrada.',
          'O projeto não foi votado OU a sessão não foi encerrada.',
          'O projeto foi votado OU a sessão não foi encerrada.'
        ],
        ans: 2,
        exp: 'Gabarito C. Para negar o "E", negam-se as duas partes e troca-se por "OU".'
      },
      {
        num: 12, cat: 'mat', mat: 'Raciocínio Lógico • Negação da Condicional (MANÉ)',
        q: 'Qual é a negação lógica da proposição condicional "Se o candidato estuda a Lei Orgânica, então acerta a questão"?',
        opts: [
          'Se o candidato não estuda a Lei Orgânica, então não acerta a questão.',
          'O candidato estuda a Lei Orgânica E não acerta a questão.',
          'O candidato não estuda a Lei Orgânica OU acerta a questão.',
          'O candidato não estuda a Lei Orgânica E não acerta a questão.'
        ],
        ans: 1,
        exp: 'Gabarito B. Regra do MANÉ: MAntém a primeira (estuda) E NEga a segunda (não acerta).'
      },
      {
        num: 13, cat: 'mat', mat: 'Matemática • Divisão Diretamente Proporcional',
        q: 'Um lote com 360 processos administrativos será distribuído entre 3 técnicos legislativos em partes diretamente proporcionais a 2, 3 e 4. Quantos processos receberá o técnico que ficará com a MENOR parte?',
        opts: [
          '60 processos.',
          '80 processos.',
          '120 processos.',
          '160 processos.'
        ],
        ans: 1,
        exp: 'Gabarito B. Soma = 2+3+4 = 9. Cada parte = 360 ÷ 9 = 40. Menor parte = 2 × 40 = 80 processos.'
      },
      {
        num: 14, cat: 'mat', mat: 'Matemática • Porcentagem e Desconto',
        q: 'Na aquisição de equipamentos para a Câmara, uma impressora teve desconto de 15% no pagamento à vista, saindo por R$ 850,00. Qual era o preço original dessa impressora sem o desconto?',
        opts: [
          'R$ 950,00.',
          'R$ 977,50.',
          'R$ 1.000,00.',
          'R$ 1.050,00.'
        ],
        ans: 2,
        exp: 'Gabarito C. 850 ÷ 0,85 = R$ 1.000,00.'
      },
      {
        num: 15, cat: 'mat', mat: 'Raciocínio Lógico • Negação de Quantificadores',
        q: 'A negação correta da afirmação "Todos os servidores da Câmara assinaram o ponto eletrônico" é:',
        opts: [
          'Nenhum servidor da Câmara assinou o ponto eletrônico.',
          'Todos os servidores da Câmara deixaram de assinar o ponto.',
          'Pelo menos um servidor da Câmara não assinou o ponto eletrônico.',
          'Apenas metade dos servidores assinou o ponto eletrônico.'
        ],
        ans: 2,
        exp: 'Gabarito C. A negação de "Todo" é "Algum não" / "Pelo menos um não".'
      },
      {
        num: 16, cat: 'info', mat: 'Informática • Atalhos do Microsoft Word (Português)',
        q: 'No Microsoft Word (versão em português), os atalhos de teclado utilizados para SALVAR o documento atual e para LOCALIZAR uma palavra no texto são, respectivamente:',
        opts: [
          'Ctrl + S e Ctrl + F',
          'Ctrl + B e Ctrl + L',
          'Ctrl + G e Ctrl + P',
          'Ctrl + T e Ctrl + U'
        ],
        ans: 1,
        exp: 'Gabarito B. No Word em português: Ctrl + B salva e Ctrl + L localiza.'
      },
      {
        num: 17, cat: 'info', mat: 'Informática • Fórmulas do Microsoft Excel',
        q: 'Considere uma planilha do Microsoft Excel em que as células de A1 até A5 possuem 4 números e 1 palavra (texto). Qual função retorna o total de células NÃO VAZIAS desse intervalo (resultando em 5)?',
        opts: [
          '=CONT.NÚM(A1:A5)',
          '=SOMA(A1;A5)',
          '=CONT.VALORES(A1:A5)',
          '=MÉDIA(A1:A5)'
        ],
        ans: 2,
        exp: 'Gabarito C. =CONT.VALORES conta todas as células preenchidas (números e textos).'
      },
      {
        num: 18, cat: 'info', mat: 'Informática • Navegadores Web',
        q: 'Durante o uso do navegador Google Chrome ou Microsoft Edge no Windows, caso o usuário feche acidentalmente uma guia (aba) importante, qual atalho permite REABRIR imediatamente a última guia fechada?',
        opts: [
          'Ctrl + Shift + T',
          'Ctrl + T',
          'Ctrl + Shift + N',
          'Ctrl + W'
        ],
        ans: 0,
        exp: 'Gabarito A. Ctrl + Shift + T reabre a última aba fechada.'
      },
      {
        num: 19, cat: 'info', mat: 'Informática • Segurança da Informação (Malwares)',
        q: 'O tipo de código malicioso (malware) que sequestra os dados do computador por meio de criptografia e exige o pagamento de um resgate financeiro para devolver o acesso aos arquivos é chamado de:',
        opts: [
          'Spyware.',
          'Adware.',
          'Ransomware.',
          'Firewall.'
        ],
        ans: 2,
        exp: 'Gabarito C. Ransomware criptografa os dados e exige resgate.'
      },
      {
        num: 20, cat: 'info', mat: 'Informática • Windows & Armazenamento',
        q: 'No sistema operacional Windows 10/11, ao selecionar um arquivo no Explorador de Arquivos e pressionar a combinação de teclas "Shift + Delete", o sistema irá:',
        opts: [
          'Enviar o arquivo para a Lixeira com proteção contra exclusão.',
          'Excluir o arquivo permanentemente (após confirmação), sem enviá-lo para a Lixeira.',
          'Criar uma cópia de backup automática na pasta Documentos.',
          'Compactar o arquivo no formato .ZIP.'
        ],
        ans: 1,
        exp: 'Gabarito B. Shift + Delete apaga permanentemente sem passar pela Lixeira.'
      },
      {
        num: 21, cat: 'esp', mat: 'Lei Orgânica de Meruoca • Autonomia e Poderes',
        q: 'Nos termos da Constituição Federal e da Lei Orgânica do Município de Meruoca/CE, o Município goza de autonomia política, administrativa e financeira, sendo seus Poderes independentes e harmônicos entre si:',
        opts: [
          'O Legislativo, o Executivo e o Judiciário Municipal.',
          'Apenas o Poder Legislativo e o Poder Executivo.',
          'O Prefeito, o Juiz de Direito da Comarca e o Promotor de Justiça.',
          'A Câmara Municipal, a Prefeitura e o Tribunal de Contas Municipal.'
        ],
        ans: 1,
        exp: 'Gabarito B. No Município existem apenas o Poder Legislativo e o Poder Executivo.'
      },
      {
        num: 22, cat: 'esp', mat: 'Lei Orgânica & CF/88 • Controle Externo e Parecer do TCE',
        q: 'A fiscalização do Município é exercida pelo Poder Legislativo Municipal, mediante controle externo, com o auxílio do Tribunal de Contas do Estado. O parecer prévio emitido pelo Tribunal de Contas sobre as contas anuais do Prefeito:',
        opts: [
          'É meramente opinativo e pode ser derrubado por maioria simples dos vereadores presentes.',
          'Só deixará de prevalecer por decisão de 2/3 (dois terços) dos membros da Câmara Municipal.',
          'Vincula absolutamente os vereadores, que não podem votar contra o parecer do TCE.',
          'Deixa de prevalecer pelo voto da maioria absoluta da Mesa Diretora.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 31, § 2º da CF/88: O parecer prévio do TCE só deixa de prevalecer por voto de 2/3 dos membros da Câmara.'
      },
      {
        num: 23, cat: 'esp', mat: 'Lei Orgânica & CF/88 • Exame das Contas pelos Contribuintes',
        q: 'As contas do Município de Meruoca ficarão, anualmente, à disposição de qualquer contribuinte, para exame e apreciação, o qual poderá questionar-lhes a legitimidade nos termos da lei, durante o prazo de:',
        opts: [
          '30 (trinta) dias.',
          '45 (quarenta e cinco) dias.',
          '60 (sessenta) dias.',
          '90 (noventa) dias.'
        ],
        ans: 2,
        exp: 'Gabarito C. Art. 31, § 3º da CF/88: 60 (sessenta) dias anualmente.'
      },
      {
        num: 24, cat: 'esp', mat: 'Lei Orgânica & CF/88 • Iniciativa Popular de Lei',
        q: 'A iniciativa popular de projetos de lei de interesse específico do Município, da cidade ou de bairros, perante a Câmara Municipal, exige a manifestação de, pelo menos:',
        opts: [
          '1% (um por cento) da população total do Estado.',
          '5% (cinco por cento) do eleitorado do Município.',
          '10% (dez por cento) dos servidores públicos municipais.',
          '2/3 (dois terços) das associações comunitárias locais.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 29, XIII da CF/88: no mínimo 5% do eleitorado do Município.'
      },
      {
        num: 25, cat: 'esp', mat: 'Processo Legislativo • Aprovação e Emenda à Lei Orgânica',
        q: 'Para que a Lei Orgânica Municipal seja emendada ou alterada pela Câmara Municipal, exige-se votação em:',
        opts: [
          'Turno único, aprovada por maioria simples dos presentes.',
          'Dois turnos, com interstício mínimo de 10 (dez) dias, e aprovação por 2/3 (dois terços) dos membros da Câmara.',
          'Dois turnos no mesmo dia, aprovada por maioria absoluta.',
          'Três turnos, com sanção obrigatória do Prefeito Municipal.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 29 da CF/88: 2 turnos, interstício mínimo de 10 dias e aprovação por 2/3 dos membros da Câmara.'
      },
      {
        num: 26, cat: 'esp', mat: 'Processo Legislativo • Princípio da Irrepetibilidade',
        q: 'A matéria constante de projeto de lei rejeitado pelo Plenário da Câmara Municipal somente poderá constituir objeto de novo projeto, na mesma sessão legislativa, mediante proposta da:',
        opts: [
          'Maioria simples dos vereadores presentes na sessão seguinte.',
          'Maioria absoluta dos membros da Câmara Municipal.',
          'Presidência da Câmara de forma monocrática.',
          'Comissão de Constituição e Justiça por unanimidade.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 67 da CF/88: mediante proposta da maioria absoluta dos membros da Casa.'
      },
      {
        num: 27, cat: 'esp', mat: 'Processo Legislativo • Sanção, Veto e Promulgação',
        q: 'Aprovado o projeto de lei pela Câmara Municipal, ele é enviado ao Prefeito, que, aquiescendo, o sancionará. Caso o Prefeito permaneça em silêncio após decorrido o prazo de 15 (quinze) dias úteis:',
        opts: [
          'O silêncio importará em veto total automático.',
          'O silêncio do Prefeito importará em sanção tácita.',
          'O projeto será automaticamente arquivado até o ano seguinte.',
          'Caberá ao Tribunal de Justiça sancionar a lei municipal.'
        ],
        ans: 1,
        exp: 'Gabarito B. Decorridos 15 dias úteis, o silêncio do Prefeito importa em sanção tácita.'
      },
      {
        num: 28, cat: 'esp', mat: 'Regimento Interno • Resolução vs. Decreto Legislativo',
        q: 'No processo legislativo da Câmara Municipal, o ato normativo destinado a regular matérias de competência privativa da Casa de caráter político-administrativo com efeitos INTERNOS (como alterações do Regimento Interno), promulgado pela Mesa e que NÃO depende de sanção do Prefeito, denomina-se:',
        opts: [
          'Lei Delegada.',
          'Medida Provisória Municipal.',
          'Resolução.',
          'Portaria Executiva.'
        ],
        ans: 2,
        exp: 'Gabarito C. Resolução regula matérias de efeito interno da Câmara Municipal.'
      },
      {
        num: 29, cat: 'esp', mat: 'Regimento Interno & CF/88 • Limites Financeiros da Câmara',
        q: 'Sobre os limites constitucionais e fiscais da Câmara Municipal, assinale a alternativa CORRETA:',
        opts: [
          'A Câmara Municipal pode gastar até 95% de sua receita exclusivamente com a folha de pagamento.',
          'A Câmara não gastará mais de 70% de sua receita com folha de pagamento, incluído o gasto com o subsídio de seus Vereadores (Art. 29-A, § 1º da CF/88), e seu limite total de despesa com pessoal na LRF é de 6% da Receita Corrente Líquida do Município.',
          'Para a criação de uma CPI na Câmara, exige-se a aprovação de 2/3 do plenário.',
          'Os Vereadores gozam de inviolabilidade em todo o território nacional.'
        ],
        ans: 1,
        exp: 'Gabarito B. Máximo de 70% de sua receita com folha de pagamento (CF Art. 29-A, § 1º) e máximo de 6% da RCL na LRF.'
      },
      {
        num: 30, cat: 'esp', mat: 'Nova Lei de Licitações (Lei 14.133/2021) • Modalidades',
        q: 'De acordo com o Art. 28 da Lei nº 14.133/2021, são modalidades de licitação expressamente previstas na nova legislação:',
        opts: [
          'Pregão, Concorrência, Tomada de Preços, Convite e Leilão.',
          'Pregão, Concorrência, Concurso, Leilão e Diálogo Competitivo.',
          'Concorrência, Tomada de Preços, RDC, Pregão e Concurso.',
          'Convite, Pregão Presencial, Leilão e Consulta Pública.'
        ],
        ans: 1,
        exp: 'Gabarito B. As 5 modalidades são: Pregão, Concorrência, Concurso, Leilão e Diálogo Competitivo.'
      },
      {
        num: 31, cat: 'esp', mat: 'Nova Lei de Licitações (Lei 14.133/2021) • Alienação de Imóveis',
        q: 'Nos termos da Lei nº 14.133/2021, a alienação de bens imóveis da Administração Pública dependerá de autorização legislativa, avaliação prévia e licitação na modalidade:',
        opts: [
          'Leilão.',
          'Pregão.',
          'Concurso.',
          'Diálogo Competitivo.'
        ],
        ans: 0,
        exp: 'Gabarito A. Art. 76 da Lei 14.133/2021: a alienação de bens imóveis agora ocorre por Leilão.'
      },
      {
        num: 32, cat: 'esp', mat: 'Nova Lei de Licitações (Lei 14.133/2021) • Inexigibilidade',
        q: 'Segundo o Art. 74 da Lei nº 14.133/2021, é INEXIGÍVEL a licitação quando inviável a competição, sendo expressamente VEDADA a inexigibilidade para:',
        opts: [
          'Treinamento e aperfeiçoamento de pessoal.',
          'Pareceres, perícias e avaliações em geral.',
          'Serviços de publicidade e divulgação.',
          'Patrocínio ou defesa de causas judiciais ou administrativas.'
        ],
        ans: 2,
        exp: 'Gabarito C. É expressamente vedada a inexigibilidade para serviços de publicidade e divulgação.'
      },
      {
        num: 33, cat: 'esp', mat: 'Direito Administrativo • Princípios (Art. 37 CF/88)',
        q: 'Quando o Presidente da Câmara ou o Prefeito inclui seu nome, símbolo ou fotografia pessoal em placas de obras ou campanhas institucionais custeadas pelo erário, há violação direta do Art. 37, § 1º da CF/88 e do princípio da:',
        opts: [
          'Impessoalidade.',
          'Autotutela.',
          'Continuidade.',
          'Hierarquia.'
        ],
        ans: 0,
        exp: 'Gabarito A. Proibição de promoção pessoal em publicidade oficial decorre do princípio da Impessoalidade.'
      },
      {
        num: 34, cat: 'esp', mat: 'Direito Administrativo • Desconcentração vs. Descentralização',
        q: 'Quando a Câmara Municipal de Meruoca cria internamente um novo Departamento de Arquivo e Protocolo subordinado à Diretoria Administrativa, sem criação de nova pessoa jurídica, ocorre:',
        opts: [
          'Descentralização por outorga.',
          'Desconcentração administrativa.',
          'Concessão de serviço público.',
          'Privatização funcional.'
        ],
        ans: 1,
        exp: 'Gabarito B. DesCOncentração cria Órgão interno na mesma pessoa jurídica.'
      },
      {
        num: 35, cat: 'esp', mat: 'Direito Administrativo • Administração Indireta',
        q: 'Assinale a entidade da Administração Indireta que possui personalidade jurídica de DIREITO PÚBLICO e é criada DIRETAMENTE por lei específica (Art. 37, XIX da CF/88):',
        opts: [
          'Sociedade de Economia Mista.',
          'Empresa Pública.',
          'Autarquia.',
          'Organização da Sociedade Civil.'
        ],
        ans: 2,
        exp: 'Gabarito C. Somente a Autarquia é criada diretamente por lei específica e possui direito público.'
      },
      {
        num: 36, cat: 'esp', mat: 'Direito Administrativo • Anulação vs. Revogação',
        q: 'A respeito da extinção dos atos administrativos (Súmula 473 STF), é CORRETO afirmar que:',
        opts: [
          'A revogação recai sobre atos ilegais e produz efeitos retroativos (ex tunc).',
          'A anulação recai sobre atos ilegais com efeitos retroativos (ex tunc), enquanto a revogação recai sobre atos válidos por conveniência e oportunidade, com efeitos prospectivos (ex nunc).',
          'O Poder Judiciário pode revogar atos discricionários da Câmara Municipal.',
          'Atos vinculados podem ser livremente revogados.'
        ],
        ans: 1,
        exp: 'Gabarito B. Anulação = ato ilegal (ex tunc). Revogação = ato legal inconveniente/inoportuno (ex nunc).'
      },
      {
        num: 37, cat: 'esp', mat: 'Direito Administrativo • Atributos do Ato Administrativo',
        q: 'O atributo pelo qual os atos administrativos presumem-se verdadeiros e legítimos até prova em contrário (presunção relativa) denomina-se:',
        opts: [
          'Autoexecutoriedade absoluta.',
          'Tipicidade.',
          'Presunção de legitimidade e veracidade.',
          'Imperatividade.'
        ],
        ans: 2,
        exp: 'Gabarito C. Presunção de legitimidade e veracidade.'
      },
      {
        num: 38, cat: 'esp', mat: 'Direito Constitucional • Art. 5º (Crimes Imprescritíveis)',
        q: 'Segundo o Art. 5º, XLII e XLIV da CF/88, constituem crimes INAFIANÇÁVEIS e IMPRESCRITÍVEIS:',
        opts: [
          'A prática da tortura e o tráfico ilícito de entorpecentes.',
          'A prática do racismo e a ação de grupos armados, civis ou militares, contra a ordem constitucional e o Estado Democrático.',
          'O terrorismo e os crimes hediondos.',
          'O peculato e a improbidade administrativa.'
        ],
        ans: 1,
        exp: 'Gabarito B. Mnemônico RAÇÃO: Racismo e Ação de grupos armados contra a ordem constitucional.'
      },
      {
        num: 39, cat: 'esp', mat: 'Direito Constitucional • Estabilidade (Art. 41 CF/88)',
        q: 'O servidor nomeado para cargo de provimento efetivo em virtude de concurso público adquire estabilidade após:',
        opts: [
          '3 (três) anos de efetivo exercício, mediante avaliação especial de desempenho.',
          '2 (dois) anos de posse, inclusive em cargos em comissão.',
          '1 (um) ano de estágio probatório.',
          '5 (cinco) anos de serviço público.'
        ],
        ans: 0,
        exp: 'Gabarito A. Art. 41 da CF/88: 3 anos de efetivo exercício + avaliação especial de desempenho.'
      },
      {
        num: 40, cat: 'esp', mat: 'Redação Oficial • Padrão Ofício',
        q: 'De acordo com o Manual de Redação da Presidência da República (3ª edição), os fechos oficiais padronizados para todas as comunicações são apenas:',
        opts: [
          '"Respeitosamente," (para autoridades superiores) e "Atenciosamente," (para autoridades de mesma hierarquia, inferiores ou particulares).',
          '"Saudações cordiais" e "Abraços fraternos".',
          '"Sem mais para o momento" e "Atenciosamente".',
          '"Deferimento" e "Respeitosamente".'
        ],
        ans: 0,
        exp: 'Gabarito A. Existem apenas dois fechos oficiais: "Respeitosamente," (para autoridades superiores) e "Atenciosamente," (para mesma hierarquia ou inferiores).'
      }
    ];

    let currentRound = 2; // Abre direto na Rodada 2 Nova!
    let choicesR1 = {};
    let choicesR2 = {};
    let currentFilterCat = 'all';

    function getActiveList() {
      return currentRound === 2 ? QUESTIONS_R2 : QUESTIONS_R1;
    }

    function getActiveChoices() {
      return currentRound === 2 ? choicesR2 : choicesR1;
    }

    function switchRound(roundNum) {
      currentRound = roundNum;
      document.getElementById('round2Content').style.display = (roundNum === 2) ? 'block' : 'none';
      document.getElementById('round1Content').style.display = (roundNum === 1) ? 'block' : 'none';

      document.getElementById('bigBtnR2').classList.toggle('active', roundNum === 2);
      document.getElementById('bigBtnR1').classList.toggle('active', roundNum === 1);
      document.getElementById('tabBtnR2').classList.toggle('active', roundNum === 2);
      document.getElementById('tabBtnR1').classList.toggle('active', roundNum === 1);

      document.getElementById('quizSectionTitle').innerHTML = (roundNum === 2)
        ? '<i class="fas fa-crosshairs"></i> SIMULADO RODADA 2 — 40 NOVAS QUESTÕES INÉDITAS'
        : '<i class="fas fa-crosshairs"></i> SIMULADO RODADA 1 — 40 QUESTÕES BASE';

      updateLiveScore();
      renderQuestions();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function renderQuestions() {
      const container = document.getElementById('questionsContainer');
      container.innerHTML = '';
      const letters = ['A', 'B', 'C', 'D'];
      const list = getActiveList();
      const userChoices = getActiveChoices();

      const filtered = list.filter(item => {
        if (currentFilterCat === 'all') return true;
        if (currentFilterCat === 'wrong') {
          return userChoices[item.num] !== undefined && userChoices[item.num] !== item.ans;
        }
        return item.cat === currentFilterCat;
      });

      if (filtered.length === 0) {
        container.innerHTML = `<div style="background:white; padding:24px; border-radius:12px; text-align:center; font-weight:700; color:#166534;">🎉 Nenhuma questão pendente neste filtro!</div>`;
        return;
      }

      filtered.forEach(item => {
        const chosen = userChoices[item.num];
        const isAnswered = chosen !== undefined;
        const isCorrect = isAnswered && chosen === item.ans;

        const card = document.createElement('div');
        card.className = 'q-card' + (isAnswered ? (isCorrect ? ' correct-card' : ' wrong-card') : '');

        let optsHtml = '';
        item.opts.forEach((optTxt, idx) => {
          let cls = 'opt-btn';
          if (isAnswered) {
            if (idx === item.ans) cls += ' is-correct';
            else if (idx === chosen && chosen !== item.ans) cls += ' is-wrong';
          }
          optsHtml += `
            <button type="button" class="${cls}" onclick="chooseAnswer(${item.num}, ${idx})">
              <span class="opt-let">${letters[idx]}</span>
              <span>${optTxt}</span>
            </button>
          `;
        });

        card.innerHTML = `
          <div class="q-top">
            <span class="q-badge">RODADA ${currentRound} • QUESTÃO ${String(item.num).padStart(2, '0')} / 40</span>
            <span class="q-mat">${item.mat}</span>
          </div>
          <div class="q-enun">${item.q}</div>
          <div class="q-opts">${optsHtml}</div>
          <div class="q-exp ${isAnswered ? 'visible' : ''}">
            <strong><i class="fas fa-check-circle" style="color:#16a34a;"></i> Fundamentação Direta:</strong> ${item.exp}
          </div>
        `;
        container.appendChild(card);
      });
    }

    function chooseAnswer(qNum, optIdx) {
      const userChoices = getActiveChoices();
      userChoices[qNum] = optIdx;
      updateLiveScore();
      renderQuestions();
    }

    function revealAllCurrentRound() {
      const list = getActiveList();
      const userChoices = getActiveChoices();
      list.forEach(item => {
        if (userChoices[item.num] === undefined) {
          userChoices[item.num] = item.ans;
        }
      });
      updateLiveScore();
      renderQuestions();
      scrollToSection('sec-questoes');
    }

    function resetCurrentRoundQuiz() {
      if (currentRound === 2) choicesR2 = {};
      else choicesR1 = {};
      updateLiveScore();
      renderQuestions();
    }

    function filterQuestions(cat, btn) {
      currentFilterCat = cat;
      document.querySelectorAll('.f-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderQuestions();
    }

    function updateLiveScore() {
      const list = getActiveList();
      const userChoices = getActiveChoices();
      const answeredNums = Object.keys(userChoices);
      let hits = 0;
      answeredNums.forEach(numStr => {
        const q = list.find(i => i.num === Number(numStr));
        if (q && userChoices[q.num] === q.ans) hits++;
      });
      const totalAns = answeredNums.length;
      const pct = totalAns > 0 ? Math.round((hits / totalAns) * 100) : 0;
      document.getElementById('hitsCount').innerText = hits;
      document.getElementById('ansCount').innerText = totalAns;
      document.getElementById('pctCount').innerText = `${pct}%`;
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderQuestions();
    });
  </script>
</body>
</html>
"""

with open("TUDO_OU_NADA_1HORA.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

with open(os.path.join("provas", "TUDO_OU_NADA_1HORA.html"), "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("[OK] TUDO_OU_NADA_1HORA.html atualizado com Rodada 2 Inedita e zero codigos LaTeX!")

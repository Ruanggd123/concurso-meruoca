import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

# Carregar questoes extraidas
with open('provas/questoes_especificas.json', 'r', encoding='utf-8') as f:
    questoes = json.load(f)

print(f"Total de questoes carregadas para o Provão Mobile: {len(questoes)}")

# Preparar o HTML interativo mobile
html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>PROVÃO MOBILE — ESPECÍFICAS MERUOCA 2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --primary: #1e3a8a;
      --primary-dark: #0f172a;
      --primary-light: #3b82f6;
      --accent: #dc2626;
      --success: #16a34a;
      --success-light: #dcfce7;
      --danger: #dc2626;
      --danger-light: #fee2e2;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow: 0 3px 12px rgba(0,0,0,0.06);
    }

    * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
    
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      margin: 0;
      padding: 0;
      line-height: 1.5;
      font-size: 15px;
    }

    /* Top Sticky Header */
    .sticky-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      box-shadow: 0 2px 10px rgba(0,0,0,0.04);
      padding: 10px 14px;
    }

    .header-top-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
    }

    .brand-title {
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 6px;
      margin: 0;
    }

    .brand-title i { color: var(--accent); }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .timer-badge {
      background: #f1f5f9;
      color: #334155;
      padding: 4px 8px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.8rem;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .btn-finish-quick {
      background: var(--accent);
      color: white;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.8rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .progress-info-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-top: 8px;
    }

    .progress-bar-track {
      width: 100%;
      height: 6px;
      background: #e2e8f0;
      border-radius: 999px;
      overflow: hidden;
      margin-top: 4px;
    }

    .progress-bar-fill {
      width: 0%;
      height: 100%;
      background: linear-gradient(90deg, #2563eb, #16a34a);
      transition: width 0.3s ease;
    }

    /* Container Principal */
    .main-container {
      max-width: 760px;
      margin: 0 auto;
      padding: 14px 14px 80px 14px;
    }

    /* Seletor de Modo de Estudo */
    .mode-selector-box {
      background: white;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 14px;
      margin-bottom: 14px;
      box-shadow: var(--shadow);
    }

    .mode-label {
      font-size: 0.8rem;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .pills-scroll {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 6px;
      scrollbar-width: none;
    }
    .pills-scroll::-webkit-scrollbar { display: none; }

    .pill-btn {
      white-space: nowrap;
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .pill-btn.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
      box-shadow: 0 2px 8px rgba(30, 58, 138, 0.25);
    }

    /* Opcoes extras de Marcacao da Opcao Certa */
    .options-toolbar {
      margin-top: 10px;
      padding-top: 10px;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .study-mode-toggle {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #f0fdf4;
      border: 1.5px solid #86efac;
      border-radius: 8px;
      padding: 6px 12px;
      font-size: 0.82rem;
      font-weight: 700;
      color: #166534;
      cursor: pointer;
      user-select: none;
      transition: background 0.2s;
    }
    .study-mode-toggle:hover { background: #dcfce7; }
    .study-mode-toggle input {
      cursor: pointer;
      width: 17px;
      height: 17px;
      accent-color: #16a34a;
    }

    .btn-reveal-all {
      background: #f8fafc;
      color: #1e3a8a;
      border: 1px solid #cbd5e1;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .btn-reveal-all:hover {
      background: #e2e8f0;
    }

    /* Placar de Resultado (Exibido após finalizar) */
    .result-card {
      display: none;
      background: white;
      border: 2px solid #22c55e;
      border-radius: var(--radius);
      padding: 20px;
      margin-bottom: 20px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
      text-align: center;
      animation: fadeIn 0.4s ease;
    }

    .score-circle {
      width: 90px;
      height: 90px;
      border-radius: 50%;
      background: #f0fdf4;
      border: 4px solid var(--success);
      margin: 0 auto 12px auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      color: #15803d;
      font-size: 1.4rem;
    }

    .score-circle span { font-size: 0.72rem; font-weight: 700; color: #4b5563; }

    .result-title {
      font-size: 1.25rem;
      font-weight: 800;
      margin: 0 0 6px 0;
    }

    .result-stats-row {
      display: flex;
      justify-content: center;
      gap: 16px;
      margin: 14px 0;
      font-size: 0.88rem;
    }

    .stat-badge {
      padding: 6px 12px;
      border-radius: 6px;
      font-weight: 800;
    }
    .stat-badge.correct { background: #dcfce7; color: #166534; }
    .stat-badge.wrong { background: #fee2e2; color: #991b1b; }
    .stat-badge.skipped { background: #f1f5f9; color: #475569; }

    .result-actions {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 14px;
    }

    .btn-action {
      padding: 10px 18px;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.85rem;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .btn-action.retry-wrong { background: #eab308; color: #713f12; }
    .btn-action.reset { background: #e2e8f0; color: #1e293b; }

    /* Cards de Questões */
    .question-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 18px 16px;
      margin-bottom: 16px;
      box-shadow: var(--shadow);
      transition: border-color 0.2s, box-shadow 0.2s;
    }

    .question-card.answered {
      border-color: #93c5fd;
    }

    .question-card.status-correct {
      border: 2px solid var(--success) !important;
      background: #f0fdf4 !important;
    }

    .question-card.status-wrong {
      border: 2px solid var(--danger) !important;
      background: #fff1f2 !important;
    }

    .card-meta-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
      flex-wrap: wrap;
    }

    .q-number-badge {
      background: var(--primary);
      color: white;
      font-weight: 800;
      font-size: 0.76rem;
      padding: 3px 8px;
      border-radius: 6px;
    }

    .q-discipline-badge {
      background: #e0e7ff;
      color: #3730a3;
      font-weight: 700;
      font-size: 0.74rem;
      padding: 3px 8px;
      border-radius: 6px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 250px;
    }

    .q-result-badge {
      display: none;
      font-weight: 800;
      font-size: 0.76rem;
      padding: 3px 8px;
      border-radius: 6px;
    }
    .status-correct .q-result-badge.badge-correct { display: inline-block; background: #22c55e; color: white; }
    .status-wrong .q-result-badge.badge-wrong { display: inline-block; background: #ef4444; color: white; }

    .question-text {
      font-size: 1rem;
      font-weight: 600;
      color: #0f172a;
      line-height: 1.48;
      margin: 0 0 14px 0;
    }

    /* Alternativas de Toque (Grandes e Fáceis de Clicar) */
    .options-group {
      display: flex;
      flex-direction: column;
      gap: 9px;
    }

    .option-btn {
      width: 100%;
      text-align: left;
      background: #f8fafc;
      border: 1.5px solid #e2e8f0;
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 0.94rem;
      color: #1e293b;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      transition: all 0.18s ease;
      position: relative;
    }

    .option-btn:hover {
      background: #f1f5f9;
      border-color: #cbd5e1;
    }

    .option-letter {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #e2e8f0;
      color: #475569;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.8rem;
      flex-shrink: 0;
      margin-top: 1px;
      transition: all 0.18s;
    }

    .option-text {
      flex: 1;
      line-height: 1.4;
      font-weight: 500;
    }

    /* Estado Marcado */
    .option-btn.selected {
      background: #eff6ff;
      border-color: #2563eb;
      box-shadow: 0 0 0 1px #2563eb;
    }

    .option-btn.selected .option-letter {
      background: #2563eb;
      color: white;
    }

    /* Destaque da Opcao Certa e Errada (Funciona individualmente ou ao finalizar) */
    .finished .option-btn { cursor: default; }

    .option-btn.correct-answer {
      background: #dcfce7 !important;
      border-color: #16a34a !important;
      box-shadow: 0 0 0 1.5px #16a34a !important;
      color: #14532d !important;
    }
    .option-btn.correct-answer .option-letter {
      background: #16a34a !important;
      color: white !important;
    }

    .option-btn.selected.wrong-answer {
      background: #fee2e2 !important;
      border-color: #dc2626 !important;
      box-shadow: 0 0 0 1.5px #dc2626 !important;
      color: #7f1d1d !important;
    }
    .option-btn.selected.wrong-answer .option-letter {
      background: #dc2626 !important;
      color: white !important;
    }

    /* Barra de Ação Individual da Questão */
    .q-action-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px dashed var(--border);
      flex-wrap: wrap;
      gap: 8px;
    }

    .btn-reveal-one {
      background: #f1f5f9;
      color: #1e3a8a;
      border: 1px solid #cbd5e1;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.18s;
    }
    .btn-reveal-one:hover {
      background: #e2e8f0;
      border-color: #94a3b8;
    }
    .btn-reveal-one.revealed {
      background: #dcfce7;
      color: #166534;
      border-color: #86efac;
    }

    /* Box de Comentário e Gabarito */
    .commentary-box {
      display: none;
      margin-top: 12px;
      padding: 12px 14px;
      border-radius: 8px;
      background: #f8fafc;
      border-left: 4px solid var(--primary);
      font-size: 0.86rem;
      color: #334155;
      animation: fadeIn 0.3s ease;
    }

    .commentary-box strong { color: var(--primary); }

    .finished .commentary-box {
      display: block;
    }

    /* Botão Flutuante de Concluir no Rodapé */
    .footer-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(10px);
      border-top: 1px solid var(--border);
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 999;
      box-shadow: 0 -3px 12px rgba(0,0,0,0.06);
    }

    .btn-finish-big {
      width: 100%;
      background: #16a34a;
      color: white;
      border: none;
      padding: 14px 20px;
      border-radius: 10px;
      font-size: 1rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 4px 15px rgba(22, 163, 74, 0.3);
      transition: transform 0.15s, background 0.15s;
    }

    .btn-finish-big:hover {
      background: #15803d;
      transform: translateY(-1px);
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>

  <!-- Sticky Header -->
  <header class="sticky-header">
    <div class="header-top-row">
      <h1 class="brand-title">
        <i class="fas fa-landmark"></i> PROVÃO ESPECÍFICAS
      </h1>
      <div class="header-actions">
        <div class="timer-badge" id="timerBadge">
          <i class="fas fa-clock"></i> <span id="timerText">00:00</span>
        </div>
        <button class="btn-finish-quick" onclick="handleFinishClick()">
          <i class="fas fa-check-circle"></i> Finalizar
        </button>
      </div>
    </div>

    <div class="progress-info-row">
      <span>Respondidas: <strong id="answeredCount" style="color: var(--primary);">0</strong> de <span id="totalCount">0</span></span>
      <span id="percentCount">0%</span>
    </div>
    <div class="progress-bar-track">
      <div class="progress-bar-fill" id="progressBarFill"></div>
    </div>
  </header>

  <main class="main-container">

    <!-- Seletor de Modo / Bloco -->
    <div class="mode-selector-box" id="modeSelectorBox">
      <div class="mode-label">
        <i class="fas fa-sliders-h"></i> Escolha o Bloco para Responder:
      </div>
      <div class="pills-scroll">
        <button class="pill-btn active" onclick="switchFilter('foco50', this)">
          ⭐ Provão Ouro (50Q Foco Máximo)
        </button>
        <button class="pill-btn" onclick="switchFilter('meruoca', this)">
          🏛️ Lei Orgânica & Regimento (52Q)
        </button>
        <button class="pill-btn" onclick="switchFilter('licitacao', this)">
          📜 Licitações 14.133 (40Q)
        </button>
        <button class="pill-btn" onclick="switchFilter('administrativo', this)">
          ⚖️ D. Administrativo & Atos (70Q)
        </button>
        <button class="pill-btn" onclick="switchFilter('constitucional', this)">
          🏛️ D. Constitucional & TCE (60Q)
        </button>
        <button class="pill-btn" onclick="switchFilter('todas', this)">
          🚀 Mega Provão (Todas 339Q)
        </button>
      </div>

      <!-- Barra de Opcoes de Marcacao e Estudo -->
      <div class="options-toolbar">
        <label class="study-mode-toggle" title="Ao ativar, tocar em qualquer opção já marca e destaca a resposta certa imediatamente!">
          <input type="checkbox" id="chkInstantMode" onchange="toggleInstantMode(this.checked)">
          <span><i class="fas fa-bolt" style="color: #16a34a;"></i> Modo Estudo: Marcar Certa ao Tocar</span>
        </label>
        
        <button type="button" class="btn-reveal-all" onclick="revealAllQuestionsInBlock()">
          <i class="fas fa-check-double" style="color: #16a34a;"></i> Marcar Todas as Certas (Apostila)
        </button>
      </div>
    </div>

    <!-- Card de Resultado Final (Aparece após confirmar) -->
    <div class="result-card" id="resultCard">
      <div class="score-circle">
        <div id="scorePercent">0%</div>
        <span>APROVEITAMENTO</span>
      </div>
      <h2 class="result-title" id="resultHeading">Resultado do Provão</h2>
      <p style="font-size: 0.92rem; color: #4b5563; margin: 0 0 10px 0;" id="resultSubtitle">
        Confira abaixo o seu gabarito comentado questão por questão.
      </p>

      <div class="result-stats-row">
        <div class="stat-badge correct"><i class="fas fa-check"></i> <span id="statCorrect">0</span> Acertos</div>
        <div class="stat-badge wrong"><i class="fas fa-times"></i> <span id="statWrong">0</span> Erros</div>
        <div class="stat-badge skipped"><i class="fas fa-minus"></i> <span id="statSkipped">0</span> Em branco</div>
      </div>

      <div class="result-actions">
        <button class="btn-action retry-wrong" onclick="retryWrongQuestions()">
          <i class="fas fa-redo-alt"></i> Refazer Apenas as Erradas
        </button>
        <button class="btn-action reset" onclick="resetCurrentQuiz()">
          <i class="fas fa-sync-alt"></i> Reiniciar Este Bloco
        </button>
      </div>
    </div>

    <!-- Lista de Questões Injetada Dinamicamente -->
    <div id="questionsList"></div>

  </main>

  <!-- Barra Fixa do Rodapé -->
  <div class="footer-bar" id="footerBar">
    <button class="btn-finish-big" onclick="handleFinishClick()">
      <i class="fas fa-check-double"></i> CONFIRMAR TODAS AS RESPOSTAS
    </button>
  </div>

  <script>
    // BANCO COMPLETO DE QUESTÕES ESPECÍFICAS
    const ALL_ESPECIFICAS = """ + json.dumps(questoes, ensure_ascii=False) + """;

    // Estado da Aplicação
    let currentFilter = 'foco50';
    let activeQuestions = [];
    let userAnswers = {}; // { qId: selectedOptionIndex }
    let revealedQuestions = {}; // { qId: true }
    let isFinished = false;
    let instantMode = false;
    let timerSeconds = 0;
    let timerInterval = null;

    // Inicialização
    document.addEventListener('DOMContentLoaded', () => {
      startTimer();
      loadFilter('foco50');
    });

    function startTimer() {
      if (timerInterval) clearInterval(timerInterval);
      timerSeconds = 0;
      timerInterval = setInterval(() => {
        timerSeconds++;
        const mins = String(Math.floor(timerSeconds / 60)).padStart(2, '0');
        const secs = String(timerSeconds % 60).padStart(2, '0');
        document.getElementById('timerText').innerText = `${mins}:${secs}`;
      }, 1000);
    }

    function toggleInstantMode(enabled) {
      instantMode = enabled;
    }

    function switchFilter(filterKey, btnElement) {
      document.querySelectorAll('.pill-btn').forEach(btn => btn.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');
      loadFilter(filterKey);
    }

    function loadFilter(filterKey) {
      currentFilter = filterKey;
      userAnswers = {};
      revealedQuestions = {};
      isFinished = false;
      document.body.classList.remove('finished');
      document.getElementById('resultCard').style.display = 'none';
      document.getElementById('footerBar').style.display = 'flex';

      if (filterKey === 'foco50') {
        // 50 questões mais representativas e balanceadas de cada disciplina
        const mer = ALL_ESPECIFICAS.filter(q => q.discipline && q.discipline.includes('Meruoca')).slice(0, 15);
        const lic = ALL_ESPECIFICAS.filter(q => q.discipline && q.discipline.includes('14.133')).slice(0, 15);
        const adm = ALL_ESPECIFICAS.filter(q => q.category === 'administrativo').slice(0, 10);
        const con = ALL_ESPECIFICAS.filter(q => q.category === 'constitucional').slice(0, 10);
        activeQuestions = [...mer, ...lic, ...adm, ...con];
      } else if (filterKey === 'meruoca') {
        activeQuestions = ALL_ESPECIFICAS.filter(q => 
          (q.discipline && (q.discipline.includes('Meruoca') || q.discipline.includes('Regimento') || q.discipline.includes('Legislativo')))
        );
      } else if (filterKey === 'licitacao') {
        activeQuestions = ALL_ESPECIFICAS.filter(q => q.discipline && q.discipline.includes('14.133'));
      } else if (filterKey === 'administrativo') {
        activeQuestions = ALL_ESPECIFICAS.filter(q => q.category === 'administrativo');
      } else if (filterKey === 'constitucional') {
        activeQuestions = ALL_ESPECIFICAS.filter(q => q.category === 'constitucional');
      } else {
        // Todas
        activeQuestions = ALL_ESPECIFICAS;
      }

      renderQuestions();
      updateProgress();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function renderQuestions() {
      const container = document.getElementById('questionsList');
      container.innerHTML = '';
      document.getElementById('totalCount').innerText = activeQuestions.length;

      const letters = ['A', 'B', 'C', 'D'];

      activeQuestions.forEach((q, idx) => {
        const card = document.createElement('div');
        card.className = 'question-card';
        card.id = `qCard_${q.id}`;

        const discName = q.discipline || (q.category ? q.category.toUpperCase() : 'Específica');
        const topicName = q.topic ? ` • ${q.topic}` : '';

        let optionsHtml = '';
        q.options.forEach((optText, optIdx) => {
          optionsHtml += `
            <button type="button" class="option-btn" id="optBtn_${q.id}_${optIdx}" onclick="selectOption(${q.id}, ${optIdx})">
              <span class="option-letter">${letters[optIdx]}</span>
              <span class="option-text">${optText}</span>
            </button>
          `;
        });

        card.innerHTML = `
          <div class="card-meta-row">
            <span class="q-number-badge">Questão ${idx + 1} de ${activeQuestions.length}</span>
            <span class="q-discipline-badge">${discName}${topicName}</span>
            <span class="q-result-badge badge-correct"><i class="fas fa-check"></i> Correto</span>
            <span class="q-result-badge badge-wrong"><i class="fas fa-times"></i> Errou</span>
          </div>

          <div class="question-text">${q.question}</div>

          <div class="options-group">
            ${optionsHtml}
          </div>

          <div class="q-action-bar">
            <button type="button" class="btn-reveal-one" id="btnRev_${q.id}" onclick="revealSingleQuestion(${q.id})">
              <i class="fas fa-lightbulb" style="color: #eab308;"></i> Ver / Marcar Opção Certa
            </button>
            <span class="q-status-hint" id="hint_${q.id}" style="font-size: 0.78rem; font-weight: 700;"></span>
          </div>

          <div class="commentary-box" id="comBox_${q.id}">
            <strong>Gabarito Oficial & Justificativa:</strong><br>
            ${q.commentary || 'Comentário fundamentado da banca.'}
          </div>
        `;

        container.appendChild(card);
      });
    }

    function selectOption(qId, optIdx) {
      if (isFinished) return; // travado apos finalizar

      userAnswers[qId] = optIdx;

      // Atualizar estilo visual dos botões desta questão
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById(`optBtn_${qId}_${i}`);
        if (btn) {
          if (i === optIdx) {
            btn.classList.add('selected');
          } else {
            btn.classList.remove('selected');
          }
        }
      }

      const card = document.getElementById(`qCard_${qId}`);
      if (card) card.classList.add('answered');

      updateProgress();

      // Se o Modo Estudo Instantâneo estiver ativo, marca e revela a certa imediatamente!
      if (instantMode) {
        revealSingleQuestion(qId);
      }
    }

    function revealSingleQuestion(qId) {
      const q = activeQuestions.find(item => item.id === qId);
      if (!q) return;

      revealedQuestions[qId] = true;
      const card = document.getElementById(`qCard_${qId}`);
      const correctChoice = q.correctAnswer;
      const userChoice = userAnswers[qId];
      const letters = ['A', 'B', 'C', 'D'];

      // Destacar a opção correta em verde
      const correctBtn = document.getElementById(`optBtn_${qId}_${correctChoice}`);
      if (correctBtn) correctBtn.classList.add('correct-answer');

      const hintSpan = document.getElementById(`hint_${qId}`);

      if (userChoice !== undefined) {
        if (userChoice === correctChoice) {
          if (card) {
            card.classList.add('status-correct');
            card.classList.remove('status-wrong');
          }
          if (hintSpan) {
            hintSpan.innerHTML = '<span style="color: #16a34a;"><i class="fas fa-check-circle"></i> Você acertou! (' + letters[correctChoice] + ')</span>';
          }
        } else {
          if (card) {
            card.classList.add('status-wrong');
            card.classList.remove('status-correct');
          }
          const wrongBtn = document.getElementById(`optBtn_${qId}_${userChoice}`);
          if (wrongBtn) wrongBtn.classList.add('wrong-answer');
          if (hintSpan) {
            hintSpan.innerHTML = '<span style="color: #dc2626;"><i class="fas fa-times-circle"></i> Certa: Letra ' + letters[correctChoice] + '</span>';
          }
        }
      } else {
        if (hintSpan) {
          hintSpan.innerHTML = '<span style="color: #16a34a;"><i class="fas fa-info-circle"></i> Gabarito: Letra ' + letters[correctChoice] + '</span>';
        }
      }

      // Exibir o comentário da questão
      const comBox = document.getElementById(`comBox_${qId}`);
      if (comBox) comBox.style.display = 'block';

      // Atualizar o botão
      const btnRev = document.getElementById(`btnRev_${qId}`);
      if (btnRev) {
        btnRev.classList.add('revealed');
        btnRev.innerHTML = '<i class="fas fa-check-double" style="color: #16a34a;"></i> Certa: ' + letters[correctChoice];
      }
    }

    function revealAllQuestionsInBlock() {
      activeQuestions.forEach(q => {
        revealSingleQuestion(q.id);
      });
    }

    function updateProgress() {
      const answered = Object.keys(userAnswers).length;
      const total = activeQuestions.length;
      const pct = total > 0 ? Math.round((answered / total) * 100) : 0;

      document.getElementById('answeredCount').innerText = answered;
      document.getElementById('percentCount').innerText = `${pct}%`;
      document.getElementById('progressBarFill').style.width = `${pct}%`;
    }

    function handleFinishClick() {
      if (isFinished) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }

      const answered = Object.keys(userAnswers).length;
      const total = activeQuestions.length;

      if (answered < total) {
        const pendentes = total - answered;
        const confirmMsg = `Você respondeu ${answered} de ${total} questões (${pendentes} em branco).\\n\\nDeseja finalizar agora e conferir o gabarito?`;
        if (!confirm(confirmMsg)) {
          return;
        }
      }

      finishQuiz();
    }

    function finishQuiz() {
      isFinished = true;
      document.body.classList.add('finished');
      document.getElementById('footerBar').style.display = 'none';

      let correct = 0;
      let wrong = 0;
      let skipped = 0;

      activeQuestions.forEach(q => {
        const card = document.getElementById(`qCard_${q.id}`);
        const userChoice = userAnswers[q.id];
        const correctChoice = q.correctAnswer;

        // Revelar resposta correta
        const correctBtn = document.getElementById(`optBtn_${q.id}_${correctChoice}`);
        if (correctBtn) correctBtn.classList.add('correct-answer');

        if (userChoice === undefined) {
          skipped++;
        } else if (userChoice === correctChoice) {
          correct++;
          if (card) card.classList.add('status-correct');
        } else {
          wrong++;
          if (card) card.classList.add('status-wrong');
          const wrongBtn = document.getElementById(`optBtn_${q.id}_${userChoice}`);
          if (wrongBtn) wrongBtn.classList.add('wrong-answer');
        }

        // Abrir comentarios
        const comBox = document.getElementById(`comBox_${q.id}`);
        if (comBox) comBox.style.display = 'block';

        const btnRev = document.getElementById(`btnRev_${q.id}`);
        if (btnRev) {
          btnRev.classList.add('revealed');
          btnRev.innerHTML = '<i class="fas fa-check-double" style="color: #16a34a;"></i> Certa: ' + ['A','B','C','D'][correctChoice];
        }
      });

      const total = activeQuestions.length;
      const pct = total > 0 ? Math.round((correct / total) * 100) : 0;

      document.getElementById('scorePercent').innerText = `${pct}%`;
      document.getElementById('statCorrect').innerText = correct;
      document.getElementById('statWrong').innerText = wrong;
      document.getElementById('statSkipped').innerText = skipped;

      const heading = document.getElementById('resultHeading');
      if (pct >= 80) {
        heading.innerText = `🎉 Excelente! ${correct} de ${total} Acertos`;
        heading.style.color = '#15803d';
      } else if (pct >= 60) {
        heading.innerText = `👍 Bom Desempenho! ${correct} de ${total} Acertos`;
        heading.style.color = '#1e3a8a';
      } else {
        heading.innerText = `⚠️ Atenção! ${correct} de ${total} Acertos`;
        heading.style.color = '#dc2626';
      }

      const resultCard = document.getElementById('resultCard');
      resultCard.style.display = 'block';

      // Rolar suavemente para o card de resultado
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    function resetCurrentQuiz() {
      loadFilter(currentFilter);
    }

    function retryWrongQuestions() {
      const wrongList = activeQuestions.filter(q => userAnswers[q.id] !== q.correctAnswer);
      if (wrongList.length === 0) {
        alert('Parabéns! Você não errou nenhuma questão neste bloco!');
        return;
      }

      activeQuestions = wrongList;
      userAnswers = {};
      revealedQuestions = {};
      isFinished = false;
      document.body.classList.remove('finished');
      document.getElementById('resultCard').style.display = 'none';
      document.getElementById('footerBar').style.display = 'flex';

      renderQuestions();
      updateProgress();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  </script>
</body>
</html>
"""

# Salvar na raiz e em provas
with open('PROVAO_MOBILE_ESPECIFICAS.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Salvo: PROVAO_MOBILE_ESPECIFICAS.html na raiz!")

with open('provas/PROVAO_MOBILE_ESPECIFICAS.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Salvo: provas/PROVAO_MOBILE_ESPECIFICAS.html!")

import os, re, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

PROVAS_DIR = r"C:\Users\Ruan Gomes\Downloads\Meruoca\provas"

INTERACTIVE_CSS = """
    /* === ESTILOS INTERATIVOS DE MARCAÇÃO E GABARITO === */
    @media print {
      .no-print, .interactive-header, .btn-action-quiz, .inline-feedback { display: none !important; }
      body { padding: 0 !important; }
    }

    body {
      padding-top: 10px !important;
    }

    /* Barra Fixa Superior com Progresso e Placar */
    .interactive-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 10px;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.08);
      padding: 10px 14px;
      margin: 0 0 20px 0;
    }

    .header-top-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 8px;
    }

    .btn-back-nav {
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 700;
      color: #1e3a8a;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      padding: 5px 10px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: background 0.18s;
    }
    .btn-back-nav:hover { background: #dbeafe; }

    .score-stats {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.82rem;
      font-weight: 800;
    }

    .stat-pill {
      padding: 3px 8px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .stat-pill.total { background: #f1f5f9; color: #334155; }
    .stat-pill.correct { background: #dcfce7; color: #15803d; }
    .stat-pill.wrong { background: #fee2e2; color: #b91c1c; }
    .stat-pill.percent { background: #1e3a8a; color: #ffffff; }

    .progress-track {
      width: 100%;
      height: 6px;
      background: #e2e8f0;
      border-radius: 9999px;
      overflow: hidden;
    }
    .progress-bar-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #2563eb, #16a34a);
      transition: width 0.3s ease;
    }

    .header-controls {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 8px;
      padding-top: 8px;
      border-top: 1px dashed #e2e8f0;
    }

    .mode-toggle-label {
      font-size: 0.82rem;
      font-weight: 700;
      color: #166534;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      user-select: none;
      background: #f0fdf4;
      padding: 5px 10px;
      border-radius: 6px;
      border: 1px solid #bbf7d0;
    }
    .mode-toggle-label input { cursor: pointer; accent-color: #16a34a; }

    .btn-action-quiz {
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.18s;
    }
    .btn-action-quiz.retry {
      background: #f8fafc;
      color: #334155;
      border: 1px solid #cbd5e1;
    }
    .btn-action-quiz.retry:hover { background: #e2e8f0; }
    .btn-action-quiz.primary {
      background: #2563eb;
      color: white;
    }
    .btn-action-quiz.primary:hover { background: #1d4ed8; }

    /* Alternativas Estilizadas e Clicáveis */
    .options-list {
      list-style: none !important;
      padding-left: 0 !important;
      margin: 10px 0 !important;
      display: flex !important;
      flex-direction: column !important;
      gap: 8px !important;
    }

    .option-item {
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 0.94rem;
      color: #1e293b;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      transition: all 0.18s ease;
      user-select: none;
      position: relative;
    }
    .option-item:hover {
      background: #f1f5f9;
      border-color: #94a3b8;
    }

    .option-bubble {
      width: 25px;
      height: 25px;
      border-radius: 50%;
      background: #e2e8f0;
      color: #334155;
      font-weight: 800;
      font-size: 0.82rem;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
      transition: all 0.18s;
    }

    .option-text {
      flex: 1;
      line-height: 1.42;
      font-weight: 500;
    }

    /* Estado Marcado */
    .option-item.selected {
      background: #eff6ff;
      border-color: #2563eb;
      box-shadow: 0 0 0 1px #2563eb;
    }
    .option-item.selected .option-bubble {
      background: #2563eb;
      color: white;
    }

    /* Estado Correto (Verde) */
    .option-item.is-correct {
      background: #dcfce7 !important;
      border-color: #16a34a !important;
      box-shadow: 0 0 0 1.5px #16a34a !important;
      color: #14532d !important;
      font-weight: 600;
    }
    .option-item.is-correct .option-bubble {
      background: #16a34a !important;
      color: white !important;
    }

    /* Estado Errado (Vermelho) */
    .option-item.is-wrong {
      background: #fee2e2 !important;
      border-color: #dc2626 !important;
      box-shadow: 0 0 0 1.5px #dc2626 !important;
      color: #7f1d1d !important;
    }
    .option-item.is-wrong .option-bubble {
      background: #dc2626 !important;
      color: white !important;
    }

    /* Feedback Inline Imediato */
    .inline-feedback {
      display: none;
      margin-top: 10px;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 0.88rem;
      animation: feedbackIn 0.25s ease;
    }
    .inline-feedback.correct {
      display: block;
      background: #f0fdf4;
      border-left: 4px solid #16a34a;
      color: #14532d;
    }
    .inline-feedback.wrong {
      display: block;
      background: #fef2f2;
      border-left: 4px solid #dc2626;
      color: #991b1b;
    }
    .inline-feedback strong { font-weight: 800; }

    .inline-comentario {
      display: none;
      margin-top: 8px;
      padding: 10px 14px;
      border-radius: 8px;
      background: #f8fafc;
      border-left: 4px solid #2563eb;
      font-size: 0.86rem;
      color: #334155;
      line-height: 1.45;
      animation: feedbackIn 0.25s ease;
    }
    .inline-comentario strong { color: #1e3a8a; }

    @keyframes feedbackIn {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }
"""

INTERACTIVE_JS = """
  <script>
    // ESTADO DO SIMULADO INTERATIVO
    let userAnswers = {}; // { qNum: letter }
    let instantMode = true;
    let totalQuestions = 0;

    document.addEventListener('DOMContentLoaded', () => {
      totalQuestions = document.querySelectorAll('.question-box[data-q]').length;
      updateStats();
    });

    function toggleInstantMode(enabled) {
      instantMode = enabled;
      const btnFinish = document.getElementById('btnFinish');
      if (btnFinish) {
        btnFinish.style.display = enabled ? 'none' : 'inline-flex';
      }
    }

    function handleOptionClick(btn, qNum, selectedOpt, correctOpt) {
      const qBox = document.querySelector(`.question-box[data-q="${qNum}"]`);
      if (!qBox) return;

      // Se já respondeu no modo instantâneo, permite trocar se quiser
      userAnswers[qNum] = selectedOpt;

      // Limpar estados anteriores nas opções desta questão
      qBox.querySelectorAll('.option-item').forEach(opt => {
        opt.classList.remove('selected', 'is-correct', 'is-wrong');
      });

      btn.classList.add('selected');

      if (instantMode) {
        evaluateQuestion(qNum, selectedOpt, correctOpt);
      }
      updateStats();
    }

    function evaluateQuestion(qNum, selectedOpt, correctOpt) {
      const qBox = document.querySelector(`.question-box[data-q="${qNum}"]`);
      if (!qBox) return;

      const fb = document.getElementById(`feedback_${qNum}`);
      const com = document.getElementById(`comentario_${qNum}`);
      const isCorrect = (selectedOpt.toUpperCase() === correctOpt.toUpperCase());

      qBox.querySelectorAll('.option-item').forEach(opt => {
        const optLetter = opt.getAttribute('data-opt');
        if (optLetter === correctOpt) {
          opt.classList.add('is-correct');
        } else if (optLetter === selectedOpt && !isCorrect) {
          opt.classList.add('is-wrong');
        }
      });

      if (fb) {
        if (isCorrect) {
          fb.className = 'inline-feedback correct';
          fb.innerHTML = '<i class="fas fa-check-circle"></i> <strong>Parabéns, você acertou!</strong> Alternativa correta: <strong>(' + correctOpt + ')</strong>';
        } else {
          fb.className = 'inline-feedback wrong';
          fb.innerHTML = '<i class="fas fa-times-circle"></i> <strong>Você errou.</strong> Sua resposta foi <strong>(' + selectedOpt + ')</strong>, mas o gabarito oficial é <strong>(' + correctOpt + ')</strong>.';
        }
      }

      if (com) {
        com.style.display = 'block';
      }
    }

    function finishExam() {
      document.querySelectorAll('.question-box[data-q]').forEach(qBox => {
        const qNum = qBox.getAttribute('data-q');
        const correctOpt = qBox.getAttribute('data-gab');
        const selectedOpt = userAnswers[qNum];
        if (selectedOpt) {
          evaluateQuestion(qNum, selectedOpt, correctOpt);
        } else {
          // Revelar gabarito de não respondidas
          const fb = document.getElementById(`feedback_${qNum}`);
          const com = document.getElementById(`comentario_${qNum}`);
          qBox.querySelectorAll('.option-item').forEach(opt => {
            if (opt.getAttribute('data-opt') === correctOpt) {
              opt.classList.add('is-correct');
            }
          });
          if (fb) {
            fb.className = 'inline-feedback wrong';
            fb.innerHTML = '<i class="fas fa-minus-circle"></i> <strong>Não respondida.</strong> Gabarito oficial: <strong>(' + correctOpt + ')</strong>';
          }
          if (com) com.style.display = 'block';
        }
      });
      updateStats();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function updateStats() {
      let correct = 0;
      let wrong = 0;
      const qBoxes = document.querySelectorAll('.question-box[data-q]');
      const total = qBoxes.length || totalQuestions;

      qBoxes.forEach(qBox => {
        const qNum = qBox.getAttribute('data-q');
        const correctOpt = qBox.getAttribute('data-gab');
        const sel = userAnswers[qNum];
        if (sel) {
          if (sel.toUpperCase() === correctOpt.toUpperCase()) correct++;
          else wrong++;
        }
      });

      const answered = Object.keys(userAnswers).length;
      const percent = answered > 0 ? Math.round((correct / answered) * 100) : 0;

      const elAnswered = document.getElementById('answeredCount');
      const elCorrect = document.getElementById('correctCount');
      const elWrong = document.getElementById('wrongCount');
      const elPercent = document.getElementById('percentBadge');
      const elBar = document.getElementById('progressBar');
      const elBtnRetry = document.getElementById('btnRetryErrors');
      const elWrongBtnCount = document.getElementById('wrongBtnCount');

      if (elAnswered) elAnswered.innerText = answered;
      if (elCorrect) elCorrect.innerText = correct;
      if (elWrong) elWrong.innerText = wrong;
      if (elPercent) elPercent.innerText = percent + '%';
      if (elBar) elBar.style.width = (total > 0 ? (answered / total) * 100 : 0) + '%';

      if (elBtnRetry && elWrongBtnCount) {
        elWrongBtnCount.innerText = wrong;
        elBtnRetry.style.display = wrong > 0 ? 'inline-flex' : 'none';
      }
    }

    function retryErrors() {
      const qBoxes = document.querySelectorAll('.question-box[data-q]');
      let firstWrong = null;

      qBoxes.forEach(qBox => {
        const qNum = qBox.getAttribute('data-q');
        const correctOpt = qBox.getAttribute('data-gab');
        const sel = userAnswers[qNum];

        if (sel && sel.toUpperCase() !== correctOpt.toUpperCase()) {
          // Limpa resposta errada
          delete userAnswers[qNum];
          qBox.querySelectorAll('.option-item').forEach(opt => {
            opt.classList.remove('selected', 'is-correct', 'is-wrong');
          });
          const fb = document.getElementById(`feedback_${qNum}`);
          const com = document.getElementById(`comentario_${qNum}`);
          if (fb) fb.className = 'inline-feedback';
          if (com) com.style.display = 'none';

          if (!firstWrong) firstWrong = qBox;
        }
      });

      updateStats();
      if (firstWrong) {
        firstWrong.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    function resetQuiz() {
      if (!confirm('Deseja reiniciar todas as respostas deste caderno?')) return;
      userAnswers = {};
      document.querySelectorAll('.question-box[data-q]').forEach(qBox => {
        const qNum = qBox.getAttribute('data-q');
        qBox.querySelectorAll('.option-item').forEach(opt => {
          opt.classList.remove('selected', 'is-correct', 'is-wrong');
        });
        const fb = document.getElementById(`feedback_${qNum}`);
        const com = document.getElementById(`comentario_${qNum}`);
        if (fb) fb.className = 'inline-feedback';
        if (com) com.style.display = 'none';
      });
      updateStats();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  </script>
"""

def make_interactive(filename):
    file_path = os.path.join(PROVAS_DIR, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Identificar questoes e gabaritos
    q_boxes = []
    for b in soup.find_all('div', class_='question-box'):
        if b.find('ul', class_='options-list'):
            q_boxes.append(b)

    # Identificar gabaritos
    g_data = {} # q_num -> (gab_letter, comentario_html)

    if 'IPAPORANGA' in filename:
        # Padrão Ipaporanga: <div class="comentario-box"><strong>XX. GABARITO: X</strong> — texto</div>
        for cbox in soup.find_all('div', class_='comentario-box'):
            text = cbox.decode_contents()
            m = re.search(r'<strong>\s*(\d+)\.\s*GABARITO:\s*([ABCD])\s*</strong>\s*—?\s*(.*)', text, re.DOTALL | re.IGNORECASE)
            if m:
                q_n = int(m.group(1))
                g_l = m.group(2).upper()
                c_t = m.group(3).strip()
                g_data[q_n] = (g_l, c_t)
    else:
        # Padrão geral: <div class="question-box"><div class="question-header">QUESTÃO XX • Gabarito Oficial: <strong>(X)</strong></div><div class="comentario-box">...</div></div>
        for b in soup.find_all('div', class_='question-box'):
            cbox = b.find('div', class_='comentario-box')
            qhdr = b.find('div', class_='question-header')
            if cbox and qhdr:
                header_text = qhdr.get_text()
                m_num = re.search(r'QUEST[ÃA]O\s+(\d+)', header_text, re.IGNORECASE)
                m_gab = re.search(r'Gabarito Oficial:\s*<strong>\(([ABCD])\)</strong>', str(qhdr), re.IGNORECASE)
                if m_num and m_gab:
                    q_n = int(m_num.group(1))
                    g_l = m_gab.group(1).upper()
                    c_t = cbox.decode_contents().strip()
                    # Limpar "<strong>Resolução / Fundamentação:</strong>" do inicio se houver
                    c_t = re.sub(r'^\s*<strong>\s*Resoluç[ãa]o\s*/\s*Fundamentaç[ãa]o:\s*</strong>\s*', '', c_t, flags=re.IGNORECASE)
                    g_data[q_n] = (g_l, c_t)

    print(f"[*] {filename}: {len(q_boxes)} questões, {len(g_data)} gabaritos mapeados.")

    if len(q_boxes) == 0:
        print(f"[-] Nenhuma questão encontrada em {filename}. Pulando.")
        return False

    # Modificar cada q_box
    for idx, q_box in enumerate(q_boxes, 1):
        q_num = idx
        gab_letter, com_text = g_data.get(q_num, ('A', 'Fundamentação registrada no caderno de gabaritos oficial.'))
        
        q_box['data-q'] = str(q_num)
        q_box['data-gab'] = gab_letter

        # Converter <li> em .option-item interativos
        ul = q_box.find('ul', class_='options-list')
        if ul:
            new_lis = []
            for li in ul.find_all('li'):
                raw_text = li.get_text().strip()
                m_opt = re.match(r'^\(([ABCD])\)\s*(.*)', raw_text, re.DOTALL)
                if m_opt:
                    opt_letter = m_opt.group(1).upper()
                    opt_content = m_opt.group(2).strip()
                else:
                    opt_letter = 'A'
                    opt_content = raw_text

                new_li = soup.new_tag('li')
                new_li['class'] = 'option-item'
                new_li['data-opt'] = opt_letter
                new_li['onclick'] = f"handleOptionClick(this, {q_num}, '{opt_letter}', '{gab_letter}')"

                span_bubble = soup.new_tag('span')
                span_bubble['class'] = 'option-bubble'
                span_bubble.string = opt_letter

                span_text = soup.new_tag('span')
                span_text['class'] = 'option-text'
                span_text.string = opt_content

                new_li.append(span_bubble)
                new_li.append(span_text)
                new_lis.append(new_li)

            ul.clear()
            for nli in new_lis:
                ul.append(nli)

        # Injetar inline feedback e inline comentario se ainda não existirem
        existing_fb = q_box.find('div', id=f"feedback_{q_num}")
        if not existing_fb:
            fb_tag = soup.new_tag('div')
            fb_tag['class'] = 'inline-feedback'
            fb_tag['id'] = f"feedback_{q_num}"
            q_box.append(fb_tag)

        existing_com = q_box.find('div', id=f"comentario_{q_num}")
        if not existing_com:
            com_tag = soup.new_tag('div')
            com_tag['class'] = 'inline-comentario'
            com_tag['id'] = f"comentario_{q_num}"
            com_soup = BeautifulSoup(f"<strong>Fundamentação (Gabarito {gab_letter}):</strong> {com_text}", 'html.parser')
            com_tag.append(com_soup)
            q_box.append(com_tag)

    # Injetar Meta Viewport e Font Awesome no <head>
    head = soup.find('head')
    if head:
        if not head.find('meta', attrs={'name': 'viewport'}):
            vp = soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no'})
            head.insert(0, vp)
        
        # Link Font Awesome se não houver
        if 'font-awesome' not in str(head):
            fa = soup.new_tag('link', rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css')
            head.append(fa)

        # Style tag interativa
        st = soup.new_tag('style')
        st.string = INTERACTIVE_CSS
        head.append(st)

    # Injetar Header Interativo no início de <body>
    body = soup.find('body')
    if body:
        existing_hdr = body.find('div', id='quizHeader')
        if not existing_hdr:
            total_count = len(q_boxes)
            header_html = f"""
            <div class="interactive-header no-print" id="quizHeader">
              <div class="header-top-row">
                <div style="display:flex; align-items:center; gap:8px;">
                  <a href="../PROVAO_MOBILE_ESPECIFICAS.html" class="btn-back-nav" title="Voltar ao Provão Mobile">
                    <i class="fas fa-mobile-alt"></i> Provão Mobile
                  </a>
                  <a href="CENTRAL_DE_PROVAS.html" class="btn-back-nav" title="Central de Provas">
                    <i class="fas fa-folder-open"></i> Central de Provas
                  </a>
                </div>
                <div class="score-stats">
                  <span class="stat-pill total"><i class="fas fa-tasks"></i> <span id="answeredCount">0</span>/{total_count}</span>
                  <span class="stat-pill correct"><i class="fas fa-check"></i> <span id="correctCount">0</span></span>
                  <span class="stat-pill wrong"><i class="fas fa-times"></i> <span id="wrongCount">0</span></span>
                  <span class="stat-pill percent" id="percentBadge">0%</span>
                </div>
              </div>
              <div class="progress-track">
                <div class="progress-bar-fill" id="progressBar"></div>
              </div>
              <div class="header-controls">
                <label class="mode-toggle-label" title="Ao tocar em qualquer opção, já mostra na hora se acertou ou errou!">
                  <input type="checkbox" id="chkInstant" checked onchange="toggleInstantMode(this.checked)">
                  <span><i class="fas fa-bolt" style="color: #16a34a;"></i> Modo Estudo: Resposta ao Tocar</span>
                </label>
                <div style="display:flex; gap:6px;">
                  <button class="btn-action-quiz retry" onclick="retryErrors()" id="btnRetryErrors" style="display:none;">
                    <i class="fas fa-redo-alt" style="color:#dc2626;"></i> Refazer Erradas (<span id="wrongBtnCount">0</span>)
                  </button>
                  <button class="btn-action-quiz retry" onclick="resetQuiz()">
                    <i class="fas fa-sync-alt"></i> Reiniciar
                  </button>
                  <button class="btn-action-quiz primary" id="btnFinish" onclick="finishExam()" style="display:none;">
                    <i class="fas fa-check-double"></i> Finalizar Prova
                  </button>
                </div>
              </div>
            </div>
            """
            header_soup = BeautifulSoup(header_html, 'html.parser')
            body.insert(0, header_soup)

        # Injetar Script antes de </body>
        script_soup = BeautifulSoup(INTERACTIVE_JS, 'html.parser')
        body.append(script_soup)

    # Salvar arquivo atualizado
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"[OK] Atualizado com sucesso: {filename}")
    return True

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'PROVA_REAL_10_INBRASP_INFORMATICA.html'
    if target == 'all':
        provas = [f for f in os.listdir(PROVAS_DIR) if f.startswith('PROVA_REAL_') and f.endswith('.html')]
        for p in sorted(provas):
            make_interactive(p)
    else:
        make_interactive(target)

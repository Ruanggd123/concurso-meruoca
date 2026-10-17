import os

with open("scripts/update_tudo_ou_nada.py", "r", encoding="utf-8") as f:
    old_script = f.read()

# Vamos construir o HTML completo com as 3 Rodadas (Rodada 3 Final ativa por padrão + Rodada 2 + Rodada 1)
ROUND3_HTML = """    <!-- =========================================================
         CONTEÚDO DA RODADA 3 FINAL (FECHAMENTO 100% DO EDITAL: BLOCOS 13 A 20)
         ========================================================= -->
    <div id="round3Content">
      <div class="section-banner">
        <h2><i class="fas fa-trophy"></i> RODADA 3 FINAL — OS ÚLTIMOS 8 BLOCOS QUE FECHAM 100% DO EDITAL!</h2>
        <span>FECHAMENTO TOTAL DO EDITAL</span>
      </div>

      <!-- BLOCO 13 -->
      <div class="resumo-card" id="rc13">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-scroll"></i> BLOCO 13: Técnica Legislativa & Lei Complementar nº 95/1998 (Estrutura das Leis)</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc13', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>As 3 Partes de toda Lei (LC 95/98):</strong>
            <div class="step-flow">
              <span class="step-box gold">1. PARTE PRELIMINAR</span>
              <span>Epígrafe + Ementa + Preâmbulo</span>
              <span class="step-arrow">➔</span>
              <span class="step-box gold">2. PARTE NORMATIVA</span>
              <span>Artigos e conteúdo da lei</span>
              <span class="step-arrow">➔</span>
              <span class="step-box gold">3. PARTE FINAL</span>
              <span>Vigência e Revogação</span>
            </div>
          </li>
          <li><strong>Diferença entre Epígrafe, Ementa e Preâmbulo (Cai demais para Técnico Legislativo!):</strong>
            <br>• <strong>Epígrafe:</strong> Título no topo em letras maiúsculas que identifica a espécie e o número da lei (Ex: <em>"LEI ORDINÁRIA Nº 1.234, DE 18 DE OUTUBRO DE 2026"</em>).
            <br>• <strong>Ementa:</strong> Resumo claro e conciso do assunto da lei (Ex: <em>"Dispõe sobre o Estatuto dos Servidores de Meruoca..."</em>).
            <br>• <strong>Preâmbulo:</strong> Indica a autoridade e a ordem de execução (Ex: <em>"O PREFEITO MUNICIPAL DE MERUOCA faço saber que a Câmara aprovou e eu sanciono..."</em>).</li>
          <li><strong>Hierarquia de Articulação do Texto Legal:</strong>
            <div class="step-flow">
              <span class="step-box gold">Artigo (Art. 1º a 9º ordinal; 10 em diante cardinal)</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">Parágrafo (§ 1º ou Parágrafo único)</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">Inciso (I, II, III)</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">Alínea (a, b, c)</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">Item (1, 2, 3)</span>
            </div>
          </li>
          <li><strong>Regras de Ouro da LC 95/98:</strong>
            <br>• <span class="tag-hot">PROIBIDO renumerar artigos!</span> Se precisar inserir um artigo novo entre o Art. 5º e o Art. 6º, usa-se <strong>"Art. 5º-A"</strong>.
            <br>• Quando um dispositivo é alterado em sua redação, coloca-se ao final as letras <span class="tag-num">(NR)</span> (Nova Redação). Quando uma seção inteira é acrescentada, usa-se <span class="tag-num">(AC)</span> (Acrescentado).
            <br>• A cláusula de revogação deve ser <strong>específica/expressa</strong> (declarar exatamente quais leis estão sendo revogadas, evitando o genérico "revogam-se as disposições em contrário").</li>
        </ul>
      </div>

      <!-- BLOCO 14 -->
      <div class="resumo-card" id="rc14">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-coins"></i> BLOCO 14: Orçamento Público (PPA, LDO e LOA) & LRF Complementar</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc14', this.checked)"> Já li e gravei!
          </label>
        </div>
        <table class="mini-table">
          <thead>
            <tr>
              <th style="width:28%;">Lei Orçamentária (Art. 165 CF)</th>
              <th>Para que serve? (Palavras-Chave da Banca)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>PPA (Plano Plurianual)</strong><br><small>Vigência: 4 anos</small></td>
              <td>Planejamento estratégico de <strong>médio prazo</strong>: estabelece de forma regionalizada as <span class="tag-num">Diretrizes, Objetivos e Metas (DOM)</span> para despesas de capital e programas de duração continuada.</td>
            </tr>
            <tr>
              <td><strong>LDO (Lei de Diretrizes Orçamentárias)</strong><br><small>Anual</small></td>
              <td>Elo entre o PPA e a LOA: define as <strong>metas e prioridades</strong> para o ano seguinte, orienta a elaboração da LOA, dispõe sobre alterações na legislação tributária e traz os anexos de <strong>Metas Fiscais</strong> e <strong>Riscos Fiscais</strong>.</td>
            </tr>
            <tr>
              <td><strong>LOA (Lei Orçamentária Anual)</strong><br><small>Anual</small></td>
              <td>Orçamento propriamente dito: <strong>estima a receita e fixa a despesa</strong>. Divide-se em 3 orçamentos: <strong>Fiscal</strong>, da <strong>Seguridade Social</strong> e de <strong>Investimento das Estatais</strong>.</td>
            </tr>
          </tbody>
        </table>
        <ul class="bullet-list">
          <li><strong>Os 3 Tipos de Créditos Adicionais (Quando a LOA precisa de reforço):</strong>
            <br>• <strong>Suplementares:</strong> Reforçam dotação que <em>já existe</em> no orçamento (autorizados por lei e abertos por decreto).
            <br>• <strong>Especiais:</strong> Criam dotação para despesa <em>nova</em> que não tinha dotação específica na LOA.
            <br>• <strong>Extraordinários:</strong> Despesas <strong>imprevisíveis e urgentes</strong> (guerra, comoção interna ou calamidade pública).</li>
          <li><strong>LRF — Relatórios e Restos a Pagar:</strong>
            <br>• <strong>RGF (Relatório de Gestão Fiscal):</strong> Emitido pela Câmara e pela Prefeitura a cada <span class="tag-num">QUADRIMESTRE</span> (controla gastos com pessoal). Já o <strong>RREO</strong> (Execução Orçamentária) é emitido pelo Executivo a cada <span class="tag-num">BIMESTRE</span>.
            <br>• <strong>Art. 42 da LRF (Restos a Pagar):</strong> Nos <strong>últimos 2 quadrimestres</strong> do mandato (últimos 8 meses), é proibido contrair obrigação de despesa que não possa ser cumprida integralmente dentro dele, ou que tenha parcelas para o ano seguinte sem deixar dinheiro em caixa!</li>
        </ul>
      </div>

      <!-- BLOCO 15 -->
      <div class="resumo-card" id="rc15">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-user-shield"></i> BLOCO 15: Transparência (LAI 12.527/11), Proteção de Dados (LGPD) & Ética</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc15', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Lei de Acesso à Informação — LAI (Lei nº 12.527/2011):</strong>
            <br>• Regra geral: <strong>A publicidade é o preceito geral e o sigilo é a exceção!</strong> Qualquer interessado pode pedir informações à Câmara <strong>sem precisar dizer o motivo (independe de justificativa)</strong>!
            <br>• <strong>Transparência Ativa:</strong> O próprio órgão publica espontaneamente no Portal da Transparência (salários, licitações, contratos).
            <br>• <strong>Transparência Passiva:</strong> O cidadão faz um pedido (SIC/e-SIC) e o órgão responde. Prazo se não puder dar na hora: até <span class="tag-num">20 dias</span> (prorrogável por mais <span class="tag-num">10 dias</span> mediante justificativa).
            <br>• <strong>Prazos de Sigilo na LAI:</strong> <strong>Ultrassecreta</strong> = <span class="tag-num">25 anos</span> | <strong>Secreta</strong> = <span class="tag-num">15 anos</span> | <strong>Reservada</strong> = <span class="tag-num">5 anos</span>.</li>
          <li><strong>Lei Geral de Proteção de Dados — LGPD (Lei nº 13.709/2018):</strong>
            <br>• <strong>Dado Pessoal:</strong> Qualquer informação que identifique uma pessoa natural (nome, CPF, RG, e-mail).
            <br>• <strong>Dado Pessoal SENSÍVEL:</strong> Origem racial/étnica, convicção religiosa, opinião política, filiação a sindicato, dado de saúde, vida sexual ou dado genético/biométrico.
            <br>• <strong>Atores da LGPD:</strong> <strong>Controlador</strong> (quem toma as decisões sobre o tratamento dos dados — ex: a Câmara Municipal); <strong>Operador</strong> (quem realiza o tratamento em nome do controlador); <strong>Encarregado (DPO)</strong> (pessoa indicada para ser a ponte de comunicação entre a Câmara, os cidadãos titulares e a ANPD).</li>
        </ul>
      </div>

      <!-- BLOCO 16 -->
      <div class="resumo-card" id="rc16">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-gavel"></i> BLOCO 16: Responsabilidade Civil do Estado (Art. 37, § 6º) & Convalidação</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc16', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Responsabilidade Civil do Estado (Art. 37, § 6º da CF/88):</strong>
            <br>• As pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos respondem pelos danos que seus agentes, nessa qualidade, causarem a terceiros de forma <span class="tag-ok">OBJETIVA (Teoria do Risco Administrativo)</span> — ou seja, a vítima <strong>NÃO precisa provar dolo ou culpa</strong>, basta provar: Conduta + Dano + Nexo Causal!
            <br>• <strong>Excludentes da responsabilidade do Estado:</strong> Culpa exclusiva da vítima, caso fortuito/força maior e fato exclusivo de terceiro.
            <br>• <strong>E a responsabilidade do servidor público perante o Estado (Ação Regressiva)?</strong> É <span class="tag-num">SUBJETIVA</span>! O Município/Câmara paga a vítima primeiro e depois cobra do servidor em ação de regresso <strong>somente se provar que o servidor agiu com DOLO ou CULPA</strong>.</li>
          <li><strong>Convalidação do Ato Administrativo (Art. 55 da Lei 9.784/99):</strong>
            <br>• É a correção de um ato com defeito leve (sanável), com efeitos retroativos (<em>ex tunc</em>), desde que não cause lesão ao interesse público nem prejuízo a terceiros.
            <br>• <strong>Quais são os 2 únicos elementos que admitem Convalidação?</strong> Mnemônico <span class="tag-num">FO-CO</span>: vício de <strong>FO</strong>rma (desde que não essencial) e vício de <strong>CO</strong>mpetência (desde que não exclusiva). Vícios de Finalidade, Motivo e Objeto são insanáveis (devem ser anulados)!</li>
        </ul>
      </div>

      <!-- BLOCO 17 -->
      <div class="resumo-card" id="rc17">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-users"></i> BLOCO 17: Ciência Política, Políticas Públicas & Gestão na Câmara</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc17', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Estado vs. Governo:</strong> <strong>Estado</strong> é a instituição permanente e soberana (composta por Povo, Território e Soberania). <strong>Governo</strong> é a cúpula diretiva transitória e política que conduz o Estado por determinado mandato.</li>
          <li><strong>Funções Típicas e Atípicas do Poder Legislativo (Câmara Municipal):</strong>
            <br>• <strong>Funções Típicas (Principais):</strong> <span class="tag-ok">Legislar</span> (elaborar leis) e <span class="tag-ok">Fiscalizar</span> (controle externo sobre o Executivo com auxílio do TCE).
            <br>• <strong>Funções Atípicas (Secundárias):</strong> <strong>Administrar</strong> (quando organiza seus próprios servidores, faz concurso e licitação interna) e <strong>Julgar</strong> (quando julga o Prefeito ou Vereadores por infração político-administrativa).</li>
          <li><strong>Ciclo das Políticas Públicas:</strong>
            <div class="step-flow">
              <span class="step-box">1. Identificação do Problema</span>
              <span class="step-arrow">➔</span>
              <span class="step-box gold">2. Formação da Agenda</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">3. Formulação de Alternativas</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">4. Tomada de Decisão</span>
              <span class="step-arrow">➔</span>
              <span class="step-box gold">5. Implementação (Execução)</span>
              <span class="step-arrow">➔</span>
              <span class="step-box">6. Avaliação</span>
            </div>
          </li>
          <li><strong> os 3 "Es" da Gestão Pública:</strong>
            <br>• <strong>Eficiência:</strong> Fazer da melhor forma possível, gastando menos recursos (meios/economia).
            <br>• <strong>Eficácia:</strong> Atingir a meta/resultado planejado (fins).
            <br>• <strong>Efetividade:</strong> Impacto real e transformação social positiva na vida da população.</li>
        </ul>
      </div>

      <!-- BLOCO 18 -->
      <div class="resumo-card" id="rc18">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-cloud"></i> BLOCO 18: Informática Nível Superior — Nuvem (IaaS, PaaS, SaaS), Linux & Algoritmos</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc18', this.checked)"> Já li e gravei!
          </label>
        </div>
        <table class="mini-table">
          <thead>
            <tr>
              <th style="width:28%;">Tópico do Edital</th>
              <th>Resumo Direto para Acertar a Questão</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Computação em Nuvem:<br>SaaS, PaaS e IaaS</strong></td>
              <td>• <strong>SaaS (Software como Serviço):</strong> Programas prontos para o usuário final usar no navegador (Ex: <em>Google Docs, Gmail, Office 365, Google Drive</em>).<br>
              • <strong>PaaS (Plataforma como Serviço):</strong> Ambiente para <em>desenvolvedores</em> criarem e hospedarem sistemas e bancos de dados (Ex: <em>Google App Engine, Heroku</em>).<br>
              • <strong>IaaS (Infraestrutura como Serviço):</strong> Aluguel de servidores virtuais, redes e discos brutos (Ex: <em>AWS EC2, Google Compute Engine</em>).</td>
            </tr>
            <tr>
              <td><strong>Comandos Básicos do Linux (Ubuntu)</strong></td>
              <td>• <code>ls</code> = listar arquivos da pasta | <code>cd</code> = mudar de diretório | <code>pwd</code> = mostrar pasta atual.<br>
              • <code>mkdir</code> = criar pasta | <code>rm</code> = remover arquivo | <code>cp</code> = copiar | <code>mv</code> = mover ou renomear.<br>
              • <code>sudo</code> = executar comando como superusuário (administrador / root).</td>
            </tr>
            <tr>
              <td><strong>Algoritmos & Programação Básica</strong></td>
              <td>• <strong>Algoritmo:</strong> Sequência finita, lógica e ordenada de passos para resolver um problema.<br>
              • <strong>Estruturas de Controle:</strong> <em>Condicional / Seleção</em> (<code>if / else</code> = se / senão) e <em>Repetição / Laço</em> (<code>for / while</code> = para / enquanto).<br>
              • <strong>Fluxograma:</strong> Oval = Início/Fim; Retângulo = Processamento/Cálculo; Losango (Diamante) = <strong>Decisão / Condição (Sim/Não)</strong>.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- BLOCO 19 -->
      <div class="resumo-card" id="rc19">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-chart-pie"></i> BLOCO 19: Matemática Completa — Conjuntos, Média/Moda/Mediana, Probabilidade e Áreas</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc19', this.checked)"> Já li e gravei!
          </label>
        </div>
        <ul class="bullet-list">
          <li><strong>Problema de 2 Conjuntos (Diagrama de Venn — Cai muito!):</strong>
            <br>Ex: <em>"De 50 servidores, 30 usam Word, 25 usam Excel e 10 usam AMBOS. Quantos usam pelo menos um?"</em>
            <br>➔ <strong>Regra Rápida:</strong> Soma os dois grupos e <strong>SUBTRAI a interseção (ambos)</strong>: 30 + 25 - 10 = <strong>45 servidores</strong> (e 50 - 45 = 5 não usam nenhum!).</li>
          <li><strong>Estatística Básica (Média, Moda e Mediana):</strong>
            <br>• <strong>Média Aritmética:</strong> Soma todos os valores e divide pela quantidade de elementos.
            <br>• <strong>Moda:</strong> É o valor que <strong>MAIS SE REPETE</strong> (está "na moda"). Ex: em (2, 4, 4, 7, 9), a Moda é <strong>4</strong>.
            <br>• <strong>Mediana:</strong> Coloque os números em <strong>ordem crescente</strong> e pegue o valor exatamente do <strong>MEIO</strong> (se a quantidade for par, faça a média dos dois do meio).</li>
          <li><strong>Probabilidade (Casos Favoráveis ÷ Total de Casos Possíveis):</strong>
            <br>Ex: Em uma urna com 3 bolas azuis e 7 bolas brancas (total = 10 bolas), a chance de sortear uma azul é 3 ÷ 10 = <strong>30%</strong> (ou 3/10).</li>
          <li><strong>Geometria Plana Básica:</strong>
            <br>• <strong>Perímetro:</strong> Soma de todos os lados da figura.
            <br>• <strong>Área do Retângulo / Quadrado:</strong> Base × Altura. (Ex: sala de 6m por 4m tem área = 24 m² e perímetro = 6+6+4+4 = 20m).
            <br>• <strong>Área do Triângulo:</strong> (Base × Altura) ÷ 2.</li>
        </ul>
      </div>

      <!-- BLOCO 20 -->
      <div class="resumo-card" id="rc20">
        <div class="resumo-header">
          <h3 class="resumo-title"><i class="fas fa-book-open"></i> BLOCO 20: Português Completo — Tipologia Textual, Coesão e Termos da Oração</h3>
          <label class="check-read-lbl">
            <input type="checkbox" onchange="toggleCardRead('rc20', this.checked)"> Já li e gravei!
          </label>
        </div>
        <table class="mini-table">
          <thead>
            <tr>
              <th>Assunto de Português</th>
              <th>Como Identificar na Prova da INBRASP</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Os 5 Tipos Textuais</strong></td>
              <td>• <strong>Narrativo:</strong> Conta uma história com personagens, tempo, espaço e enredo (verbos de ação no passado).<br>
              • <strong>Descritivo:</strong> Faz um "retrato" detalhado de pessoa, objeto ou lugar (muitos adjetivos).<br>
              • <strong>Dissertativo-Expositivo:</strong> Informa e explica um tema de modo neutro/objetivo, sem tentar convencer.<br>
              • <strong>Dissertativo-Argumentativo:</strong> Defende uma tese/opinião com argumentos para convencer o leitor.<br>
              • <strong>Injuntivo / Instrucional:</strong> Dá instruções, ordens ou passo a passo (verbos no imperativo: <em>faça, vote, leia</em> — ex: manual, receita, edital).</td>
            </tr>
            <tr>
              <td><strong>Coesão Anafórica vs. Catafórica</strong></td>
              <td>• <strong>Anáfora (Olha para TRÁS):</strong> O pronome retoma algo que <em>já foi dito antes</em> no texto (usa-se <strong>este/esse/aquele/ele</strong>).<br>
              • <strong>Catáfora (Olha para FRENTE):</strong> O pronome anuncia algo que <em>ainda vai ser dito</em> adiante (usa-se <strong>este/isto</strong>: <em>"Só desejo <u>isto</u>: que todos sejam aprovados."</em>).</td>
            </tr>
            <tr>
              <td><strong>Denotação vs. Conotação</strong></td>
              <td>• <strong>Denotação (Com D de Dicionário):</strong> Sentido real, literal e objetivo da palavra.<br>
              • <strong>Conotação:</strong> Sentido figurado, poético ou simbólico.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
"""

QUESTIONS_R3_JS = """
    // =========================================================================
    // RODADA 3 FINAL: 40 QUESTÕES DE FECHAMENTO 100% DO EDITAL (BLOCOS 13 A 20)
    // =========================================================================
    const QUESTIONS_R3 = [
      // 1 a 10: Língua Portuguesa (Tipologia, Coesão, Semântica e Sintaxe)
      {
        num: 1, cat: 'pt', mat: 'Língua Portuguesa • Tipologia Textual',
        q: 'Um documento administrativo ou manual da Câmara que apresenta instruções passo a passo de como o servidor deve protocolar projetos, utilizando verbos no modo imperativo ("registre", "confira", "encaminhe"), predomina como tipo textual:',
        opts: [
          'Narrativo ficcional.',
          'Injuntivo / Instrucional.',
          'Descritivo poético.',
          'Lírico subjetivo.'
        ],
        ans: 1,
        exp: 'Gabarito B. O texto injuntivo (ou instrucional) tem como finalidade orientar, instruir ou dar comandos ao leitor, empregando verbos no imperativo ou infinitivo (ex: manuais, editais, receitas).'
      },
      {
        num: 2, cat: 'pt', mat: 'Língua Portuguesa • Coesão Referencial (Anáfora x Catáfora)',
        q: 'No período "A Mesa Diretora estabeleceu APENAS ESTA META para o semestre: digitalizar todo o acervo legislativo", o termo destacado ("esta meta") antecipa uma informação que será dita logo à frente, exercendo função coesiva:',
        opts: [
          'Catafórica (coesão para a frente).',
          'Anafórica (retomada de termo anterior).',
          'Elíptica verbal.',
          'Ambiguidade lexical.'
        ],
        ans: 0,
        exp: 'Gabarito A. Quando o pronome demonstrativo ("esta/isto") anuncia um termo que ainda vai aparecer adiante no texto, ocorre coesão CATAFÓRICA. Quando retoma o que já passou, é ANAFÓRICA.'
      },
      {
        num: 3, cat: 'pt', mat: 'Língua Portuguesa • Denotação vs. Conotação',
        q: 'Assinale a alternativa em que a palavra destacada foi empregada em sentido DENOTATIVO (sentido literal, próprio do dicionário):',
        opts: [
          'O relator foi uma verdadeira ROCHA diante das críticas na sessão.',
          'Aquela emenda parlamentar foi a CHAVE do sucesso do projeto.',
          'Os vereadores aprovaram a construção de uma PONTE sobre o rio do Município.',
          'O discurso do parlamentar INFLAMOU o coração dos presentes.'
        ],
        ans: 2,
        exp: 'Gabarito C. Em "construção de uma ponte sobre o rio", a palavra "ponte" está no seu sentido real, literal e objetivo (Denotação = D de Dicionário). Nas demais, há sentido figurado (conotação).'
      },
      {
        num: 4, cat: 'pt', mat: 'Língua Portuguesa • Tipos de Sujeito',
        q: 'Na oração "Faltam apenas dois dias para a realização do concurso da Câmara de Meruoca", o sujeito da forma verbal "Faltam" é classificado como:',
        opts: [
          'Oração sem sujeito (verbo impessoal).',
          'Sujeito oculto / desinencial.',
          'Sujeito simples e posposto ("apenas dois dias").',
          'Sujeito indeterminado.'
        ],
        ans: 2,
        exp: 'Gabarito C. Pergunte ao verbo: O que é que falta? Resposta: "apenas dois dias" (= Eles faltam). Trata-se de sujeito simples colocado depois do verbo (posposto), razão pela qual o verbo "Faltam" vai para o plural!'
      },
      {
        num: 5, cat: 'pt', mat: 'Língua Portuguesa • Conjunções Condicionais e Proporcionais',
        q: 'No período "À MEDIDA QUE os pareceres técnicos eram lidos, as dúvidas dos vereadores diminuíam", a locução conjuntiva destacada indica circunstância de:',
        opts: [
          'Proporcionalidade.',
          'Condição.',
          'Finalidade.',
          'Concessão.'
        ],
        ans: 0,
        exp: 'Gabarito A. "À medida que" e "à proporção que" são as locuções conjuntivas adverbiais PROPORCIONAIS por excelência.'
      },
      {
        num: 6, cat: 'pt', mat: 'Língua Portuguesa • Vozes Verbais (Conversão)',
        q: 'Transpondo-se a oração ativa "A Comissão de Justiça analisará o projeto de lei" para a VOZ PASSIVA ANALÍTICA, a forma verbal correta será:',
        opts: [
          'havia analisado.',
          'será analisado.',
          'foi analisado.',
          'analisar-se-ia.'
        ],
        ans: 1,
        exp: 'Gabarito B. "Analisará" está no Futuro do Presente do Indicativo. Na voz passiva analítica, o verbo auxiliar "SER" assume o mesmo tempo ("será") + particípio ("analisado"): "O projeto de lei será analisado pela Comissão".'
      },
      {
        num: 7, cat: 'pt', mat: 'Língua Portuguesa • Acentuação Gráfica (Hiatos e Ditongos)',
        q: 'De acordo com o Novo Acordo Ortográfico, assinale a opção que explica corretamente o acento gráfico da palavra "SAÚDE":',
        opts: [
          'É uma palavra proparoxítona.',
          'Acentua-se a vogal "U" tônica quando forma hiato com a vogal anterior, estando sozinha na sílaba (sa-ú-de).',
          'É uma oxítona terminada em vogal aberta.',
          'Recebe acento diferencial de timbre.'
        ],
        ans: 1,
        exp: 'Gabarito B. Regra do hiato: acentuam-se o "I" e o "U" tônicos quando formam hiato com a vogal anterior, estando sozinhos na sílaba ou seguidos de "s" (sa-ú-de, pa-ís, ba-ú).'
      },
      {
        num: 8, cat: 'pt', mat: 'Língua Portuguesa • Uso de Há vs. A (Tempo)',
        q: 'Complete corretamente as lacunas: "A Câmara Municipal foi fundada ________ muitas décadas, e a nova sessão solene ocorrerá daqui ________ duas semanas."',
        opts: [
          'a — há',
          'há — a',
          'há — há',
          'à — a'
        ],
        ans: 1,
        exp: 'Gabarito B. Para tempo PASSADO (já decorrido = faz), usa-se "HÁ" com H ("há muitas décadas"). Para tempo FUTURO ("daqui a duas semanas"), usa-se a preposição "A" sem H e sem crase.'
      },
      {
        num: 9, cat: 'pt', mat: 'Língua Portuguesa • Sintaxe (Aposto vs. Vocativo)',
        q: 'Na frase "Meruoca, belo município serrano do Ceará, realizará concurso público para a Câmara", o trecho isolado entre vírgulas exerce a função sintática de:',
        opts: [
          'Vocativo.',
          'Aposto explicativo.',
          'Complemento nominal.',
          'Agente da passiva.'
        ],
        ans: 1,
        exp: 'Gabarito B. "Belo município serrano do Ceará" explica e resume o substantivo anterior ("Meruoca"), exercendo a função de APOSTO EXPLICATIVO.'
      },
      {
        num: 10, cat: 'pt', mat: 'Língua Portuguesa • Reescrita e Sentido de Palavras (Semântica)',
        q: 'No trecho "A decisão do Plenário é IRREVOGÁVEL e exige cumprimento IMEDIATO", os vocábulos destacados podem ser substituídos, sem alteração de sentido, por:',
        opts: [
          'provisória — facultativo',
          'definitiva — célere/pronto',
          'questionável — posterior',
          'tácita — eventual'
        ],
        ans: 1,
        exp: 'Gabarito B. Irrevogável = que não pode ser revogado, definitivo; Imediato = pronto, célere, instantâneo.'
      },

      // 11 a 15: Matemática & RLM (Conjuntos, Estatística, Probabilidade e Geometria)
      {
        num: 11, cat: 'mat', mat: 'Matemática • Operações com Conjuntos (Diagrama de Venn)',
        q: 'Em uma pesquisa com 50 servidores públicos, constatou-se que 30 dominam o Microsoft Word, 25 dominam o Microsoft Excel e 10 dominam AMBOS os programas. Quantos servidores dominam PELO MENOS UM desses dois programas?',
        opts: [
          '35 servidores.',
          '40 servidores.',
          '45 servidores.',
          '50 servidores.'
        ],
        ans: 2,
        exp: 'Gabarito C. Fórmula da união de dois conjuntos: Soma os dois grupos e subtrai a interseção (para não contar duas vezes quem domina ambos): 30 + 25 - 10 = 45 servidores.'
      },
      {
        num: 12, cat: 'mat', mat: 'Matemática • Estatística (Média, Moda e Mediana)',
        q: 'Durante cinco dias da semana, o setor de protocolo da Câmara registrou as seguintes quantidades diárias de ofícios recebidos: 4, 7, 7, 10 e 12. Assinale a alternativa que apresenta, respectivamente, a MODA e a MÉDIA ARITMÉTICA desses valores:',
        opts: [
          'Moda = 7 e Média = 8.',
          'Moda = 8 e Média = 7.',
          'Moda = 10 e Média = 8.',
          'Moda = 7 e Média = 7.'
        ],
        ans: 0,
        exp: 'Gabarito A. MODA é o valor que mais se repete (o número 7 aparece duas vezes -> Moda = 7). MÉDIA é a soma dividida por 5: (4 + 7 + 7 + 10 + 12) = 40 ÷ 5 = 8.'
      },
      {
        num: 13, cat: 'mat', mat: 'Matemática • Probabilidade Básica',
        q: 'Sobre a mesa da Presidência há uma pasta contendo 10 projetos de lei numerados, sendo 3 projetos do Poder Executivo e 7 projetos de autoria de Vereadores. Escolhendo-se ao acaso um único projeto dessa pasta, qual é a probabilidade de ele ser do Poder Executivo?',
        opts: [
          '15%',
          '30%',
          '50%',
          '70%'
        ],
        ans: 1,
        exp: 'Gabarito B. Probabilidade = Casos Favoráveis (3 projetos do Executivo) ÷ Total de Casos (10 projetos) = 3/10 = 0,30 = 30%.'
      },
      {
        num: 14, cat: 'mat', mat: 'Matemática • Geometria Plana (Área e Perímetro)',
        q: 'O plenário da Câmara Municipal possui formato retangular medindo 12 metros de comprimento por 8 metros de largura. Qual é, respectivamente, a ÁREA total do piso e o PERÍMETRO desse plenário?',
        opts: [
          'Área de 96 m² e Perímetro de 40 m.',
          'Área de 40 m² e Perímetro de 96 m.',
          'Área de 96 m² e Perímetro de 20 m.',
          'Área de 80 m² e Perímetro de 40 m.'
        ],
        ans: 0,
        exp: 'Gabarito A. Área do retângulo = Base × Altura = 12 × 8 = 96 m². Perímetro = soma dos 4 lados = 12 + 12 + 8 + 8 = 40 metros.'
      },
      {
        num: 15, cat: 'mat', mat: 'Raciocínio Lógico • Sequências Lógicas e Progressão Aritmética',
        q: 'Observe a sequência numérica formada pelos protocolos emitidos a cada hora: (5, 11, 17, 23, 29, ...). Mantendo-se o mesmo padrão lógico (razão constante), qual será o 6º termo dessa sequência?',
        opts: [
          '33',
          '35',
          '36',
          '37'
        ],
        ans: 1,
        exp: 'Gabarito B. Trata-se de uma Progressão Aritmética (PA) em que cada termo aumenta sempre +6 em relação ao anterior (5+6=11; 11+6=17; 17+6=23; 23+6=29; 29+6 = 35).'
      },

      // 16 a 20: Informática (Nuvem, Linux, Algoritmos e Segurança)
      {
        num: 16, cat: 'info', mat: 'Informática • Computação em Nuvem (SaaS, PaaS e IaaS)',
        q: 'No contexto de Computação em Nuvem (Cloud Computing), aplicativos completos acessados diretamente pelo usuário final via navegador web ou celular, como o Google Docs, Gmail e Microsoft Office 365, classificam-se no modelo:',
        opts: [
          'SaaS (Software as a Service — Software como Serviço).',
          'IaaS (Infrastructure as a Service).',
          'BIOS (Basic Input/Output System).',
          'LAN (Local Area Network).'
        ],
        ans: 0,
        exp: 'Gabarito A. SaaS (Software como Serviço) entrega o aplicativo pronto para uso imediato do usuário final (Google Workspace, Office 365, Gmail).'
      },
      {
        num: 17, cat: 'info', mat: 'Informática • Sistema Operacional Linux (Ubuntu)',
        q: 'No terminal de comandos do sistema operacional Ubuntu Linux, os comandos utilizados para LISTAR os arquivos do diretório atual e para CRIAR um novo diretório (pasta) são, respectivamente:',
        opts: [
          'ls e mkdir',
          'format e del',
          'ipconfig e ping',
          'ctrl e alt'
        ],
        ans: 0,
        exp: 'Gabarito A. No Linux: "ls" (list) lista o conteúdo do diretório atual, e "mkdir" (make directory) cria uma nova pasta/diretório.'
      },
      {
        num: 18, cat: 'info', mat: 'Informática • Algoritmos e Fluxogramas',
        q: 'Na construção de algoritmos representados graficamente por FLUXOGRAMAS, a figura geométrica padrão utilizada para representar uma estrutura condicional de DECISÃO (teste lógico com saídas tipo "Sim/Verdadeiro" ou "Não/Falso") é o:',
        opts: [
          'Losango (Diamante).',
          'Retângulo simples.',
          'Círculo pequeno.',
          'Linha tracejada.'
        ],
        ans: 0,
        exp: 'Gabarito A. Em fluxogramas padronizados: o Losango (diamante) representa Decisão/Condição (if/else); o Retângulo representa Processamento/Cálculo; o Oval/Terminal representa Início ou Fim.'
      },
      {
        num: 19, cat: 'info', mat: 'Informática • Segurança da Informação (Princípios CID)',
        q: 'Entre os pilares fundamentais da Segurança da Informação, a propriedade que garante que a informação não foi alterada, adulterada ou corrompida de forma não autorizada durante seu armazenamento ou transmissão denomina-se:',
        opts: [
          'Integridade.',
          'Portabilidade.',
          'Volatilidade.',
          'Fragmentação.'
        ],
        ans: 0,
        exp: 'Gabarito A. Mnemônico CID: Confidencialidade (acesso apenas por pessoas autorizadas), Integridade (informação íntegra, exata e sem alteração indevida) e Disponibilidade (acessível quando necessário).'
      },
      {
        num: 20, cat: 'info', mat: 'Informática • Navegação Segura (HTTPS e DNS)',
        q: 'Ao acessar o Portal da Transparência da Câmara Municipal, o endereço exibido inicia-se com "HTTPS://" acompanhado de um ícone de cadeado, e o nome do domínio é convertido automaticamente no endereço IP do servidor. O protocolo "HTTPS" e o serviço que traduz nomes de domínio em endereços IP são, respectivamente:',
        opts: [
          'Protocolo de hipertexto seguro com criptografia (SSL/TLS) e sistema DNS (Domain Name System).',
          'Protocolo exclusivo de envio de e-mail e cabo de fibra óptica.',
          'Antivírus do Windows e planilha eletrônica.',
          'Memória RAM volátil e protocolo FTP.'
        ],
        ans: 0,
        exp: 'Gabarito A. O HTTPS adiciona a camada de criptografia SSL/TLS ao HTTP, e o DNS (Domain Name System) traduz nomes amigáveis (ex: meruoca.ce.leg.br) nos respectivos endereços IP numéricos.'
      },

      // 21 a 40: Conhecimentos Específicos Finais (Técnica Legislativa, Orçamento, LAI, LGPD, Responsabilidade Civil e Ciência Política)
      {
        num: 21, cat: 'esp', mat: 'Técnica Legislativa (LC 95/1998) • Estrutura da Lei',
        q: 'De acordo com a Lei Complementar nº 95/1998, que dispõe sobre a elaboração, a redação, a alteração e a consolidação das leis, a parte do ato normativo que explicita, de modo conciso e sob a epígrafe, o resumo do OBJETO da lei (ex: "Dispõe sobre o Regimento Interno da Câmara...") denomina-se:',
        opts: [
          'Ementa.',
          'Apêndice.',
          'Fecho.',
          'Errata.'
        ],
        ans: 0,
        exp: 'Gabarito A. Na parte preliminar da lei: Epígrafe é o título com número e data ("LEI Nº..."); EMENTA é o resumo claro e conciso do objeto da lei; Preâmbulo indica a autoria e ordem de execução.'
      },
      {
        num: 22, cat: 'esp', mat: 'Técnica Legislativa (LC 95/1998) • Articulação e Numeração',
        q: 'Segundo as normas de técnica legislativa da LC nº 95/1998, a unidade básica de articulação de qualquer lei é o ARTIGO, que se desdobra em parágrafos ou em incisos. Sobre a numeração dos artigos e alterações legais, é CORRETO afirmar:',
        opts: [
          'Os artigos são numerados de forma ordinal até o nono (Art. 1º ao Art. 9º) e cardinal a partir do dez (Art. 10, Art. 11...), sendo VEDADA a renumeração de artigos quando da inclusão de novos dispositivos.',
          'Todos os artigos de uma lei devem ser numerados em algarismos romanos.',
          'Sempre que um artigo for revogado, todos os artigos seguintes devem ser renumerados.',
          'Os parágrafos são representados por letras minúsculas (a, b, c).'
        ],
        ans: 0,
        exp: 'Gabarito A. Art. 10 e Art. 12 da LC 95/98: numeração ordinal até o Art. 9º e cardinal a partir do Art. 10. Além disso, é expressamente VEDADA a renumeração de artigos (se inserir artigo novo entre o 5º e o 6º, usa-se "Art. 5º-A").'
      },
      {
        num: 23, cat: 'esp', mat: 'Orçamento Público • PPA, LDO e LOA (Art. 165 CF/88)',
        q: 'No sistema orçamentário brasileiro aplicável aos Municípios, o instrumento legal que estabelece as metas e prioridades da administração pública para o exercício financeiro subsequente, orienta a elaboração da Lei Orçamentária Anual (LOA) e dispõe sobre as alterações na legislação tributária é:',
        opts: [
          'O Plano Plurianual (PPA).',
          'A Lei de Diretrizes Orçamentárias (LDO).',
          'O Decreto de Calamidade Financeira.',
          'O Regimento Interno da Câmara.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 165, § 2º da CF/88: A LDO compreende as metas e prioridades para o exercício seguinte, orienta a elaboração da LOA e dispõe sobre alterações na legislação tributária. (O PPA traz Diretrizes, Objetivos e Metas de médio prazo para 4 anos).'
      },
      {
        num: 24, cat: 'esp', mat: 'Orçamento Público • Créditos Adicionais (Lei 4.320/64 e CF/88)',
        q: 'Durante a execução do orçamento anual (LOA), os créditos adicionais destinados a despesas para as quais NÃO HAJA dotação orçamentária específica (criação de uma despesa nova não prevista na LOA) classificam-se como:',
        opts: [
          'Créditos Suplementares.',
          'Créditos Especiais.',
          'Créditos Ordinários.',
          'Restos a Pagar.'
        ],
        ans: 1,
        exp: 'Gabarito B. Lembre-se da diferença: Crédito SUPLEMENTAR reforça dotação que já existe na LOA; Crédito ESPECIAL cria dotação para despesa nova que não tinha previsão na LOA; Crédito EXTRAORDINÁRIO atende despesas imprevisíveis e urgentes (calamidade pública/guerra).'
      },
      {
        num: 25, cat: 'esp', mat: 'Lei de Responsabilidade Fiscal • Relatório de Gestão Fiscal (RGF)',
        q: 'De acordo com o Art. 54 da Lei de Responsabilidade Fiscal (LC nº 101/2000), ao final de cada QUADRIMESTRE será emitido pelos titulares dos Poderes (incluindo o Presidente da Câmara Municipal) o relatório que demonstra o cumprimento dos limites de despesa total com pessoal, denominado:',
        opts: [
          'Relatório de Gestão Fiscal (RGF).',
          'Balanço Patrimonial Privado.',
          'Ata de Conferência de Caixa.',
          'Certidão Negativa de Débitos.'
        ],
        ans: 0,
        exp: 'Gabarito A. O Relatório de Gestão Fiscal (RGF) é quadrimestral e obrigatório para todos os Poderes (inclusive a Câmara Municipal), focando no controle dos limites de despesa com pessoal (6% na Câmara).'
      },
      {
        num: 26, cat: 'esp', mat: 'Lei de Responsabilidade Fiscal • Restos a Pagar no Fim de Mandato (Art. 42)',
        q: 'Nos termos do Art. 42 da Lei de Responsabilidade Fiscal, é VEDADO ao titular de Poder ou órgão (Prefeito ou Presidente da Câmara), nos últimos DOIS QUADRIMESTRES do seu mandato:',
        opts: [
          'Realizar o pagamento da folha salarial normal dos servidores efetivos.',
          'Contrair obrigação de despesa que não possa ser cumprida integralmente dentro dele, ou que tenha parcelas a serem pagas no exercício seguinte sem que haja suficiente disponibilidade de caixa para este efeito.',
          'Encaminhar o projeto da Lei Orçamentária Anual.',
          'Publicar os relatórios de transparência fiscal.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 42 da LRF: Nos últimos 2 quadrimestres do mandato (últimos 8 meses), é proibido contrair obrigação de despesa que não possa ser paga no próprio mandato, salvo se deixar dinheiro suficiente em caixa.'
      },
      {
        num: 27, cat: 'esp', mat: 'Lei de Acesso à Informação (Lei 12.527/2011) • Regras e Prazos',
        q: 'Segundo a Lei nº 12.527/2011 (Lei de Acesso à Informação - LAI), aplicável à Câmara Municipal de Meruoca, sobre o pedido de acesso a informações públicas feito por qualquer cidadão, é CORRETO afirmar:',
        opts: [
          'O cidadão é obrigado a comprovar interesse jurídico e justificar detalhadamente os motivos determinantes da sua solicitação.',
          'São VEDADAS quaisquer exigências relativas aos motivos determinantes da solicitação de informações de interesse público, e, não sendo possível conceder o acesso imediato, o órgão tem o prazo de até 20 (vinte) dias para responder, prorrogável por mais 10 (dez) dias mediante justificativa.',
          'Todas as informações sobre remuneração de servidores são classificadas como ultrassecretas por 25 anos.',
          'O prazo para resposta do órgão público é de 180 dias úteis.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 10, § 3º e Art. 11 da LAI: É proibido exigir que o cidadão justifique o motivo do pedido! E se o acesso não puder ser imediato, o prazo máximo é de 20 dias, prorrogável por mais 10 dias.'
      },
      {
        num: 28, cat: 'esp', mat: 'Lei Geral de Proteção de Dados (Lei 13.709/2018 - LGPD)',
        q: 'De acordo com o Art. 5º da Lei Geral de Proteção de Dados Pessoais (LGPD — Lei nº 13.709/2018), o dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou referente à saúde ou a dado biométrico é classificado especificamente como:',
        opts: [
          'Dado público irrestrito.',
          'Dado pessoal sensível.',
          'Dado anonimizado descartável.',
          'Metadado financeiro.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 5º, II da LGPD: Dados sobre origem racial/étnica, religião, opinião política, sindicato, saúde, vida sexual, genética ou biometria são DADOS PESSOAIS SENSÍVEIS e possuem proteção mais rigorosa.'
      },
      {
        num: 29, cat: 'esp', mat: 'LGPD (Lei 13.709/2018) • Atores (Controlador, Operador e Encarregado)',
        q: 'Na estrutura da LGPD aplicada ao Poder Público, a pessoa indicada pelo controlador para atuar como CANAL DE COMUNICAÇÃO entre o controlador (Câmara), os titulares dos dados (cidadãos/servidores) e a Autoridade Nacional de Proteção de Dados (ANPD) denomina-se:',
        opts: [
          'Encarregado pelo tratamento de dados pessoais (DPO).',
          'Vereador Relator.',
          'Leiloeiro Oficial.',
          'Perito Judicial.'
        ],
        ans: 0,
        exp: 'Gabarito A. Art. 5º, VIII da LGPD: O Encarregado (Data Protection Officer - DPO) é a pessoa indicada para atuar como canal de comunicação entre a instituição, os titulares dos dados e a ANPD.'
      },
      {
        num: 30, cat: 'esp', mat: 'Direito Administrativo • Responsabilidade Civil do Estado (Art. 37, § 6º CF)',
        q: 'Nos termos do Art. 37, § 6º da Constituição Federal de 1988, as pessoas jurídicas de direito público respondem pelos danos que seus agentes, nessa qualidade, causarem a terceiros sob a modalidade de responsabilidade:',
        opts: [
          'Subjetiva, cabendo à vítima provar o dolo específico do servidor.',
          'Objetiva (baseada na Teoria do Risco Administrativo), assegurado o direito de regresso contra o agente responsável nos casos de dolo ou culpa (responsabilidade subjetiva do agente).',
          'Inexistente, pois o Estado é isento de indenizar particulares.',
          'Solidária criminal.'
        ],
        ans: 1,
        exp: 'Gabarito B. Art. 37, § 6º da CF/88: O Estado responde de forma OBJETIVA perante o terceiro lesado (independe de dolo ou culpa), e o servidor responde de forma SUBJETIVA perante o Estado em ação regressiva (exige prova de dolo ou culpa).'
      },
      {
        num: 31, cat: 'esp', mat: 'Direito Administrativo • Convalidação do Ato Administrativo',
        q: 'A respeito da CONVALIDAÇÃO dos atos administrativos (Art. 55 da Lei nº 9.784/99), quando um ato apresenta defeito sanável e não acarreta lesão ao interesse público nem prejuízo a terceiros, a Administração pode convalidá-lo. Os dois únicos requisitos/elementos que admitem convalidação são:',
        opts: [
          'Finalidade e Motivo.',
          'Competência (desde que não exclusiva) e Forma (desde que não essencial) — mnemônico FO-CO.',
          'Objeto ilícito e Desvio de finalidade.',
          'Apenas o mérito administrativo.'
        ],
        ans: 1,
        exp: 'Gabarito B. Mnemônico FO-CO: apenas vícios sanáveis de FOrma e COmpetência admitem convalidação (com efeitos retroativos ex tunc).'
      },
      {
        num: 32, cat: 'esp', mat: 'Poder Legislativo • Funções Típicas e Atípicas da Câmara',
        q: 'O Poder Legislativo Municipal exerce funções típicas e atípicas. Assinale a alternativa que apresenta, respectivamente, as duas funções TÍPICAS e uma função ATÍPICA da Câmara Municipal de Meruoca:',
        opts: [
          'Típicas: Legislar e Fiscalizar; Atípica: Administrar seus serviços internos (ou julgar o Prefeito por infração político-administrativa).',
          'Típicas: Executar obras e Cobrar impostos; Atípica: Elaborar leis.',
          'Típicas: Julgar ações civis e Prender infratores; Atípica: Fiscalizar o Executivo.',
          'Típicas: Sancionar e Vetar leis; Atípica: Promulgar resoluções.'
        ],
        ans: 0,
        exp: 'Gabarito A. As funções típicas do Poder Legislativo são LEGISLAR e FISCALIZAR. Suas funções atípicas são ADMINISTRAR (gestão interna de pessoal e compras da Câmara) e JULGAR (julgamento político-administrativo).'
      },
      {
        num: 33, cat: 'esp', mat: 'Ciência Política & Políticas Públicas • Ciclo de Políticas Públicas',
        q: 'No estudo das Políticas Públicas municipais, a fase do ciclo em que as decisões planejadas saem do papel e são colocadas em prática por meio da execução de programas, ações e prestação efetiva de serviços aos cidadãos denomina-se:',
        opts: [
          'Formação da Agenda.',
          'Implementação.',
          'Extinção prévia.',
          'Sondagem de opinião.'
        ],
        ans: 1,
        exp: 'Gabarito B. A fase de IMPLEMENTAÇÃO é o momento da execução prática da política pública (transformar as metas planejadas na formulação em ações concretas).'
      },
      {
        num: 34, cat: 'esp', mat: 'Gestão Pública • Eficiência, Eficácia e Efetividade',
        q: 'Na moderna Administração Pública, os conceitos de Eficiência, Eficácia e Efetividade possuem significados distintos. Quando uma ação pública alcança o impacto social desejado, transformando positivamente a realidade da comunidade meruoquense, diz-se que houve:',
        opts: [
          'Efetividade (impacto real e transformação social).',
          'Mera formalidade burocrática.',
          'Desconcentração tarifária.',
          'Inexigibilidade.'
        ],
        ans: 0,
        exp: 'Gabarito A. Eficiência = fazer certo com economia de meios; Eficácia = atingir a meta numérica prevista; EFETIVIDADE = gerar impacto real e transformação social duradoura.'
      },
      {
        num: 35, cat: 'esp', mat: 'Nova Lei de Licitações (Lei 14.133/2021) • Sistema de Registro de Preços (SRP)',
        q: 'Nos termos do Art. 82 e 84 da Lei nº 14.133/2021, o Sistema de Registro de Preços (SRP) é um procedimento auxiliar formalizado por meio da Ata de Registro de Preços, cujo prazo de vigência será de:',
        opts: [
          '1 (um) ano e poderá ser prorrogado, por igual período, desde que comprovado o preço vantajoso.',
          '5 (cinco) anos improrrogáveis.',
          '30 (trinta) dias apenas.',
          '10 (dez) anos automáticos.'
        ],
        ans: 0,
        exp: 'Gabarito A. Art. 84 da Lei 14.133/2021: O prazo de vigência da ata de registro de preços será de 1 (um) ano e poderá ser prorrogado, por igual período (totalizando até 2 anos), desde que comprovado o preço vantajoso.'
      },
      {
        num: 36, cat: 'esp', mat: 'Regimento Interno & Atos Parlamentares • Requerimento, Indicação e Moção',
        q: 'No âmbito das proposições parlamentares na Câmara Municipal, o instrumento pelo qual o Vereador SUGERE ao Poder Executivo a realização de obra, serviço ou medida de interesse público local (como pavimentação de uma rua ou reforma de posto de saúde), sem caráter de lei coercitiva, denomina-se:',
        opts: [
          'Indicação.',
          'Emenda à Lei Orgânica.',
          'Decreto Legislativo.',
          'Veto Parcial.'
        ],
        ans: 0,
        exp: 'Gabarito A. INDICAÇÃO é a proposição em que o Vereador sugere aos Poderes competentes medidas de interesse público. Já a MOÇÃO manifesta aplauso, congratulação, protesto ou pesar; e o REQUERIMENTO pede informações ou providências à Mesa/Plenário.'
      },
      {
        num: 37, cat: 'esp', mat: 'Arquivologia • Métodos de Arquivamento',
        q: 'Quando o setor de arquivo da Câmara Municipal organiza os dossiês dos servidores utilizando como elemento principal o NOME de cada servidor, respeitando as regras de alfabetação, está utilizando o método básico de arquivamento:',
        opts: [
          'Alfabético (Nominal).',
          'Cronológico puro.',
          'Geográfico estadual.',
          'Duplex aleatório.'
        ],
        ans: 0,
        exp: 'Gabarito A. Quando o elemento principal de busca é o nome da pessoa física ou jurídica, adota-se o método Alfabético (sistema direto).'
      },
      {
        num: 38, cat: 'esp', mat: 'Direito Constitucional • Competência Legislativa Municipal (Art. 30 CF)',
        q: 'De acordo com o Art. 30, I e II da Constituição Federal de 1988, compete aos Municípios:',
        opts: [
          'Legislar sobre assuntos de interesse local e suplementar a legislação federal e a estadual no que couber.',
          'Legislar privativamente sobre direito penal, eleitoral e militar.',
          'Manter o serviço postal e o correio aéreo nacional.',
          'Declarar a guerra e celebrar a paz.'
        ],
        ans: 0,
        exp: 'Gabarito A. Art. 30, I e II da CF/88: Compete aos Municípios legislar sobre assuntos de interesse local e suplementar a legislação federal e a estadual no que couber.'
      },
      {
        num: 39, cat: 'esp', mat: 'Ética no Serviço Público • Conduta do Servidor da Câmara',
        q: 'No atendimento ao público e no exercício das atribuições do cargo de Técnico Legislativo na Câmara Municipal de Meruoca, constitui DEVER ético fundamental do servidor:',
        opts: [
          'Retardar o andamento de protocolos de cidadãos que pertençam a partidos de oposição.',
          'Exercer suas atribuições com presteza, urbanidade, cortesia, imparcialidade, zelo pela coisa pública e respeito à hierarquia legal.',
          'Valer-se do cargo para lograr proveito pessoal ou receber presentes e comissões de fornecedores.',
          'Divulgar informações sigilosas protegidas pela LGPD em redes sociais.'
        ],
        ans: 1,
        exp: 'Gabarito B. São deveres éticos essenciais do servidor: urbanidade, cortesia, presteza, imparcialidade (impessoalidade), probidade e lealdade às instituições.'
      },
      {
        num: 40, cat: 'esp', mat: 'Revisão Final • Raio-X Geral da Câmara de Meruoca',
        q: 'Assinale a alternativa que reúne APENAS informações 100% CORRETAS para você gabaritar a prova da Câmara Municipal de Meruoca amanhã:',
        opts: [
          'O parecer do TCE só cai por 2/3 da Câmara; a LOM exige 2 turnos (10 dias) e 2/3; a iniciativa popular exige 5% do eleitorado; as contas ficam 60 dias à disposição; e o limite de gasto com pessoal da Câmara na LRF é de 6% da RCL.',
          'O parecer do TCE cai por maioria simples; a LOM exige apenas 1 turno; e a Lei 14.133 ainda mantém a modalidade Convite.',
          'A Câmara pode gastar 90% da RCL com pessoal e o Prefeito tem 60 dias para sancionar projetos.',
          'O Judiciário pode revogar atos legítimos da Câmara por conveniência política.'
        ],
        ans: 0,
        exp: 'Gabarito A! Este é o resumo de ouro da sua aprovação: 2/3 para derrubar parecer do TCE e aprovar/emendar a LOM (2 turnos, 10 dias); 5% do eleitorado para iniciativa popular; 60 dias para exame das contas; e 6% da RCL na LRF (e 70% da receita da Câmara com folha)!'
      }
    ];
"""

with open("TUDO_OU_NADA_1HORA.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Atualizar os botões de navegação e seletor de rodadas para ter Rodada 3 (Ativa), Rodada 2 e Rodada 1
html = html.replace(
    """    .round-switcher {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 18px;
    }""",
    """    .round-switcher {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 10px;
      margin-bottom: 18px;
    }"""
)

old_nav = """    <div class="nav-tabs">
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
    </div>"""

new_nav = """    <div class="nav-tabs">
      <button class="tab-jump active" id="tabBtnR3" onclick="switchRound(3)">
        🏆 RODADA 3 FINAL (Blocos 13 a 20 + 40Q Fechamento)
      </button>
      <button class="tab-jump" id="tabBtnR2" onclick="switchRound(2)">
        🚀 RODADA 2 (Blocos 7 a 12 + 40Q)
      </button>
      <button class="tab-jump" id="tabBtnR1" onclick="switchRound(1)">
        🔥 RODADA 1 (Blocos 1 a 6 + 40Q)
      </button>
      <button class="tab-jump" onclick="scrollToSection('sec-questoes')">
        🎯 Ir p/ Questões
      </button>
      <button class="tab-jump" onclick="revealAllCurrentRound()">
        ⚡ Marcar Todas Certas
      </button>
    </div>"""

html = html.replace(old_nav, new_nav)

old_switcher = """    <!-- SELETOR DE RODADA -->
    <div class="round-switcher">
      <button type="button" class="round-btn active" id="bigBtnR2" onclick="switchRound(2)">
        <div>🚀 RODADA 2 INÉDITA (PARTE 2)</div>
        <span>6 Novos Blocos de Resumo + 40 Questões Novas</span>
      </button>
      <button type="button" class="round-btn" id="bigBtnR1" onclick="switchRound(1)">
        <div>🔥 RODADA 1 (PARTE 1 LIMPA)</div>
        <span>Blocos 1 a 6 (Sem códigos) + 40 Questões Base</span>
      </button>
    </div>"""

new_switcher = """    <!-- SELETOR DE RODADA -->
    <div class="round-switcher">
      <button type="button" class="round-btn active" id="bigBtnR3" onclick="switchRound(3)">
        <div>🏆 RODADA 3 FINAL (100% EDITAL)</div>
        <span>Últimos 8 Blocos (13 a 20) + 40 Questões Finais</span>
      </button>
      <button type="button" class="round-btn" id="bigBtnR2" onclick="switchRound(2)">
        <div>🚀 RODADA 2 (PARTE 2)</div>
        <span>Blocos 7 a 12 + 40 Questões Intermediárias</span>
      </button>
      <button type="button" class="round-btn" id="bigBtnR1" onclick="switchRound(1)">
        <div>🔥 RODADA 1 (PARTE 1)</div>
        <span>Blocos 1 a 6 + 40 Questões Base</span>
      </button>
    </div>"""

html = html.replace(old_switcher, new_switcher)

# 2. Inserir ROUND3_HTML antes de round2Content e ocultar round2Content inicialmente
html = html.replace(
    '<div id="round2Content">',
    ROUND3_HTML + '\n    <div id="round2Content" style="display: none;">'
)

# 3. Atualizar titulo inicial da secao de questoes
html = html.replace(
    '<h2 id="quizSectionTitle"><i class="fas fa-crosshairs"></i> SIMULADO RODADA 2 — 40 NOVAS QUESTÕES INÉDITAS</h2>',
    '<h2 id="quizSectionTitle"><i class="fas fa-trophy"></i> SIMULADO RODADA 3 FINAL — 40 QUESTÕES DE FECHAMENTO DO EDITAL</h2>'
)

# 4. Inserir QUESTIONS_R3_JS e atualizar logica JS para 3 rodadas
old_js_tail = """    let currentRound = 2; // Abre direto na Rodada 2 Nova!
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
    }"""

new_js_tail = QUESTIONS_R3_JS + """
    let currentRound = 3; // Abre direto na Rodada 3 Final (Blocos 13 a 20)!
    let choicesR1 = {};
    let choicesR2 = {};
    let choicesR3 = {};
    let currentFilterCat = 'all';

    function getActiveList() {
      if (currentRound === 3) return QUESTIONS_R3;
      if (currentRound === 2) return QUESTIONS_R2;
      return QUESTIONS_R1;
    }

    function getActiveChoices() {
      if (currentRound === 3) return choicesR3;
      if (currentRound === 2) return choicesR2;
      return choicesR1;
    }

    function switchRound(roundNum) {
      currentRound = roundNum;
      document.getElementById('round3Content').style.display = (roundNum === 3) ? 'block' : 'none';
      document.getElementById('round2Content').style.display = (roundNum === 2) ? 'block' : 'none';
      document.getElementById('round1Content').style.display = (roundNum === 1) ? 'block' : 'none';

      document.getElementById('bigBtnR3').classList.toggle('active', roundNum === 3);
      document.getElementById('bigBtnR2').classList.toggle('active', roundNum === 2);
      document.getElementById('bigBtnR1').classList.toggle('active', roundNum === 1);
      document.getElementById('tabBtnR3').classList.toggle('active', roundNum === 3);
      document.getElementById('tabBtnR2').classList.toggle('active', roundNum === 2);
      document.getElementById('tabBtnR1').classList.toggle('active', roundNum === 1);

      if (roundNum === 3) {
        document.getElementById('quizSectionTitle').innerHTML = '<i class="fas fa-trophy"></i> SIMULADO RODADA 3 FINAL — 40 QUESTÕES DE FECHAMENTO DO EDITAL';
      } else if (roundNum === 2) {
        document.getElementById('quizSectionTitle').innerHTML = '<i class="fas fa-crosshairs"></i> SIMULADO RODADA 2 — 40 QUESTÕES INTERMEDIÁRIAS';
      } else {
        document.getElementById('quizSectionTitle').innerHTML = '<i class="fas fa-crosshairs"></i> SIMULADO RODADA 1 — 40 QUESTÕES BASE';
      }

      updateLiveScore();
      renderQuestions();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }"""

html = html.replace(old_js_tail, new_js_tail)

html = html.replace(
    """    function resetCurrentRoundQuiz() {
      if (currentRound === 2) choicesR2 = {};
      else choicesR1 = {};
      updateLiveScore();
      renderQuestions();
    }""",
    """    function resetCurrentRoundQuiz() {
      if (currentRound === 3) choicesR3 = {};
      else if (currentRound === 2) choicesR2 = {};
      else choicesR1 = {};
      updateLiveScore();
      renderQuestions();
    }"""
)

with open("TUDO_OU_NADA_1HORA.html", "w", encoding="utf-8") as f:
    f.write(html)

with open(os.path.join("provas", "TUDO_OU_NADA_1HORA.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("[OK] Rodada 3 Final adicionada com sucesso! Total: 20 Blocos + 120 Questoes (100% do Edital)!")

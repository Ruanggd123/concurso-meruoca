import json

QUESTOES_S3_D3 = [
  {
  "id": 461,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Principios da Licitacao (Art. 5º): Rol Expresso",
  "question": "Conforme o Art. 5º da Lei nº 14.133/2021 (Nova Lei de Licitações e Contratos), na aplicação da lei serão observados, dentre outros, os princípios da:",
  "options": [
    "Legalidade, impessoalidade, moralidade, publicidade, eficiência, interesse público, probidade administrativa, igualdade, planejamento, transparência e segregação de funções.",
    "Legalidade, supremacia do interesse privado, moralidade seletiva, sigilo absoluto, eficiência presumida e concentração de funções.",
    "Publicidade restrita, pessoalidade, informalidade, julgamento subjetivo e sigilo das propostas após a adjudicação.",
    "Vinculação parcial ao edital, julgamento discricionário livre e dispensa de planejamento formal."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 5º da Lei 14.133/21: legalidade, impessoalidade, moralidade, publicidade, eficiência, interesse público, probidade administrativa, igualdade, planejamento, transparência, eficácia, segregação de funções, motivação, vinculação ao edital, julgamento objetivo, segurança jurídica, razoabilidade, competitividade, proporcionalidade, celeridade, economicidade e desenvolvimento nacional sustentável."
},
  {
  "id": 462,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Principio do Planejamento e Segregacao de Funcoes (Art. 5º)",
  "question": "A Lei nº 14.133/2021 elevou ao status de princípio expresso da licitação o planejamento e a segregação de funções. Sobre esses princípios, assinale a opção correta no padrão INBRASP:",
  "options": [
    "O planejamento é mera recomendação sem força normativa, podendo o gestor licitar sem qualquer estudo prévio.",
    "O planejamento impõe estudo técnico preliminar e termo de referência antes de licitar; a segregação de funções veda que o mesmo agente acumule autorização, execução e fiscalização do contrato.",
    "A segregação de funções autoriza que o pregoeiro adjudique, homologue, fiscalize e receba o objeto sozinho para dar celeridade.",
    "O planejamento aplica-se apenas a obras de grande vulto acima de R$ 100 milhões, sendo dispensado nas demais contratações."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 5º c/c Art. 7º, §1º e Art. 18 da Lei 14.133/21. Planejamento: fase preparatória obrigatória (ETP, TR, pesquisa de preços). Segregação de funções: princípio de controle interno que impede concentração de atribuições críticas no mesmo agente (quem autoriza não fiscaliza, quem licita não recebe)."
},
  {
  "id": 463,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Principios: Vinculacao ao Edital e Julgamento Objetivo",
  "question": "Quanto aos princípios da vinculação ao edital e do julgamento objetivo na Lei nº 14.133/2021, é correto afirmar que:",
  "options": [
    "A Administração pode alterar as regras do edital durante a sessão sem divulgar, desde que beneficie a proposta mais barata.",
    "O julgamento objetivo permite ao pregoeiro escolher a proposta por simpatia pessoal, desde que motive oralmente.",
    "A Administração está estritamente vinculada às regras do edital, e o julgamento das propostas deve ocorrer por critérios objetivos previamente definidos, vedado o subjetivismo.",
    "A vinculação ao edital obriga apenas os licitantes, não se aplicando à Administração Pública."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 5º da Lei 14.133/21. Vinculação ao edital: edital é a lei interna da licitação (vincula Administração e licitantes). Julgamento objetivo: critérios mensuráveis do edital (menor preço, técnica e preço etc.), vedada subjetividade. Pegadinha INBRASP: vincula AMBOS os lados, não só o particular."
},
  {
  "id": 464,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Principio da Publicidade e Transparencia vs Sigilo do Orcamento",
  "question": "A Lei nº 14.133/2021 consagra a publicidade e a transparência, mas admite o orçamento sigiloso. Sobre o tema, assinale a alternativa correta:",
  "options": [
    "Todo orçamento da licitação é obrigatoriamente sigiloso até a execução total do contrato, vedado qualquer acesso.",
    "A publicidade foi abolida na Nova Lei, sendo toda licitação sigilosa para garantir a competitividade.",
    "O orçamento sigiloso impede para sempre a divulgação dos quantitativos e do valor estimado, mesmo após a homologação.",
    "A regra é a publicidade dos atos; o sigilo do orçamento estimado é exceção facultativa, que deve ser justificado e será tornado público após o julgamento das propostas, sem prejuízo da divulgação do detalhamento dos quantitativos."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 13 e Art. 24 da Lei 14.133/21. Regra: publicidade no PNCP. Exceção: orçamento sigiloso (facultativo, justificado). Mesmo com sigilo do VALOR, os QUANTITATIVOS e demais informações do edital são públicos, e o valor sigiloso é revelado após o julgamento. Pegadinha: sigilo é do valor, não do edital inteiro."
},
  {
  "id": 465,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Agente de Contratacao e Pregoeiro (Art. 8º)",
  "question": "Nos termos do Art. 8º da Lei nº 14.133/2021, a condução da licitação na modalidade pregão e nas demais caberá, respectivamente, ao:",
  "options": [
    "Pregoeiro (no pregão) e ao agente de contratação (nas demais modalidades), ambos designados entre servidores efetivos ou empregados públicos do quadro permanente.",
    "Prefeito municipal em pessoa, vedada qualquer delegação a servidores.",
    "Leiloeiro oficial contratado em todos os casos, inclusive no pregão eletrônico.",
    "Vereador presidente da comissão de finanças, por ser autoridade política."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 8º da Lei 14.133/21: licitação conduzida por agente de contratação (regra) ou pregoeiro (quando pregão). Exigência: servidor efetivo/empregado público do quadro permanente. Podem ser auxiliados por equipe de apoio e, se necessário, por comissão de contratação (bens/serviços especiais)."
},
  {
  "id": 466,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Comissao de Contratacao (Art. 8º, §2º)",
  "question": "A comissão de contratação prevista na Lei nº 14.133/2021:",
  "options": [
    "É formada por 2 vereadores e 1 prefeito, atuando em todas as dispensas de pequeno valor.",
    "É formada por no mínimo 3 membros, sendo a maioria servidores efetivos, e atua em substituição ao agente de contratação nas licitações de bens ou serviços especiais.",
    "Substitui o Tribunal de Contas no julgamento das contas do Prefeito.",
    "É obrigatória em todo pregão eletrônico para bens comuns do dia a dia."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 8º, §2º da Lei 14.133/21. Comissão de contratação: mínimo 3 membros, maioria efetivos, substitui o agente de contratação em bens/serviços ESPECIAIS (complexos, não comuns). No pregão comum, atua o pregoeiro singular + equipe de apoio."
},
  {
  "id": 467,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Gestor e Fiscal do Contrato (Arts. 7º e 117)",
  "question": "Sobre a gestão e fiscalização dos contratos na Lei nº 14.133/2021, assinale a opção correta:",
  "options": [
    "A fiscalização do contrato é facultativa e pode ser dispensada verbalmente pelo prefeito.",
    "O contratado fiscaliza a si próprio, sendo vedada a designação de fiscal pela Câmara Municipal.",
    "A execução do contrato deve ser acompanhada e fiscalizada por representante da Administração (fiscal), permitida a contratação de terceiros para subsidiá-lo, sem que isso exclua a responsabilidade do fiscal.",
    "A contratação de terceiros para auxiliar a fiscalização transfere totalmente a responsabilidade ao particular, isentando o servidor."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Arts. 7º e 117 da Lei 14.133/21. Todo contrato tem gestor (coordena) e fiscal (acompanha execução, anota ocorrências, determina correção). Pode contratar terceiro para subsidiar (ex: laudo técnico), mas a responsabilidade do fiscal/gestor permanece. Pegadinha: terceirizar apoio NÃO terceiriza responsabilidade."
},
  {
  "id": 468,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Requisitos do Agente Publico: Capacitacao e Vedacao (Art. 7º)",
  "question": "O Art. 7º da Lei nº 14.133/2021 exige para o agente público designado atuar na licitação ou contrato que ele:",
  "options": [
    "Seja necessariamente bacharel em Direito com OAB ativa, independentemente do objeto licitado.",
    "Acumule as funções de agente de contratação, fiscal e pregoeiro no mesmo certame para economizar pessoal.",
    "Seja indicado por empresa licitante para garantir imparcialidade técnica.",
    "Tenha atribuições relacionadas a licitações e contratos ou formação compatível, não seja cônjuge/companheiro de licitante contratado habitual e não responda a penalidade funcional que vede sua atuação."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 7º da Lei 14.133/21: agente deve ter qualificação (atribuição do cargo ou capacitação), observar segregação de funções e impedimentos (parentesco com licitante, conflito de interesses). Não exige bacharelado em Direito como regra geral."
},
  {
  "id": 469,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Fase Preparatoria: ETP e Termo de Referencia (Art. 18)",
  "question": "Na fase preparatória do processo licitatório (Art. 18 da Lei nº 14.133/2021), o Estudo Técnico Preliminar (ETP) e o Termo de Referência (TR) destinam-se, respectivamente, a:",
  "options": [
    "O ETP a evidenciar o problema a resolver e a melhor solução (viabilidade técnica e econômica); o TR a detalhar o objeto, quantitativos, custos, prazos e critérios de seleção do fornecedor.",
    "O ETP a homologar o vencedor e o TR a empenhar a despesa sem previsão orçamentária.",
    "O ETP a substituir o edital e o TR a substituir o contrato administrativo.",
    "O ETP a dispensar a pesquisa de preços e o TR a vedar a definição de quantitativos."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 18, I e II da Lei 14.133/21. ETP = diagnóstico da necessidade + levantamento de soluções + viabilidade. TR (bens/serviços) / Projeto Básico (obras) = especificação completa para licitar: objeto, fundamentação, quantidades, estimativa de valor, modelo de execução, critérios de medição e pagamento."
},
  {
  "id": 470,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Pesquisa de Precos e Estimativa de Valor (Art. 23)",
  "question": "Para a estimativa do valor da contratação (Art. 23 da Lei nº 14.133/2021), a Administração deverá realizar pesquisa de preços observando, prioritariamente, os seguintes parâmetros:",
  "options": [
    "Apenas um orçamento por telefone com empresa indicada pelo prefeito, sem registro formal.",
    "Composição de custos unitários menores ou iguais à mediana do item no PNCP e contratações similares da Administração em execução ou concluídas no último ano.",
    "Preços de sites estrangeiros sem conversão cambial e sem data de referência.",
    "Valor aleatório fixado pelo pregoeiro no dia da sessão conforme sua intuição."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 23, §1º da Lei 14.133/21. Prioridade: 1) mediana do PNCP; 2) contratações similares públicas (último 1 ano). Parâmetros complementares: pesquisa direta com 3 fornecedores, mídia especializada, tabelas oficiais. Tudo deve ser documentado e criticado (desconsiderar inexequíveis/inconsistentes)."
},
  {
  "id": 471,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Inversao de Fases: Julgamento Antes da Habilitacao (Art. 17)",
  "question": "Uma das grandes novidades da Lei nº 14.133/2021 em relação à antiga Lei nº 8.666/93 é a sequência das fases da licitação. Como regra geral (Art. 17), a ordem é:",
  "options": [
    "Habilitação de todos, depois julgamento, depois edital, depois homologação antes da fase preparatória.",
    "Homologação primeiro, depois julgamento, dispensada a habilitação em qualquer caso.",
    "Preparatória, divulgação do edital, apresentação de propostas, julgamento, habilitação, recursal e homologação — ou seja, primeiro julgam-se as propostas e só depois se habilita o vencedor.",
    "Apresentação de propostas após a assinatura do contrato, invertendo toda a lógica."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 17 da Lei 14.133/21. Inversão de fases como REGRA: julga propostas/lances primeiro, habilita SÓ o primeiro colocado (economia processual). Na Lei 8.666/93 a regra era inversa (habilitava todos antes). Exceção: edital pode prever habilitação antecedente em casos justificados (Art. 17, §1º)."
},
  {
  "id": 472,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Edital e PNCP: Divulgacao Obrigatoria (Arts. 54-55)",
  "question": "Sobre a divulgação do edital na Lei nº 14.133/2021, assinale a alternativa correta:",
  "options": [
    "Basta afixar o edital no mural da Câmara, vedada a divulgação eletrônica.",
    "O PNCP foi extinto pela Nova Lei, voltando a publicação apenas em Diário Oficial impresso.",
    "O prazo mínimo entre edital e propostas é sempre de 24 horas, qualquer que seja a modalidade.",
    "A publicidade do edital será feita mediante divulgação no Portal Nacional de Contratações Públicas (PNCP), sendo obrigatória, além disso, em jornal diário de grande circulação apenas nos casos de concorrência de grande vulto."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Arts. 54-55 da Lei 14.133/21. PNCP é o sítio oficial centralizado e obrigatório. Prazos mínimos variam por modalidade/critério (ex: 10 dias úteis para pregão menor preço bens comuns; 25 dias para concorrência técnica). Pegadinha INBRASP: não é prazo único, e PNCP é obrigatório."
},
  {
  "id": 473,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Rol Taxativo das Modalidades (Art. 28)",
  "question": "São modalidades de licitação previstas no Art. 28 da Lei nº 14.133/2021:",
  "options": [
    "Pregão, concorrência, concurso, leilão e diálogo competitivo.",
    "Pregão, concorrência, tomada de preços, convite e concurso.",
    "Concorrência, convite, leilão, carta-convite e chamada pública genérica.",
    "Pregão, tomada de preços, convite, RDC e credenciamento como modalidade."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 28 da Lei 14.133/21: rol TAXATIVO de 5 modalidades: Pregão, Concorrência, Concurso, Leilão e Diálogo Competitivo. EXTINTAS: Tomada de Preços e Convite (da Lei 8.666/93). Credenciamento, pré-qualificação e SRP são PROCEDIMENTOS AUXILIARES (Art. 78), não modalidades."
},
  {
  "id": 474,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Pregao vs Concorrencia: Objeto",
  "question": "A diferença essencial de objeto entre pregão e concorrência na Lei nº 14.133/2021 é que:",
  "options": [
    "O pregão destina-se apenas a obras bilionárias e a concorrência apenas a compras de café e papel.",
    "O pregão destina-se a bens e serviços COMUNS (padrões objetivos de mercado); a concorrência destina-se a bens/serviços ESPECIAIS e a obras e serviços de engenharia.",
    "Ambos destinam-se exclusivamente a serviços técnicos intelectuais com concurso de beleza.",
    "O pregão foi extinto e só existe concorrência na Nova Lei."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 6º, XIII/XIV e Art. 29 da Lei 14.133/21. Bem/serviço COMUM = especificação usual de mercado (pregão obrigatório para o comum). Bem/serviço ESPECIAL ou obra/engenharia = concorrência. Pegadinha: pregão NÃO é definido por valor, mas pela NATUREZA comum do objeto."
},
  {
  "id": 475,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Concurso e Leilao: Conceitos",
  "question": "Na Lei nº 14.133/2021, as modalidades concurso e leilão destinam-se, respectivamente, a:",
  "options": [
    "Compra de bens comuns por menor preço e contratação de obras por técnica e preço.",
    "Alienação de bens e escolha de trabalho artístico de forma invertida (leilão premia tese e concurso vende sucata).",
    "Escolha de trabalho técnico, científico ou artístico (com prêmio/remuneração) e alienação de bens móveis inservíveis ou imóveis (quem oferecer maior lance).",
    "Contratação de empréstimos internacionais e venda de ações em bolsa."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 30 (Concurso) e Art. 31 (Leilão) da Lei 14.133/21. Concurso: seleção intelectual/artística com prêmio (ex: projeto arquitetônico). Leilão: venda de bens (móveis inservíveis, apreendidos, imóveis) ao maior lance. Não confundir concurso-licitação com concurso público de pessoal."
},
  {
  "id": 476,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Dialogo Competitivo: Hipoteses",
  "question": "O diálogo competitivo, novidade da Lei nº 14.133/2021, é cabível quando:",
  "options": [
    "A Administração quer comprar papel A4 e canetas de forma mais rápida, sem edital.",
    "O prefeito quer conversar informalmente com um amigo empresário para dispensar a licitação.",
    "Em toda compra de bens comuns de prateleira para simplificar o pregão.",
    "A Administração visa contratar objeto com inovação tecnológica ou técnica, ou quando não consegue definir com precisão as especificações, necessitando dialogar com licitantes pré-selecionados para desenvolver a solução."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 32 da Lei 14.133/21. Diálogo competitivo: objeto complexo/inovador (ex: solução de TI inédita, obra com tecnologia nova). Fases: pré-seleção, diálogo para definir solução, apresentação de propostas finais. Vedado para bens comuns simples."
},
  {
  "id": 477,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Modalidades Extintas: Tomada de Precos e Convite",
  "question": "Sobre as antigas modalidades tomada de preços e convite (Lei nº 8.666/93) diante da Lei nº 14.133/2021, é correto afirmar que:",
  "options": [
    "Foram expressamente extintas; os processos devem usar pregão, concorrência, concurso, leilão ou diálogo competitivo, observados os novos limites de dispensa por valor.",
    "Continuam vigentes como 6ª e 7ª modalidades da Nova Lei, ao lado do diálogo competitivo.",
    "Foram mantidas apenas para municípios com menos de 20 mil habitantes como Meruoca.",
    "Foram fundidas em uma só chamada credenciamento-convite, ainda por valor."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. A Lei 14.133/21 revogou a Lei 8.666/93 e extinguiu tomada de preços e convite. O critério de valor agora define DISPENSA (Art. 75, I e II: R$ 119 mil obras/engenharia e R$ 59 mil outros — valores atualizados por decreto), não mais modalidade. Pegadinha favorita INBRASP."
},
  {
  "id": 478,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Criterios de Julgamento: Rol (Art. 33)",
  "question": "O Art. 33 da Lei nº 14.133/2021 prevê como critérios de julgamento das propostas:",
  "options": [
    "Menor preço, melhor simpatia, maior tempo de amizade e menor distância da prefeitura.",
    "Menor preço, maior desconto, melhor técnica ou conteúdo artístico, técnica e preço, maior lance (leilão) e maior retorno econômico.",
    "Apenas menor preço, vedado qualquer outro critério na Nova Lei.",
    "Sorteio público como critério autônomo de julgamento."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 33 da Lei 14.133/21, I a VI. Maior desconto incide sobre tabela referencial. Maior lance só no leilão. Maior retorno econômico: economia gerada à Administração (ex: contrato de eficiência energética). Sorteio só como DESEMPATE, não critério."
},
  {
  "id": 479,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Maior Desconto e Maior Retorno Economico",
  "question": "Quanto aos critérios maior desconto e maior retorno econômico na Lei nº 14.133/2021, assinale a correta:",
  "options": [
    "Maior desconto é sorteio entre preços iguais e maior retorno é promessa verbal de economia.",
    "Ambos são vedados para obras e só valem para concurso artístico.",
    "Maior desconto toma por base preço de referência/tabela (vence quem dá maior percentual de desconto); maior retorno econômico considera a economia futura gerada à Administração, com remuneração do contratado vinculada a esse ganho.",
    "Maior retorno econômico dispensa medição da economia real, bastando declaração do licitante."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Arts. 34 e 39 da Lei 14.133/21. Maior desconto: comum em registro de preços/passagens (ex: 15% sobre tabela SINAPI). Maior retorno: contrato de eficiência (ex: empresa troca iluminação pública e recebe % da conta de luz economizada). Exige aferição objetiva da economia."
},
  {
  "id": 480,
  "category": "administrativo",
  "day": "w3_d3",
  "discipline": "Lei 14.133/2021",
  "topic": "Tecnica e Preco: Quando Usar",
  "question": "O critério técnica e preço (Art. 35 da Lei nº 14.133/2021) é adequado para:",
  "options": [
    "Compra de bens comuns de prateleira, onde só o preço importa.",
    "Alienação de sucatas, onde vence o maior lance.",
    "Toda e qualquer contratação, a critério livre do pregoeiro sem previsão no edital.",
    "Serviços técnicos especializados de natureza predominantemente intelectual (estudos, projetos, pareceres), quando a qualidade técnica é relevante além do preço, mediante ponderação objetiva no edital."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 35 da Lei 14.133/21. Técnica e preço: ponderação (ex: 60% técnica + 40% preço) definida no edital para serviços intelectuais. Para bens comuns usa-se menor preço/maior desconto. Exige critérios objetivos de pontuação técnica."
},
  {
  "id": 481,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "Internet vs Intranet vs Extranet",
  "question": "Quanto aos conceitos de Internet, Intranet e Extranet, cobrados no padrão INBRASP, assinale a alternativa correta:",
  "options": [
    "Internet é a rede mundial pública; Intranet é a rede privada interna de uma organização (ex: Câmara de Meruoca) com acesso restrito; Extranet é a extensão controlada da Intranet para parceiros externos via login.",
    "Internet e Intranet são sinônimos, ambas públicas e sem controle de acesso.",
    "Intranet é mundial e pública, enquanto a Internet é restrita aos servidores da Câmara.",
    "Extranet é a internet via satélite e Intranet é a internet discada antiga."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Internet = pública mundial (TCP/IP). Intranet = privada corporativa (mesmos protocolos, acesso interno). Extranet = Intranet estendida a fornecedores/parceiros com autenticação (ex: portal do fornecedor da Câmara). Pegadinha: todas usam TCP/IP, o que muda é o alcance/controle."
},
  {
  "id": 482,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "Navegadores: Chrome, Edge e Firefox",
  "question": "Sobre os navegadores Google Chrome, Microsoft Edge e Mozilla Firefox, é correto afirmar que:",
  "options": [
    "São sistemas operacionais que substituem o Windows 11 e o Ubuntu Linux.",
    "São aplicativos de navegação na web que permitem acessar sites, gerenciar abas, favoritos, histórico e extensões, sendo todos citados no edital de Meruoca.",
    "São antivírus gratuitos que removem ransomware sem atualização.",
    "São editores de planilhas que calculam fórmulas SE e PROCV."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Edital 2.2: aplicativos de navegação (Edge, Firefox, Chrome). Funções comuns: abas, favoritos, histórico, downloads, modo anônimo, sincronização, extensões. Não são SO nem antivírus. Edge é padrão do Windows 11 (base Chromium, mesmo motor do Chrome)."
},
  {
  "id": 483,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "Pesquisa Avancada: Operadores de Busca",
  "question": "Um Técnico Legislativo precisa pesquisar no Google apenas páginas do site oficial da Câmara que mencionem Lei Orgânica, excluindo notícias de 2020. A sintaxe mais eficiente é:",
  "options": [
    "www.google-Lei Orgânica +2020 +todas",
    "pesquisar Lei Orgânica sem aspas e sem filtros para trazer tudo",
    "site:meruoca.ce.gov.br \"Lei Orgânica\" -2020",
    "inurl:senha + anexar CPF na busca para refinar"
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Operadores: site: restringe ao domínio; \" \" busca expressão exata; - exclui termo; OR amplia. Ex: site:meruoca.ce.gov.br \"Lei Orgânica\" -2020. Pegadinha INBRASP: jamais digitar dados pessoais na busca; usar aspas para exatidão."
},
  {
  "id": 484,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "Protocolos: HTTP vs HTTPS",
  "question": "Ao acessar o portal da Câmara para consultar um edital, o cadeado do navegador indica HTTPS. A diferença entre HTTP e HTTPS é que:",
  "options": [
    "HTTP é seguro e HTTPS é inseguro e deve ser evitado em sites públicos.",
    "Ambos são antivírus, sem diferença prática para o usuário.",
    "HTTPS funciona apenas sem internet, de forma offline.",
    "HTTPS é o HTTP com camada de segurança (TLS/SSL) que criptografa os dados entre navegador e servidor, garantindo confidencialidade e autenticidade."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. HTTP (porta 80) = texto puro; HTTPS (porta 443) = HTTP + TLS/SSL com criptografia e certificado digital. Cadeado = conexão segura. Regra INBRASP: nunca digitar senha em site só-HTTP."
},
  {
  "id": 485,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "DNS, IP e FTP",
  "question": "Relacione: 1-DNS 2-Endereço IP 3-FTP. ( ) Traduz nomes (ex: meruoca.ce.gov.br) em números. ( ) Identifica cada dispositivo na rede. ( ) Transfere arquivos entre computadores. A sequência correta é:",
  "options": [
    "1 — 2 — 3",
    "3 — 2 — 1",
    "2 — 1 — 3",
    "1 — 3 — 2"
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. DNS (Domain Name System) = agenda telefônica da internet (nome -> IP). IP = identidade numérica (ex: 192.168.0.10 ou IPv6). FTP (File Transfer Protocol, porta 21) = envio/recebimento de arquivos. SFTP/FTPS são versões seguras."
},
  {
  "id": 486,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "Redes LAN, WAN e Wi-Fi",
  "question": "A rede cabeada dos gabinetes da Câmara (alcance local) e a internet que liga Meruoca a Fortaleza classificam-se, respectivamente, como:",
  "options": [
    "WAN e LAN, invertidas, sendo Wi-Fi um tipo de cabo submarino.",
    "LAN (Local Area Network) e WAN (Wide Area Network); o acesso sem fio nessa LAN pode ser via Wi-Fi (padrão IEEE 802.11).",
    "Ambas PAN, restritas a 10 cm de alcance via Bluetooth apenas.",
    "MAN e Bluetooth, sem relação com LAN/WAN."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. LAN = curta distância (sala/prédio, ex: rede da Câmara). MAN = cidade/região. WAN = longa distância (ex: Meruoca-Fortaleza, internet). Wi-Fi = LAN sem fio (802.11 a/b/g/n/ac/ax). Pegadinha: Wi-Fi não é internet, é a forma de acesso à rede."
},
  {
  "id": 487,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "E-mail vs Mensageria: Conceitos",
  "question": "Embora o edital cite correio eletrônico e mensageria (WhatsApp/Telegram), a diferença técnica fundamental é que:",
  "options": [
    "E-mail e WhatsApp são idênticos e usam os mesmos protocolos SMTP/IMAP.",
    "E-mail dispensa endereço e mensageria exige carta registrada.",
    "O e-mail usa endereço eletrônico com @ e protocolos SMTP (envio) / IMAP-POP (recebimento), é assíncrono e formal; a mensageria instantânea é síncrona/quase imediata via apps com conta vinculada a número/conta.",
    "Mensageria é formal e oficial, e e-mail é sempre informal e sem validade."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. E-mail: endereço usuario@dominio, SMTP porta 25/587 envia, IMAP (143/993) mantém no servidor, POP3 (110/995) baixa. Mensageria (WhatsApp/Telegram/Discord): entrega instantânea, confirmação de leitura, grupos. No setor público, e-mail institucional (ex: Thunderbird/webmail) tem valor formal; WhatsApp é ágil mas exige cautela probatória."
},
  {
  "id": 488,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "URL: Partes do Endereco Web",
  "question": "Na URL https://www.meruoca.ce.gov.br:443/portal/editais?q=001#art1, o trecho https, www.meruoca.ce.gov.br e /portal/editais correspondem, respectivamente, a:",
  "options": [
    "Domínio, protocolo e senha de acesso.",
    "Caminho, protocolo e IP reverso.",
    "Antivírus, firewall e backup.",
    "Protocolo, domínio (host) e caminho/recurso no servidor."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. URL = protocolo://domínio:porta/caminho?consulta#fragmento. https = protocolo seguro; www.meruoca.ce.gov.br = domínio/host (br=comercial-país? na verdade .gov.br governamental + .ce estadual); :443 = porta HTTPS; /portal/editais = caminho; ?q=001 = query; #art1 = âncora/fragmento."
},
  {
  "id": 489,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "Redes Sociais e Grupos de Discussao: Uso Seguro",
  "question": "O edital exige noções de redes sociais e grupos de discussão. No uso corporativo na Câmara, a conduta SEGURA é:",
  "options": [
    "Verificar a fonte antes de compartilhar, não publicar dados pessoais/sigilosos de processos e desconfiar de links com promessas milagrosas (phishing).",
    "Compartilhar senhas da intranet nos grupos para agilizar o trabalho.",
    "Publicar fotos de documentos internos sigilosos para provar produtividade.",
    "Clicar em todo link recebido no grupo sem verificar o remetente."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Segurança em redes/grupos: checar fonte, não expor dados pessoais (LGPD), não compartilhar credenciais, desconfiar de phishing/boato. Grupos (WhatsApp/Telegram/Discord) e redes (Instagram/Facebook) são vetores de engenharia social mais explorados em prova INBRASP."
},
  {
  "id": 490,
  "category": "informatica",
  "day": "w3_d3",
  "discipline": "Informática",
  "topic": "TCP-IP e Conexao: Pacotes e Roteador",
  "question": "Quando um servidor da Câmara acessa um edital no site do INBRASP, os dados trafegam pela internet via TCP/IP. Nesse modelo, é correto afirmar que:",
  "options": [
    "O TCP é o cabo físico e o IP é o monitor do computador.",
    "O TCP divide os dados em pacotes, garante entrega ordenada e sem erro; o IP endereça e roteia cada pacote até o destino, onde são remontados.",
    "Os dados vão inteiros sem divisão, dispensando roteadores.",
    "TCP/IP funciona apenas em intranet offline, nunca na internet pública."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Pilha TCP/IP: IP (camada rede) endereça/encaminha; TCP (camada transporte) fragmenta, numera, controla fluxo, retransmite perdidos e remonta em ordem. Roteador escolhe o melhor caminho por pacote. É a base da Internet/Intranet citada no edital."
}
]

print(f"[OK] Total de questões S3/D3 geradas: {len(QUESTOES_S3_D3)}")

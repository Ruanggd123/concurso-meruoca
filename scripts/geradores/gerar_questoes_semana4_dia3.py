# -*- coding: utf-8 -*-
import json
import re

QUESTOES_S4_D3 = [
  # =========================================================================
  # ORÇAMENTO PÚBLICO — PPA, LDO, LOA E PRINCÍPIOS (CF/88 E LEI 4.320/64)
  # QUESTÕES 613 A 622 (10 QUESTÕES)
  # =========================================================================
  {
    "id": 613,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Princípio da Exclusividade (CF/88, Art. 165, § 8º)",
    "question": "O princípio orçamentário da exclusividade estabelece que a Lei Orçamentária Anual não conterá dispositivo estranho à previsão da receita e à fixação da despesa. Contudo, a própria Constituição Federal de 1988 ressalva expressamente da proibição:",
    "options": [
      "A criação de cargos públicos e a concessão de reajustes salariais para os servidores do Poder Executivo.",
      "A autorização para a abertura de créditos suplementares e contratação de operações de crédito, ainda que por antecipação de receita.",
      "A fixação dos subsídios dos vereadores e do prefeito para a legislatura subsequente.",
      "A alteração das alíquotas de tributos municipais para cobrir eventuais déficits orçamentários."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 165, § 8º da CF/88: 'A lei orçamentária anual não conterá dispositivo estranho à previsão da receita e à fixação da despesa, não se incluindo na proibição a autorização para abertura de créditos suplementares e contratação de operações de crédito, ainda que por antecipação de receita, nos termos da lei.' Essa é a clássica exceção ao princípio da exclusividade cobrada pela INBRASP."
  },
  {
    "id": 614,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Princípio da Universalidade e Orçamento Bruto (Lei 4.320/64)",
    "question": "O princípio orçamentário segundo o qual a Lei Orçamentária Anual deve computar a totalidade das receitas e a totalidade das despesas de todos os órgãos e poderes da administração pública, vedadas quaisquer deduções prévias, denomina-se:",
    "options": [
      "Princípio da Universalidade (orçamento bruto).",
      "Princípio da Não Afetação de Receitas.",
      "Princípio da Especificação ou Especialização.",
      "Princípio da Publicidade e Transparência."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 2º da Lei nº 4.320/1964 e Art. 165, § 5º da CF/88. Pelo princípio da universalidade (regra do orçamento bruto), todas as receitas e despesas devem constar no orçamento pelos seus valores brutos, sem qualquer dedução, impedindo caixas paralelas ou ocultação de operações financeiras."
  },
  {
    "id": 615,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Princípio da Anualidade ou Periodicidade",
    "question": "Em relação ao princípio orçamentário da anualidade ou periodicidade, é CORRETO afirmar que no âmbito da administração pública brasileira:",
    "options": [
      "O orçamento tem validade indeterminada, vigorando até que novo projeto seja sancionado pelo Executivo.",
      "O exercício financeiro coincide com o ano civil, tendo início em 1º de janeiro e encerramento em 31 de dezembro.",
      "O exercício financeiro municipal tem duração obrigatória de dois anos para coincidir com a renovação da Mesa Diretora.",
      "O orçamento municipal possui período de vigência definido livremente por decreto anual do Prefeito."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 34 da Lei nº 4.320/1964: 'O exercício financeiro coincidirá com o ano civil' (1º de janeiro a 31 de dezembro). O princípio da anualidade exige que as estimativas de receita e fixações de despesa sejam delimitadas temporalmente para um período de um ano."
  },
  {
    "id": 616,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Plano Plurianual - PPA: Conteúdo e Diretrizes (CF/88)",
    "question": "Conforme preceitua o Art. 165, § 1º da Constituição Federal de 1988, a lei que instituir o Plano Plurianual (PPA) estabelecerá, de forma regionalizada:",
    "options": [
      "A relação completa de todas as compras e contratações diretas por dispensa do exercício seguinte.",
      "As diretrizes, objetivos e metas da administração pública para as despesas de capital e outras delas decorrentes e para as relativas aos programas de duração continuada.",
      "Os índices e metas de inflação para a cobrança do IPTU e do ISS no município.",
      "A tabela remuneratória exclusiva dos cargos em comissão da Câmara de Vereadores."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 165, § 1º da CF/88: 'A lei que instituir o plano plurianual estabelecerá, de forma regionalizada, as diretrizes, objetivos e metas da administração pública federal para as despesas de capital e outras delas decorrentes e para as relativas aos programas de duração continuada.' Mnemônico clássico da banca: D-O-M (Diretrizes, Objetivos e Metas)."
  },
  {
    "id": 617,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Vigência e Continuidade do PPA",
    "question": "O Plano Plurianual (PPA) possui vigência de quatro anos. Com o objetivo constitucional de assegurar a continuidade administrativa das políticas públicas planejadas entre mandatos de governos distintos, a vigência do PPA:",
    "options": [
      "Coincide com os quatro anos de mandato do Prefeito, iniciando em 1º de janeiro do primeiro ano e terminando no último dia do mandato.",
      "Inicia-se no segundo ano do mandato do chefe do Poder Executivo e vigora até o término do primeiro ano do mandato subsequente.",
      "Inicia-se no último ano do mandato e vigora pelos quatro anos da administração seguinte.",
      "Tem vigência de apenas dois anos, sendo obrigatória a elaboração de dois PPAs para cada mandato municipal."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. ADCT, art. 35, § 2º, I da CF/88. O projeto de PPA é enviado pelo Prefeito até 31 de agosto do seu 1º ano de mandato, é votado e entra em vigor no 2º ano de mandato (1º de janeiro), estendendo-se até o final do 1º ano do mandato seguinte. Isso garante a continuidade do planejamento público."
  },
  {
    "id": 618,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Lei de Diretrizes Orçamentárias - LDO (CF/88 e LRF)",
    "question": "A Lei de Diretrizes Orçamentárias (LDO) atua como elo orientador entre o PPA e a LOA. Dentre as atribuições conferidas à LDO pela Constituição Federal e pela Lei de Responsabilidade Fiscal (LRF), destaca-se:",
    "options": [
      "Compreender as metas e prioridades da administração pública, orientar a elaboração da LOA e dispor sobre alterações na legislação tributária, contendo o Anexo de Metas Fiscais.",
      "Autorizar a execução direta de todas as obras municipais sem necessidade de prévia licitação.",
      "Aprovar as contas de gestão do Prefeito antes do julgamento do Tribunal de Contas.",
      "Fixar as alíquotas do imposto de renda e da contribuição previdenciária de competência da União."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 165, § 2º da CF/88 e Art. 4º da LRF (LC 101/2000). A LDO traça as prioridades do exercício subsequente, direciona a elaboração da LOA, dispõe sobre alterações na legislação tributária e traz o Anexo de Metas Fiscais e o Anexo de Riscos Fiscais."
  },
  {
    "id": 619,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Estrutura da LOA: Orçamentos Fiscal, Seguridade e Investimento",
    "question": "De acordo com o Art. 165, § 5º da Constituição Federal de 1988, a Lei Orçamentária Anual (LOA) é estruturada em três esferas orçamentárias integradas, que são:",
    "options": [
      "O orçamento ordinário, o orçamento extraordinário e o orçamento suplementar.",
      "O orçamento fiscal, o orçamento de investimento das estatais e o orçamento da seguridade social.",
      "O orçamento de custeio, o orçamento da dívida consolidada e o orçamento patrimonial.",
      "O orçamento legislativo, o orçamento executivo e o orçamento judiciário autônomo."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 165, § 5º da CF/88: A LOA compreende: I - o orçamento fiscal (poderes, órgãos e fundos); II - o orçamento de investimento das empresas em que o ente detenha a maioria do capital social com direito a voto; III - o orçamento da seguridade social (saúde, previdência e assistência social)."
  },
  {
    "id": 620,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Princípio da Não Afetação / Não Vinculação de Impostos (CF/88)",
    "question": "O princípio constitucional da não afetação (ou não vinculação) da receita proíbe a vinculação prévia a órgão, fundo ou despesa. Contudo, nos termos do Art. 167, IV da CF/88, essa vedação aplica-se expressa e restritivamente à receita de:",
    "options": [
      "Taxas decorrentes do exercício regular do poder de polícia.",
      "Contribuições de melhoria por valorização imobiliária de obras públicas.",
      "Impostos, ressalvadas as exceções expressas na CF (como saúde, educação e garantias).",
      "Preços públicos e tarifas cobradas por concessionárias de transporte."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 167, IV da CF/88: É vedada 'a vinculação de receita de IMPOSTOS a órgão, fundo ou despesa', ressalvadas as repartições constitucionais, as parcelas da saúde (15% municípios), da educação (25%), garantias a operações de crédito, etc. A banca INBRASP costuma colocar 'tributos' para induzir o candidato ao erro, pois a vedação atinge apenas os IMPOSTOS."
  },
  {
    "id": 621,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Emendas Parlamentares ao Projeto de LOA (CF/88, Art. 166)",
    "question": "Na tramitação do projeto de Lei Orçamentária Anual na Câmara Municipal, os vereadores têm o direito de apresentar emendas parlamentares. Para serem aprovadas, as emendas individuais ou de bancada que indiquem recursos devem:",
    "options": [
      "Ser compatíveis com o PPA e com a LDO, e indicar recursos provenientes de anulação de despesas, excluídas as dotações para pessoal e encargos da dívida.",
      "Determinar a anulação integral das dotações destinadas à folha salarial dos servidores públicos efetivos.",
      "Indicar como fonte financeira empréstimos particulares a serem contratados diretamente pelos vereadores.",
      "Dispensar a compatibilidade com o PPA desde que aprovadas por metade dos membros presentes."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 166, § 3º da CF/88: As emendas ao projeto de lei do orçamento anual devem: I - ser compatíveis com o PPA e com a LDO; II - indicar os recursos necessários, admitidos apenas os provenientes de anulação de despesa, EXCLUÍDAS as que incidam sobre: a) dotações para pessoal e seus encargos; b) serviço da dívida."
  },
  {
    "id": 622,
    "category": "especificos",
    "day": "w4_d3",
    "discipline": "Orçamento Público",
    "topic": "Créditos Adicionais: Suplementares, Especiais e Extraordinários",
    "question": "Durante o ano financeiro, o Poder Executivo constata a necessidade de realizar despesa pública urgente e imprevisível, decorrente de grave calamidade pública provocada por fortes chuvas no município. De acordo com a Lei nº 4.320/1964 e a CF/88, deve ser aberto crédito adicional do tipo:",
    "options": [
      "Crédito Suplementar, destinado ao reforço de dotação já contemplada na LOA.",
      "Crédito Especial, que depende de autorização prévia por lei ordinária e dotação genérica.",
      "Crédito Extraordinário, aberto por medida provisória ou decreto do Executivo para despesas urgentes e imprevisíveis (guerra, comoção ou calamidade).",
      "Crédito Remanescente, criado unicamente ao término da legislatura para pagamento de restos a pagar."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Arts. 41, III e 44 da Lei nº 4.320/64 c/c Art. 167, § 3º da CF/88. Os créditos extraordinários destinam-se a despesas urgentes e imprevistas, em caso de guerra, comoção interna ou calamidade pública. Diferem dos suplementares (reforço) e especiais (nova despesa sem dotação na LOA)."
  },

  # =========================================================================
  # INFORMÁTICA — COMUNICAÇÃO DIGITAL, E-MAIL, PROTOCOLOS E COLABORAÇÃO
  # QUESTÕES 623 A 630 (8 QUESTÕES)
  # =========================================================================
  {
    "id": 623,
    "category": "informatica",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Correio Eletrônico: Campos Para, Cc e Cco",
    "question": "Ao redigir uma mensagem de correio eletrônico institucional, um servidor insere o endereço de Ana no campo 'Para', o endereço de Bruno no campo 'Cc' e o endereço de Carlos no campo 'Cco'. A respeito da visibilidade dos endereços para os destinatários, é CORRETO afirmar que:",
    "options": [
      "Ana e Bruno poderão visualizar que Carlos recebeu uma cópia da mensagem.",
      "Carlos poderá ver que a mensagem foi enviada para Ana e com cópia para Bruno, mas Ana e Bruno não saberão que Carlos recebeu a mensagem.",
      "O endereço de Ana fica oculto para todos os destinatários da mensagem.",
      "Bruno não recebe a mensagem se Carlos estiver listado no campo de cópia oculta."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O campo Cco (Com Cópia Oculta / Bcc) oculta o endereço de Carlos de todos os demais destinatários (Para e Cc). Carlos, ao receber o e-mail, vê perfeitamente quem estava em Para (Ana) e Cc (Bruno), mas ninguém além do remetente sabe que Carlos recebeu o e-mail."
  },
  {
    "id": 624,
    "category": "informatica",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Protocolo SMTP (Simple Mail Transfer Protocol)",
    "question": "No modelo de comunicação de correio eletrônico pela internet, o protocolo da camada de aplicação responsável especificamente pela transmissão/saída (envio) de mensagens do cliente para o servidor e entre servidores de e-mail é o:",
    "options": [
      "POP3 (Post Office Protocol v3).",
      "IMAP (Internet Message Access Protocol).",
      "SMTP (Simple Mail Transfer Protocol).",
      "DHCP (Dynamic Host Configuration Protocol)."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O SMTP (Simple Mail Transfer Protocol) é o protocolo padrão para ENVIO de e-mails. Mnemônico para não esquecer na prova: 'Sua Mensagem Tá Partindo' (SMTP). Os protocolos POP3 e IMAP são utilizados para recebimento/leitura de mensagens."
  },
  {
    "id": 625,
    "category": "informatica",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Protocolos de Recebimento: POP3 vs IMAP",
    "question": "Ao configurar uma conta de correio eletrônico, o usuário deve escolher entre os protocolos de recebimento POP3 e IMAP. A distinção fundamental entre ambos reside no fato de que:",
    "options": [
      "O POP3 sincroniza automaticamente as pastas no servidor em tempo real em todos os dispositivos móveis.",
      "O IMAP mantém as mensagens e pastas armazenadas e sincronizadas no servidor permitindo o acesso simultâneo de múltiplos dispositivos, enquanto o POP3 transfere as mensagens para o computador local e, por padrão, as exclui do servidor.",
      "O POP3 funciona exclusivamente através de navegadores web (webmail) e o IMAP requer conexão física via cabo serial.",
      "O IMAP é um protocolo de envio seguro com assinatura digital e o POP3 serve para compactar arquivos ZIP."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O POP3 descarrega (baixa) as mensagens para o computador local e remove do servidor por padrão. O IMAP mantém as mensagens no servidor, sincronizando o status de lido/não lido e as pastas em tempo real entre celular, notebook e webmail."
  },
  {
    "id": 626,
    "category": "informatica",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Portas Padrão de E-mail (SMTP 587)",
    "question": "No Brasil, para evitar a propagação de spams e garantir a autenticação de remetentes, a porta padrão recomendada pelos provedores e pela internet para o envio de e-mails de clientes locais via protocolo SMTP com criptografia STARTTLS é a porta:",
    "options": [
      "Porta 587.",
      "Porta 80.",
      "Porta 21.",
      "Porta 110."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A porta 587 (Submission / SMTP autenticado com STARTTLS) substituiu a porta 25 no Brasil para envio de e-mails por usuários finais. A porta 110 é do POP3 sem SSL, a porta 80 é do HTTP comum e a porta 21 é do FTP."
  },
  {
    "id": 627,
    "category": "informatica",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Mozilla Thunderbird: Recursos e Configuração",
    "question": "O Mozilla Thunderbird é um aplicativo de correio eletrônico amplamente empregado na administração pública. A respeito das características do Thunderbird, é CORRETO afirmar:",
    "options": [
      "É um software pago de código fechado que só opera integrado ao sistema operacional Windows 11.",
      "É um cliente de e-mail gratuito e de código aberto (open-source), multiplataforma, que permite configurar múltiplas contas (POP/IMAP), gerenciar catálogos de endereços, calendários e filtros de mensagens.",
      "Não aceita anexos em mensagens com extensões .pdf ou .docx por questões de segurança nativa.",
      "Funciona apenas online através de uma aba no navegador Mozilla Firefox, sem armazenamento de mensagens locais."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O Mozilla Thunderbird é um cliente de e-mail open-source mantido pela comunidade Mozilla. Ele roda localmente no Windows, Linux e macOS, permitindo gerenciamento de contas POP e IMAP, catálogo de contatos, calendário integrado (Lightning) e criptografia OpenPGP."
  },
  {
    "id": 628,
    "category": "informatica",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Webmail vs Cliente de E-mail Local",
    "question": "Ao utilizar serviços de correio eletrônico, o usuário pode optar pelo Webmail ou por um cliente de e-mail instalado na máquina. Assinale a afirmativa que apresenta CORRETAMENTE uma característica do Webmail:",
    "options": [
      "O Webmail é acessado diretamente por meio de um navegador web (via HTTP/HTTPS), não dependendo de software cliente de e-mail instalado no computador.",
      "O Webmail exige obrigatoriamente a configuração manual das portas de entrada e saída SMTP e POP3 pelo usuário final a cada login.",
      "O Webmail só permite visualizar mensagens de texto puro, sendo incapaz de baixar anexos ou renderizar imagens em HTML.",
      "O Webmail apaga automaticamente todos os e-mails da caixa de entrada após o encerramento da sessão do navegador."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Webmail roda diretamente no browser (Chrome, Edge, Firefox) por meio do protocolo web (HTTP/HTTPS). Não exige instalação nem configuração de portas de envio/recebimento no dispositivo do usuário, facilitando o acesso em qualquer computador conectado à internet."
  },
  {
    "id": 629,
    "category": "informatica",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Colaboração Digital: WhatsApp e Telegram",
    "question": "No contexto das ferramentas modernas de colaboração e mensagens digitais, comparando o WhatsApp e o Telegram, é CORRETO afirmar:",
    "options": [
      "O Telegram opera com arquitetura em nuvem (cloud-based), permitindo acesso autônomo em múltiplos computadores e celulares e suporte a canais unidirecionais de transmissão pública com número ilimitado de inscritos.",
      "O WhatsApp não suporta chamadas de vídeo em grupo nem o compartilhamento de arquivos com extensão .pdf.",
      "O Telegram não possui versão web nem aplicativo para computadores desktop.",
      "O WhatsApp não permite a criação de comunidades ou agrupamento de múltiplos grupos sob uma mesma administração."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Telegram é baseado em nuvem, permitindo que o usuário use o aplicativo em vários dispositivos simultaneamente sem depender do celular estar conectado à rede, além de oferecer Canais públicos para transmissão de mensagens a inscritos ilimitados. O WhatsApp utiliza criptografia ponta a ponta por padrão e suporta comunidades e envio de arquivos."
  },
  {
    "id": 630,
    "category": "informatica",
    "day": "w4_d3",
    "discipline": "Informática",
    "topic": "Colaboração Digital: Discord (Servidores e Canais)",
    "question": "O Discord consolidou-se como uma plataforma de comunicação em grupo amplamente adotada em equipes de trabalho. Na arquitetura do Discord, o ambiente de uma equipe organiza-se em um 'Servidor', que por sua vez é subdividido em:",
    "options": [
      "Canais de texto e canais de voz/vídeo, onde permissões de acesso e moderação podem ser atribuídas com base em cargos (roles).",
      "Planilhas estáticas de cálculo que não admitem troca de mensagens de áudio em tempo real.",
      "Apenas salas de bate-papo privadas para duas pessoas, sem suporte a múltiplos participantes simultâneos.",
      "Pastas locais protegidas por senha que impedem o compartilhamento de tela durante reuniões."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Um servidor Discord é uma comunidade própria estruturada em canais de texto (mensagens, links, arquivos) e canais de voz/vídeo (reuniões, chamadas de áudio, compartilhamento de tela). A administração e o acesso aos canais são controlados por meio de papéis/cargos (roles) com permissões específicas."
  }
]

if __name__ == '__main__':
    print(f"Total de questões estruturadas para o Dia 23/09 (w4_d3): {len(QUESTOES_S4_D3)}")
    orc = [q for q in QUESTOES_S4_D3 if q['discipline'] == 'Orçamento Público']
    inf = [q for q in QUESTOES_S4_D3 if q['discipline'] == 'Informática']
    print(f"  Orçamento Público: {len(orc)} questões (IDs {orc[0]['id']} a {orc[-1]['id']})")
    print(f"  Informática: {len(inf)} questões (IDs {inf[0]['id']} a {inf[-1]['id']})")

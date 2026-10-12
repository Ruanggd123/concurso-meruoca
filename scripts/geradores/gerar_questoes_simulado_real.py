import json

QUESTOES_SIMREAL = [
  {
    "id": 539,
    "category": "administrativo",
    "day": "simReal",
    "discipline": "Direito Administrativo",
    "topic": "Licitações (Lei nº 14.133/2021) [INBRASP 2026 • Q4155841]",
    "question": "[Real INBRASP 2026] A Lei n.º 14.133/2021 estabelece normas gerais de licitações e contratos administrativos, introduzindo novos procedimentos e princípios que visam modernizar e tornar mais eficiente a contratação pública. Nesse contexto, assinale a alternativa CORRETA:",
    "options": [
      "A modalidade de contratação integrada impede o contratado elaborar projeto básico executivo.",
      "O critério de julgamento de maior desconto é aplicável exclusivamente concessões de serviço.",
      "A contratação semi-integrada autoriza alterações quantitativas ilimitadas do objeto contratado sem restrições.",
      "A inversão de fases permite julgamento das propostas antes habilitação dos licitantes."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): Na Lei 14.133/2021 (Art. 17), a regra geral do rito procedimental é a inversão de fases (fase de julgamento de propostas antecede a fase de habilitação)."
  },
  {
    "id": 540,
    "category": "administrativo",
    "day": "simReal",
    "discipline": "Direito Administrativo",
    "topic": "Atos Administrativos [INBRASP 2026 • Q4155840]",
    "question": "[Real INBRASP 2026] Em relação ao Direito Administrativo, o Ato administrativo possui requisitos e atributos específicos que condicionam sua validade e eficácia e cuja compreensão é indispensável aos agentes públicos. Acerca do tema, é CORRETO afirmar que:",
    "options": [
      "Competência, objeto, forma, motivo e vontade compõem os requisitos do ato administrativo.",
      "Os atributos do ato administrativo incluem presunção de legitimidade, imperatividade e autoexecutoriedade.",
      "O ato administrativo é irrevogável e imutável independentemente do interesse público relevante.",
      "Um ato ilegal pode ser convalidado quando houver vício insanável de competência."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito oficial INBRASP (B): Os atributos do ato administrativo são: Presunção de Legitimidade, Imperatividade, Autoexecutoriedade e Tipicidade (mnemônico PIAT)."
  },
  {
    "id": 541,
    "category": "constitucional",
    "day": "simReal",
    "discipline": "Direito Constitucional",
    "topic": "Organização do Estado & Princípios (Art. 37 CF) [INBRASP 2026 • Q4155839]",
    "question": "[Real INBRASP 2026] A Constituição regula a organização do Estado definindo competências e princípios administrativos que orientam o funcionamento da União, estados, Distrito Federal e municípios e estabelecem limites para a atuação do poder público. Conforme o enunciado, assinale a alternativa CORRETA:",
    "options": [
      "O Brasil organiza-se em departamentos, províncias, vilas e Distritos Federais federados autônomos.",
      "Compete exclusivamente aos estados legislar sobre direitos processuais penais e civis federais.",
      "A autonomia municipal abrange criação de leis estaduais tributos e organização administrativa nacional.",
      "O art. 37 consagra princípios, legalidade, impessoalidade, moralidade, publicidade e eficiência administrativa."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): O caput do Art. 37 da Constituição Federal consagra expressamente os princípios fundamentais da Administração Pública (LIMPE: Legalidade, Impessoalidade, Moralidade, Publicidade e Eficiência)."
  },
  {
    "id": 542,
    "category": "constitucional",
    "day": "simReal",
    "discipline": "Direito Constitucional",
    "topic": "Direitos Fundamentais (Art. 5º CF) [INBRASP 2026 • Q4155838]",
    "question": "[Real INBRASP 2026] Os direitos e garantias fundamentais previstos na Constituição visam assegurar a proteção das liberdades individuais e de outros direitos essenciais ao cidadão, limitando o poder estatal e promovendo a dignidade da pessoa humana. Diante do exposto, assinale CORRETAMENTE:",
    "options": [
      "A liberdade de expressão é assegurada independentemente de censura e anonimato autorizado.",
      "A inviolabilidade do domicílio pode ser relativizada em casos de flagrante delito.",
      "A tortura é admitida quando necessária para investigação de crimes hediondos graves.",
      "A liberdade de reunião não precisa obedecer a requisitos previstos na lei."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito oficial INBRASP (B): Art. 5º, XI, CF/88: A casa é asilo inviolável do indivíduo, salvo em caso de flagrante delito, desastre, socorro ou, durante o dia, por determinação judicial."
  },
  {
    "id": 543,
    "category": "constitucional",
    "day": "simReal",
    "discipline": "Direito Constitucional",
    "topic": "Princípios & Objetivos da República (Art. 3º CF) [INBRASP 2026 • Q4155837]",
    "question": "[Real INBRASP 2026] De acordo com a Constituição Federal (CF) de 1988, os princípios fundamentais orientam a República Federativa do Brasil, estabelecendo valores e objetivos que norteiam a vida política e social do país. Nesse contexto, assinale a alternativa CORRETA:",
    "options": [
      "São fundamentos da República a soberania a submissão e a dignidade humana.",
      "A república tem como fundamento o pluralismo político e a monarquia hereditária.",
      "O artigo quarto orienta relações internacionais com base intervenção em outros povos.",
      "São objetivos fundamentais erradicar a pobreza promover justiça social e reduzir desigualdades."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): Art. 3º, III, CF/88: Constitui objetivo fundamental da República Federativa do Brasil erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais."
  },
  {
    "id": 544,
    "category": "legislacao",
    "day": "simReal",
    "discipline": "Legislação Municipal",
    "topic": "Lei Orgânica Municipal [INBRASP 2026 • Q4156058]",
    "question": "[Real INBRASP 2026] A Lei Orgânica Municipal (LOM) funciona como a lei fundamental do ente federativo local. Com base no tema e à luz do Direito Administrativo e Constitucional brasileiro, a função precípua da Lei Orgânica é:",
    "options": [
      "Funcionar como norma soberana e autônoma, com prerrogativa para revogar dispositivos da Constituição Federal dentro do território municipal.",
      "Atuar como lei fundamental do município, incumbida de organizar os poderes locais (Executivo e Legislativo) e estruturar a administração pública, operando em estrita harmonia e subordinação às Constituições Federal e Estadual.",
      "Subordinar a gestão local às diretrizes emitidas exclusivamente pelo Poder Judiciário do Estado, mitigando a atuação da Câmara de Vereadores.",
      "Regulamentar de forma restrita e exclusiva a instituição e arrecadação dos tributos municipais, sem competência sobre os poderes ou servidores locais."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito oficial INBRASP (B): A Lei Orgânica é a lei fundamental municipal que estrutura e organiza os poderes locais (Executivo e Legislativo), subordinada às Constituições Federal e Estadual."
  },
  {
    "id": 545,
    "category": "especificos",
    "day": "simReal",
    "discipline": "Administração Geral",
    "topic": "Rotinas Administrativas & Protocolo [INBRASP 2026 • Q4155830]",
    "question": "[Real INBRASP 2026] As rotinas administrativas buscam racionalizar processos e assegurar eficiência na execução das atividades por meio de padrões e protocolos que reduzem retrabalho e evitam erros, garantindo fluidez ao serviço. Sobre o tema e, à luz dessa análise, assinale a alternativa CORRETA:",
    "options": [
      "A padronização de procedimentos complica fluxos e aumenta retrabalho e erros administrativos.",
      "A ausência de rotina aumenta produtividade e garante distribuição equitativa de tarefas.",
      "A racionalização pressupõe eliminar etapas essenciais para acelerar a execução dos serviços.",
      "O protocolo registra movimentação documental garantindo autenticidade e rastreabilidade das informações formais."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): O setor de protocolo é responsável pelo registro de entrada, movimentação e saída de documentos oficiais, garantindo autenticidade e rastreabilidade formal."
  },
  {
    "id": 546,
    "category": "especificos",
    "day": "simReal",
    "discipline": "Administração Geral",
    "topic": "Funções Administrativas (Planejar, Organizar, Dirigir, Controlar) [INBRASP 2026 • Q4155829]",
    "question": "[Real INBRASP 2026] A administração é um processo voltado à consecução de objetivos organizacionais e envolve o exercício de funções específicas que estruturam e direcionam os esforços dos colaboradores para resultados planejados. Diante do exposto, é CORRETO afirmar que:",
    "options": [
      "Planejar é prever objetivos sem considerar estratégias e recursos para alcançar resultados.",
      "Organizar significa delegar autoridade e distribuir tarefas de forma aleatória pelos chefes.",
      "Dirigir envolve coordenar pessoas punindo-as na execução das metas previamente definidas sempre.",
      "Controlar é acompanhar resultados corrigindo desvios e comparando com padrões estabelecidos sempre."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): Na Teoria Geral da Administração, a função 'Controlar' consiste em acompanhar a execução, comparar com os padrões planejados e corrigir eventuais desvios."
  },
  {
    "id": 547,
    "category": "especificos",
    "day": "simReal",
    "discipline": "Arquivologia",
    "topic": "Gestão de Documentos & Protocolo [INBRASP 2026 • Q4155826]",
    "question": "[Real INBRASP 2026] O recebimento e a transmissão de informações exigem procedimentos padronizados de modo a assegurar controle, rastreabilidade e segurança nos fluxos comunicacionais dentro da organização. Dessa forma, assinale CORRETAMENTE:",
    "options": [
      "Registrar data hora e origem é fundamental para controle e rastreabilidade documental.",
      "Ignorar o protocolo simplifica o fluxo e evita burocracia no setor administrativo.",
      "Transmitir informação confidencial sem verificação preserva a agilidade e eficiência total.",
      "Deixar de arquivar documentos recebidos reduz a transparência e a responsabilidade institucional."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito oficial INBRASP (A): O registro criterioso de data, hora e procedência do documento é indispensável para o controle da cadeia de custódia e rastreabilidade no protocolo."
  },
  {
    "id": 548,
    "category": "especificos",
    "day": "simReal",
    "discipline": "Arquivologia",
    "topic": "Métodos de Arquivamento & Classificação [INBRASP 2026 • Q4155824]",
    "question": "[Real INBRASP 2026] O controle de materiais e a organização de arquivos são fundamentais para a eficiência institucional, pois garantem o acesso rápido e a disponibilidade de recursos, além de evitar perdas e desperdícios. Nesse contexto, assinale a alternativa CORRETA:",
    "options": [
      "O controle de materiais utiliza a técnica primeiro a entrar primeiro a sair.",
      "O arquivamento por ordem alfabética ignora critérios temáticos e prazos legais sempre.",
      "O método de arrumação por cor prioriza estética e subjetividade na gestão.",
      "A classificação por assunto facilita o acesso e preservação de documentos organizacionais."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): O método de arquivamento por assunto (ideográfico) organiza os documentos segundo o tema, facilitando sua recuperação célere e preservação institucional."
  },
  {
    "id": 549,
    "category": "especificos",
    "day": "simReal",
    "discipline": "Ética na Administração Pública",
    "topic": "INBRASP 2026 [INBRASP 2026 • Q4155828]",
    "question": "[Real INBRASP 2026] A Ética profissional e as relações interpessoais orientam os comportamentos dos servidores públicos, influenciando a confiança da sociedade e a credibilidade dos órgãos, pois valores éticos e convivência harmoniosa são essenciais ao bom serviço. Com base no enunciado, assinale CORRETAMENTE:",
    "options": [
      "A ética permite aceitar presentes de fornecedores como prova de gentileza empresarial.",
      "As relações interpessoais baseiam-se em competição rivalidade e desconfiança entre pares.",
      "É legítimo utilizar informações internas para obter vantagens pessoais no serviço público.",
      "O cumprimento das normas éticas fortalece a imagem e credibilidade da instituição."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): O cumprimento rigoroso dos preceitos éticos e deontológicos pelo servidor público fortalece a credibilidade e a confiança da sociedade na instituição."
  },
  {
    "id": 550,
    "category": "especificos",
    "day": "simReal",
    "discipline": "Redação Oficial",
    "topic": "Espécies Documentais (Ofício, Memorando) [INBRASP 2026 • Q4155822]",
    "question": "[Real INBRASP 2026] No contexto da redação oficial, as diversas espécies documentais possuem características e finalidades distintas que determinam o seu uso apropriado na administração pública. Sobre o tema, é CORRETO afirmar que:",
    "options": [
      "O ofício é usado para comunicações externas com autoridades do mesmo nível ou de outros órgãos.",
      "O memorando destina-se a expedientes enviados a autoridades de outros poderes apenas.",
      "A carta pessoal oficial é utilizada para registrar acordos informais entre órgãos.",
      "A comunicação interna é instrumento para registros patrimoniais de documentos e materiais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito oficial INBRASP (A): No Manual de Redação Oficial da Presidência da República, o Ofício é a comunicação formal destinada a autoridades de outros órgãos ou entidades externas."
  },
  {
    "id": 551,
    "category": "especificos",
    "day": "simReal",
    "discipline": "Atendimento ao Público",
    "topic": "Princípios do Atendimento [INBRASP 2026 • Q4155835]",
    "question": "[Real INBRASP 2026] A qualidade no atendimento ao público está associada a práticas que valorizam o cidadão e incluem atendimento humanizado, acessibilidade e resolução eficaz de demandas. Diante do exposto, assinale a alternativa CORRETA:",
    "options": [
      "Ouvir demandas com atenção, oferecer informações claras e resolver problemas com eficiência.",
      "Desconsiderar reclamações legitima sentimentos positivos e aprimora a confiança do público sempre.",
      "Garantir acessibilidade, promover a igualdade e respeitar a diversidade fortalecem o serviço prestado sempre.",
      "Informar inadequadamente gera satisfação e fideliza o usuário de forma contínua total."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito oficial INBRASP (A): O atendimento de excelência no serviço público fundamenta-se na escuta ativa, presteza, clareza nas orientações e resolutividade das demandas dos cidadãos."
  },
  {
    "id": 552,
    "category": "especificos",
    "day": "simReal",
    "discipline": "Gestão de Pessoas",
    "topic": "Comunicação Organizacional & Feedback [INBRASP 2026 • Q4155833]",
    "question": "[Real INBRASP 2026] A comunicação eficaz é essencial para o sucesso das organizações, pois melhora o entendimento, reduz conflitos e promove a colaboração entre os membros da equipe por meio de feedbacks e escuta ativa. Nesse contexto, assinale a alternativa CORRETA.",
    "options": [
      "Ouvir passivamente facilita compreensão reduz conflitos e fortalece relacionamentos no trabalho sempre.",
      "Informações difusas e incompletas promovem confiança e melhoram o clima organizacional saudável.",
      "O excesso de ruído na comunicação promove entendimento e eficiência continuamente sempre.",
      "O feedback construtivo contribui para aprendizado contínuo e melhoria de processos organizacionais."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): O feedback construtivo e transparente orienta os servidores, estimula o aprimoramento contínuo das rotinas e aperfeiçoa o clima organizacional."
  },
  {
    "id": 553,
    "category": "informatica",
    "day": "simReal",
    "discipline": "Noções de Informática",
    "topic": "Microsoft Word & Excel [INBRASP 2026 • Q4155827]",
    "question": "[Real INBRASP 2026] Considerando que ao trabalhar com programas de edição de texto e planilhas eletrônicas, é importante dominar funções básicas que permitam formatar documentos e realizar cálculos simples ou complexos de forma precisa e eficiente, assinale a alternativa CORRETA:",
    "options": [
      "No Word, é possível formatar texto alterar fontes cores e inserir tabelas.",
      "No Excel, a fórmula SOMA serve para calcular quantidades entre células selecionadas.",
      "No Word, as planilhas são criadas para cálculos complexos com fórmulas matemáticas.",
      "No Excel, a ferramenta de revisão aplica correção ortográfica em parágrafos escritos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito oficial INBRASP (A): O Microsoft Word permite a edição, formatação completa de fontes (tamanho, cor, família), parágrafos e inserção de tabelas e elementos gráficos."
  },
  {
    "id": 554,
    "category": "matematica",
    "day": "simReal",
    "discipline": "Matemática",
    "topic": "Frações e Números Decimais em Ordem Crescente [INBRASP 2026 • Q4156055]",
    "question": "[Real INBRASP 2026] Os valores foram obtidos em uma pesquisa estatística, observe: (4/5; 0,75; 1,2; 3/2; 0,8̅). Para facilitar a análise dos dados, é necessário organizá-los em ordem crescente. Assim, a ordem crescente dos números é, CORRETA e, respectivamente:",
    "options": [
      "0,75; 0,8̅; 4/5; 1,2; 3/2.",
      "0,75; 4/5; 0,8̅; 1,2; 3/2.",
      "4/5; 0,75; 0,8̅; 1,2; 3/2.",
      "3/2; 0,8̅; 4,5; 1,2; 0,75."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito oficial INBRASP (B): Convertendo para decimais: 4/5 = 0,80; 0,75 = 0,75; 1,2 = 1,20; 3/2 = 1,50; 0,8̅ = 0,888... Ordem crescente: 0,75 < 4/5 (0,80) < 0,8̅ (0,888) < 1,2 < 3/2 (1,50)."
  },
  {
    "id": 555,
    "category": "matematica",
    "day": "simReal",
    "discipline": "Matemática",
    "topic": "Aritmética & Resto de Divisão [INBRASP 2026 • Q4156054]",
    "question": "[Real INBRASP 2026] Sendo R o resto da divisão do número 1004505 por 6, então R é um número:",
    "options": [
      "Divisor de 20.",
      "Múltiplo de 9.",
      "Maior do que 5.",
      "Primo."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): Soma dos dígitos de 1004505 = 1+0+0+4+5+0+5 = 15 (múltiplo de 3). Como é ímpar, 1004505 mod 6 = 3. O número 3 é um número Primo."
  },
  {
    "id": 556,
    "category": "matematica",
    "day": "simReal",
    "discipline": "Matemática",
    "topic": "Sistema de Medidas de Tempo [INBRASP 2026 • Q4156053]",
    "question": "[Real INBRASP 2026] Considerando que um relógio adianta 3 minutos a cada dia, após 4 semanas, ele estará adiantado em:",
    "options": [
      "1 hora e 12 minutos.",
      "1 hora e 16 minutos.",
      "1 hora e 20 minutos.",
      "1 hora e 24 minutos."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): 4 semanas = 28 dias. 28 dias × 3 min/dia = 84 minutos. 84 minutos = 60 min + 24 min = 1 hora e 24 minutos."
  },
  {
    "id": 557,
    "category": "matematica",
    "day": "simReal",
    "discipline": "Matemática",
    "topic": "Operações com Frações [INBRASP 2026 • Q4156052]",
    "question": "[Real INBRASP 2026] Pedro recebeu 3/4 das figurinhas que estavam em um álbum. Do total de figurinhas recebidas, ele deu 2/5 para um amigo. Dessa forma, a fração do total de figurinhas contidas no álbum que foi recebida pelo amigo de Pedro foi:",
    "options": [
      "3/10.",
      "1/20.",
      "1/4.",
      "1/3."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito oficial INBRASP (A): Pedro recebeu 3/4 e deu 2/5 dessa parte ao amigo: (3/4) × (2/5) = 6/20 = 3/10 do álbum total."
  },
  {
    "id": 558,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Classes de Palavras: Adjetivo Caracterizador [INBRASP 2026 • Q4156051]",
    "question": "[Real INBRASP 2026] Assinale a alternativa cujo termo destacado é um adjetivo caracterizador de um substantivo:",
    "options": [
      "As críticas mais recentes se baseiam nas exigências do Pacto Ecológico Europeu.",
      "A potência asiática oferece algo a mais que os europeus.",
      "Alguns interesses, por outro lado, podem se camuflar neste cenário.",
      "É um bloco, um continente estratégico, não podemos reduzir sua importância."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): Em \"continente estratégico\", a palavra \"estratégico\" qualifica e caracteriza o substantivo \"continente\"."
  },
  {
    "id": 559,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Adjunto Adverbial de Tempo [INBRASP 2026 • Q4156050]",
    "question": "[Real INBRASP 2026] Assinale a alternativa que apresenta CORRETAMENTE apenas expressões que indicam tempo:",
    "options": [
      "Historicamente, temos tido um problema de diálogo com a União Europeia. Eles decidem regras importantes do jogo não em negociação, mas por conta própria.",
      "Vale mencionar que há uma boa dose de protecionismo por parte do agronegócio europeu que também influencia a negociação com o Mercosul.",
      "As críticas mais recentes se baseiam nas exigências do Pacto Ecológico Europeu, o Green Deal.",
      "Ingo Plöger, empresário que acompanha há décadas a negociação do acordo e atualmente está na vice-presidência da Abag, ressalta que a UE é um importante provedor de conceitos mundiais."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): As locuções adverbiais e advérbios \"há décadas\" (tempo decorrido) e \"atualmente\" (tempo presente) expressam circunstância temporal estrita."
  },
  {
    "id": 560,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Regras de Acentuação Gráfica [INBRASP 2026 • Q4156049]",
    "question": "[Real INBRASP 2026] A palavra ‘política’ está acentuada graficamente pelo mesmo motivo que em:",
    "options": [
      "Inflexível.",
      "Café.",
      "Cômputo.",
      "Fóruns."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito oficial INBRASP (C): A palavra \"po-lí-ti-ca\" é proparoxítona (sílaba tônica antepenúltima). Todas as proparoxítonas são acentuadas, assim como \"Côm-pu-to\"."
  },
  {
    "id": 561,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Orações Subordinadas Adverbiais: Condicional [INBRASP 2026 • Q4156048]",
    "question": "[Real INBRASP 2026] No trecho “o acordo de livre comércio entre Mercosul e União Europeia corre o risco de não ser ratificado, caso a Europa permaneça inflexível”, a palavra destacada ('caso') introduz o significado de:",
    "options": [
      "Condição.",
      "Consequência.",
      "Causa.",
      "Oposição."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito oficial INBRASP (A): A conjunção subordinativa \"caso\" expressa uma condição necessária para que a oração principal se realize."
  },
  {
    "id": 562,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Sintaxe do Verbo Haver Impessoal [INBRASP 2026 • Q4156047]",
    "question": "[Real INBRASP 2026] Em “não houve nenhuma oportunidade de diálogo de demonstrar o que é viável”, é CORRETO afirmar, de acordo com os termos da oração, que:",
    "options": [
      "O termo ‘nenhuma oportunidade de diálogo’ exerce a função de sujeito do verbo ‘haver’.",
      "O verbo ‘haver’ é impessoal e transitivo direto.",
      "O termo ‘viável’ exerce a função de complemento nominal.",
      "O verbo ‘haver’ é pessoal e concorda com o sujeito da oração."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito oficial INBRASP (B): No sentido de existir/ocorrer, o verbo 'haver' é impessoal (não tem sujeito) e é transitivo direto, exigindo objeto direto (\"nenhuma oportunidade de diálogo\")."
  },
  {
    "id": 563,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Classes de Palavras: Preposição vs. Artigo [INBRASP 2026 • Q4156046]",
    "question": "[Real INBRASP 2026] No trecho “os produtores reunidos na Abag estariam dispostos a contribuir com a meta de acabar com o desmatamento ilegal”, as palavras 'a' em destaque (\"a contribuir\" e \"a meta\") são classificadas, CORRETA e respectivamente, como:",
    "options": [
      "Conjunção e pronome.",
      "Preposição e pronome.",
      "Conjunção e artigo.",
      "Preposição e artigo."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito oficial INBRASP (D): Em \"a contribuir\", 'a' é preposição antes do verbo no infinitivo; em \"a meta\", 'a' é artigo definido feminino que determina o substantivo 'meta'."
  },
  {
    "id": 564,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Significação de Palavras (Sinônimos) [INBRASP 2026 • Q4156045]",
    "question": "[Real INBRASP 2026] Em “o acordo de livre comércio entre Mercosul e União Europeia corre o risco de não ser ratificado”, o termo destacado ('ratificado') significa:",
    "options": [
      "Validado.",
      "Cancelado.",
      "Proposto.",
      "Corrigido."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito oficial INBRASP (A): O verbo \"ratificar\" significa confirmar, validar, comprovar juridicamente um ato ou tratado prévio."
  },
  {
    "id": 565,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Morfossintaxe de Conjunção Causal [INBRASP 2026 • Q4156044]",
    "question": "[Real INBRASP 2026] Assinale a alternativa que apresenta CORRETAMENTE a classificação do termo destacado:",
    "options": [
      "O atual presidente brasileiro parece empenhado em reverter a situação. (Conjunção)",
      "O Brasil foi o principal vendedor de produtos do setor para UE. (Substantivo)",
      "Não dá pra prever todas as variáveis porque não se trata de um processo linear. (Conjunção)",
      "Isso pode estar sendo provocado em parte às posições ambíguas de Lula. (Adjetivo)"
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito oficial INBRASP (C): No período \"...porque não se trata...\", a palavra \"porque\" atua como conjunção subordinativa explicativa/causal ligando as orações."
  },
  {
    "id": 566,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Semântica Modalizadora [INBRASP 2026 • Q4156043]",
    "question": "[Real INBRASP 2026] No trecho “Se houver mudança do governo, o acordo tem que assegurar que ele mesmo não sirva de incentivo para quem está desmatando”, a expressão destacada ('tem que') indica:",
    "options": [
      "Possibilidade.",
      "Obrigação.",
      "Proibição.",
      "Restrição."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito oficial INBRASP (B): A locução verbal modalizadora \"tem que\" veicula valor semântico de obrigatoriedade/dever imperativo."
  },
  {
    "id": 567,
    "category": "portugues",
    "day": "simReal",
    "discipline": "Português",
    "topic": "Vocabulário Contextual: Sinônimos [INBRASP 2026 • Q4156042]",
    "question": "[Real INBRASP 2026] Em “é preciso ter cautela com as assimetrias do acordo e algumas previsões muito otimistas”, o termo destacado ('assimetrias') pode ser substituído CORRETAMENTE por:",
    "options": [
      "Tendências.",
      "Lacunas.",
      "Discrepâncias.",
      "Propostas."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito oficial INBRASP (C): O vocábulo \"assimetrias\" refere-se à ausência de igualdade, desníveis, descompassos ou discrepâncias entre as partes negociadoras."
  }
]

print(f"[OK] Total de questões reais extraídas: {len(QUESTOES_SIMREAL)}")

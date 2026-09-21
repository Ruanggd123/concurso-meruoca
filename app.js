// Plano Mestre - Câmara de Meruoca 2026 (Técnico Legislativo)

// =========================================================================
// BANCO DE FLASHCARDS INTERATIVOS (MEMORIZAÇÃO ATIVA & MNEMÔNICOS)
// =========================================================================
const FLASHCARDS_DATA = [
  {
    id: 1,
    category: "legislacao",
    tag: "Lei Orgânica de Meruoca",
    question: "Qual o prazo que o Prefeito de Meruoca tem para sancionar ou vetar um Projeto de Lei aprovado pela Câmara?",
    answer: "15 dias úteis.",
    explanation: "O silêncio do Prefeito após os 15 dias úteis importa em sanção tácita. Se ele vetar, o veto deve ser apreciado pela Câmara em até 30 dias."
  },
  {
    id: 2,
    category: "legislacao",
    tag: "Lei Orgânica de Meruoca",
    question: "Qual é o quórum necessário na Câmara de Meruoca para REJEITAR o parecer prévio do Tribunal de Contas (TCE) sobre as contas do Prefeito?",
    answer: "2/3 (dois terços) dos membros da Câmara.",
    explanation: "O parecer prévio do Tribunal de Contas só deixará de prevalecer por decisão de 2/3 dos membros da Câmara Municipal."
  },
  {
    id: 3,
    category: "legislacao",
    tag: "Regimento Interno",
    question: "Quais são as duas funções TÍPICAS do Poder Legislativo Municipal?",
    answer: "1. Legislar (criar leis) e 2. Fiscalizar (controle externo).",
    explanation: "Funções atípicas: Administrar seus próprios serviços e Julgar (ex: julgar o Prefeito e Vereadores por infrações político-administrativas)."
  },
  {
    id: 4,
    category: "constitucional",
    tag: "Constitucional — Art. 5º",
    question: "Quais são os únicos crimes INAFIANÇÁVEIS e IMPRESCRITÍVEIS segundo a CF/88? (Mnemônico)",
    answer: "Mnemônico: RAÇÃO\n• RA = Racismo (Art. 5º, XLII)\n• ÇÃO = Ação de grupos armados (Art. 5º, XLIV)",
    explanation: "Estão sujeitos à pena de reclusão. Não prescrevem jamais e não admitem fiança."
  },
  {
    id: 5,
    category: "constitucional",
    tag: "Constitucional — Art. 5º",
    question: "Quais são os crimes INAFIANÇÁVEIS e INSUSCETÍVEIS DE GRAÇA OU ANISTIA? (Mnemônico)",
    answer: "Mnemônico: 3T.H\n• Tráfico ilícito de entorpecentes\n• Tortura\n• Terrorismo\n• Hediondos",
    explanation: "Art. 5º, XLIII: São inafiançáveis e não recebem graça/anistia/indulto. (Atenção: eles PRESCREVEM, diferentemente de racismo e ação de grupos armados)."
  },
  {
    id: 6,
    category: "constitucional",
    tag: "Remédios Constitucionais",
    question: "Qual o prazo decadencial para impetrar Mandado de Segurança?",
    answer: "120 dias corridos.",
    explanation: "Art. 23 da Lei 12.016/09 e Súmula 632 do STF. Conta-se a partir da ciência oficial, pelo interessado, do ato impugnado."
  },
  {
    id: 7,
    category: "constitucional",
    tag: "Constitucional — Art. 5º",
    question: "A entrada forçada em domicílio por determinação JUDICIAL só pode ocorrer em qual horário?",
    answer: "Apenas DURANTE O DIA.",
    explanation: "Art. 5º, XI: Determinação judicial = só de dia. Flagrante delito, desastre ou socorro = a qualquer hora (dia ou noite)."
  },
  {
    id: 8,
    category: "constitucional",
    tag: "Remédios Constitucionais",
    question: "Quem tem legitimidade ativa para propor Ação Popular?",
    answer: "Exclusivamente o CIDADÃO (no gozo dos direitos políticos).",
    explanation: "Art. 5º, LXXIII: Estrangeiros, pessoas jurídicas e partidos políticos não podem propor Ação Popular; exige-se título de eleitor regular."
  },
  {
    id: 9,
    category: "administrativo",
    tag: "Direito Administrativo",
    question: "Quais são os 5 REQUISITOS / ELEMENTOS de validade do Ato Administrativo? (Mnemônico)",
    answer: "Mnemônico: CO-M-FI-FO-R\n• Competência\n• Motivo\n• Finalidade\n• Forma\n• Objeto",
    explanation: "Competência, Finalidade e Forma são sempre VINCULADOS. Motivo e Objeto podem ser discricionários."
  },
  {
    id: 10,
    category: "administrativo",
    tag: "Direito Administrativo",
    question: "Quais são os 4 ATRIBUTOS do Ato Administrativo? (Mnemônico)",
    answer: "Mnemônico: P-A-T-I\n• Presunção de legitimidade/veracidade\n• Autoexecutoriedade\n• Tipicidade\n• Imperatividade",
    explanation: "A Presunção e a Tipicidade estão presentes em TODOS os atos administrativos."
  },
  {
    id: 11,
    category: "administrativo",
    tag: "Lei 14.133/2021 (Licitações)",
    question: "Quais são as 5 MODALIDADES de licitação previstas na Nova Lei 14.133/2021?",
    answer: "1. Pregão\n2. Concorrência\n3. Concurso\n4. Leilão\n5. Diálogo Competitivo",
    explanation: "ATENÇÃO: Tomada de Preços e Convite foram EXTINTOS pela Lei 14.133/21!"
  },
  {
    id: 12,
    category: "administrativo",
    tag: "Lei 14.133/2021 (Licitações)",
    question: "Qual a diferença fundamental entre INEXIGIBILIDADE e DISPENSA de licitação?",
    answer: "• Inexigibilidade = Inviabilidade de competição (rol exemplificativo).\n• Dispensa = Competição é viável, mas a lei permite dispensar (rol taxativo).",
    explanation: "Exemplos de Inexigibilidade: fornecedor exclusivo, artista consagrado, serviços técnicos especializados singulares."
  },
  {
    id: 13,
    category: "administrativo",
    tag: "Orçamento / LRF (LC 101/00)",
    question: "Qual o limite MÁXIMO de despesa total com PESSOAL para o Poder Legislativo Municipal (Câmara)?",
    answer: "6% (seis por cento) da Receita Corrente Líquida (RCL).",
    explanation: "No Município: Poder Executivo = 54%, Poder Legislativo = 6%. Total municipal = 60% da RCL."
  },
  {
    id: 14,
    category: "legislacao",
    tag: "Técnica Legislativa (LC 95/98)",
    question: "Como se desdobra hierarquicamente a estrutura de uma lei conforme a LC 95/98?",
    answer: "Artigo (Art.) ➔ Parágrafo (§) ➔ Inciso (I, II) ➔ Alínea (a, b) ➔ Item (1, 2).",
    explanation: "Os artigos são indicados por ordinais até o nono (Art. 1º ao Art. 9º) e por cardinais a partir do décimo (Art. 10, Art. 11)."
  },
  {
    id: 15,
    category: "constitucional",
    tag: "Constitucional — Art. 5º",
    question: "O direito de reunião pacífica (Art. 5º, XVI) exige autorização policial?",
    answer: "NÃO. Independe de autorização.",
    explanation: "Exige-se apenas: fins pacíficos, sem armas, em locais abertos ao público, prévio aviso (para evitar choque com outra reunião) e não frustração de reunião anterior."
  },
  {
    id: 16,
    category: "administrativo",
    tag: "Responsabilidade do Estado",
    question: "Qual é a regra geral da Responsabilidade Civil do Estado no Brasil (Art. 37, § 6º da CF)?",
    answer: "Responsabilidade OBJETIVA (Teoria do Risco Administrativo).",
    explanation: "A vítima precisa provar apenas: Conduta estatal, Dano e Nexo Causal. Não precisa provar dolo nem culpa da administração."
  },
  {
    id: 17,
    category: "administrativo",
    tag: "Improbidade (Lei 8.429/92)",
    question: "Atos de improbidade administrativa admitem modalidade CULPOSA após a reforma da Lei 14.230/21?",
    answer: "NÃO. Exige-se DOLO ESPECÍFICO em todas as hipóteses.",
    explanation: "A mera voluntariedade ou negligência/imprudência não configura mais ato de improbidade administrativa."
  },
  {
    id: 18,
    category: "legislacao",
    tag: "LGPD (Lei 13.709/18)",
    question: "O que é considerado 'Dado Pessoal Sensível' na LGPD?",
    answer: "Dados sobre origem racial/étnica, convicção religiosa, opinião política, filiação sindical, saúde, vida sexual, dado genético ou biométrico.",
    explanation: "Possuem regime de tratamento muito mais rigoroso e restritivo que os dados pessoais comuns."
  },
  {
    id: 19,
    category: "legislacao",
    tag: "LAI (Lei 12.527/11)",
    question: "Qual o prazo que a Administração Pública tem para responder a um pedido de acesso à informação (LAI) se a informação não puder ser concedida de imediato?",
    answer: "Até 20 dias (prorrogáveis por mais 10 dias justificadamente).",
    explanation: "A regra geral é o acesso imediato. Se não for possível, o prazo é de 20 + 10 dias."
  },
  {
    id: 20,
    category: "constitucional",
    tag: "Poder Legislativo",
    question: "Qual a diferença entre SANÇÃO, VETO e PROMULGAÇÃO de uma lei?",
    answer: "• Sanção = Concordância do Chefe do Executivo.\n• Veto = Recusa expressa (por inconstitucionalidade ou interesse público).\n• Promulgação = Atestado formal de existência e executoriedade da lei.",
    explanation: "Se o Prefeito vetar e a Câmara derrubar o veto, o Prefeito tem 48h para promulgar. Se não o fizer, o Presidente da Câmara promulgará em 48h."
  },
  {
    id: 21,
    category: "portugues",
    tag: "Língua Portuguesa",
    question: "Qual a diferença entre TEXTO INJUNTIVO e TEXTO PRESCRITIVO?",
    answer: "• Injuntivo = Sugestão/instrução/conselho (ex: receita culinária, manual).\n• Prescritivo = Ordem impositiva e obrigatória (ex: cláusulas de contrato, leis, placas de trânsito).",
    explanation: "Ambos usam verbos no imperativo, mas o prescritivo não dá margem de escolha ao leitor."
  },
  {
    id: 22,
    category: "legislacao",
    tag: "Orçamento Público",
    question: "Qual a função de cada instrumento orçamentário: PPA, LDO e LOA?",
    answer: "• PPA (4 anos) = Diretrizes, objetivos e metas de médio prazo.\n• LDO (Anual) = Metas, prioridades e orienta a elaboração da LOA.\n• LOA (Anual) = Estima a receita e fixa a despesa para o exercício.",
    explanation: "A LOA é o orçamento executivo real; a LDO faz a ponte estratégica entre o PPA e a LOA."
  },

  // =========================================================================
  // FLASHCARDS ESPECÍFICOS DO DIA 3 (02/09/2026 — D. ADMINISTRATIVO & INFORMÁTICA)
  // =========================================================================
  {
    id: 23,
    category: "administrativo",
    day: "dia3",
    tag: "D. Administrativo — Princípios LIMPE",
    question: "Quais são os 5 Princípios Expressos da Administração Pública no Art. 37, caput da CF/88? (Mnemônico)",
    answer: "Mnemônico: L - I - M - P - E\n• L = Legalidade\n• I = Impessoalidade\n• M = Moralidade\n• P = Publicidade\n• E = Eficiência (EC 19/98)",
    explanation: "Atenção: Razoabilidade, Proporcionalidade e Supremacia do Interesse Público são princípios IMPLÍCITOS, não estão expressos no LIMPE!"
  },
  {
    id: 24,
    category: "administrativo",
    day: "dia3",
    tag: "D. Administrativo — Impessoalidade",
    question: "Qual a regra constitucional sobre publicidade de atos e campanhas de órgãos públicos (Art. 37, § 1º)?",
    answer: "Deve ter caráter educativo, informativo ou de orientação social, sendo VEDADA a promoção pessoal (nomes, fotos, símbolos de autoridades).",
    explanation: "A vedação de autopromoção de prefeitos e vereadores decorre diretamente do princípio da IMPESSOALIDADE."
  },
  {
    id: 25,
    category: "administrativo",
    day: "dia3",
    tag: "D. Administrativo — Moralidade",
    question: "O que estabelece a Súmula Vinculante nº 13 do STF sobre Nepotismo?",
    answer: "É proibida a nomeação de cônjuge, companheiro ou parente até o 3º GRAU da autoridade nomeante para cargo em comissão ou função de confiança.",
    explanation: "Ofende os princípios da Moralidade, Impessoalidade e Isonomia em todos os Poderes da União, Estados e Municípios."
  },
  {
    id: 26,
    category: "administrativo",
    day: "dia3",
    tag: "D. Administrativo — Autotutela",
    question: "O que é o Princípio da Autotutela (Súmulas 346 e 473 do STF)?",
    answer: "A Administração pode rever seus próprios atos:\n• ANULAR os atos ILEGAIS (efeito ex tunc - retroage).\n• REVOGAR os atos INOPORTUNOS/INCONVENIENTES (efeito ex nunc - não retroage).",
    explanation: "A Administração não precisa pedir autorização judicial para anular seus atos ilegais nem para revogar atos inoportunos."
  },
  {
    id: 27,
    category: "administrativo",
    day: "dia3",
    tag: "D. Administrativo — Organização",
    question: "Qual a diferença essencial entre DESCONCENTRAÇÃO e DESCENTRALIZAÇÃO? (Mnemônico)",
    answer: "• DescoNcentração (com O de Órgão) = Divisão interna na MESMA pessoa jurídica (com hierarquia).\n• DesceNtralização (com E de Entidade) = Criação/transferência para OUTRA pessoa jurídica (sem hierarquia, apenas tutela).",
    explanation: "Órgãos públicos NÃO têm personalidade jurídica própria nem patrimônio separado; entidades da administração indireta têm."
  },
  {
    id: 28,
    category: "administrativo",
    day: "dia3",
    tag: "D. Administrativo — Administração Indireta",
    question: "Qual é a ÚNICA entidade da Administração Indireta que é criada DIRETAMENTE por lei específica?",
    answer: "A AUTARQUIA (personalidade jurídica de direito público).",
    explanation: "Art. 37, XIX da CF/88: Somente a Autarquia é criada por lei específica. Empresas Públicas, SEM e Fundações têm sua criação apenas AUTORIZADA por lei."
  },
  {
    id: 29,
    category: "administrativo",
    day: "dia3",
    tag: "D. Administrativo — Empresas Públicas vs SEM",
    question: "Quais as 2 principais diferenças entre Empresa Pública (EP) e Sociedade de Economia Mista (SEM)?",
    answer: "1. Capital:\n• EP = 100% público\n• SEM = Misto (maioria votante pública)\n2. Formato:\n• EP = Qualquer formato (Ltda, S/A)\n• SEM = Obrigatoriamente S/A",
    explanation: "Exemplo de Empresa Pública: Caixa Econômica / Correios. Exemplo de Sociedade de Economia Mista: Banco do Brasil / Petrobras."
  },
  {
    id: 30,
    category: "administrativo",
    day: "dia3",
    tag: "D. Administrativo — Órgãos Públicos",
    question: "Qual teoria explica a relação entre o agente público e o órgão/Estado no Brasil?",
    answer: "Teoria do Órgão (ou da Imputação Volitiva) de Otto Gierke.",
    explanation: "A vontade e os atos praticados pelo servidor público são imputados diretamente à pessoa jurídica do Estado (ex: Município de Meruoca)."
  },
  {
    id: 31,
    category: "informatica",
    day: "dia3",
    tag: "Windows 11 — Nomes de Arquivos",
    question: "Quais são os 9 caracteres PROIBIDOS em nomes de arquivos e pastas no Windows?",
    answer: "Barras (\\ /), Dois pontos (:), Asterisco (*), Interrogação (?), Aspas (\"), Menor (<), Maior (>) e Pipe (|).",
    explanation: "Mnemônico: 'Dois pontos, duas barras, aspas, asterisco, interrogação, menor, maior e pipe'."
  },
  {
    id: 32,
    category: "informatica",
    day: "dia3",
    tag: "Windows 11 — Atalhos de Teclado",
    question: "Quais as funções dos atalhos: Win + L, Win + E e Shift + Delete no Windows 11?",
    answer: "• Win + L = Bloqueia a tela do computador (Lock)\n• Win + E = Abre o Explorador de Arquivos (Explorer)\n• Shift + Delete = Exclui permanentemente (sem passar pela Lixeira)",
    explanation: "Ctrl + Shift + Esc abre o Gerenciador de Tarefas diretamente."
  },
  {
    id: 33,
    category: "informatica",
    day: "dia3",
    tag: "Linux Ubuntu — Diretórios",
    question: "No Linux Ubuntu, para que servem os diretórios /etc, /home e /root?",
    answer: "• /etc = Arquivos de configuração globais do sistema\n• /home = Pastas dos usuários comuns\n• /root = Pasta pessoal do superusuário (administrador)",
    explanation: "/bin armazena comandos executáveis essenciais; /var armazena dados variáveis (logs e spool)."
  },
  {
    id: 34,
    category: "informatica",
    day: "dia3",
    tag: "Linux Ubuntu — Comandos",
    question: "No terminal do Linux, o que fazem os comandos 'ls', 'mkdir' e 'pwd'?",
    answer: "• ls = Lista arquivos e pastas\n• mkdir = Cria novo diretório (pasta)\n• pwd = Exibe o caminho absoluto do diretório atual (Print Working Directory)",
    explanation: "O Linux é Case Sensitive (diferencia maiúsculas de minúsculas: Relatorio.txt ≠ relatorio.txt)."
  },
  {
    id: 35,
    category: "informatica",
    day: "dia3",
    tag: "Hardware — Memórias",
    question: "Qual a diferença fundamental entre Memória RAM e Memória ROM?",
    answer: "• RAM = Primária, ultrarrápida e VOLÁTIL (apaga tudo ao desligar o PC).\n• ROM = Primária, NÃO-VOLÁTIL, gravada de fábrica com a BIOS/firmware.",
    explanation: "SSD e HD são memórias secundárias (armazenamento permanente de arquivos do usuário)."
  },
  {
    id: 36,
    category: "informatica",
    day: "dia3",
    tag: "Hardware — CPU",
    question: "Quais são as 3 unidades fundamentais da CPU (Processador)?",
    answer: "1. ULA (Unidade Lógica e Aritmética - cálculos matemáticos e lógicos)\n2. UC (Unidade de Controle - gerencia fluxo de dados)\n3. Registradores (memória interna ultrarrápida)",
    explanation: "A CPU executa o ciclo de busca, decodificação e execução das instruções dos programas."
  },
  {
    id: 37,
    category: "informatica",
    day: "dia3",
    tag: "Backup — Tipos e Regra 3-2-1",
    question: "Qual a diferença entre Backup Incremental e Backup Diferencial, e o que é a Regra 3-2-1?",
    answer: "• Incremental = Copia alterações desde o ÚLTIMO backup (qualquer tipo).\n• Diferencial = Copia alterações desde o último backup FULL.\n• Regra 3-2-1 = 3 cópias, 2 mídias diferentes, 1 cópia fora do local (nuvem).",
    explanation: "O Incremental é mais rápido de gravar; o Diferencial é mais rápido de restaurar."
  }
,
  {
    id: 38,
    category: "portugues",
    day: "dia4",
    tag: "Português — Proparoxítonas",
    question: "Qual é a regra geral de acentuação gráfica das palavras PROPAROXÍTONAS na Língua Portuguesa?",
    answer: "TODAS as palavras proparoxítonas são acentuadas graficamente.",
    explanation: "Exemplos clássicos da INBRASP: po-LÍ-ti-ca, CÔM-pu-to, TÉC-ni-co, CÂ-ma-ra, DÉ-fi-cit."
  },
  {
    id: 39,
    category: "portugues",
    day: "dia4",
    tag: "Português — Crase Proibida",
    question: "Quais são os 3 casos mais cobrados em concursos em que a CRASE é expressamente PROIBIDA?",
    answer: "1. Antes de palavras masculinas;\n2. Antes de verbos no infinitivo;\n3. Antes de pronomes que não aceitam artigo (esta, essa, quem, alguém, todos).",
    explanation: "Crase é a fusão de preposição 'a' + artigo 'a'. Se a palavra seguinte não aceita artigo feminino, a crase não pode ocorrer."
  },
  {
    id: 40,
    category: "portugues",
    day: "dia4",
    tag: "Português — Crase Facultativa",
    question: "Quais são os 3 casos clássicos em que a CRASE é FACULTATIVA (opcional)? (Mnemônico)",
    answer: "Mnemônico: ATÉ, NOME DE MULHER, POSSESSIVO\n1. Depois da palavra 'até';\n2. Antes de nomes próprios femininos sem qualificativo;\n3. Antes de pronome possessivo feminino singular (minha, sua, tua).",
    explanation: "Exemplos: 'Fui até a/à praça'; 'Entreguei o ofício a/à Maria'; 'Dirigi-me a/à sua sala'."
  },
  {
    id: 41,
    category: "portugues",
    day: "dia4",
    tag: "Português — Hiatos Tônicos",
    question: "Por que 'SAÍDA' e 'BAÚ' têm acento gráfico, mas 'RAINHA' e 'JUIZ' não têm?",
    answer: "'I' e 'U' tônicos em hiato recebem acento quando sozinhos na sílaba (ou com 's'). Não recebem acento se seguidos de 'nh' (ra-i-nha) ou de outra consoante como 'z' (ju-iz).",
    explanation: "Sa-í-da (acentua); Ba-ú (acentua); Ju-iz (não acentua, mas 'ju-í-zes' acentua porque o 'i' fica sozinho com a divisão silábica)."
  },
  {
    id: 42,
    category: "constitucional",
    day: "dia4",
    tag: "Constitucional — Direitos Sociais",
    question: "Quais são os limites constitucionais de jornada de trabalho para empregados urbanos e rurais (Art. 7º, XIII)?",
    answer: "Até 8 HORAS diárias e até 44 HORAS semanais.",
    explanation: "É facultada a compensação de horários e a redução de jornada mediante acordo ou convenção coletiva de trabalho."
  },
  {
    id: 43,
    category: "constitucional",
    day: "dia4",
    tag: "Constitucional — Menores de Idade",
    question: "Quais são as 3 idades-chave para o trabalho de menores segundo a CF/88 (Art. 7º, XXXIII)?",
    answer: "• 18 anos: Proibido trabalho noturno, perigoso ou insalubre.\n• 16 anos: Proibido qualquer trabalho em geral.\n• 14 anos: Permitido exclusivamente na condição de APRENDIZ.",
    explanation: "Atenção: A INBRASP adora tentar colocar aprendiz a partir de 12 anos ou trocar 16 por 14 anos na regra geral!"
  },
  {
    id: 44,
    category: "constitucional",
    day: "dia4",
    tag: "Constitucional — Horas Extras e Férias",
    question: "Qual o percentual MÍNIMO de adicional de horas extras e o acréscimo de férias na CF/88?",
    answer: "• Hora extra: no mínimo 50% superior à hora normal.\n• Férias: acréscimo de pelo menos 1/3 (um terço) a mais do salário normal.",
    explanation: "Art. 7º, XVI e XVII da CF/88."
  },
  {
    id: 45,
    category: "constitucional",
    day: "dia4",
    tag: "Constitucional — Estabilidade Sindical",
    question: "Qual o período da estabilidade provisória do dirigente sindical (Art. 8º, VIII da CF)?",
    answer: "A partir do registro da candidatura e, se eleito (mesmo suplente), até 1 ANO após o término do mandato.",
    explanation: "Salvo se cometer falta grave devidamente apurada nos termos da lei."
  },
  {
    id: 46,
    category: "legislacao",
    day: "dia4",
    tag: "Lei Orgânica de Meruoca",
    question: "Quem são os únicos detentores dos Poderes Políticos no âmbito do Município de Meruoca?",
    answer: "O Poder Legislativo (Câmara Municipal) e o Poder Executivo (Prefeitura).",
    explanation: "Município NÃO possui Poder Judiciário nem Ministério Público local. O Judiciário é estadual."
  },
  {
    id: 47,
    category: "legislacao",
    day: "dia4",
    tag: "Lei Orgânica de Meruoca",
    question: "Qual a diferença essencial entre Competência Privativa e Competência Comum do Município de Meruoca?",
    answer: "• Privativa: Assuntos de interesse estritamente local, tributos municipais, fixação de tarifas e zoneamento urbano.\n• Comum: Saúde, proteção ao meio ambiente, educação e assistência pública (exercida em cooperação com Estado e União).",
    explanation: "Competência privativa = só o município faz; comum = município, Estado e União atuam juntos."
  },
  {
    id: 48,
    category: "especificos",
    day: "w2_d3",
    tag: "Processo Legislativo — Espécies Normativas (CF art. 59)",
    question: "Quais são as 7 espécies normativas do Processo Legislativo Constitucional segundo o Art. 59 da CF/88?",
    answer: "1. Emendas à Constituição;\n2. Leis Complementares;\n3. Leis Ordinárias;\n4. Leis Delegadas;\n5. Medidas Provisórias;\n6. Decretos Legislativos;\n7. Resoluções.",
    explanation: "No âmbito municipal típico não existem Leis Delegadas nem Medidas Provisórias; os atos principais são Leis, Decretos Legislativos e Resoluções."
  },
  {
    id: 49,
    category: "especificos",
    day: "w2_d3",
    tag: "Processo Legislativo — Quóruns de Aprovação",
    question: "Qual a diferença de quórum de aprovação entre LEI COMPLEMENTAR e LEI ORDINÁRIA?",
    answer: "• Lei Complementar: Exige MAIORIA ABSOLUTA (primeiro número inteiro superior à metade de TODOS os membros da Casa).\n• Lei Ordinária: Exige MAIORIA SIMPLES (maioria dos votos dos presentes na sessão, presente a maioria absoluta).",
    explanation: "Pegadinha INBRASP: Confundir maioria simples (relativa) com maioria absoluta."
  },
  {
    id: 50,
    category: "especificos",
    day: "w2_d3",
    tag: "Processo Legislativo — Veto e Prazos",
    question: "Qual o prazo para o Chefe do Executivo vetar um projeto de lei e qual o quórum para a Câmara DERRUBAR o veto?",
    answer: "• Prazo para veto: 15 DIAS ÚTEIS (o silêncio importa sanção tácita).\n• Derrubada do veto: MAIORIA ABSOLUTA dos membros da Câmara no prazo de 30 dias.",
    explanation: "Se o veto não for apreciado em 30 dias corridos, sobresta as demais proposições da pauta (tranca a pauta)."
  },
  {
    id: 51,
    category: "especificos",
    day: "w2_d2",
    tag: "Técnico Legislativo — Funções da Câmara",
    question: "Quais são as 2 funções TÍPICAS e as 2 funções ATÍPICAS da Câmara Municipal de Meruoca?",
    answer: "• Típicas: LEGISLAR (produzir leis) e FISCALIZAR (controle contábil, orçamentário e político).\n• Atípicas: ADMINISTRAR (gerir sua estrutura e servidores) e JULGAR (julgar Prefeito e Vereadores por infrações político-administrativas).",
    explanation: "A função julgadora exige quórum qualificado de dois terços (2/3) para cassação."
  },
  {
    id: 52,
    category: "administrativo",
    day: "w1_d5",
    tag: "D. Administrativo — Atributos do Ato (PATI)",
    question: "Quais são os 4 atributos do ato administrativo? (Mnemônico PATI)",
    answer: "• P = Presunção de Legitimidade e Veracidade\n• A = Autoexecutoriedade\n• T = Tipicidade\n• I = Imperatividade (Poder Extroverso)",
    explanation: "A imperatividade e a autoexecutoriedade não estão presentes em todos os atos (ex.: certidões e atestados)."
  },
  {
    id: 53,
    category: "administrativo",
    day: "w1_d5",
    tag: "D. Administrativo — Poder de Polícia",
    question: "Qual a diferença essencial entre Polícia Administrativa e Polícia Judiciária?",
    answer: "• Polícia Administrativa: Incide sobre BENS, DIREITOS e ATIVIDADES; predominantemente PREVENTIVA; exercida por órgãos administrativos da prefeitura.\n• Polícia Judiciária: Incide sobre PESSOAS; predominantemente REPRESSIVA; exercida por órgãos de segurança pública.",
    explanation: "Conceito clássico do Art. 78 do CTN recorrente nas provas da banca INBRASP."
  },
  {
    id: 54,
    category: "informatica",
    day: "w2_d3",
    tag: "Informática — Fórmulas do Excel",
    question: "No MS Excel, qual a diferença entre =CONT.VALORES(A1:A10) e =CONT.NÚM(A1:A10)?",
    answer: "• =CONT.VALORES: Conta qualquer célula NÃO VAZIA (números, textos, datas e erros).\n• =CONT.NÚM: Conta EXCLUSIVAMENTE as células que contêm valores numéricos.",
    explanation: "Para contar células em branco utiliza-se a função =CONTAR.VAZIO(A1:A10)."
  },
  {
    id: 55,
    category: "informatica",
    day: "w2_d3",
    tag: "Informática — Atalhos de Teclado",
    question: "No Windows 11 e MS Word (versão em português), quais são os atalhos para: Salvar documento e Captura de tela parcial?",
    answer: "• Salvar no Word PT-BR: Ctrl + B (No LibreOffice e navegadores é Ctrl + S)\n• Captura de tela parcial: Windows + Shift + S",
    explanation: "A banca INBRASP costuma explorar a diferença entre Ctrl+B (Word PT) e Ctrl+S (Browsers/Office EN)."
  },
  {
    id: 56,
    category: "portugues",
    day: "w2_d2",
    tag: "Português — Conjunções Subordinativas",
    question: "Qual o valor semântico exato das conjunções: 'CONQUANTO', 'CONTANTO QUE' e 'POR CONSEGUINTE'?",
    answer: "• CONQUANTO = Concessão (embora, ainda que)\n• CONTANTO QUE = Condição (caso, desde que)\n• POR CONSEGUINTE = Conclusão (portanto, logo, por isso)",
    explanation: "Pegadinha INBRASP: Conquanto NUNCA é conclusão; expressa oposição concessiva!"
  },
  {
    id: 57,
    category: "legislacao",
    day: "w2_d5",
    tag: "Técnica Legislativa — LC 95/1998",
    question: "Qual a hierarquia e forma correta de desdobramento de um Artigo segundo a Lei Complementar 95/1998?",
    answer: "• O Artigo desdobra-se em PARÁGRAFOS (§) ou em INCISOS (I, II, III).\n• Os Incisos desdobram-se em ALÍNEAS (a, b, c).\n• As Alíneas desdobram-se em ITENS (1, 2, 3).",
    explanation: "Artigos de 1 a 9 usam numeração ordinal (Art. 1º ao 9º); de 10 em diante usam cardinais (Art. 10, 11, etc.)."
  }
];

// =========================================================================
// BANCO OFICIAL DE QUESTÕES INBRASP (30 Questões - 4 Alternativas)
// =========================================================================
const QUIZ_QUESTIONS_DATA = [
  {
    "id": 1,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, XI (Inviolabilidade do Domicílio)",
    "question": "Conforme o Art. 5º, XI, da CF/88, a casa é asilo inviolável do indivíduo. A entrada no domicílio sem o consentimento do morador por determinação judicial só pode ocorrer:",
    "options": [
      "Durante o dia.",
      "A qualquer hora do dia ou da noite.",
      "Apenas durante a noite, com a presença de testemunhas.",
      "Em dias úteis, no período das 6h às 22h."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 5º, XI da CF/88: 'A casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, salvo em caso de flagrante delito ou desastre, ou para prestar socorro, ou, durante o dia, por determinação judicial'."
  },
  {
    "id": 2,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, XLII e XLIV (Crimes Inafiançáveis e Imprescritíveis)",
    "question": "Segundo a Constituição Federal de 1988, constituem crimes inafiançáveis e imprescritíveis:",
    "options": [
      "A prática da tortura e o tráfico ilícito de entorpecentes.",
      "Os crimes hediondos e o terrorismo.",
      "A prática do racismo e a ação de grupos armados contra a ordem constitucional.",
      "O roubo qualificado e a corrupção passiva."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Mnemônico 'RAÇÃO': Racismo (Art. 5º, XLII) e Ação de grupos armados, civis ou militares, contra a ordem constitucional e o Estado Democrático (Art. 5º, XLIV) são os dois únicos crimes inafiançáveis e imprescritíveis na CF/88."
  },
  {
    "id": 3,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, XLIII (Crimes Inafiançáveis e Insuscetíveis de Graça)",
    "question": "A Constituição Federal define o crime de tráfico ilícito de entorpecentes e drogas afins como:",
    "options": [
      "Imprescritível e afiançável mediante depósito judicial.",
      "Inafiançável e insuscetível de graça ou anistia.",
      "Suscetível de graça, desde que cumprido 1/3 da pena.",
      "Prescritível e passível de liberdade provisória com fiança."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 5º, XLIII da CF/88: Os crimes '3T.H' (Tráfico de drogas, Tortura, Terrorismo e Hediondos) são inafiançáveis e insuscetíveis de graça ou anistia."
  },
  {
    "id": 4,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, LXVIII (Habeas Corpus)",
    "question": "O remédio constitucional cabível para garantir a liberdade de locomoção, sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de ir e vir, por ilegalidade ou abuso de poder, é o:",
    "options": [
      "Habeas Corpus.",
      "Mandado de Segurança.",
      "Habeas Data.",
      "Mandado de Injunção."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 5º, LXVIII da CF/88: Conceder-se-á Habeas Corpus sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder."
  },
  {
    "id": 5,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, LXXII (Habeas Data)",
    "question": "A respeito do Habeas Data (Art. 5º, LXXII), assinale a afirmativa correta:",
    "options": [
      "Pode ser impetrado para requerer certidões sobre atos e contratos de terceiros.",
      "Destina-se a assegurar o conhecimento de informações relativas à pessoa do impetrante, constantes de registros de entidades governamentais.",
      "É uma ação judicial onerosa que exige o recolhimento prévio de taxas.",
      "Não exige a intervenção de advogado para a sua propositura em juízo."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 5º, LXXII da CF/88: O Habeas Data é ação personalíssima para assegurar o conhecimento/retificação de informações relativas à pessoa do impetrante em bancos de dados governamentais. É gratuito (Art. 5º, LXXVII), mas exige advogado."
  },
  {
    "id": 6,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, LXIX (Mandado de Segurança)",
    "question": "Para proteger direito líquido e certo, não amparado por Habeas Corpus ou Habeas Data, quando o responsável pela ilegalidade for autoridade pública, concede-se:",
    "options": [
      "Mandado de Segurança.",
      "Ação Popular.",
      "Mandado de Injunção.",
      "Arguição de Descumprimento de Preceito Fundamental."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 5º, LXIX da CF/88: Conceder-se-á Mandado de Segurança para proteger direito líquido e certo, não amparado por Habeas Corpus ou Habeas Data, contra ilegalidade de autoridade pública."
  },
  {
    "id": 7,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Mandado de Segurança (Prazo Decadencial)",
    "question": "O prazo decadencial para a impetração de Mandado de Segurança é de:",
    "options": [
      "30 dias contados da publicação da portaria.",
      "60 dias contados da ocorrência do fato danoso.",
      "90 dias contados da notificação do ato coator.",
      "120 dias contados da ciência, pelo interessado, do ato impugnado."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 23 da Lei nº 12.016/2009 e Súmula 632 do STF: Prazo decadencial de 120 dias contados da ciência do ato impugnado."
  },
  {
    "id": 8,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, LXXI (Mandado de Injunção)",
    "question": "Sempre que a falta de norma regulamentadora tornar inviável o exercício dos direitos e liberdades constitucionais e das prerrogativas inerentes à nacionalidade, à soberania e à cidadania, conceder-se-á:",
    "options": [
      "Habeas Corpus.",
      "Mandado de Segurança Coletivo.",
      "Mandado de Injunção.",
      "Ação Civil Pública."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 5º, LXXI da CF/88: Conceder-se-á Mandado de Injunção diante da ausência de norma regulamentadora que inviabilize o exercício de direito constitucional."
  },
  {
    "id": 9,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, LXXIII (Ação Popular)",
    "question": "A legitimidade ativa para a propositura de Ação Popular (Art. 5º, LXXIII) pertence exclusivamente ao:",
    "options": [
      "Membro do Ministério Público.",
      "Estrangeiro residente há mais de cinco anos no país.",
      "Partido político com representação na Câmara Municipal.",
      "Cidadão no gozo de seus direitos políticos."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 5º, LXXIII da CF/88: 'Qualquer cidadão é parte legítima para propor ação popular...'. A cidadania comprova-se pelo título de eleitor."
  },
  {
    "id": 10,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, IV (Manifestação do Pensamento)",
    "question": "A manifestação do pensamento é garantida a todos no Art. 5º, IV, da CF/88, sendo expressamente:",
    "options": [
      "Permitida sob a égide do anonimato.",
      "Condicionada à aprovação prévia de órgão censor municipal.",
      "Restrita a maiores de 21 anos em pleno gozo de direitos civis.",
      "Vedado o anonimato."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 5º, IV da CF/88: 'É livre a manifestação do pensamento, sendo vedado o anonimato'."
  },
  {
    "id": 11,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, XII (Sigilo das Comunicações)",
    "question": "A inviolabilidade do sigilo da correspondência e das comunicações telegráficas e de dados é garantida pela CF/88. Já a interceptação de comunicações telefônicas:",
    "options": [
      "Pode ser realizada por ordem judicial, para fins de investigação criminal ou instrução processual penal.",
      "É terminantemente proibida sob qualquer hipótese no território nacional.",
      "Pode ser determinada por autoridade policial durante o inquérito administrativo.",
      "Depende de autorização do Presidente da Câmara Municipal quando envolver servidores públicos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 5º, XII da CF/88: A quebra de sigilo telefônico exige ordem judicial para fins de investigação criminal ou instrução processual penal."
  },
  {
    "id": 12,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, XVI (Direito de Reunião)",
    "question": "No que diz respeito ao direito de reunião pacífica (Art. 5º, XVI), a Constituição Federal exige que:",
    "options": [
      "Haja prévia autorização da autoridade policial competente.",
      "Não haja frustração de outra reunião anteriormente convocada para o mesmo local, sendo exigido prévio aviso.",
      "Os participantes estejam armados para garantir a própria segurança.",
      "O número de participantes seja previamente aprovado pelo Poder Executivo local."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 5º, XVI da CF/88: Reunião pacífica sem armas independe de autorização, exigindo-se apenas prévio aviso à autoridade."
  },
  {
    "id": 13,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, XVII e XVIII (Liberdade de Associação)",
    "question": "Sobre a criação e funcionamento de associações (Art. 5º, XVII a XXI):",
    "options": [
      "O Poder Executivo pode dissolver compulsoriamente uma associação por meio de decreto.",
      "As atividades de uma associação só podem ser suspensas por ato fundamentado do delegado de polícia.",
      "Ninguém poderá ser compelido a associar-se, exceto se houver previsão em convenção coletiva.",
      "A criação independe de autorização e é vedada a interferência estatal em seu funcionamento."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 5º, XVIII da CF/88: A criação de associações independe de autorização e é vedada a interferência estatal em seu funcionamento."
  },
  {
    "id": 14,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, XXV (Requisição Administrativa)",
    "question": "Em caso de iminente perigo público, a autoridade competente poderá usar de propriedade particular, assegurada ao proprietário:",
    "options": [
      "Indenização prévia, justa e em títulos da dívida pública.",
      "Indenização ulterior, se houver dano.",
      "Isenção permanente de tributos imobiliários sobre o imóvel.",
      "Nenhuma contraprestação financeira por se tratar de encargo cívico."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 5º, XXV da CF/88: Na requisição administrativa por iminente perigo público, a indenização é ulterior (posterior) e condicionada ao dano."
  },
  {
    "id": 15,
    "category": "constitucional",
    "discipline": "D. Constitucional",
    "topic": "Art. 5º, XXXVIII (Tribunal do Júri)",
    "question": "É reconhecida a instituição do júri pela CF/88, com a organização que lhe der a lei, assegurada expressamente a competência para o julgamento dos:",
    "options": [
      "Crimes praticados por servidores públicos contra a administração em geral.",
      "Crimes de responsabilidade praticados por prefeitos e vereadores.",
      "Crimes dolosos contra a vida.",
      "Crimes culposos de trânsito que resultem em morte."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 5º, XXXVIII, alínea 'd' da CF/88: Competência do Tribunal do Júri para julgamento dos crimes dolosos contra a vida."
  },
  {
    "id": 16,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Tipologia Textual: Narração",
    "question": "O tipo textual que se caracteriza pela sucessão temporal de fatos e pela presença de personagens, narrador, tempo e espaço denomina-se:",
    "options": [
      "Narrativo.",
      "Expositivo.",
      "Descritivo.",
      "Injuntivo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O tipo narrativo estrutura-se em torno de uma sequência de acontecimentos no tempo e no espaço vividos por personagens."
  },
  {
    "id": 17,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Tipologia Textual: Descrição",
    "question": "O excerto 'O casarão antigo possuía portas largas de madeira escura, paredes descascadas pelo tempo e um assoalho de tábuas corridas que rangia' classifica-se predominantemente como:",
    "options": [
      "Argumentativo.",
      "Descritivo.",
      "Injuntivo.",
      "Expositivo."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A tipologia descritiva constrói um retrato estático de um ambiente ou objeto com adjetivos e qualificadores."
  },
  {
    "id": 18,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Tipologia Textual: Dissertação Argumentativa",
    "question": "O texto que se estrutura com o objetivo principal de defender um ponto de vista (tese), recorrendo a argumentos, dados e raciocínio lógico para convencer o leitor, é do tipo:",
    "options": [
      "Dissertativo-argumentativo.",
      "Narrativo.",
      "Dissertativo-expositivo.",
      "Instrucional."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O texto dissertativo-argumentativo visa persuadir o leitor por meio da defesa de uma tese com argumentos lógicos."
  },
  {
    "id": 19,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Tipologia Textual: Injunção / Instrução",
    "question": "Os manuais de instalação de equipamentos, receitas culinárias e bulas de medicamentos (na seção posologia) têm em comum a presença de verbos no imperativo ou infinitivo com instruções ao leitor. Essa tipologia é a:",
    "options": [
      "Descritiva.",
      "Narrativa.",
      "Dialógica.",
      "Injuntiva ou instrucional."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O tipo textual injuntivo orienta ou instrui ações ao leitor com verbos no imperativo ou infinitivo."
  },
  {
    "id": 20,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Gênero Textual: Editorial",
    "question": "Assinale a alternativa que define corretamente o gênero textual Editorial:",
    "options": [
      "Texto jornalístico que expressa o posicionamento institucional da empresa/jornal e não leva assinatura individual.",
      "Texto assinado por um colunista que expressa sua visão pessoal e subjetiva sobre um fato.",
      "Comunicação estritamente interna trocada entre departamentos de uma mesma empresa.",
      "Relatório técnico produzido por peritos judiciais para embasar decisões do tribunal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Editorial expressa a opinião do jornal/empresa de comunicação e não leva assinatura de um articulista individual."
  },
  {
    "id": 21,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Redação Oficial: Ofício",
    "question": "A comunicação formal e padronizada emitida por autoridades públicas para tratar de assuntos oficiais de serviço com outras autoridades ou cidadãos denomina-se:",
    "options": [
      "Ofício.",
      "Carta comercial.",
      "Abaixo-assinado.",
      "Artigo de opinião."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Ofício é o documento padrão de comunicação da Administração Pública com outras entidades ou cidadãos."
  },
  {
    "id": 22,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Funções da Linguagem: Conotativa / Apelativa",
    "question": "Em um cartaz institucional afixado em repartição pública constam os dizeres: 'Economize energia elétrica. Apague as lâmpadas ao sair da sala.' O texto emprega tipologia injuntiva com a função de linguagem predominantemente:",
    "options": [
      "Fática.",
      "Emotiva.",
      "Conotativa (ou apelativa).",
      "Metalinguística."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A função conotativa/apelativa busca influenciar e orientar o comportamento do leitor ('economize', 'apague')."
  },
  {
    "id": 23,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Teoria Textual: Tipo vs. Gênero",
    "question": "Sobre a diferença entre Tipo Textual e Gênero Textual, é correto afirmar que:",
    "options": [
      "Os tipos textuais são infinitos e adaptáveis às situações sociais do cotidiano.",
      "Os gêneros textuais constituem um conjunto fixo e fechado de apenas cinco modelos gramaticais.",
      "Os tipos textuais dizem respeito à estrutura formal interna do texto, enquanto os gêneros referem-se aos usos sociais da língua.",
      "Não há diferença técnica entre eles, sendo termos perfeitamente sinônimos em concursos públicos."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Tipos textuais são modelos teóricos finitos (5 estruturas); gêneros textuais são infinitos e práticos (usos sociais)."
  },
  {
    "id": 24,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Gênero Textual: Artigo de Divulgação Científica",
    "question": "Um texto de Artigo de Divulgação Científica tem como finalidade primordial:",
    "options": [
      "Contar uma narrativa fictícia com elementos mágicos e fabulosos.",
      "Transmitir conhecimentos científicos ao público geral por meio de linguagem acessível e informativa.",
      "Vender produtos cosméticos por meio de apelos emocionais e imagens publicitárias.",
      "Estabelecer normas jurídicas imperativas para cumprimento obrigatório de pesquisadores."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O artigo de divulgação científica adapta a linguagem acadêmica para informar o público leigo."
  },
  {
    "id": 25,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Gênero Textual: Artigo de Opinião",
    "question": "O gênero textual Artigo de Opinião caracteriza-se formalmente por:",
    "options": [
      "Apresentar a visão neutra do veículo de comunicação sem a identificação do autor.",
      "Conter exclusivamente tabelas numéricas e dados matemáticos sem texto explicativo.",
      "Limitar-se a narrar uma sequência cronológica de eventos policiais sem emitir juízo de valor.",
      "Ser um texto argumentativo assinado pelo próprio autor, que assume a responsabilidade pela tese defendida."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O Artigo de Opinião é assinado pelo articulista e defende uma tese com argumentação subjetiva."
  },
  {
    "id": 26,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Gênero Textual: Carta Comercial",
    "question": "A correspondência escrita formal utilizada especificamente no meio corporativo e privado para transações mercantis, pedidos de cotação ou cobranças é a:",
    "options": [
      "Petição inicial.",
      "Portaria ministerial.",
      "Carta comercial.",
      "Notícia de jornal."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A Carta Comercial é o gênero formal para comunicação de negócios entre empresas privadas."
  },
  {
    "id": 27,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Tipologia Textual: Dissertação Expositiva",
    "question": "O trecho 'A inflação é o aumento persistente e generalizado dos preços em uma economia. Ocorre quando a demanda por bens supera a capacidade produtiva' exemplifica a tipologia:",
    "options": [
      "Narrativa.",
      "Dissertativa-expositiva.",
      "Injuntiva.",
      "Prescritiva."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A dissertação expositiva define e explica um conceito com neutralidade e impessoalidade."
  },
  {
    "id": 28,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Semiótica: Texto Multimodal / Misto",
    "question": "Um anúncio publicitário que mescla ilustrações, cores contrastantes, slogan curto e texto explicativo é considerado um texto:",
    "options": [
      "Exclusivamente não-verbal.",
      "Puramente descritivo sem intenção persuasiva.",
      "Científico rigoroso.",
      "Multimodal (ou misto), por conjugar recursos verbais e visuais."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Textos multimodais conjugam linguagem verbal e não-verbal (imagens, cores, diagramação)."
  },
  {
    "id": 29,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Gênero Textual: Crônica",
    "question": "O gênero Crônica destaca-se na imprensa e na literatura por:",
    "options": [
      "Registrar normas regimentais e decretos administrativos com rigor técnico.",
      "Exigir obrigatoriamente a assinatura de um colegiado de juristas para ser publicado.",
      "Abordar situações cotidianas e corriqueiras com estilo leve, reflexivo e por vezes poético.",
      "Apresentar fórmulas matemáticas aplicadas a cálculos orçamentários."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A crônica parte de fatos cotidianos para desenvolver reflexões leves, críticas ou bem-humoradas."
  },
  {
    "id": 30,
    "category": "portugues",
    "discipline": "Língua Portuguesa",
    "topic": "Tipologia Textual: Prescrição / Sinalização",
    "question": "A placa indicativa que estampa 'Velocidade máxima permitida: 60 km/h' possui caráter essencialmente:",
    "options": [
      "Narrativo ficcional.",
      "Prescritivo / Injuntivo.",
      "Descritivo poético.",
      "Argumentativo subjetivo."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Placas com regras e ordens obrigatórias possuem caráter prescritivo/injuntivo."
  },
  {
    "id": 31,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Princípios Expressos (Art. 37, caput CF/88)",
    "question": "Conforme o Art. 37, caput, da Constituição Federal de 1988, a administração pública direta e indireta de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios obedecerá aos seguintes princípios expressos:",
    "options": [
      "Legalidade, Supremacia do interesse público, Moralidade, Finalidade e Eficiência.",
      "Legalidade, Impessoalidade, Moralidade, Publicidade e Eficiência.",
      "Proporcionalidade, Impessoalidade, Razoabilidade, Publicidade e Celeridade.",
      "Legalidade, Isonomia, Moralidade, Transparência e Motivação."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 37, caput da CF/88 (Mnemônico LIMPE): Legalidade, Impessoalidade, Moralidade, Publicidade e Eficiência (incluído pela EC 19/98)."
  },
  {
    "id": 32,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Princípio da Impessoalidade (Vedação de Promoção Pessoal)",
    "question": "De acordo com o Art. 37, § 1º, da CF/88, a publicidade dos atos, programas, obras, serviços e campanhas dos órgãos públicos deverá ter caráter educativo, informativo ou de orientação social, dela não podendo constar nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades ou servidores públicos. Tal comando decorre diretamente do princípio da:",
    "options": [
      "Continuidade do serviço público.",
      "Autotutela.",
      "Especialidade.",
      "Impessoalidade."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A vedação de nomes, símbolos e imagens para autopromoção de prefeitos/vereadores é aplicação direta do princípio da IMPESSOALIDADE."
  },
  {
    "id": 33,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Princípio da Moralidade & Súmula Vinculante 13 (Nepotismo)",
    "question": "A nomeação de cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau, da autoridade nomeante para o exercício de cargo em comissão ou de confiança viola a Constituição Federal (Súmula Vinculante nº 13 do STF). Essa proibição fundamenta-se principalmente no princípio da:",
    "options": [
      "Moralidade administrativa.",
      "Eficiência econômica.",
      "Subsidiariedade.",
      "Segurança jurídica."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A vedação ao nepotismo (Súmula Vinculante 13) tem como pilar maior a MORALIDADE e a Impessoalidade administrativa."
  },
  {
    "id": 34,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Princípio da Autotutela (Súmulas 346 e 473 do STF)",
    "question": "A prerrogativa conferida à Administração Pública de rever seus próprios atos, anulando os ilegais e revogando os inoportunos ou inconvenientes, sem a necessidade de intervenção judicial prévia, decorre do princípio da:",
    "options": [
      "Autotutela.",
      "Legalidade estrita.",
      "Continuidade.",
      "Razoabilidade."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Princípio da Autotutela (Súmulas 346 e 473 do STF): a Administração anula atos ilegais (efeito ex tunc) e revoga atos inoportunos (efeito ex nunc)."
  },
  {
    "id": 35,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Organização Administrativa: Desconcentração vs. Descentralização",
    "question": "A distribuição interna de competências e atribuições dentro de uma mesma pessoa jurídica, criando uma relação de subordinação hierárquica e dando origem a órgãos públicos despersonalizados, denomina-se:",
    "options": [
      "Descentralização por serviços.",
      "Delegação por colaboração.",
      "Terceirização administrativa.",
      "Desconcentração."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. DescoNcentração (com 'O' de Órgão): distribuição interna de atribuições na mesma pessoa. DesceNtralização (com 'E' de Entidade): criação de nova pessoa jurídica."
  },
  {
    "id": 36,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Administração Indireta: Criação de Autarquias",
    "question": "Sobre as entidades que integram a Administração Pública Indireta, assinale a entidade que é criada DIRETAMENTE por lei específica e possui personalidade jurídica de direito público:",
    "options": [
      "Autarquia.",
      "Empresa Pública.",
      "Sociedade de Economia Mista.",
      "Fundação Pública de direito privado."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 37, XIX da CF/88: Somente a AUTARQUIA é criada diretamente por lei específica. As demais entidades têm sua criação autorizada por lei."
  },
  {
    "id": 37,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Sociedade de Economia Mista (Forma Societária)",
    "question": "A respeito das Sociedades de Economia Mista, assinale a afirmativa correta segundo o regime jurídico-constitucional brasileiro:",
    "options": [
      "Seu capital social é integralmente pertencente ao Poder Público.",
      "Possuem personalidade jurídica de direito público e seus bens são inpenhoráveis.",
      "Podem adotar qualquer formato societário, como Sociedade Limitada (Ltda).",
      "Devem ser constituídas obrigatoriamente sob a forma de Sociedade Anônima (S/A)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Sociedades de Economia Mista adotam OBRIGATORIAMENTE a forma de S/A (Art. 235 da Lei 6.404/76 e Art. 4º da Lei 13.303/16). Já a Empresa Pública pode adotar qualquer formato."
  },
  {
    "id": 38,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Empresa Pública vs. Sociedade de Economia Mista (Capital)",
    "question": "Uma Empresa Pública distingue-se de uma Sociedade de Economia Mista quanto à composição de seu capital porque a Empresa Pública:",
    "options": [
      "Admite a participação de capital privado minoritário na sua constituição.",
      "É criada obrigatoriamente sob a forma de cooperativa sem fins lucrativos.",
      "Possui seu capital social formado 100% (exclusivamente) por recursos públicos.",
      "Não se submete à fiscalização do Tribunal de Contas respectivo."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O capital social da Empresa Pública é 100% público (da União, Estados ou Municípios). Na SEM, o capital é misto (maioria com direito a voto pública)."
  },
  {
    "id": 39,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Teoria do Órgão / Imputação Volitiva",
    "question": "A teoria adotada no Brasil segundo a qual a manifestação de vontade dos agentes públicos é diretamente atribuída (imputada) à pessoa jurídica a qual pertencem denomina-se:",
    "options": [
      "Teoria do Órgão (ou da Imputação Volitiva).",
      "Teoria do Mandato.",
      "Teoria da Representação.",
      "Teoria do Risco Integral."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A Teoria do Órgão (criada por Otto Gierke) estabelece que a atuação do servidor/agente é imputada diretamente à pessoa jurídica (ente estatal)."
  },
  {
    "id": 40,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Órgãos Públicos (Personalidade e Capacidade)",
    "question": "Os órgãos públicos são centros de competência desprovidos de personalidade jurídica própria. Como regra geral em juízo, os órgãos públicos:",
    "options": [
      "Podem ser réus diretos em qualquer ação de cobrança sem representação do Município.",
      "Têm patrimônio próprio separado das contas gerais da Prefeitura ou Câmara.",
      "Podem emitir notas fiscais comerciais em nome próprio para prestar serviços a terceiros.",
      "Não possuem capacidade processual, cabendo ao ente federativo figurar no polo da ação."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Como regra geral, órgãos não possuem capacidade processual nem patrimônio próprio; quem responde em juízo é a pessoa jurídica (ex: Município de Meruoca)."
  },
  {
    "id": 41,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Princípio da Proporcionalidade e Razoabilidade",
    "question": "O princípio que impõe à Administração Pública e aos seus agentes a adequação entre os meios empregados e os fins a serem alcançados, vedando a imposição de restrições ou sanções em medida superior à estritamente necessária, é o princípio da:",
    "options": [
      "Continuidade do serviço.",
      "Publicidade.",
      "Hierarquia funcional.",
      "Proporcionalidade e Razoabilidade."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A Razoabilidade e a Proporcionalidade proíbem o excesso de poder e exigem a justa medida entre meios e fins na atuação administrativa."
  },
  {
    "id": 42,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Autarquias (Imunidade Tributária Recíproca)",
    "question": "As Autarquias gozam de prerrogativas próprias de entidades de direito público. Entre elas destaca-se expressamente na CF/88:",
    "options": [
      "Isenção absoluta de prestar concurso público para admissão de seus servidores.",
      "Imunidade tributária recíproca sobre seu patrimônio, renda e serviços vinculados às suas finalidades essenciais.",
      "Livre contratação de serviços e compras sem necessidade de licitação.",
      "Possibilidade de decretação de falência por credores privados."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 150, § 2º da CF/88: A imunidade tributária recíproca é expressamente extensiva às autarquias e fundações mantidas pelo Poder Público."
  },
  {
    "id": 43,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Princípio da Continuidade do Serviço Público",
    "question": "O princípio da Continuidade do Serviço Público fundamenta diversas regras na administração, EXCETO:",
    "options": [
      "A exigência de regras rígidas para manutenção de serviços essenciais em caso de greve.",
      "A autorização para que o servidor público abandone suas funções a qualquer momento sem responder por processo disciplinar.",
      "A prerrogativa da administração de utilizar equipamentos do contratado para evitar paralisação de serviço essencial.",
      "A restrição temporária à rescisão unilateral imediata por parte de concessionárias privadas."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O abandono de cargo é falta funcional gravíssima que gera demissão, decorrendo justamente do dever de continuidade dos serviços públicos."
  },
  {
    "id": 44,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Fundações Públicas (Art. 37, XIX CF/88)",
    "question": "Segundo o Art. 37, XIX, da CF/88, as Fundações Públicas:",
    "options": [
      "São criadas diretamente por decreto do Chefe do Poder Executivo.",
      "Não necessitam de autorização em lei, bastando registro em cartório civil.",
      "Têm sua criação autorizada por lei específica, cabendo a lei complementar definir as áreas de sua atuação.",
      "Devem atuar exclusivamente na exploração comercial com fins lucrativos."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 37, XIX da CF/88: Somente por lei específica é autorizada a instituição de fundação pública, cabendo a lei complementar definir as áreas de sua atuação."
  },
  {
    "id": 45,
    "category": "administrativo",
    "day": "dia3",
    "discipline": "D. Administrativo",
    "topic": "Princípio da Segurança Jurídica & Confiança Legítima",
    "question": "O princípio da Segurança Jurídica, em sua vertente de Proteção à Confiança Legítima, visa precipuamente a:",
    "options": [
      "Garantir que qualquer servidor possa alterar regras de editais após a homologação do concurso.",
      "Permitir a anulação de atos favoráveis ao administrado a qualquer tempo, mesmo após decorridos 40 anos.",
      "Proteger a boa-fé do administrado contra alterações retroativas e abruptas de interpretação normativa pela administração.",
      "Impedir que o Poder Legislativo crie ou altere leis municipais."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A proteção à confiança legítima (vertente subjetiva da segurança jurídica) impede que novas interpretações retroajam para prejudicar situações consolidadas de boa-fé."
  },
  {
    "id": 46,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Windows 11: Caracteres Proibidos em Nomes de Arquivos",
    "question": "No sistema operacional Microsoft Windows 11, ao tentar renomear um arquivo ou pasta, o usuário é impedido de utilizar determinados caracteres reservados pelo sistema. Assinale a alternativa que contém apenas caracteres PROIBIDOS em nomes de arquivos no Windows:",
    "options": [
      "@ # $ % _ - +",
      "\\ / : * ? \" < > |",
      "( ) [ ] { } .",
      "! & = ~ ^ ;"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Os 9 caracteres proibidos no Windows são: barras (\\ /), dois pontos (:), asterisco (*), interrogação (?), aspas (\"), menor (<), maior (>) e pipe (|)."
  },
  {
    "id": 47,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Windows 11: Atalho de Bloqueio de Tela",
    "question": "No Windows 11, o atalho de teclado padrão utilizado para BLOQUEAR rapidamente o computador ao se ausentar da mesa de trabalho é:",
    "options": [
      "Ctrl + Alt + B",
      "Alt + F4",
      "Logotipo do Windows + L",
      "Ctrl + Shift + Esc"
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Win + L (Lock) bloqueia a sessão imediatamente sem fechar os programas abertos, exigindo senha para desbloqueio."
  },
  {
    "id": 48,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Windows 11: Exclusão Permanente (Shift + Delete)",
    "question": "No Windows 11, ao selecionar um arquivo e pressionar a combinação de teclas Shift + Delete, o sistema:",
    "options": [
      "Move o arquivo para a Lixeira do sistema para posterior restauração.",
      "Cria um atalho na área de trabalho e oculta o arquivo original.",
      "Exclui permanentemente o arquivo sem enviá-lo para a Lixeira.",
      "Envia o arquivo automaticamente por e-mail para a nuvem."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Shift + Delete executa exclusão permanente direta sem passar pela Lixeira do Windows."
  },
  {
    "id": 49,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Windows 11: Atalho do Explorador de Arquivos",
    "question": "O atalho de teclado padrão para abrir instantaneamente o Explorador de Arquivos (File Explorer) no Windows 11 é:",
    "options": [
      "Logotipo do Windows + R",
      "Logotipo do Windows + E",
      "Ctrl + E",
      "Alt + Tab"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Win + E (Explorer) abre o Explorador de Arquivos. Win + R abre o diálogo Executar."
  },
  {
    "id": 50,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Linux Ubuntu: Diretório de Configurações (/etc)",
    "question": "Na estrutura de diretórios do sistema operacional Linux (como o Ubuntu), o diretório responsável por armazenar os arquivos de configuração globais do sistema e dos serviços instalados é o:",
    "options": [
      "/bin",
      "/home",
      "/dev",
      "/etc"
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O diretório /etc armazena arquivos de configuração essenciais de programas e do sistema no Linux."
  },
  {
    "id": 51,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Linux Ubuntu: Diretório dos Usuários (/home)",
    "question": "No Linux Ubuntu, o diretório onde são armazenados os arquivos pessoais, pastas e documentos de cada usuário comum do sistema é o:",
    "options": [
      "/root",
      "/var",
      "/usr",
      "/home"
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O diretório /home contém as pastas de cada usuário comum (ex: /home/ruan). O diretório /root é a pasta pessoal do superusuário."
  },
  {
    "id": 52,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Linux: Comando para Listar Arquivos (ls)",
    "question": "No terminal de comandos do Linux, o comando utilizado para LISTAR os arquivos e subdiretórios contidos no diretório atual é:",
    "options": [
      "ls",
      "cd",
      "pwd",
      "mkdir"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O comando 'ls' (list) lista arquivos e pastas. 'cd' navega, 'pwd' mostra o caminho atual e 'mkdir' cria diretório."
  },
  {
    "id": 53,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Linux: Comando para Criar Diretório (mkdir)",
    "question": "No Linux, para CRIAR um novo diretório chamado 'documentos_camara' via linha de comando no terminal, deve-se utilizar:",
    "options": [
      "rmdir documentos_camara",
      "touch documentos_camara",
      "mkdir documentos_camara",
      "cat documentos_camara"
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. 'mkdir' (make directory) cria novas pastas. 'touch' cria arquivos vazios."
  },
  {
    "id": 54,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Hardware: Memória RAM (Volatilidade)",
    "question": "A respeito da memória RAM (Random Access Memory) de um computador, assinale a afirmativa correta:",
    "options": [
      "É uma memória secundária de armazenamento permanente de fotos e vídeos.",
      "É uma memória volátil, cujo conteúdo é totalmente apagado quando o computador é desligado.",
      "Armazena a BIOS e não pode ser gravada nem alterada pelo usuário.",
      "Possui velocidade de leitura e gravação muito inferior à de um disco rígido tradicional (HD)."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A memória RAM é memória primária e VOLÁTIL: necessita de energia elétrica contínua para reter suas informações."
  },
  {
    "id": 55,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Hardware: Memória ROM / BIOS (Não-volatilidade)",
    "question": "A memória do tipo ROM (Read Only Memory), presente na placa-mãe de computadores, caracteriza-se por:",
    "options": [
      "Ser não-volátil, retendo instruções essenciais de inicialização (firmware/BIOS) mesmo com o computador desligado.",
      "Permitir que o usuário instale programas e salve arquivos pessoais diretamente nela no dia a dia.",
      "Perder todos os dados gravados a cada reinicialização do sistema operacional.",
      "Ter capacidade de armazenamento na ordem de dezenas de Terabytes (TB)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A ROM é NÃO-VOLÁTIL (mantém dados sem energia) e é de somente leitura na operação normal, gravada de fábrica com a BIOS/firmware."
  },
  {
    "id": 56,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Hardware: Comparativo SSD vs. Disco Rígido (HD)",
    "question": "Em comparação aos discos rígidos magnéticos convencionais (HDs), as unidades de estado sólido (SSDs):",
    "options": [
      "Utilizam discos metálicos giratórios que produzem mais ruído e aquecimento.",
      "Utilizam chips de memória flash sem peças móveis mecânicas, oferecendo taxas de transferência muito mais rápidas e maior resistência a impactos.",
      "São muito mais lentas na inicialização do sistema operacional Windows.",
      "Só podem ser conectadas a computadores via rede sem fio (Wi-Fi)."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. SSDs gravam dados em circuitos integrados de memória flash (sem peças mecânicas), sendo muito mais rápidos, silenciosos e resistentes."
  },
  {
    "id": 57,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Hardware: Componentes da CPU (ULA, UC e Registradores)",
    "question": "A Unidade Central de Processamento (CPU) é o cérebro do computador. Ela é composta internamente por três blocos principais fundamentais:",
    "options": [
      "Fonte de alimentação, cooler e placa de som.",
      "Unidade Lógica e Aritmética (ULA), Unidade de Controle (UC) e Registradores.",
      "Teclado, mouse e monitor de vídeo.",
      "Memória Cache, porta USB e leitor óptico de DVD."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A arquitetura clássica da CPU divide-se em: ULA (cálculos matemáticos e lógicos), UC (orquestração das instruções) e Registradores (memória interna)."
  },
  {
    "id": 58,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Backup: Backup Incremental",
    "question": "O tipo de cópia de segurança (backup) que grava APENAS os arquivos que foram criados ou modificados desde o último backup (seja ele um backup completo ou outro incremental) é o:",
    "options": [
      "Backup Completo (Full).",
      "Backup Espelho (Mirror).",
      "Backup Incremental.",
      "Backup Residual."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O Backup Incremental salva apenas as alterações ocorridas desde o último backup realizado, sendo o mais rápido de executar."
  },
  {
    "id": 59,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Backup: Backup Diferencial",
    "question": "A diferença básica entre o Backup DIFERENCIAL e o Backup INCREMENTAL é que o Backup Diferencial:",
    "options": [
      "Copia sempre todos os arquivos criados ou modificados desde o último backup COMPLETO (Full).",
      "Apaga todos os arquivos originais do computador após a conclusão da cópia.",
      "Só pode ser executado em disquetes ou fitas magnéticas antigas.",
      "Não armazena nenhum arquivo com tamanho superior a 1 Megabyte (MB)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Backup Diferencial copia todas as alterações feitas a partir do último backup FULL (acumulando os dados modificados até novo Full)."
  },
  {
    "id": 60,
    "category": "informatica",
    "day": "dia3",
    "discipline": "Informática",
    "topic": "Segurança de Dados: Regra 3-2-1 de Backup",
    "question": "A consagrada regra de segurança de dados '3-2-1 para Backup' recomenda manter:",
    "options": [
      "3 cópias dos dados, em 2 tipos de mídia diferentes, com pelo menos 1 cópia armazenada fora do local de trabalho (offsite/nuvem).",
      "3 computadores ligados ao mesmo tempo, durante 2 horas por dia, com 1 funcionário supervisionando.",
      "3 senhas iguais em 2 sistemas diferentes para 1 único usuário.",
      "3 antivírus instalados simultaneamente na mesma máquina durante 2 dias."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Regra 3-2-1: 3 cópias no total (1 primária + 2 backups), em pelo menos 2 tipos de mídia diferentes, e 1 cópia mantida fora da empresa/offsite (nuvem)."
  },
  {
    "id": 61,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Acentuação Gráfica: Regra das Proparoxítonas",
    "question": "No padrão da banca INBRASP, a regra de acentuação gráfica que justifica o acento na palavra 'LEGISLATIVO' não existe pois a palavra é paroxítona sem acento. Entretanto, assinale a alternativa em que TODAS as palavras são acentuadas rigorosamente pela regra das proparoxítonas:",
    "options": [
      "Técnico, caráter, público e relatório.",
      "Orgânico, histórico, mérito e autarquia.",
      "Político, cômputo, câmara e déficit.",
      "Público, relógio, secretária e país."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Todas as palavras de (A) são proparoxítonas (po-LÍ-ti-co, CÔM-pu-to, CÂ-ma-ra, DÉ-fi-cit), que são 100% acentuadas. Em (B), 'caráter' e 'relatório' são paroxítonas; em (C), 'autarquia' é paroxítona terminada em ditongo; em (D), 'país' é hiato e 'relógio' é paroxítona terminada em ditongo."
  },
  {
    "id": 62,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Acentuação Gráfica: Regra dos Hiatos",
    "question": "Assinale a alternativa em que a palavra destacada recebe acento gráfico pela MESMA regra que justifica o acento na palavra 'SAÚDE':",
    "options": [
      "A saída de emergência da Câmara Municipal foi desobstruída pela fiscalização.",
      "O servidor municipal goza de total autonomia no exercício da função pública.",
      "O vereador realizou um discurso com alto teor patriótico perante a mesa.",
      "A assembleia legislativa deliberou favoravelmente à concessão do benefício."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 'Sa-ú-de' e 'sa-í-da' são acentuadas pela REGRA DO HIATO: a vogal 'i' ou 'u' tônica, segunda vogal do hiato, sozinha na sílaba (ou com 's'), sem ser seguida de 'nh' e sem estar precedida de ditongo em paroxítona. 'Autonomia' e 'assembleia' não recebem acento; 'patriótico' é proparoxítona."
  },
  {
    "id": 63,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Ortografia: Novo Acordo Ortográfico (Ditongos Abertos)",
    "question": "De acordo com o Acordo Ortográfico vigente da Língua Portuguesa, os ditongos abertos 'EI' e 'OI' perderam o acento gráfico quando se encontram na posição de:",
    "options": [
      "Monossílabos tônicos (ex: dói, réis, méis).",
      "Oxítonas (ex: herói, troféu, constrói).",
      "Paroxítonas (ex: ideia, jiboia, assembleia, heroico).",
      "Proparoxítonas (ex: helicóptero, cômputo)."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O Acordo Ortográfico eliminou o acento dos ditongos abertos 'EI' e 'OI' exclusivamente nas palavras PAROXÍTONAS (i-dei-a, ji-boi-a, as-sem-blei-a, pla-tei-a). Nas oxítonas e monossílabos tônicos, o acento PERMANECE: he-rói, cons-trói, céu, réis."
  },
  {
    "id": 64,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Fonologia: Contagem de Fonemas e Letras",
    "question": "A palavra 'MUNICÍPIO' e a palavra 'TRABALHO' apresentam, respectivamente, o seguinte número de letras e fonemas:",
    "options": [
      "9 letras e 8 fonemas; 8 letras e 8 fonemas.",
      "9 letras e 10 fonemas; 8 letras e 6 fonemas.",
      "9 letras e 9 fonemas; 8 letras e 7 fonemas.",
      "8 letras e 8 fonemas; 7 letras e 6 fonemas."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Em 'MU-NI-CÍ-PIO': 9 letras e 9 fonemas (não há dígrafos). Em 'TRA-BA-LHO': 8 letras e 7 fonemas, pois o dígrafo 'lh' representa um único fonema consonantal [λ]."
  },
  {
    "id": 65,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Fonologia: Encontros Vocálicos (Hiato vs Ditongo)",
    "question": "Considere as palavras: I. História; II. Juízes; III. Rainha; IV. Coordenar. Classificam-se, respectivamente, quanto aos encontros vocálicos, como:",
    "options": [
      "Ditongo decrescente, Ditongo crescente, Tritongo e Hiato.",
      "Ditongo crescente, Hiato, Hiato e Hiato.",
      "Hiato, Ditongo crescente, Ditongo decrescente e Tritongo.",
      "Ditongo crescente, Hiato, Ditongo decrescente e Hiato."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. I. His-tó-ria: semivogal + vogal (ditongo crescente oral); II. Ju-í-zes: duas vogais em sílabas separadas (hiato acentuado); III. Ra-i-nha: duas vogais em sílabas separadas (hiato, não acentuado antes de 'nh'); IV. Co-or-de-nar: repetição de vogais em sílabas separadas (hiato)."
  },
  {
    "id": 66,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego do Sinal Indicativo de Crase: Casos Proibidos",
    "question": "O emprego do sinal indicativo de crase é rigorosamente PROIBIDO na seguinte frase:",
    "options": [
      "O presidente da Câmara dirigiu-se a todos os vereadores com respeito.",
      "O projeto de lei foi remetido à Comissão de Constituição e Justiça.",
      "A sessão solene teve início às nove horas da manhã em ponto.",
      "O servidor compareceu à reunião extraordinária do plenário."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em 'a todos os vereadores', o 'a' antecede pronome indefinido ('todos') e palavra masculina no plural ('vereadores'). Não há artigo definido feminino 'a', logo a crase é terminantemente proibida."
  },
  {
    "id": 67,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego da Crase: Casos Facultativos",
    "question": "A ocorrência do acento grave indicativo de crase é FACULTATIVA (opcional) em:",
    "options": [
      "O técnico legislativo entregou a ata à sua chefia imediata.",
      "A comissão parlamentar passou a investigar os fatos noticiados.",
      "O cidadão compareceu a pé até a portaria do prédio público.",
      "Ele redigiu a ata a lápis para posterior digitação oficial."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A crase é facultativa em três casos clássicos (Mnemônico 'NOME DE MULHER, ATÉ, MINHA'): 1. Antes de pronome possessivo feminino no singular ('à sua' ou 'a sua'); 2. Antes de nomes próprios femininos sem especificador ('à Maria' ou 'a Maria'); 3. Após a preposição 'até' ('até à' ou 'até a')."
  },
  {
    "id": 68,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego da Crase: Antes de Verbos",
    "question": "Analise a frase: 'O relator começou ___ expor as razões do veto e colocou o parecer ___ disposição da bancada'. Assinale a alternativa que preenche correta e respectivamente as lacunas:",
    "options": [
      "à — à",
      "a — à",
      "a — a",
      "à — a"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Antes de verbo ('expor'), não ocorre artigo feminino, logo usa-se apenas a preposição simples 'a' (sem crase). Na expressão 'à disposição', trata-se de locução adverbial/prepositiva com núcleo feminino, exigindo crase obrigatória."
  },
  {
    "id": 69,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Ortografia Oficial: Emprego de Mal vs Mau",
    "question": "Assinale a alternativa em que o termo sublinhado foi empregado em estrita conformidade com o padrão culto da língua:",
    "options": [
      "O servidor desempenhou mau as atribuições do seu cargo comissionado.",
      "Ele é um homem mal, incapaz de agir com empatia no atendimento ao público.",
      "O projeto de lei foi mau redigido pela assessoria parlamentar.",
      "Mal o presidente declarou aberta a sessão, o plenário ficou em silêncio."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. 'Mal' é conjunção temporal com sentido de 'assim que / logo que' ('Mal o presidente declarou aberta...'). Em (A), deveria ser 'desempenhou mal' (oposto de bem); em (B), 'homem mau' (oposto de bom); em (D), 'mal redigido' (oposto de bem redigido)."
  },
  {
    "id": 70,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Divisão Silábica e Separação de Dígrafos",
    "question": "Assinale a alternativa em que a partição silábica de todas as palavras está inteiramente CORRETA:",
    "options": [
      "Su-bli-nhar, ex-ce-ção, car-ro e p-neu-má-ti-co.",
      "Sub-li-nhar, e-xce-ção, ca-rro e pneu-má-ti-co.",
      "Sub-lin-har, ex-ce-ção, car-ro e pneu-má-ti-co.",
      "Sub-lin-har, ex-ce-ç-ão, ca-rro e pne-u-má-ti-co."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Os dígrafos 'rr', 'ss', 'sc', 'sç', 'xc' se SEPARAM na partição silábica (ex-ce-ção, car-ro). O prefixo 'sub' seguido de consoante mantém o 'b' na sílaba anterior: sub-lin-har. Encontros consonantais no início de palavra não se separam: pneu-má-ti-co."
  },
  {
    "id": 71,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego do Porquê / Por quê / Porque / Por que",
    "question": "Identifique a frase em que o uso do porquê está rigorosamente CORRETO:",
    "options": [
      "O projeto foi rejeitado por que a comissão apontou inconstitucionalidade.",
      "Os vereadores protestaram porque? Não houve justificativa clara.",
      "Por quê você não compareceu à audiência pública de Meruoca ontem?",
      "Não entendi o porquê de tanta discussão em torno de uma emenda simples."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. 'O porquê' é substantivo (vem acompanhado de artigo ou determinante) e deve ser grafado junto e com acento circunflexo. Em (A), deveria ser 'porque' (conjunção explicativa/causal); em (C), 'por quê' (fim de frase interrogativa); em (D), 'Por que' (início de pergunta direta, separado e sem acento)."
  },
  {
    "id": 72,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Acentuação Gráfica: Oxítonas Terminadas em A, E, O, EM",
    "question": "A palavra 'TAMBÉM' e a palavra 'PARABÉNS' recebem acento gráfico pela regra de acentuação das palavras:",
    "options": [
      "Paroxítonas terminadas em consoante nasal.",
      "Monossílabos tônicos terminados em ditongo nasal.",
      "Oxítonas terminadas em -em e -ens.",
      "Proparoxítonas aparentes ou eventuais."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Acentuam-se as palavras oxítonas terminadas em -a(s), -e(s), -o(s), -em e -ens (ex: tam-bém, pa-ra-béns, ar-ma-zém, vinténs)."
  },
  {
    "id": 73,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Crase diante de Pronomes Demonstrativos",
    "question": "Assinale a frase em que a crase foi empregada CORRETAMENTE antes de pronome demonstrativo:",
    "options": [
      "Ele entregou o requerimento à esta servidora do protocolo.",
      "O parecer foi contrário à essa proposta orçamentária do prefeito.",
      "A moção de repúdio foi dirigida à quem faltou à sessão solene.",
      "Refiro-me àquele vereador que presidiu a comissão de finanças."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Ocorre crase na junção da preposição 'a' (exigida pela regência de 'referir-se a') com a letra 'a' inicial dos pronomes aquele, aquela, aquilo: 'Refiro-me àquele'. Antes de 'esta', 'essa' ou 'quem', a crase é proibida."
  },
  {
    "id": 74,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Acentuação Diferencial e Novo Acordo",
    "question": "O Novo Acordo Ortográfico manteve o acento gráfico diferencial em um número muito reduzido de pares de palavras. Assinale a alternativa que contém uma palavra com acento diferencial OBRIGATÓRIO mantido:",
    "options": [
      "Pára (verbo parar, em oposição à preposição para).",
      "Pêlo (substantivo, em oposição à contração pelo).",
      "Pôde (pretérito perfeito do verbo poder, em oposição a pode, presente).",
      "Pólo (substantivo, em oposição à combinação polo)."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O Acordo Ortográfico aboliu o acento diferencial de pára/para, pêlo/pelo, pólo/polo. Foi MANTIDO obrigatoriamente em: PÔDE (passado) vs. PODE (presente) e PÔR (verbo) vs. POR (preposição). É facultativo em fôrma/forma."
  },
  {
    "id": 75,
    "category": "portugues",
    "day": "dia4",
    "discipline": "Língua Portuguesa",
    "topic": "Emprego do Hífen com Prefixos",
    "question": "Com o Novo Acordo Ortográfico, usa-se o hífen quando o prefixo termina com a mesma vogal com que se inicia o segundo elemento. Assinale a grafia CORRETA:",
    "options": [
      "Micro-ondas e anti-inflamatório.",
      "Microondas e antiinflamatório.",
      "Micro-ondas e antiinflamatório.",
      "Microondas e anti-inflamatório."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Regra geral do hífen com prefixos: vogais iguais se separam por hífen (mi-cro-on-das, an-ti-in-fla-ma-tó-rio, au-to-ob-ser-va-ção); vogais diferentes se unem sem hífen (au-toes-ti-ma, an-ti-a-é-re-o)."
  },
  {
    "id": 76,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 6º da CF/88: Rol dos Direitos Sociais",
    "question": "O Art. 6º da Constituição Federal de 1988 estabelece os direitos sociais fundamentais. Assinale a alternativa que contém APENAS direitos sociais expressamente elencados no caput desse dispositivo:",
    "options": [
      "Propriedade, liberdade de crença, previdência social e segurança.",
      "Inviolabilidade de domicílio, direito de herança, lazer e trabalho.",
      "Nacionalidade, direitos políticos, saúde e assistência aos desamparados.",
      "Educação, saúde, alimentação, trabalho, moradia e transporte."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Mnemônico 'EDU MORA LÁ, SAÚ TRABALHA ALI EM TRANSPORTE, SEGURA ASSIS PROSSEGUE PRENDENDO': Educação, Saúde, Alimentação, Trabalho, Moradia, Transporte, Lazer, Segurança, Previdência Social, Proteção à Maternidade e à Infância, e Assistência aos Desamparados (Art. 6º da CF/88)."
  },
  {
    "id": 77,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XIII da CF/88: Duração do Trabalho",
    "question": "Conforme o Art. 7º, XIII, da CF/88, a duração do trabalho normal dos trabalhadores urbanos e rurais não poderá ser superior a:",
    "options": [
      "8 horas diárias e 44 horas semanais, facultada a compensação de horários e a redução da jornada, mediante acordo ou convenção coletiva de trabalho.",
      "8 horas diárias e 40 horas semanais, vedada qualquer forma de compensação de horário.",
      "6 horas diárias e 36 horas semanais para todas as categorias profissionais urbanas.",
      "10 horas diárias e 48 horas semanais, desde que haja autorização do sindicato da categoria."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XIII da CF/88: 'duração do trabalho normal não superior a oito horas diárias e quarenta e quatro semanais, facultada a compensação de horários e a redução da jornada, mediante acordo ou convenção coletiva de trabalho'."
  },
  {
    "id": 78,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XIV da CF/88: Turnos Ininterruptos de Revezamento",
    "question": "A jornada de trabalho fixada pela Constituição Federal para o trabalho realizado em turnos ininterruptos de revezamento é de:",
    "options": [
      "8 horas improrrogáveis em qualquer hipótese.",
      "4 horas diárias com intervalo de 30 minutos.",
      "6 horas, salvo negociação coletiva.",
      "12 horas seguidas de 36 horas de descanso."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 7º, XIV da CF/88: 'jornada de seis horas para o trabalho realizado em turnos ininterruptos de revezamento, salvo negociação coletiva'."
  },
  {
    "id": 79,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XVI da CF/88: Remuneração da Hora Extra",
    "question": "Nos termos da Constituição Federal de 1988, a remuneração do serviço extraordinário (horas extras) será superior, no mínimo, à do normal em:",
    "options": [
      "20% (vinte por cento).",
      "100% (cem por cento).",
      "30% (trinta por cento).",
      "50% (cinquenta por cento)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 7º, XVI da CF/88: 'remuneração do serviço extraordinário superior, no mínimo, em cinquenta por cento à do normal'."
  },
  {
    "id": 80,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XVIII e XIX da CF/88: Licenças Gestante e Paternidade",
    "question": "Quanto à proteção à maternidade e à paternidade, a CF/88 assegura licença à gestante, sem prejuízo do emprego e do salário, com a duração de:",
    "options": [
      "120 dias, e licença-paternidade nos termos fixados em lei.",
      "90 dias, e licença-paternidade de 30 dias improrrogáveis.",
      "180 dias obrigatórios em todas as empresas privadas do país.",
      "60 dias, renováveis por igual período mediante atestado médico."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XVIII da CF/88: 'licença à gestante, sem prejuízo do emprego e do salário, com a duração de cento e vinte dias'. A prorrogação para 180 dias (Programa Empresa Cidadã / Estatutos de Servidores) decorre de lei, mas o texto constitucional expresso fixa 120 dias."
  },
  {
    "id": 81,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XXXIII da CF/88: Trabalho do Menor",
    "question": "Sobre a proibição de trabalho a menores de idade, a Constituição Federal estabelece expressamente a proibição de:",
    "options": [
      "Qualquer trabalho a menores de dezoito anos, mesmo na condição de aprendiz em empresas familiares.",
      "Trabalho noturno, perigoso ou insalubre a menores de dezoito e de qualquer trabalho a menores de dezesseis anos, salvo na condição de aprendiz, a partir de quatorze anos.",
      "Trabalho noturno a menores de dezesseis anos e de qualquer trabalho a menores de catorze anos, sem exceções.",
      "Trabalho insalubre a menores de vinte e um anos e aprendizagem a partir de doze anos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 7º, XXXIII da CF/88 (redação da EC 20/98): 'proibição de trabalho noturno, perigoso ou insalubre a menores de dezoito e de qualquer trabalho a menores de dezesseis anos, salvo na condição de aprendiz, a partir de quatorze anos'. Regra de ouro da INBRASP: 18 (noturno/perigoso/insalubre), 16 (regra geral de vedação) e 14 (aprendiz)."
  },
  {
    "id": 82,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XXI da CF/88: Aviso Prévio",
    "question": "A Constituição Federal de 1988 assegura o aviso prévio proporcional ao tempo de serviço, sendo de no mínimo:",
    "options": [
      "15 (quinze) dias para contratos de até um ano.",
      "30 (trinta) dias, nos termos da lei.",
      "60 (sessenta) dias para todos os trabalhadores urbanos.",
      "45 (quarenta e cinco) dias incondicionalmente."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 7º, XXI da CF/88: 'aviso prévio proporcional ao tempo de serviço, sendo no mínimo de trinta dias, nos termos da lei'."
  },
  {
    "id": 83,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, XVII da CF/88: Férias Remuneradas",
    "question": "O gozo de férias anuais remuneradas assegurado pela Constituição Federal de 1988 prevê o pagamento de remuneração com acréscimo de:",
    "options": [
      "Pelo menos, um terço a mais do que o salário normal.",
      "Cinquenta por cento a mais do que a remuneração ordinária.",
      "Metade do salário base calculado sobre o último mês de trabalho.",
      "Vinte por cento a título de gratificação de descanso anual."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 7º, XVII da CF/88: 'gozo de férias anuais remuneradas com, pelo menos, um terço a mais do que o salário normal'."
  },
  {
    "id": 84,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, IX da CF/88: Remuneração do Trabalho Noturno",
    "question": "Nos termos do Art. 7º, IX, da CF/88, em relação ao trabalho noturno, é direito constitucional do trabalhador:",
    "options": [
      "Jornada máxima reduzida para 4 horas sem adicional monetário.",
      "Remuneração do trabalho noturno superior à do diurno.",
      "Folga semanal dobrada para quem cumpre jornada noturna.",
      "Aposentadoria especial automática aos cinco anos de trabalho noturno."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 7º, IX da CF/88: 'remuneração do trabalho noturno superior à do diurno'."
  },
  {
    "id": 85,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 7º, VI da CF/88: Irredutibilidade Salarial",
    "question": "A regra constitucional acerca do salário dos trabalhadores estabelece a sua irredutibilidade, SALVO:",
    "options": [
      "Decisão unilateral discricionária do empregador em época de crise.",
      "Atraso no pagamento de tributos pelo estabelecimento comercial.",
      "O disposto em convenção ou acordo coletivo de trabalho.",
      "Determinação verbal do delegado regional do trabalho."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 7º, VI da CF/88: 'irredutibilidade do salário, salvo o disposto em convenção ou acordo coletivo'."
  },
  {
    "id": 86,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 8º, I da CF/88: Autonomia e Liberdade Sindical",
    "question": "Conforme o Art. 8º, I, da CF/88, é livre a associação profissional ou sindical, sendo expressamente VEDADA:",
    "options": [
      "Ao Poder Público a interferência e a intervenção na organização sindical, ressalvado o registro no órgão competente.",
      "A criação de sindicatos representativos de categorias diferenciadas.",
      "A filiação de servidores públicos a entidades de classe municipais.",
      "A cobrança de mensalidade associativa voluntária pelo sindicato."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 8º, I da CF/88: 'a lei não poderá exigir autorização do Estado para a fundação de sindicato, ressalvado o registro no órgão competente, vedadas ao Poder Público a interferência e a intervenção na organização sindical'."
  },
  {
    "id": 87,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 8º, II da CF/88: Princípio da Unicidade Sindical",
    "question": "O princípio da unicidade sindical estabelecido no Art. 8º, II, da CF/88 veda a criação de mais de uma organização sindical, em qualquer grau, representativa da mesma categoria:",
    "options": [
      "No mesmo Estado da federação, devendo haver sindicato único estadual.",
      "Em todo o território nacional para uma mesma profissão regulamentada.",
      "Na mesma base territorial, que será definida pelos trabalhadores interessados, não podendo ser inferior à área de um Município.",
      "Na mesma microrregião geográfica estabelecida pelo IBGE."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 8º, II da CF/88: 'é vedada a criação de mais de uma organização sindical, em qualquer grau, representativa de categoria profissional ou econômica, na mesma base territorial, que será definida pelos trabalhadores ou empregadores interessados, não podendo ser inferior à área de um Município'."
  },
  {
    "id": 88,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 8º, VIII da CF/88: Estabilidade do Dirigente Sindical",
    "question": "A estabilidade provisória do empregado sindicalizado que se candidata a cargo de direção ou representação sindical compreende o período:",
    "options": [
      "Apenas durante os meses de exercício efetivo do mandato sindical na sede.",
      "A partir da posse até o dia do término estrito do mandato parlamentar.",
      "Desde o registro da candidatura e, se eleito, ainda que suplente, até um ano após o final do mandato, salvo se cometer falta grave nos termos da lei.",
      "Desde a fundação do sindicato até a sua dissolução voluntária."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 8º, VIII da CF/88: 'é vedada a dispensa do empregado sindicalizado a partir do registro da candidatura a cargo de direção ou representação sindical e, se eleito, ainda que suplente, até um ano após o final do mandato, salvo se cometer falta grave nos termos da lei'."
  },
  {
    "id": 89,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 9º da CF/88: Direito de Greve",
    "question": "O direito de greve é expressamente garantido pelo Art. 9º da Constituição Federal de 1988, competindo aos:",
    "options": [
      "Empregadores autorizar previamente a paralisação das atividades operacionais.",
      "Magistrados do trabalho convocar a greve mediante portaria ministerial.",
      "Prefeitos municipais decretar a legalidade do movimento paradista.",
      "Trabalhadores decidir sobre a oportunidade de exercê-lo e sobre os interesses que devam por meio dele defender."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 9º, caput da CF/88: 'É assegurado o direito de greve, competindo aos trabalhadores decidir sobre a oportunidade de exercê-lo e sobre os interesses que devam por meio dele defender'."
  },
  {
    "id": 90,
    "category": "constitucional",
    "day": "dia4",
    "discipline": "D. Constitucional",
    "topic": "Art. 11 da CF/88: Representação de Empregados",
    "question": "Nas empresas com mais de quantos empregados é assegurada a eleição de um representante destes com a finalidade exclusiva de promover o entendimento direto com os empregadores (Art. 11 da CF)?",
    "options": [
      "Mais de 200 (duzentos) empregados.",
      "Mais de 100 (cem) empregados.",
      "Mais de 500 (quinhentos) empregados.",
      "Mais de 50 (cinquenta) empregados."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 11 da CF/88: 'Nas empresas de mais de duzentos empregados, é assegurada a eleição de um representante destes com a finalidade exclusiva de promover-lhes o entendimento direto com os empregadores'."
  },
  {
    "id": 91,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Arts. 1º e 2º: Princípios e Autonomia Municipal",
    "question": "De acordo com os princípios fundamentais da Lei Orgânica do Município de Meruoca/CE, o Município integra a República Federativa do Brasil e o Estado do Ceará, sendo dotado de autonomia:",
    "options": [
      "Política, administrativa e financeira.",
      "Soberana, judiciária e militar.",
      "Legislativa apenas, dependendo administrativamente do Estado.",
      "Econômica, porém subordinada hierarquicamente ao Governo Estadual."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A Lei Orgânica de Meruoca consagra a tríplice autonomia municipal conferida pelo Art. 18 e 29 da CF/88: Autonomia Política (eleição de prefeitos e vereadores), Administrativa (organização dos serviços locais) e Financeira (instituição e arrecadação de tributos próprios)."
  },
  {
    "id": 92,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Soberania Popular no Município de Meruoca",
    "question": "Nos termos da Lei Orgânica Municipal, todo o poder emana do povo meruoquense, que o exerce por meio de representantes eleitos ou diretamente. São formas de exercício direto da soberania popular no Município:",
    "options": [
      "Ação popular, mandado de segurança e inquérito civil público.",
      "Plebiscito, referendo e iniciativa popular de projetos de lei.",
      "Audiência prévia do Tribunal de Contas e veto do prefeito.",
      "Votação nominal em comissões parlamentares de inquérito."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Em consonância com o Art. 14 da CF/88 e a Lei Orgânica de Meruoca, a soberania popular direta é exercida mediante: 1. Plebiscito (consulta prévia); 2. Referendo (consulta posterior à lei); 3. Iniciativa popular de leis perante a Câmara Municipal."
  },
  {
    "id": 93,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Símbolos Oficiais do Município de Meruoca",
    "question": "São símbolos oficiais do Município de Meruoca expressamente consagrados em sua legislação fundamental:",
    "options": [
      "O Selo Municipal, o Estandarte e o Brasão do Estado do Ceará.",
      "O Brasão e a Bandeira apenas, sendo o Hino de competência estadual.",
      "A Faixa do Prefeito e a Insígnia do Presidente da Câmara.",
      "O Brasão, a Bandeira e o Hino do Município."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Conforme preceitua a Lei Orgânica Municipal (em harmonia com o Art. 13, § 2º da CF/88), os símbolos representativos do Município de Meruoca são a Bandeira, o Brasão e o Hino municipais."
  },
  {
    "id": 94,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Poderes do Município de Meruoca",
    "question": "São Poderes do Município de Meruoca, independentes e harmônicos entre si:",
    "options": [
      "O Legislativo, o Executivo e o Judiciário.",
      "O Executivo, o Judiciário e o Ministério Público Municipal.",
      "Apenas o Executivo, sendo o Legislativo um órgão consultivo auxiliar.",
      "O Legislativo e o Executivo."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. No âmbito municipal NÃO HÁ Poder Judiciário nem Ministério Público local (ambos são órgãos estaduais/federais). Os únicos poderes municipais são o Poder Legislativo (Câmara Municipal) e o Poder Executivo (Prefeitura Municipal)."
  },
  {
    "id": 95,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Competência Privativa do Município: Tributos e Orçamento",
    "question": "Compete privativamente ao Município de Meruoca, no exercício de sua autonomia legislativa e administrativa:",
    "options": [
      "Legislar privativamente sobre direito civil, penal e processual eleitoral.",
      "Instituir e arrecadar os tributos de sua competência e aplicar suas rendas, bem como fixar tarifas de serviços públicos municipais.",
      "Emitir moeda municipal e controlar as taxas de juros bancários locais.",
      "Organizar e manter o Poder Judiciário e a Defensoria Pública da Comarca."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Compete ao Município instituir tributos municipais (IPTU, ISS, ITBI, taxas e contribuições de iluminação pública), aplicar rendas e fixar tarifas de transporte e serviços locais. Legislar sobre direito civil/penal e emitir moeda são competências privativas da União (Art. 22 da CF)."
  },
  {
    "id": 96,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Competência Privativa: Uso e Ocupação do Solo Urbano",
    "question": "É matéria de interesse local inserida na competência privativa do Município de Meruoca:",
    "options": [
      "Explorar diretamente os serviços de telecomunicações e radiodifusão sonora.",
      "Promover o adequado ordenamento territorial, mediante planejamento e controle do uso, do parcelamento e da ocupação do solo urbano.",
      "Disciplinar a navegação aérea e a infraestrutura aeroespacial da Serra da Meruoca.",
      "Autorizar a exploração de jazidas minerais e riquezas do subsolo na região."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 30, VIII da CF/88 e Lei Orgânica de Meruoca: o ordenamento territorial, zoneamento urbano e controle de parcelamento/ocupação do solo (Plano Diretor, código de obras) é competência eminentemente municipal."
  },
  {
    "id": 97,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Competência Comum do Município com a União e o Estado",
    "question": "Assinale a alternativa que indica uma competência COMUM do Município de Meruoca em cooperação com o Estado do Ceará e a União:",
    "options": [
      "Criar e extinguir cargos privativos da Mesa Diretora da Assembleia Legislativa.",
      "Instituir o Imposto sobre Circulação de Mercadorias e Serviços (ICMS).",
      "Expedir passaportes e carteiras de identidade civil para estrangeiros.",
      "Cuidar da saúde e assistência pública, da proteção e garantia das pessoas com deficiência."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 23 da CF/88 e Lei Orgânica de Meruoca: a prestação de serviços de saúde, proteção de vulneráveis e pessoas com deficiência, meio ambiente e educação básica é matéria de competência comum dos três entes federados."
  },
  {
    "id": 98,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Guarda Municipal e Segurança Patrimonial",
    "question": "Nos termos da Lei Orgânica e do Art. 144, § 8º da CF/88, o Município de Meruoca poderá constituir guarda municipal destinada precipuamente à:",
    "options": [
      "Investigação de crimes eleitorais e tráfico interestadual de drogas.",
      "Proteção de seus bens, serviços e instalações.",
      "Substituição das polícias militar e civil nas ações de policiamento ostensivo geral.",
      "Fiscalização do recolhimento de impostos da União e execução fiscal federal."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 144, § 8º da CF/88 e legislação municipal: os municípios poderão constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações, atuando também na segurança comunitária e patrimonial."
  },
  {
    "id": 99,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Patrimônio e Bens Municipais",
    "question": "Constituem bens do Município de Meruoca, conforme sua Lei Orgânica:",
    "options": [
      "Exclusivamente os edifícios onde funcionam a Prefeitura e a Câmara Municipal.",
      "Todas as coisas móveis e imóveis, direitos e ações que a qualquer título lhe pertençam.",
      "Apenas as praças e ruas pavimentadas pelo poder público municipal.",
      "Os rios navegáveis que banham mais de dois estados da federação."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Constituem patrimônio e bens do Município todos os bens móveis e imóveis, direitos, títulos da dívida pública, créditos e ações pertencentes à municipalidade a qualquer título."
  },
  {
    "id": 100,
    "category": "legislacao",
    "day": "dia4",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Princípio da Publicidade e Publicação dos Atos Municipais",
    "question": "A publicação das leis e dos atos administrativos normativos da Câmara Municipal e da Prefeitura de Meruoca é requisito essencial de:",
    "options": [
      "Revogação tácita de todas as normas jurídicas anteriores.",
      "Descentralização administrativa forçada dos poderes públicos.",
      "Conversão obrigatória de projeto de lei em medida provisória.",
      "Eficácia e validade perante os munícipes e a sociedade."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Nenhum ato normativo ou lei municipal produz efeitos externos sem a devida publicação no órgão oficial ou mural público da Câmara/Prefeitura. A publicação é condição de EFICÁCIA e vigência da norma jurídica."
  },
  {
    "id": 101,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder Vinculado vs Discricionário",
    "question": "Quanto à margem de liberdade conferida ao administrador público na prática de seus atos, assinale a opção correta:",
    "options": [
      "No ato vinculado, o administrador pode avaliar livremente a conveniência de conceder ou não uma licença quando o particular preencher todos os requisitos.",
      "No ato discricionário, a lei concede margem de escolha ao gestor quanto à oportunidade e conveniência (mérito administrativo), sempre nos limites da lei.",
      "O mérito do ato discricionário pode ser revisto pelo Poder Judiciário sob o aspecto da conveniência e da oportunidade da autoridade administrativa.",
      "Todo ato administrativo é discricionário, cabendo à autoridade decidir as sanções disciplinares independentemente de previsão legal."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A discricionariedade confere juízo de mérito (conveniência e oportunidade) estritamente dentro das balizas da lei. O Judiciário fiscaliza a legalidade/moralidade, mas não pode substituir o mérito administrativo da decisão discricionária."
  },
  {
    "id": 102,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Abuso de Poder: Excesso vs Desvio de Poder",
    "question": "O abuso de poder constitui conduta ilegítima do agente público e manifesta-se sob duas modalidades distintas: o excesso de poder e o desvio de poder (ou desvio de finalidade). Ocorre EXCESSO DE PODER quando o agente público:",
    "options": [
      "Atua fora dos limites de sua competência legal ou excede os poderes que a lei lhe conferiu.",
      "Atua dentro de sua competência, mas com objetivo alheio ao interesse público ou para beneficiar amigo.",
      "Pratica um ato perfeitamente vinculado que cumpriu todas as formalidades do edital.",
      "Revoga um ato legal de sua própria lavra com base em razões supervenientes de interesse público."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico clássico: Excesso de Poder = vício de COMPETÊNCIA (o agente faz o que a lei não lhe permitiu). Desvio de Poder (ou Finalidade) = vício de FINALIDADE (o agente é competente, mas busca interesse privado ou perseguição)."
  },
  {
    "id": 103,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder Disciplinar",
    "question": "O Poder Disciplinar é a prerrogativa conferida à Administração Pública para:",
    "options": [
      "Aplicar multas e penalidades indistintamente a qualquer cidadão que transite em logradouro municipal sem habilitação.",
      "Fixar tarifas gerais de transporte urbano para toda a população da cidade.",
      "Apurar infrações e aplicar penalidades aos servidores públicos e a particulares que possuam vínculo jurídico específico com o Estado.",
      "Editar decretos normativos de caráter autônomo sem previsão em lei formal."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O poder disciplinar atinge quem tem vínculo especial/interno com o Estado (servidores públicos e contratados administrativos via licitação). A punição aos cidadãos em geral sem vínculo específico decorre do Poder de Polícia."
  },
  {
    "id": 104,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder Regulamentar / Normativo",
    "question": "A respeito do Poder Regulamentar conferido aos Chefes do Poder Executivo, é correto afirmar que os decretos regulamentares:",
    "options": [
      "Destinam-se a dar fiel execução às leis, não podendo criar direitos, obrigações ou inovar originariamente na ordem jurídica.",
      "Podem contrariar a lei em caso de emergência orçamentária do município.",
      "Permitem a criação originária de novos tributos municipais sem passar pela Câmara de Vereadores.",
      "Subordinam hierarquicamente as leis votadas pelo Poder Legislativo municipal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 84, IV da CF/88. O poder regulamentar é de caráter secundário (intra legem): serve apenas para explicitar e regulamentar a lei existente para sua fiel execução, sendo vedado criar obrigações novas ou inovar originariamente."
  },
  {
    "id": 105,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder de Polícia: Conceito e Atributos",
    "question": "Conforme o Art. 78 do Código Tributário Nacional (CTN), o Poder de Polícia é a atividade da administração pública que condiciona ou restringe o uso de bens, atividades e direitos em prol do interesse público. São atributos clássicos do poder de polícia:",
    "options": [
      "Irrevogabilidade, subordinação e imprescritibilidade.",
      "Gratuidade obrigatória, oralidade e retroatividade.",
      "Inalienabilidade, impenhorabilidade e imutabilidade.",
      "Discricionariedade, autoexecutoriedade e coercibilidade."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Mnemônico 'DAC': Discricionariedade (margem de escolha de atuação/sanção), Autoexecutoriedade (execução material direta sem prévia autorização judicial) e Coercibilidade (imposição imperativa de limites com força pública se necessário)."
  },
  {
    "id": 106,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Poder Hierárquico",
    "question": "São faculdades e prerrogativas típicas decorrentes do exercício do Poder Hierárquico na Administração Pública, EXCETO:",
    "options": [
      "Dar ordens aos subordinados, ressalvadas as ordens manifestamente ilegais.",
      "Aplicar sanções de interdição a estabelecimentos comerciais privados que violarem o código de posturas sanitárias.",
      "Fiscalizar e controlar as atividades desempenhadas pelos órgãos inferiores.",
      "Delegar e avocar competências, nos termos e limites previstos na legislação."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A interdição de comércio privado decorre do Poder de Polícia (sobre particulares). O Poder Hierárquico atua estritamente na relação interna de subordinação e coordenação entre órgãos e agentes públicos (dar ordens, fiscalizar, delegar e avocar)."
  },
  {
    "id": 107,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Atributos do Ato Administrativo: PATI",
    "question": "A doutrina de Direito Administrativo consagrada nas provas da banca INBRASP sintetiza os atributos do ato administrativo no mnemônico 'PATI'. Quais são esses atributos?",
    "options": [
      "Publicidade, Autonomia, Temporalidade e Impessoalidade.",
      "Previsibilidade, Anterioridade, Transparência e Intangibilidade.",
      "Probidade, Acessibilidade, Tipicidade e Igualdade.",
      "Presunção de legitimidade, Autoexecutoriedade, Tipicidade e Imperatividade."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Mnemônico PATI: Presunção de legitimidade/veracidade (atos presumem-se válidos até prova em contrário); Autoexecutoriedade (execução direta pelo Estado); Tipicidade (deve corresponder a figura prevista em lei); Imperatividade (impõe obrigações a terceiros independentemente de concordância)."
  },
  {
    "id": 108,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Presunção de Legitimidade e Veracidade",
    "question": "A presunção de legitimidade do ato administrativo produz como efeito prático processual a:",
    "options": [
      "Inversão do ônus da prova, cabendo a quem contesta o ato provar a sua ilegalidade ou falsidade.",
      "Impossibilidade definitiva de anulação do ato pelo Poder Judiciário.",
      "Dispensabilidade total de publicação dos atos no diário oficial do município.",
      "Transformação automática de atos discricionários em atos de império irrecorríveis."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A presunção de legitimidade é relativa (juris tantum): o ato nasce com aparência de legalidade e verdade fática, cabendo ao particular comprovar eventual defeito (inversão do ônus da prova)."
  },
  {
    "id": 109,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Autoexecutoriedade do Ato Administrativo",
    "question": "O atributo da AUTOEXECUTORIEDADE autoriza a Administração Pública a executar diretamente as suas decisões materiais sem a necessidade de prévia autorização judicial. Esse atributo:",
    "options": [
      "Existe indistintamente em 100% dos atos da administração, inclusive na cobrança coercitiva imediata de multas pecuniárias não pagas.",
      "Impede que o particular ingresse com mandado de segurança caso se sinta lesado em seu direito líquido e certo.",
      "Aplica-se somente aos atos editados pelo Poder Judiciário em suas funções típicas.",
      "Não está presente em todos os atos administrativos, existindo quando expressamente previsto em lei ou em situações urgentes de defesa do interesse público."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Pegadinha clássica: a autoexecutoriedade NÃO está em todos os atos! Ela não existe, por exemplo, na cobrança de multa em dinheiro (se o cidadão não pagar, o Estado não pode tomar o dinheiro à força; deve ingressar com Execução Fiscal no Judiciário)."
  },
  {
    "id": 110,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Imperatividade e Poder Extrínseco",
    "question": "A IMPERATIVIDADE (ou poder extroverso) do ato administrativo caracteriza-se por:",
    "options": [
      "Conceder vantagens que dependem do prévio requerimento e anuência do cidadão.",
      "Garantir a imutabilidade dos atos municipais após decorridos 30 dias de sua publicação.",
      "Permitir ao servidor público o descumprimento de ordens emanadas de seus superiores diretos.",
      "Impor deveres e obrigações a terceiros unilateralmente, independentemente da concordância do destinatário."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A imperatividade permite impor obrigações coercitivas ao administrado (ex: multa de trânsito, interdição de vigilância sanitária). Não está presente em atos enunciativos (certidões) ou negociais (autorização, licença)."
  },
  {
    "id": 111,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Tipicidade no Ato Administrativo",
    "question": "O atributo da TIPICIDADE, formulado pela professora Maria Sylvia Zanella Di Pietro, preceitua que o ato administrativo deve:",
    "options": [
      "Ser redigido exclusivamente na língua portuguesa arcaica do período colonial.",
      "Conter obrigatoriamente cláusula de sigilo prévio por até 5 anos.",
      "Corresponder a figuras previamente delineadas na lei para produzir os efeitos desejados, impedindo a prática de atos totalmente inominados.",
      "Ser publicado em pelo menos três jornais impressos de circulação nacional."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Pela tipicidade, para cada finalidade pretendida a lei já define a espécie de ato cabível (ex: se quer punir, usa demissão/advertência; se quer autorizar, usa alvará). Isso impede que a autoridade crie atos extravagantes ou sem modelo na lei."
  },
  {
    "id": 112,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Ciclo do Poder de Polícia",
    "question": "A doutrina divide o Poder de Polícia em quatro fases ou ciclos: I. Ordem de polícia (legislação); II. Consentimento de polícia (licença/autorização); III. Fiscalização de polícia (inspeção); IV. Sanção de polícia (multa/interdição). É passível de delegação a entidades estatais de direito privado integrantes da administração indireta (ex: empresas públicas e sociedades de economia mista):",
    "options": [
      "Apenas a ordem de polícia, sendo vedada a fiscalização.",
      "Todas as fases sem qualquer restrição, inclusive legislar privativamente sobre crimes.",
      "Nenhuma das fases, pois o poder de polícia é indelegável a qualquer ente.",
      "As fases de consentimento, fiscalização e sanção, conforme entendimento fixado pelo STF no Tema 532 de repercussão geral."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O STF fixou a tese de que é constitucional a delegação do poder de polícia (consentimento, fiscalização e sanção) a pessoas jurídicas de direito privado integrantes da administração pública indireta de capital majoritariamente público que prestem serviços públicos em regime não concorrencial (ex: BHTrans, CET)."
  },
  {
    "id": 113,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Desvio de Finalidade (Art. 2º da Lei da Ação Popular)",
    "question": "O prefeito de determinado município remove 'ex officio' um guarda municipal para posto de serviço remoto em área rural unicamente como forma de castigo pessoal por divergência política partidária. Essa conduta do administrador público caracteriza vício insanável de:",
    "options": [
      "Excesso de forma meramente acidental com convalidação automática.",
      "Exercício regular do poder disciplinar sem possibilidade de recurso ao Judiciário.",
      "Desvio de finalidade (ou desvio de poder), tornando o ato de remoção nulo de pleno direito.",
      "Incompetência absoluta por ausência de concurso público."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A remoção de servidor tem como finalidade atender à necessidade do serviço público. Usá-la para perseguir ou punir desvia a finalidade legal do ato (desvio de poder), gerando nulidade absoluta por violação direta ao princípio da impessoalidade."
  },
  {
    "id": 114,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Taxas de Polícia vs Preços Públicos",
    "question": "Pela atividade regular do Poder de Polícia exercida pelo Município de Meruoca, a Constituição Federal autoriza a instituição de:",
    "options": [
      "Taxas pelo exercício do poder de polícia.",
      "Impostos progressivos de natureza punitiva.",
      "Contribuições de melhoria extraordinárias sem obra pública.",
      "Tarifas alfandegárias de fiscalização internacional."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 145, II da CF/88 e Art. 77 do CTN: as taxas são tributos cobrados em razão do exercício regular do poder de polícia (ex: taxa de fiscalização de funcionamento, taxa de vigilância sanitária) ou pela utilização efetiva/potencial de serviço público específico e divisível."
  },
  {
    "id": 115,
    "category": "administrativo",
    "day": "dia5",
    "discipline": "D. Administrativo",
    "topic": "Distinção entre Atos Nulos e Anuláveis",
    "question": "No regime jurídico administrativo, quando um ato apresenta defeito quanto aos elementos de COMPETÊNCIA (desde que não seja exclusiva) ou de FORMA (desde que a lei não a exija como requisito de validade), o ato é passível de:",
    "options": [
      "Revogação obrigatória e irrecusável pelo Poder Judiciário.",
      "Cassação automática por descumprimento de deveres pelo particular.",
      "Prescrição imediata em 24 horas a contar da data de protocolo.",
      "Convalidação pela Administração Pública, aproveitando-se o ato com efeitos retroativos (ex tunc)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Mnemônico FO-CO: defeitos de Forma (não essencial) e Competência (não exclusiva) geram atos ANULÁVEIS que admitem convalidação pela própria Administração, desde que não acarretem lesão ao interesse público nem prejuízo a terceiros."
  },
  {
    "id": 116,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Conceito de Algoritmo",
    "question": "No contexto da ciência da computação e do edital da Câmara de Meruoca, um ALGORITMO pode ser conceituado como:",
    "options": [
      "Uma sequência finita de passos lógicos, ordenados e bem definidos, que visa à resolução de um problema ou à execução de uma tarefa.",
      "Um programa executável binário restrito a sistemas operacionais de grande porte.",
      "Uma peça de hardware instalada na placa-mãe responsável por resfriar o processador.",
      "Um protocolo de rede utilizado exclusivamente para tráfego seguro de e-mails corporativos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Algoritmo é uma sequência lógica, finita, ordenada e não ambígua de instruções que, ao ser processada, transforma entradas em saídas para solucionar um problema."
  },
  {
    "id": 117,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Fluxogramas: Símbolo de Decisão (Losango)",
    "question": "Em um fluxograma que representa o fluxo de tramitação de um processo administrativo, o símbolo geométrico que representa uma tomada de DECISÃO ou desvio condicional (onde o fluxo pode seguir caminhos diferentes conforme a resposta Sim/Não) é o:",
    "options": [
      "Retângulo.",
      "Círculo ou elipse.",
      "Paralelogramo.",
      "Losango."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Símbolos universais de fluxogramas: Losango = Decisão / Condição (teste lógico Se/Senão); Retângulo = Ação / Processamento / Atribuição; Oval/Elipse = Início ou Fim; Paralelogramo = Entrada ou Saída de dados."
  },
  {
    "id": 118,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Pseudocódigo e Estruturas Condicionais",
    "question": "Considere o seguinte trecho de pseudocódigo:\n\nSE (idade >= 18) ENTÃO\n    ESCREVA('Apto ao concurso')\nSENÃO\n    ESCREVA('Inapto por idade')\nFIMSE\n\nCaso o valor atribuído à variável 'idade' seja exatamente 18, o programa exibirá:",
    "options": [
      "Apto ao concurso",
      "Inapto por idade",
      "Erro de compilação por operador inexistente",
      "Nenhuma mensagem será exibida na tela"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O operador `>=` significa 'maior ou igual'. Como 18 é igual a 18, a condição é VERDADEIRA e o bloco do SE é executado, exibindo 'Apto ao concurso'."
  },
  {
    "id": 119,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Estruturas de Repetição (Laços / Loops)",
    "question": "Em lógica de programação, a estrutura que executa repetidamente um bloco de instruções ENQUANTO uma condição prévia permanecer verdadeira é chamada de:",
    "options": [
      "Função recursiva estática imutável.",
      "Laço de repetição ou loop (while / enquanto).",
      "Declaração de constante booleana.",
      "Instrução de salto incondicional irrestrita."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. As estruturas de repetição (laços ou loops) permitem executar comandos várias vezes. No laço `enquanto` (`while`), o teste é feito no início e o bloco roda enquanto o teste for verdadeiro."
  },
  {
    "id": 120,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Linguagem Python: Indentação Obrigatória",
    "question": "Diferentemente de linguagens como C ou Java que utilizam chaves `{ }` para delimitar blocos de comandos, a linguagem Python utiliza como delimitador obrigatório de blocos de código a:",
    "options": [
      "Indentação (espaçamento consistente à esquerda com espaços ou tabs).",
      "Utilização de ponto e vírgula ';' ao final de cada instrução.",
      "Inclusão da palavra reservada 'END' ao final de cada linha.",
      "Abertura e fechamento de colchetes '[ ]' em cada função."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em Python, a indentação não é apenas estética: ela define a hierarquia e o escopo dos blocos de código (corpo de funções, laços for/while, estruturas if/else)."
  },
  {
    "id": 121,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Tipos de Dados Básicos",
    "question": "Em Python, considere a atribuição: `total = 100`, `preco = 45.50` e `cargo = 'Técnico'`. Os tipos de dados primitivos dessas variáveis são, respectivamente:",
    "options": [
      "number, decimal e char.",
      "integer, currency e varchar.",
      "int (inteiro), float (número de ponto flutuante) e str (string / texto).",
      "long, double e text."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Em Python, inteiros são do tipo `int`, números com casas decimais são do tipo `float` e cadeias de caracteres entre aspas são do tipo `str`."
  },
  {
    "id": 122,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Operadores Aritméticos Divisão e Resto",
    "question": "Na linguagem Python, o operador `//` realiza a divisão inteira e o operador `%` retorna o resto da divisão. Qual será o resultado das expressões `7 // 2` e `7 % 2`?",
    "options": [
      "3.5 e 0.5",
      "3 e 0",
      "4 e 1",
      "3 e 1"
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. 7 dividido por 2 dá quociente 3 e sobra resto 1. Logo, a divisão inteira `7 // 2` resulta em 3, e o módulo/resto `7 % 2` resulta em 1."
  },
  {
    "id": 123,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Listas e Indexação",
    "question": "Em Python, as listas são coleções ordenadas de elementos e possuem indexação baseada em zero. Dada a lista `bancas = ['CETREDE', 'CONSULPAM', 'INBRASP', 'IDECAN']`, a instrução `print(bancas[2])` exibirá na tela:",
    "options": [
      "CONSULPAM",
      "INBRASP",
      "CETREDE",
      "IDECAN"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A indexação em Python inicia em zero: `bancas[0]` = 'CETREDE', `bancas[1]` = 'CONSULPAM', `bancas[2]` = 'INBRASP', `bancas[3]` = 'IDECAN'."
  },
  {
    "id": 124,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Comentários de Linha",
    "question": "Na linguagem Python, qual caractere é utilizado para inserir comentários de linha única (instruções que são ignoradas pelo interpretador)?",
    "options": [
      "// (duas barras inclinadas)",
      "/* (barra e asterisco)",
      "# (cerquilha / hashtag)",
      "-- (dois traços)"
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Em Python, comentários de linha única começam com o caractere `#`. Em linguagens como C, Java e PHP usa-se `//`; em SQL usa-se `--`."
  },
  {
    "id": 125,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Estrutura Condicional (if / elif / else)",
    "question": "Analise o seguinte código em Python:\n\npontos = 85\nif pontos >= 90:\n    print('Aprovado em 1º Lugar')\nelif pontos >= 50:\n    print('Classificado')\nelse:\n    print('Reprovado')\n\nQual será a saída exibida no terminal?",
    "options": [
      "Aprovado em 1º Lugar",
      "Classificado",
      "Reprovado",
      "Aprovado em 1º Lugar e Classificado simultaneamente"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. `pontos = 85`. A primeira condição (`85 >= 90`) é Falsa. O interpretador salta para o `elif`: `85 >= 50` é Verdadeira. Portanto, executa `print('Classificado')` e encerra a estrutura condicional."
  },
  {
    "id": 126,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Operador de Exponenciação",
    "question": "Qual operador matemático é utilizado na linguagem Python para calcular a exponenciação (potência), por exemplo, dois elevado à terceira potência (2³)?",
    "options": [
      "^ (acento circunflexo, ex: 2 ^ 3)",
      "** (dois asteriscos, ex: 2 ** 3)",
      "pow$ (ex: 2 pow$ 3)",
      "^^ (dois circunflexos, ex: 2 ^^ 3)"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Em Python, a potência é calculada com `**` (ex: `2 ** 3 = 8`). O operador `^` em Python é o operador bit a bit XOR (ou exclusivo), uma pegadinha clássica de concurso!"
  },
  {
    "id": 127,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Função len()",
    "question": "A função nativa `len()` em Python tem como finalidade:",
    "options": [
      "Converter um texto em letras maiúsculas.",
      "Ler uma entrada de dados digitada pelo usuário no teclado.",
      "Retornar a quantidade de elementos de um objeto (como tamanho de uma lista ou comprimento de uma string).",
      "Finalizar imediatamente a execução do programa em caso de erro."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. `len()` é a abreviação de 'length'. Exemplo: `len('Meruoca')` retorna 7; `len([10, 20, 30])` retorna 3."
  },
  {
    "id": 128,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Operadores Lógicos (and, or, not)",
    "question": "Em Python, os operadores lógicos booleanos para conjunção, disjunção e negação são grafados por extenso como:",
    "options": [
      "&&, ||, !",
      "and, or, not",
      ".AND., .OR., .NOT.",
      "e, ou, nao"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Python preza pela legibilidade e usa palavras em inglês em minúsculas: `and` (conjunção), `or` (disjunção) e `not` (negação). `&&` e `||` são de C/Java/JS."
  },
  {
    "id": 129,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Laço for e Função range()",
    "question": "Considere o código Python:\n\nsoma = 0\nfor i in range(1, 4):\n    soma += i\nprint(soma)\n\nLembrando que `range(1, 4)` gera os números 1, 2 e 3 (o limite superior 4 é exclusivo), qual valor será impresso?",
    "options": [
      "10",
      "4",
      "6",
      "3"
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. `range(1, 4)` produz os valores 1, 2 e 3. Na 1ª iteração: soma = 0 + 1 = 1. Na 2ª iteração: soma = 1 + 2 = 3. Na 3ª iteração: soma = 3 + 3 = 6. Saída: 6."
  },
  {
    "id": 130,
    "category": "informatica",
    "day": "dia5",
    "discipline": "Informática",
    "topic": "Python: Função print() e input()",
    "question": "As funções nativas de entrada e saída padrão em um terminal na linguagem Python são, respectivamente:",
    "options": [
      "input() para entrada de dados do usuário e print() para saída em tela.",
      "read() para entrada e write() para saída.",
      "scanf() para entrada e printf() para saída.",
      "cin para entrada e cout para saída."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em Python padrão: `input('Digite algo:')` lê dados do teclado em formato string, e `print('Mensagem')` imprime dados na tela do console."
  },
  {
    "id": 131,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Poder Legislativo Municipal e Composição",
    "question": "O Poder Legislativo do Município de Meruoca é exercido pela Câmara Municipal, composta por Vereadores eleitos pelo sistema proporcional para um mandato de:",
    "options": [
      "4 (quatro) anos, correspondendo a uma legislatura.",
      "2 (dois) anos, permitida uma recondução consecutiva.",
      "5 (cinco) anos, em consonância com o mandato dos senadores.",
      "3 (três) anos, renovando-se por terços anuais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em conformidade com a CF/88 e a Lei Orgânica de Meruoca, o mandato dos Vereadores é de 4 anos. Cada período de 4 anos de mandato parlamentar corresponde a uma LEGISLATURA."
  },
  {
    "id": 132,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Posse dos Vereadores, Prefeito e Vice",
    "question": "Nos termos da Lei Orgânica Municipal, a posse dos Vereadores, do Prefeito e do Vice-Prefeito de Meruoca realizar-se-á em sessão solene de instalação no dia:",
    "options": [
      "1º de fevereiro do ano da posse legislativa federal.",
      "15 de novembro, data da proclamação da República.",
      "1º de março, após o encerramento do recesso carnavalesco.",
      "1º de janeiro do ano subsequente ao da eleição."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A instalação da legislatura e a posse dos Vereadores, Prefeito e Vice-Prefeito ocorre obrigatoriamente no dia 1º de JANEIRO do ano subsequente à eleição municipal."
  },
  {
    "id": 133,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Mesa Diretora da Câmara Municipal",
    "question": "Imediatamente após a posse dos Vereadores de Meruoca, sob a presidência do vereador mais votado dentre os presentes, proceder-se-á à eleição dos membros da:",
    "options": [
      "Comissão Mista de Finanças e Tributação.",
      "Mesa Diretora da Câmara Municipal.",
      "Bancada Governista de Apoio ao Poder Executivo.",
      "Junta Comercial e Fiscalizatória dos Bairros."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Conforme a Lei Orgânica e o Regimento Interno, logo após o compromisso de posse no dia 1º de janeiro, os parlamentares elegem a Mesa Diretora da Câmara (Presidente, Vice-Presidente e Secretários)."
  },
  {
    "id": 134,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Quórum Geral de Deliberação na Câmara",
    "question": "Salvo disposição expressa em contrário da Lei Orgânica de Meruoca ou da Constituição Federal, as deliberações da Câmara Municipal e de suas Comissões serão tomadas por:",
    "options": [
      "Dois terços de votos, independentemente do número de presentes.",
      "Unanimidade obrigatória dos parlamentares diplomados.",
      "Maioria de votos, presente a maioria absoluta de seus membros.",
      "Voto exclusivo e soberano do Presidente da Mesa Diretora."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. É a regra geral da maioria simples (ou relativa): maioria dos votos dos presentes na sessão, desde que esteja presente a maioria absoluta (metade mais um) dos membros da Casa (Art. 47 da CF e Lei Orgânica)."
  },
  {
    "id": 135,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Imunidade Material dos Vereadores (Inviolabilidade)",
    "question": "Conforme o Art. 29, VIII da Constituição Federal e a Lei Orgânica de Meruoca, os Vereadores gozam de inviolabilidade por suas opiniões, palavras e votos:",
    "options": [
      "Em qualquer lugar do território nacional, inclusive em viagens privadas de lazer.",
      "No exercício do mandato e na circunscrição do Município.",
      "Apenas durante as sessões plenárias dentro do edifício da Câmara Municipal.",
      "Exclusivamente quando autorizados previamente pelo Presidente da Casa."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A imunidade material do Vereador é local: ele possui inviolabilidade civil e penal por palavras, votos e opiniões proferidas no exercício das funções parlamentares e restritas à CIRCUNSCRIÇÃO DO MUNICÍPIO de Meruoca."
  },
  {
    "id": 136,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Perda do Mandato por Falta às Sessões",
    "question": "Perderá o mandato o Vereador de Meruoca que deixar de comparecer, em cada sessão legislativa anual, sem justificativa legal ou licença concedida pela Casa, à:",
    "options": [
      "Metade (1/2) das sessões extraordinárias convocadas pelo prefeito.",
      "Duas sessões solenes comemorativas consecutivas.",
      "Quinta parte (1/5) das reuniões das comissões temáticas.",
      "Terça parte (1/3) das sessões ordinárias da Câmara Municipal."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 55, III da CF e Lei Orgânica: acarreta a perda do mandato parlamentar a ausência injustificada a 1/3 (uma terça parte) das sessões ordinárias do ano legislativo."
  },
  {
    "id": 137,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Remuneração dos Vereadores (Subsídio)",
    "question": "O subsídio dos Vereadores de Meruoca é fixado pela Câmara Municipal em cada legislatura para vigorar na subsequente, observados os limites constitucionais e o teto da receita municipal. O subsídio deve ser fixado sob a modalidade de:",
    "options": [
      "Parcela única, vedado o acréscimo de qualquer gratificação, adicional, abono, prêmio ou verba de representação.",
      "Salário base acrescido de 40% de gratificação de produtividade por projeto aprovado.",
      "Diárias cumulativas por sessão ordinária comparecida no mês.",
      "Comissão percentual sobre a arrecadação mensal do IPTU de Meruoca."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 39, § 4º da CF/88 e Lei Orgânica: os agentes políticos remuneram-se exclusivamente por SUBSÍDIO fixado em parcela única, sendo expressamente proibido o pagamento de penduricalhos, adicionais ou gratificações de gabinete."
  },
  {
    "id": 138,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Fiscalização Financeira e Controle Externo",
    "question": "A fiscalização contábil, financeira e orçamentária do Município de Meruoca será exercida pela Câmara Municipal, mediante controle externo, com o auxílio do:",
    "options": [
      "Tribunal de Contas da União (TCU) em primeira e última instância.",
      "Conselho Fiscal Popular eleito por voto secreto em cada bairro.",
      "Tribunal de Contas do Estado do Ceará (TCE/CE).",
      "Ministério da Fazenda e Receita Federal do Brasil."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O controle externo da Câmara Municipal sobre as contas do Município e do Prefeito é exercido com o auxílio do Tribunal de Contas do Estado (TCE/CE), que emite parecer prévio."
  },
  {
    "id": 139,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Rejeição do Parecer Prévio do TCE",
    "question": "O parecer prévio emitido pelo Tribunal de Contas sobre as contas que o Prefeito de Meruoca deve prestar anualmente só deixará de prevalecer por decisão de:",
    "options": [
      "Maioria absoluta dos vereadores presentes.",
      "Dois terços (2/3) dos membros da Câmara Municipal.",
      "Maioria simples mediante votação secreta.",
      "Unanimidade dos integrantes da comissão de orçamento."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 31, § 2º da CF/88 e Lei Orgânica de Meruoca: o parecer técnico do Tribunal de Contas tem peso qualificado e só pode ser derrubado pelo voto de 2/3 (dois terços) dos vereadores."
  },
  {
    "id": 140,
    "category": "legislacao",
    "day": "dia5",
    "discipline": "Lei Orgânica de Meruoca",
    "topic": "Comissões Parlamentares de Inquérito (CPIs)",
    "question": "As Comissões Parlamentares de Inquérito (CPI) na Câmara Municipal de Meruoca, que terão poderes de investigação próprios das autoridades judiciais, serão criadas mediante requerimento de:",
    "options": [
      "Metade mais um dos vereadores, para investigar condutas genéricas sem prazo determinado.",
      "Dois terços dos membros da Casa, exigindo-se aval prévio do juiz de direito da comarca.",
      "Um terço (1/3) dos membros da Câmara Municipal, para a apuração de fato determinado e por prazo certo.",
      "Qualquer cidadão que apresente abaixo-assinado com 50 assinaturas."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 58, § 3º da CF/88 e Lei Orgânica: a CPI é criada por requerimento de 1/3 (um terço) dos membros da Câmara, para apuração de FATO DETERMINADO e por PRAZO CERTO, sendo suas conclusões encaminhadas ao Ministério Público se for o caso."
  },
  {
    "id": 141,
    "simuladoQNum": 1,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Tipologia Textual: Narração",
    "topic": "Simulado Oficial 01 • Questão 1",
    "question": "[Simulado 01 - Q01] O tipo textual que se caracteriza pela sucessão temporal de fatos e pela presença de personagens, narrador, tempo e espaço denomina-se:",
    "options": [
      "Expositivo.",
      "Descritivo.",
      "Narrativo.",
      "Injuntivo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Morfossintaxe - Oração subordinada adverbial temporal."
  },
  {
    "id": 142,
    "simuladoQNum": 2,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Tipologia Textual: Descrição",
    "topic": "Simulado Oficial 01 • Questão 2",
    "question": "[Simulado 01 - Q02] O excerto \"O casarão antigo possuía portas largas de madeira escura, paredes descascadas pelo tempo e um assoalho de tábuas corridas que rangia\" classifica-se predominantemente como:",
    "options": [
      "Argumentativo.",
      "Descritivo.",
      "Injuntivo.",
      "Expositivo."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Crase antes de palavra feminina sem artigo definido."
  },
  {
    "id": 143,
    "simuladoQNum": 3,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Tipologia Textual: Dissertação Argumentativa",
    "topic": "Simulado Oficial 01 • Questão 3",
    "question": "[Simulado 01 - Q03] O texto que se estrutura com o objetivo principal de defender um ponto de vista (tese), recorrendo a argumentos, dados e raciocínio lógico para convencer o leitor, é do tipo:",
    "options": [
      "Narrativo.",
      "Dissertativo-argumentativo.",
      "Dissertativo-expositivo.",
      "Instrucional."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Concordância verbal com partícula apassivadora \"se\"."
  },
  {
    "id": 144,
    "simuladoQNum": 4,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Tipologia Textual: Injunção",
    "topic": "Simulado Oficial 01 • Questão 4",
    "question": "[Simulado 01 - Q04] Os manuais de instalação de equipamentos, receitas culinárias e bulas de medicamentos (na seção posologia) têm em comum a presença de verbos no imperativo ou infinitivo com instruções ao leitor. Essa tipologia é a:",
    "options": [
      "Descritiva.",
      "Dialógica.",
      "Narrativa.",
      "Injuntiva ou instrucional."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Regência verbal do verbo assistir no sentido de ver/presenciar."
  },
  {
    "id": 145,
    "simuladoQNum": 5,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Gênero Textual: Editorial",
    "topic": "Simulado Oficial 01 • Questão 5",
    "question": "[Simulado 01 - Q05] Assinale a alternativa que define corretamente o gênero textual Editorial:",
    "options": [
      "Texto assinado por um colunista que expressa sua visão pessoal e subjetiva sobre um fato.",
      "Comunicação estritamente interna trocada entre departamentos de uma mesma empresa.",
      "Relatório técnico produzido por peritos judiciais para embasar decisões do tribunal.",
      "Texto jornalístico que expressa o posicionamento institucional da empresa/jornal e não leva assinatura individual."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Gênero textual Editorial - institucional do jornal, sem assinatura."
  },
  {
    "id": 146,
    "simuladoQNum": 6,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Redação Oficial: Ofício",
    "topic": "Simulado Oficial 01 • Questão 6",
    "question": "[Simulado 01 - Q06] A comunicação formal e padronizada emitida por autoridades públicas para tratar de assuntos oficiais de serviço com outras autoridades ou cidadãos denomina-se:",
    "options": [
      "Carta comercial.",
      "Abaixo-assinado.",
      "Ofício.",
      "Artigo de opinião."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Ofício - comunicação formal da administração pública."
  },
  {
    "id": 147,
    "simuladoQNum": 7,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Funções da Linguagem",
    "topic": "Simulado Oficial 01 • Questão 7",
    "question": "[Simulado 01 - Q07] Em um cartaz institucional afixado em repartição pública constam os dizeres: \"Economize energia elétrica. Apague as lâmpadas ao sair da sala.\" O texto emprega tipologia injuntiva com a função de linguagem predominantemente:",
    "options": [
      "Conotativa (ou apelativa).",
      "Fática.",
      "Emotiva.",
      "Metalinguística."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Função Conotativa/Apelativa - foco no leitor, verbos no imperativo."
  },
  {
    "id": 148,
    "simuladoQNum": 8,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Gênero: Divulgação Científica",
    "topic": "Simulado Oficial 01 • Questão 8",
    "question": "[Simulado 01 - Q08] Um texto de Artigo de Divulgação Científica tem como finalidade primordial:",
    "options": [
      "Transmitir conhecimentos científicos ao público geral por meio de linguagem acessível e informativa.",
      "Contar uma narrativa fictícia com elementos mágicos e fabulosos.",
      "Vender produtos cosméticos por meio de apelos emocionais e imagens publicitárias.",
      "Estabelecer normas jurídicas imperativas para cumprimento obrigatório de pesquisadores."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Divulgação científica - transmitir conhecimento ao leigo."
  },
  {
    "id": 149,
    "simuladoQNum": 9,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Gênero: Artigo de Opinião",
    "topic": "Simulado Oficial 01 • Questão 9",
    "question": "[Simulado 01 - Q09] O gênero textual Artigo de Opinião caracteriza-se formalmente por:",
    "options": [
      "Apresentar a visão neutra do veículo de comunicação sem a identificação do autor.",
      "Ser um texto argumentativo assinado pelo próprio autor, que assume a responsabilidade pela tese defendida.",
      "Conter exclusivamente tabelas numéricas e dados matemáticos sem texto explicativo.",
      "Limitar-se a narrar uma sequência cronológica de eventos policiais sem emitir juízo de valor."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Artigo de opinião - texto argumentativo e assinado."
  },
  {
    "id": 150,
    "simuladoQNum": 10,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Gênero: Crônica",
    "topic": "Simulado Oficial 01 • Questão 10",
    "question": "[Simulado 01 - Q10] O gênero Crônica destaca-se na imprensa e na literatura por:",
    "options": [
      "Registrar normas regimentais e decretos administrativos com rigor técnico.",
      "Abordar situações cotidianas e corriqueiras com estilo leve, reflexivo e por vezes poético.",
      "Exigir obrigatoriamente a assinatura de um colegiado de juristas para ser publicado.",
      "Apresentar fórmulas matemáticas aplicadas a cálculos orçamentários."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Crônica - cotidiano em tom leve e reflexivo."
  },
  {
    "id": 151,
    "simuladoQNum": 11,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Windows 11: Nomenclatura de Arquivos",
    "topic": "Simulado Oficial 01 • Questão 11",
    "question": "[Simulado 01 - Q11] No sistema operacional Microsoft Windows 11, ao tentar renomear um arquivo ou pasta, o usuário é impedido de utilizar determinados caracteres reservados pelo sistema. Assinale a alternativa que contém apenas caracteres PROIBIDOS em nomes de arquivos no Windows:",
    "options": [
      "\\ / : * ? \" &lt; &gt; |",
      "@ # $ % _ - +",
      "( ) [ ] { } .",
      "! &amp; = ~ ^ ;"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Caracteres proibidos no Windows: \\ / : * ? \" < > |."
  },
  {
    "id": 152,
    "simuladoQNum": 12,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Windows 11: Atalhos",
    "topic": "Simulado Oficial 01 • Questão 12",
    "question": "[Simulado 01 - Q12] No Windows 11, o atalho de teclado padrão utilizado para BLOQUEAR rapidamente o computador ao se ausentar da mesa de trabalho é:",
    "options": [
      "Ctrl + Alt + B",
      "Logotipo do Windows + L",
      "Alt + F4",
      "Ctrl + Shift + Esc"
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Win + L - atalho de bloqueio rápido da sessão do Windows."
  },
  {
    "id": 153,
    "simuladoQNum": 13,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Linux Ubuntu: Diretórios",
    "topic": "Simulado Oficial 01 • Questão 13",
    "question": "[Simulado 01 - Q13] Na estrutura de diretórios do sistema operacional Linux (como o Ubuntu), o diretório responsável por armazenar os arquivos de configuração globais do sistema e dos serviços instalados é o:",
    "options": [
      "/bin",
      "/home",
      "/etc",
      "/dev"
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. /etc - pasta de arquivos de configuração globais do Linux."
  },
  {
    "id": 154,
    "simuladoQNum": 14,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Hardware: Memórias",
    "topic": "Simulado Oficial 01 • Questão 14",
    "question": "[Simulado 01 - Q14] A respeito da memória RAM (Random Access Memory) de um computador, assinale a afirmativa correta:",
    "options": [
      "É uma memória secundária de armazenamento permanente de fotos e vídeos.",
      "É uma memória volátil, cujo conteúdo é totalmente apagado quando o computador é desligado.",
      "Armazena a BIOS e não pode ser gravada nem alterada pelo usuário.",
      "Possui velocidade de leitura e gravação muito inferior à de um disco rígido tradicional (HD)."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Memória RAM é primária e volátil."
  },
  {
    "id": 155,
    "simuladoQNum": 15,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Segurança: Backup 3-2-1",
    "topic": "Simulado Oficial 01 • Questão 15",
    "question": "[Simulado 01 - Q15] A consagrada regra de segurança de dados \"3-2-1 para Backup\" recomenda manter:",
    "options": [
      "3 computadores ligados ao mesmo tempo, durante 2 horas por dia, com 1 funcionário supervisionando.",
      "3 senhas iguais em 2 sistemas diferentes para 1 único usuário.",
      "3 cópias dos dados, em 2 tipos de mídia diferentes, com pelo menos 1 cópia armazenada fora do local de trabalho (offsite/nuvem).",
      "3 antivírus instalados simultaneamente na mesma máquina durante 2 dias."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Regra 3-2-1 de Backup (3 cópias, 2 mídias, 1 fora/nuvem)."
  },
  {
    "id": 156,
    "simuladoQNum": 16,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Conjuntos Numéricos",
    "topic": "Simulado Oficial 01 • Questão 16",
    "question": "[Simulado 01 - Q16] Em uma pesquisa com 100 servidores da Câmara Municipal, 60 utilizam o sistema de processo eletrônico no Windows e 50 utilizam o sistema no Linux. Sabendo que 20 servidores utilizam ambos os sistemas, o número de servidores que não utilizam nenhum dos dois sistemas é:",
    "options": [
      "5 servidores.",
      "15 servidores.",
      "20 servidores.",
      "10 servidores."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Conjuntos: 60 + 50 - 20 = 90 servidores. 100 - 90 = 10 servidores."
  },
  {
    "id": 157,
    "simuladoQNum": 17,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Razão e Proporção",
    "topic": "Simulado Oficial 01 • Questão 17",
    "question": "[Simulado 01 - Q17] A razão entre o número de processos analisados pela manhã e à tarde por um Técnico Legislativo é de 3 para 5. Se em determinado dia ele analisou 40 processos no total, quantos foram analisados no período da manhã?",
    "options": [
      "12 processos.",
      "15 processos.",
      "18 processos.",
      "25 processos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Razão e proporção: 3x + 5x = 40 -> 8x = 40 -> x = 5. Manhã: 3 * 5 = 15."
  },
  {
    "id": 158,
    "simuladoQNum": 18,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Porcentagem",
    "topic": "Simulado Oficial 01 • Questão 18",
    "question": "[Simulado 01 - Q18] O orçamento anual de custeio de um setor legislativo era de R$ 50.000,00 e sofreu um acréscimo de 15%. Qual passou a ser o novo valor orçamentário?",
    "options": [
      "R$ 55.000,00.",
      "R$ 57.500,00.",
      "R$ 58.000,00.",
      "R$ 60.000,00."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Porcentagem: 50.000 + 15% = R$ 57.500,00."
  },
  {
    "id": 159,
    "simuladoQNum": 19,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Regra de Três Simples",
    "topic": "Simulado Oficial 01 • Questão 19",
    "question": "[Simulado 01 - Q19] Três técnicos legislativos realizam a digitalização de 120 atas em 4 horas. Mantendo o mesmo ritmo de trabalho, quantos técnicos seriam necessários para digitalizar as mesmas 120 atas em apenas 2 horas?",
    "options": [
      "6 técnicos.",
      "4 técnicos.",
      "5 técnicos.",
      "8 técnicos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Regra de três inversa: 3 téc * 4h = X * 2h -> X = 6 técnicos."
  },
  {
    "id": 160,
    "simuladoQNum": 20,
    "category": "matematica",
    "day": "dia6",
    "discipline": "Lógica Proposicional",
    "topic": "Simulado Oficial 01 • Questão 20",
    "question": "[Simulado 01 - Q20] Dada a proposição \"Se o Projeto de Lei for aprovado pela Câmara, então o Prefeito o sancionará\", sua negação lógica equivalente é:",
    "options": [
      "O Projeto de Lei é aprovado pela Câmara e o Prefeito não o sanciona.",
      "Se o Projeto de Lei não for aprovado, o Prefeito não o sancionará.",
      "O Projeto de Lei não é aprovado ou o Prefeito o sanciona.",
      "O Prefeito sanciona o Projeto de Lei se e somente se for aprovado."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Negação do condicional (P -> Q): P ^ ~Q (Mané)."
  },
  {
    "id": 161,
    "simuladoQNum": 21,
    "category": "portugues",
    "day": "dia6",
    "discipline": "CF/88: Inviolabilidade de Domicílio",
    "topic": "Simulado Oficial 01 • Questão 21",
    "question": "[Simulado 01 - Q21] Conforme o Art. 5º, XI, da CF/88, a casa é asilo inviolável do indivíduo. A entrada no domicílio sem o consentimento do morador por determinação judicial só pode ocorrer:",
    "options": [
      "A qualquer hora do dia ou da noite.",
      "Apenas durante a noite, com a presença de testemunhas.",
      "Durante o dia.",
      "Em dias úteis, no período das 6h às 22h."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 5º, XI CF/88 - Casa como asilo inviolável durante o dia."
  },
  {
    "id": 162,
    "simuladoQNum": 22,
    "category": "portugues",
    "day": "dia6",
    "discipline": "CF/88: Crimes Inafiançáveis e Imprescritíveis",
    "topic": "Simulado Oficial 01 • Questão 22",
    "question": "[Simulado 01 - Q22] Segundo a Constituição Federal de 1988, constituem crimes inafiançáveis e imprescritíveis:",
    "options": [
      "A prática da tortura e o tráfico ilícito de entorpecentes.",
      "Os crimes hediondos e o terrorismo.",
      "A prática do racismo e a ação de grupos armados contra a ordem constitucional.",
      "O roubo qualificado e a corrupção passiva."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Crimes inafiançáveis e imprescritíveis: Racismo e Ação de grupos armados."
  },
  {
    "id": 163,
    "simuladoQNum": 23,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Remédios Constitucionais: Mandado de Segurança",
    "topic": "Simulado Oficial 01 • Questão 23",
    "question": "[Simulado 01 - Q23] Para proteger direito líquido e certo, não amparado por Habeas Corpus ou Habeas Data, quando o responsável pela ilegalidade for autoridade pública, concede-se:",
    "options": [
      "Mandado de Segurança.",
      "Ação Popular.",
      "Mandado de Injunção.",
      "Arguição de Descumprimento de Preceito Fundamental."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Tráfico de drogas é inafiançável e insuscetível de graça ou anistia."
  },
  {
    "id": 164,
    "simuladoQNum": 24,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Mandado de Segurança: Prazo Decadencial",
    "topic": "Simulado Oficial 01 • Questão 24",
    "question": "[Simulado 01 - Q24] O prazo decadencial para a impetração de Mandado de Segurança é de:",
    "options": [
      "120 dias contados da ciência, pelo interessado, do ato impugnado.",
      "30 dias contados da publicação da portaria.",
      "60 dias contados da ocorrência do fato danoso.",
      "90 dias contados da notificação do ato coator."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Lei 12.016/09, Art. 23 - Prazo decadencial de 120 dias para Mandado de Segurança."
  },
  {
    "id": 165,
    "simuladoQNum": 25,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Remédios: Tribunal do Júri",
    "topic": "Simulado Oficial 01 • Questão 25",
    "question": "[Simulado 01 - Q25] É reconhecida a instituição do júri pela CF/88, com a organização que lhe der a lei, assegurada expressamente a competência para o julgamento dos:",
    "options": [
      "Crimes praticados por servidores públicos contra a administração em geral.",
      "Crimes de responsabilidade praticados por prefeitos e vereadores.",
      "Crimes culposos de trânsito que resultem em morte.",
      "Crimes dolosos contra a vida."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 5º, XXXVIII, \"d\" - Competência do Tribunal do Júri para crimes dolosos contra a vida."
  },
  {
    "id": 166,
    "simuladoQNum": 26,
    "category": "administrativo",
    "day": "dia6",
    "discipline": "D. Administrativo: Princípios LIMPE",
    "topic": "Simulado Oficial 01 • Questão 26",
    "question": "[Simulado 01 - Q26] Conforme o Art. 37, caput, da Constituição Federal de 1988, a administração pública direta e indireta de qualquer dos Poderes obedecerá aos seguintes princípios expressos:",
    "options": [
      "Legalidade, Impessoalidade, Moralidade, Publicidade e Eficiência.",
      "Legalidade, Supremacia do interesse público, Moralidade, Finalidade e Eficiência.",
      "Proporcionalidade, Impessoalidade, Razoabilidade, Publicidade e Celeridade.",
      "Legalidade, Isonomia, Moralidade, Transparência e Motivação."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Mnemônico LIMPE - Art. 37, caput da CF/88."
  },
  {
    "id": 167,
    "simuladoQNum": 27,
    "category": "administrativo",
    "day": "dia6",
    "discipline": "D. Administrativo: Impessoalidade",
    "topic": "Simulado Oficial 01 • Questão 27",
    "question": "[Simulado 01 - Q27] De acordo com o Art. 37, § 1º, da CF/88, a publicidade dos atos dos órgãos públicos não pode conter nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades. Tal regra decorre do princípio da:",
    "options": [
      "Continuidade do serviço público.",
      "Autotutela.",
      "Especialidade.",
      "Impessoalidade."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 37, § 1º CF/88 - Princípio da impessoalidade na publicidade institucional."
  },
  {
    "id": 168,
    "simuladoQNum": 28,
    "category": "administrativo",
    "day": "dia6",
    "discipline": "D. Administrativo: Autotutela",
    "topic": "Simulado Oficial 01 • Questão 28",
    "question": "[Simulado 01 - Q28] A prerrogativa conferida à Administração Pública de rever seus próprios atos, anulando os ilegais e revogando os inoportunos, decorre do princípio da:",
    "options": [
      "Legalidade estrita.",
      "Autotutela.",
      "Continuidade.",
      "Razoabilidade."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Autotutela - Súmulas 346 e 473 do STF."
  },
  {
    "id": 169,
    "simuladoQNum": 29,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Organização: Desconcentração vs. Descentralização",
    "topic": "Simulado Oficial 01 • Questão 29",
    "question": "[Simulado 01 - Q29] A distribuição interna de competências e atribuições dentro de uma mesma pessoa jurídica, dando origem a órgãos públicos despersonalizados com subordinação hierárquica, denomina-se:",
    "options": [
      "Descentralização por serviços.",
      "Delegação por colaboração.",
      "Desconcentração.",
      "Terceirização administrativa."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Desconcentração - distribuição interna de competências criando órgãos."
  },
  {
    "id": 170,
    "simuladoQNum": 30,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Administração Indireta: Autarquias",
    "topic": "Simulado Oficial 01 • Questão 30",
    "question": "[Simulado 01 - Q30] Sobre as entidades que integram a Administração Pública Indireta, assinale a entidade que é criada DIRETAMENTE por lei específica e possui personalidade jurídica de direito público:",
    "options": [
      "Empresa Pública.",
      "Sociedade de Economia Mista.",
      "Fundação Pública de direito privado.",
      "Autarquia."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 37, XIX - Autarquia criada diretamente por lei específica."
  },
  {
    "id": 171,
    "simuladoQNum": 31,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Sociedades de Economia Mista: Formato",
    "topic": "Simulado Oficial 01 • Questão 31",
    "question": "[Simulado 01 - Q31] A respeito das Sociedades de Economia Mista, assinale a afirmativa correta:",
    "options": [
      "Seu capital social é integralmente pertencente ao Poder Público.",
      "Possuem personalidade jurídica de direito público e bens inpenhoráveis.",
      "Devem ser constituídas obrigatoriamente sob a forma de Sociedade Anônima (S/A).",
      "Podem adotar qualquer formato societário, como Sociedade Limitada (Ltda)."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Sociedade de Economia Mista sob forma obrigatória de S/A."
  },
  {
    "id": 172,
    "simuladoQNum": 32,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Nova Lei de Licitações: Modalidades",
    "topic": "Simulado Oficial 01 • Questão 32",
    "question": "[Simulado 01 - Q32] Segundo a Lei nº 14.133/2021 (Nova Lei de Licitações), são modalidades de licitação expressamente previstas, EXCETO:",
    "options": [
      "Pregão e Concorrência.",
      "Concurso e Leilão.",
      "Tomada de Preços e Convite.",
      "Diálogo Competitivo."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Lei 14.133/2021 extinguiu as modalidades Convite e Tomada de Preços."
  },
  {
    "id": 173,
    "simuladoQNum": 33,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Licitações: Inexigibilidade vs. Dispensa",
    "topic": "Simulado Oficial 01 • Questão 33",
    "question": "[Simulado 01 - Q33] A contratação direta com fundamento na inviabilidade de competição (como na contratação de profissional do setor artístico consagrado pela crítica especializada) caracteriza hipótese de:",
    "options": [
      "Dispensa de licitação em razão do valor.",
      "Inexigibilidade de licitação.",
      "Concorrência internacional.",
      "Alienação fiduciária."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Inexigibilidade de licitação por inviabilidade de competição (Art. 74)."
  },
  {
    "id": 174,
    "simuladoQNum": 34,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Lei Orgânica de Meruoca: Prazos de Veto",
    "topic": "Simulado Oficial 01 • Questão 34",
    "question": "[Simulado 01 - Q34] Conforme a Lei Orgânica do Município de Meruoca, o Prefeito Municipal, considerando o Projeto de Lei aprovado pela Câmara inconstitucional ou contrário ao interesse público, terá qual prazo para vetá-lo?",
    "options": [
      "10 dias corridos.",
      "20 dias úteis.",
      "30 dias corridos.",
      "15 dias úteis."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Lei Orgânica de Meruoca - Prazo de veto do prefeito: 15 dias úteis."
  },
  {
    "id": 175,
    "simuladoQNum": 35,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Lei Orgânica de Meruoca: Contas do Prefeito",
    "topic": "Simulado Oficial 01 • Questão 35",
    "question": "[Simulado 01 - Q35] O parecer prévio emitido pelo Tribunal de Contas (TCE) sobre as contas anuais prestadas pelo Prefeito de Meruoca só deixará de prevalecer por decisão de:",
    "options": [
      "Maioria simples dos vereadores presentes.",
      "Maioria absoluta dos membros da Câmara.",
      "Unanimidade dos membros da Mesa Diretora.",
      "2/3 (dois terços) dos membros da Câmara Municipal."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Quórum qualificado de 2/3 da Câmara de Meruoca para rejeitar parecer do TCE."
  },
  {
    "id": 176,
    "simuladoQNum": 36,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Regimento Interno da Câmara: Funções",
    "topic": "Simulado Oficial 01 • Questão 36",
    "question": "[Simulado 01 - Q36] No âmbito do Poder Legislativo Municipal de Meruoca, constituem funções TÍPICAS da Câmara de Vereadores:",
    "options": [
      "Legislar sobre assuntos de interesse local e fiscalizar a administração pública municipal.",
      "Executar obras públicas e administrar receitas tributárias municipais.",
      "Julgar ações penais condenatórias e expedir mandados de prisão.",
      "Promover o controle concentrado de constitucionalidade perante o STF."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Funções típicas do Poder Legislativo: legislar e fiscalizar."
  },
  {
    "id": 177,
    "simuladoQNum": 37,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Técnica Legislativa: LC nº 95/1998",
    "topic": "Simulado Oficial 01 • Questão 37",
    "question": "[Simulado 01 - Q37] Segundo a Lei Complementar nº 95/1998, a articulação e numeração dos artigos de uma lei devem ser expressas por numerais ordinais até o artigo:",
    "options": [
      "Art. 5º.",
      "Art. 10.",
      "Art. 12.",
      "Art. 9º."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. LC 95/98 - Artigos são numerados com ordinais até o 9º e cardinais a partir do 10."
  },
  {
    "id": 178,
    "simuladoQNum": 38,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Orçamento / LRF: Limite de Pessoal",
    "topic": "Simulado Oficial 01 • Questão 38",
    "question": "[Simulado 01 - Q38] Nos termos da Lei de Responsabilidade Fiscal (LC nº 101/2000), a despesa total com pessoal do Poder Legislativo Municipal (Câmara de Vereadores) não poderá exceder qual percentual da Receita Corrente Líquida (RCL)?",
    "options": [
      "2% da RCL.",
      "54% da RCL.",
      "60% da RCL.",
      "6% da RCL."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. LRF - LC 101/00 - Limite total de despesa com pessoal da Câmara: 6% da RCL."
  },
  {
    "id": 179,
    "simuladoQNum": 39,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Improbidade Administrativa: Lei 8.429/92",
    "topic": "Simulado Oficial 01 • Questão 39",
    "question": "[Simulado 01 - Q39] Com as alterações promovidas pela Lei nº 14.230/2021 na Lei de Improbidade Administrativa, a configuração de ato de improbidade exige:",
    "options": [
      "Apenas a modalidade culposa em caso de negligência comprovada.",
      "O dano material ao erário, sendo dispensada a comprovação de dolo ou culpa.",
      "A presença de Dolo Específico (intenção consciente de alcançar o resultado ilícito).",
      "A condenação prévia na esfera penal com trânsito em julgado."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Lei 14.230/2021 - Exigência de dolo específico para configuração de improbidade."
  },
  {
    "id": 180,
    "simuladoQNum": 40,
    "category": "portugues",
    "day": "dia6",
    "discipline": "Transparência: LAI - Lei 12.527/2011",
    "topic": "Simulado Oficial 01 • Questão 40",
    "question": "[Simulado 01 - Q40] Conforme a Lei de Acesso à Informação (LAI), caso o órgão público não possa fornecer o acesso imediato à informação solicitada, deverá responder ao pedido no prazo de até:",
    "options": [
      "5 dias úteis, improrrogáveis.",
      "10 dias corridos, prorrogáveis por 5 dias.",
      "30 dias úteis, sem necessidade de justificativa.",
      "20 dias corridos, prorrogáveis por mais 10 dias mediante justificativa expressa."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. LAI - Lei 12.527/11 - Prazo padrão de resposta: até 20 dias, prorrogável por 10 dias."
  },
  {
    "id": 181,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Forma de Estado & Autonomia Federativa (Art. 18)",
    "question": "Conforme o Art. 18 da Constituição Federal de 1988, a organização político-administrativa da República Federativa do Brasil compreende a União, os Estados, o Distrito Federal e os Municípios. A respeito dessa estrutura, é correto afirmar que:",
    "options": [
      "A União é soberana e os demais entes federativos não possuem autonomia administrativa ou orçamentária.",
      "Todos são entes autônomos, nos termos da Constituição, sendo vedada qualquer tentativa de secessão ou dissolução do pacto federativo.",
      "Os Municípios subordinam-se administrativamente aos Estados-membros, dependendo de autorização da Assembleia Legislativa para criar seus órgãos.",
      "O Distrito Federal pode ser dividido em Municípios autônomos por lei distrital aprovada por maioria simples."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 18, caput da CF/88: 'A organização político-administrativa da República Federativa do Brasil compreende a União, os Estados, o Distrito Federal e os Municípios, todos autônomos, nos termos desta Constituição'. A República Federativa do Brasil possui SOBERANIA (no plano internacional); os entes federados (União, Estados, DF e Municípios) possuem AUTONOMIA (política, administrativa e financeira). É vedada a secessão (pacto federativo indissolúvel)."
  },
  {
    "id": 182,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Criação, Incorporação e Fusão de Municípios (Art. 18, § 4º)",
    "question": "A criação, a incorporação, a fusão e o desmembramento de Municípios, consoante o Art. 18, § 4º da CF/88 (redação da EC nº 15/96), far-se-ão por:",
    "options": [
      "Lei estadual, dentro do período determinado por lei complementar federal, e dependerão de consulta prévia, mediante plebiscito, às populações dos Municípios envolvidos, após divulgação dos Estudos de Viabilidade Municipal.",
      "Decreto legislativo da Câmara Municipal, homologado pelo Prefeito e pelo Governador do Estado.",
      "Lei complementar municipal, independentemente de plebiscito, desde que aprovada por dois terços dos vereadores.",
      "Portaria do Ministério da Justiça, mediante referendo das populações dos distritos afetados."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 18, § 4º da CF/88: Quatro requisitos cumulativos: 1. Lei Complementar Federal (fixando o período); 2. Estudos de Viabilidade Municipal (apresentados e publicados); 3. Plebiscito prévio às populações de TODOS os municípios envolvidos; 4. Lei Estadual ordinária criando/desmembrando o município."
  },
  {
    "id": 183,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Vedações Federativas (Art. 19)",
    "question": "O Art. 19 da Constituição Federal estabelece proibições expressas impostas à União, aos Estados, ao Distrito Federal e aos Municípios. Assinale a conduta expressamente VEDADA a todos esses entes:",
    "options": [
      "Manter relações de colaboração de interesse público com cultos religiosos ou igrejas na forma da lei.",
      "Criar distinções entre brasileiros ou preferências entre si.",
      "Instituir tributos municipais para a manutenção dos serviços de interesse local.",
      "Celebrar convênios de assistência mútua com órgãos de segurança pública."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 19 da CF/88 estabelece 3 vedações absolutas a todos os entes: I - Estabelecer cultos religiosos ou igrejas, subvencioná-los ou embaraçar-lhes o funcionamento (ressalvada colaboração de interesse público); II - Recusar fé aos documentos públicos; III - Criar distinções entre brasileiros ou preferências entre si."
  },
  {
    "id": 184,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Privativa da União (Art. 22)",
    "question": "No padrão recorrente da banca INBRASP, assinale a matéria cuja competência legislativa é PRIVATIVA DA UNIÃO, conforme o Art. 22 da CF/88:",
    "options": [
      "Direito civil, comercial, penal, processual, eleitoral, marítimo, aeronáutico, espacial e do trabalho.",
      "Direito tributário, financeiro, penitenciário, econômico e urbanístico.",
      "Proteção ao meio ambiente e controle da poluição em âmbito local.",
      "Fomento da produção agropecuária e organização do abastecimento alimentar municipal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 22, I da CF/88 (Mnemônico 'CAPACETE DE PIMENTA': Civil, Agrário, Penal, Aeronáutico, Comercial, Eleitoral, Trabalho, Espacial, Desapropriação, Processual, Marítimo). A opção (B) é competência concorrente da União/Estados/DF (Art. 24). A opção (C) e (D) são competências comuns (Art. 23)."
  },
  {
    "id": 185,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Delegação de Matéria Privativa da União (Art. 22, Parágrafo Único)",
    "question": "Embora as matérias do Art. 22 sejam privativas da União, a própria Constituição Federal prevê que os Estados e o DF poderão ser autorizados a legislar sobre questões específicas dessas matérias mediante:",
    "options": [
      "Medida provisória do Presidente da República.",
      "Resolução conjunta do Senado Federal e da Câmara dos Deputados.",
      "Lei complementar federal.",
      "Decreto regulamentar do Ministério da Justiça."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 22, Parágrafo único da CF/88: 'Lei complementar poderá autorizar os Estados a legislar sobre questões específicas das matérias relacionadas neste artigo'. Atenção: somente por Lei Complementar Federal (não por lei ordinária), apenas para questões específicas (não genéricas) e para todos os Estados indistintamente."
  },
  {
    "id": 186,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Comum (Art. 23 da CF/88)",
    "question": "O Art. 23 da CF/88 disciplina a competência comum (material/administrativa) da União, dos Estados, do Distrito Federal e dos Municípios. Constitui exemplo de competência comum de TODOS os entes federados:",
    "options": [
      "Legislar privativamente sobre trânsito e transporte rodoviário interestadual.",
      "Cuidar da saúde e assistência pública, da proteção e garantia das pessoas com deficiência.",
      "Emitir moeda de circulação nacional e fixar taxas de câmbio cambial.",
      "Decretar o estado de sítio e o estado de defesa em todo o território nacional."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 23, II da CF/88: 'cuidar da saúde e assistência pública, da proteção e garantia das pessoas com deficiência'. É competência material compartilhada por todos os entes (União, Estados, DF e Municípios)."
  },
  {
    "id": 187,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Concorrente e Exclusão do Município (Art. 24)",
    "question": "A competência legislativa CONCORRENTE prevista no Art. 24 da CF/88 (para legislar sobre direito tributário, financeiro, penitenciário, econômico e urbanístico) foi atribuída pela Constituição expressamente a:",
    "options": [
      "União, aos Estados, ao Distrito Federal e a todos os Municípios com mais de cem mil habitantes.",
      "União, aos Estados e ao Distrito Federal, não figurando os Municípios no rol desse artigo.",
      "Exclusivamente aos Municípios e ao Distrito Federal.",
      "Apenas à União e aos Municípios que possuam câmara municipal instalada."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 24, caput da CF/88: 'Compete à União, aos Estados e ao Distrito Federal legislar concorrentemente sobre...'. Os MUNICÍPIOS NÃO figuram no Art. 24! A competência dos Municípios em matéria concorrente é apenas SUPLEMENTAR à legislação federal e estadual no que couber, por força do Art. 30, II."
  },
  {
    "id": 188,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Normas Gerais vs Suplementares no Art. 24",
    "question": "No âmbito da legislação concorrente (Art. 24), a competência da União limitar-se-á a estabelecer normas gerais (§ 1º). Sobre essa dinâmica, assinale a opção correta:",
    "options": [
      "A superveniência de lei federal sobre normas gerais suspende a eficácia da lei estadual, no que lhe for contrário.",
      "A superveniência de lei federal revoga expressamente e extingue a lei estadual anterior por completo.",
      "Inexistindo lei federal sobre normas gerais, os Estados ficam impedidos de legislar sobre a matéria.",
      "A competência da União para normas gerais exclui a competência suplementar dos Estados-membros."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 24, § 4º da CF/88: 'A superveniência de lei federal sobre normas gerais suspende a eficácia da lei estadual, no que lhe for contrário'. Pegadinha favorita de concurso: a lei federal NÃO revoga a lei estadual, apenas SUSPENDE SUA EFICÁCIA naquilo que for incompatível."
  },
  {
    "id": 189,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Legislativa do Município (Art. 30, I e II)",
    "question": "De acordo com o Art. 30, I e II da CF/88, compete aos Municípios:",
    "options": [
      "Legislar privativamente sobre direito processual civil e normas penais de menor potencial ofensivo.",
      "Fixar normas gerais de direito financeiro nacional com eficácia perante os Estados vizinhos.",
      "Instituir imposto sobre operações relativas à circulação de mercadorias e serviços (ICMS).",
      "Legislar sobre assuntos de interesse local e suplementar a legislação federal e a estadual no que couber."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 30 da CF/88: 'Compete aos Municípios: I - legislar sobre assuntos de interesse local; II - suplementar a legislação federal e a estadual no que couber'. É o núcleo da autonomia legislativa do Município de Meruoca."
  },
  {
    "id": 190,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Municipal: Serviços Públicos e Transporte (Art. 30, V)",
    "question": "Nos termos do Art. 30, V da CF/88, compete ao Município organizar e prestar, diretamente ou sob regime de concessão ou permissão, os serviços públicos de interesse local, incluído o de:",
    "options": [
      "Energia nuclear e exploração de jazidas de petróleo na plataforma continental.",
      "Correios e telégrafos em âmbito interestadual.",
      "Transporte coletivo, que tem caráter essencial.",
      "Radiodifusão sonora e televisiva educativa regional."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 30, V da CF/88: 'organizar e prestar, diretamente ou sob regime de concessão ou permissão, os serviços públicos de interesse local, incluído o de transporte coletivo, que tem caráter essencial'."
  },
  {
    "id": 191,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Competência Municipal: Solo Urbano e Plano Diretor (Art. 30, VIII)",
    "question": "Compete aos Municípios promover, no que couber, adequado ordenamento territorial, mediante planejamento e controle do uso, do parcelamento e da ocupação do:",
    "options": [
      "Espaço aéreo nacional e rotas de aviação civil.",
      "Leito dos rios que banham mais de um Estado da Federação.",
      "Subsolo mineral e reservas de minérios estratégicos da União.",
      "Solo urbano."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 30, VIII da CF/88: 'promover, no que couber, adequado ordenamento territorial, mediante planejamento e controle do uso, do parcelamento e da ocupação do solo urbano'. É a base para a criação do Plano Diretor e do Código de Obras Municipal."
  },
  {
    "id": 192,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Lei Orgânica Municipal e Quórum de Aprovação (Art. 29)",
    "question": "O Município reger-se-á por lei orgânica, votada em dois turnos, com o interstício mínimo de dez dias, e aprovada por:",
    "options": [
      "Maioria simples dos vereadores presentes, sendo sancionada pelo Prefeito.",
      "Maioria absoluta da Câmara, com homologação obrigatória pelo Governador.",
      "Dois terços dos membros da Câmara Municipal, que a promulgará.",
      "Três quintos dos votos dos parlamentares em sessão conjunta com o Judiciário."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 29, caput da CF/88: 'O Município reger-se-á por lei orgânica, votada em dois turnos, com o interstício mínimo de dez dias, e aprovada por dois terços dos membros da Câmara Municipal, que a promulgará'. O Prefeito NÃO sanciona nem veta a Lei Orgânica; ela é PROMULGADA diretamente pela Mesa da Câmara!"
  },
  {
    "id": 193,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Limites de Subsídio dos Vereadores (Art. 29, VI)",
    "question": "O subsídio dos Vereadores será fixado pelas respectivas Câmaras Municipais em cada legislatura para a subsequente, observados os limites da CF. Em municípios de até dez mil habitantes (faixa base), o subsídio máximo do Vereador corresponderá a qual percentual do subsídio dos Deputados Estaduais?",
    "options": [
      "50% (cinquenta por cento).",
      "75% (setenta e cinco por cento).",
      "10% (dez por cento).",
      "20% (vinte por cento)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 29, VI, 'a' da CF/88: em municípios de até 10.000 habitantes, o subsídio máximo do vereador é 20% do subsídio do Deputado Estadual. A escala sobe: 20%, 30%, 40%, 50%, 60% até 75% em municípios com mais de 500.000 habitantes."
  },
  {
    "id": 194,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Limite de Gasto com Folha de Pagamento da Câmara (Art. 29-A, § 1º)",
    "question": "A Câmara Municipal não gastará mais de qual percentual de sua receita total com folha de pagamento, incluído o gasto com o subsídio de seus Vereadores (Art. 29-A, § 1º da CF)?",
    "options": [
      "50% (cinquenta por cento).",
      "60% (sessenta por cento).",
      "80% (oitenta por cento).",
      "70% (setenta por cento)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 29-A, § 1º da CF/88: 'A Câmara Municipal não gastará mais de setenta por cento de sua receita com folha de pagamento, incluído o gasto com o subsídio de seus Vereadores'. O descumprimento desse limite constitui crime de responsabilidade do Presidente da Câmara (Art. 29-A, § 3º)."
  },
  {
    "id": 195,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Fiscalização Contábil e Tribunal de Contas (Art. 31)",
    "question": "A fiscalização do Município será exercida pelo Poder Legislativo Municipal, mediante controle externo, e pelos sistemas de controle interno do Executivo. O controle externo da Câmara Municipal é exercido com o auxílio do:",
    "options": [
      "Tribunal de Justiça do Estado, mediante sentença transitada em julgado proferida anualmente.",
      "Tribunal de Contas do Estado (ou do Município onde houver), cujo parecer prévio só deixa de prevalecer por decisão de dois terços dos vereadores.",
      "Ministério Público Estadual, através de inquérito civil conclusivo homologado pela Mesa.",
      "Conselho Fiscal de Contabilidade Comunitária eleito pelos contribuintes locais."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 31, §§ 1º e 2º da CF/88: O controle externo é auxiliado pelo TCE. O parecer prévio do TCE sobre as contas anuais do Prefeito só pode ser rejeitado por decisão qualificada de DOIS TERÇOS (2/3) dos membros da Câmara Municipal."
  },
  {
    "id": 196,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Vedação de Novos Tribunais de Contas Municipais (Art. 31, § 4º)",
    "question": "Sobre a estrutura de controle externo das contas municipais, o Art. 31, § 4º da Constituição Federal expressamente estabelece que:",
    "options": [
      "É vedada a criação de Tribunais, Conselhos ou órgãos de Contas Municipais.",
      "Todos os municípios com mais de cinquenta mil eleitores devem instituir seu próprio Tribunal de Contas.",
      "Os Municípios podem criar órgãos de contas municipais mediante autorização prévia do Senado Federal.",
      "A fiscalização externa dos municípios dispensa a atuação de Tribunais de Contas estaduais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Art. 31, § 4º da CF/88: 'É vedada a criação de Tribunais, Conselhos ou órgãos de Contas Municipais'. Apenas os tribunais municipais já existentes antes de 1988 (como os dos municípios de São Paulo e Rio de Janeiro) foram mantidos; é proibido criar novos."
  },
  {
    "id": 197,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Contas Municipais à Disposição dos Contribuintes (Art. 31, § 3º)",
    "question": "Conforme o Art. 31, § 3º da CF/88, as contas dos Municípios ficarão, anualmente, durante quantos dias, à disposição de qualquer contribuinte, para exame e apreciação, o qual poderá questionar-lhes a legitimidade, nos termos da lei?",
    "options": [
      "30 (trinta) dias.",
      "60 (sessenta) dias.",
      "90 (noventa) dias.",
      "15 (quinze) dias."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Art. 31, § 3º da CF/88: 'As contas dos Municípios ficarão, no decorrer de sessenta dias, anualmente, à disposição de qualquer contribuinte, para exame e apreciação, o qual poderá questionar-lhes a legitimidade, nos termos da lei'."
  },
  {
    "id": 198,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Bens da União vs Bens dos Estados (Arts. 20 e 26)",
    "question": "A Constituição Federal define expressamente os bens pertencentes à União e aos Estados. Incluem-se entre os BENS DOS ESTADOS-MEMBROS (Art. 26 da CF/88):",
    "options": [
      "Os rios que banhem mais de um Estado da Federação ou sirvam de limite com países vizinhos.",
      "Os potenciais de energia hidráulica e os recursos minerais, inclusive os do subsolo.",
      "As águas superficiais ou subterrâneas, fluentes, emergentes e em depósito, ressalvadas, neste caso, na forma da lei, as decorrentes de obras da União.",
      "As terras devolutas indispensáveis à defesa das fronteiras e fortificações militares."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Art. 26, I da CF/88. As águas que nascem e correm exclusivamente dentro do território de um único estado são bens do Estado. Rios que atravessam mais de um estado ou fazem fronteira com outro país (Art. 20, III), potenciais de energia hidráulica (Art. 20, VIII) e terras de fronteira (Art. 20, II) pertencem à UNIÃO."
  },
  {
    "id": 199,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Intervenção do Estado no Município (Art. 35 da CF/88)",
    "question": "O Estado-membro NÃO intervirá em seus Municípios, SALVO quando (Art. 35 da CF):",
    "options": [
      "O prefeito pertencer a partido político de oposição ao governador do Estado.",
      "A câmara municipal aprovar moção de desconfiança contra a diretoria do hospital municipal.",
      "O município apresentar índice de desemprego superior à média estadual no semestre.",
      "Deixar de ser paga, sem motivo de força maior, por dois anos consecutivos, a dívida fundada."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Art. 35 da CF/88: O Estado só pode intervir no Município se: I - deixar de pagar dívida fundada por 2 anos consecutivos; II - não prestar contas devidas na lei; III - não aplicar o mínimo constitucional em saúde e educação; IV - o TJ prover representação para assegurar princípios ou prover execução de lei/ordem judicial."
  },
  {
    "id": 200,
    "category": "constitucional",
    "day": "w2_d1",
    "discipline": "D. Constitucional",
    "topic": "Intervenção Federal em Municípios localizados em Estado",
    "question": "A respeito da intervenção federal em Municípios localizados dentro de um Estado-membro (como o Município de Meruoca no Estado do Ceará), é correto afirmar que:",
    "options": [
      "A União não intervém diretamente em Municípios localizados em Estados, cabendo ao próprio Estado a intervenção municipal (a intervenção federal direta em município só cabe em Território Federal).",
      "O Presidente da República pode decretar intervenção federal direta em qualquer município sem consultar o Governador do Estado.",
      "A intervenção no município é sempre realizada pelo Ministério Público Federal mediante portaria ministerial.",
      "O Governador do Estado pode intervir na União caso haja atraso no repasse do Fundo de Participação dos Estados."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Regra do Art. 35 e Art. 36 da CF: O Estado é quem intervém em seus Municípios. A União só intervém diretamente em Municípios localizados em TERRITÓRIOS FEDERAIS (Art. 35, caput)."
  },
  {
    "id": 201,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Derivação Parassintética vs Prefixal e Sufixal",
    "question": "A DERIVAÇÃO PARASSINTÉTICA ocorre quando prefixo e sufixo são agregados simultaneamente ao radical, de modo que a palavra não existe sem um deles. Assinale a alternativa que apresenta um vocábulo formado por derivação parassintética:",
    "options": [
      "Anoitecer (a + noit + ecer)",
      "Infelizmente (in + feliz + mente)",
      "Deslealdade (des + leal + dade)",
      "Reorganização (re + organiza + ção)"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em 'a-noit-ecer', o prefixo 'a-' e o sufixo '-ecer' foram anexados simultaneamente ao radical 'noit-'. Se retirarmos o prefixo, não existe a palavra 'noitecer'; se retirarmos o sufixo, não existe 'anoite'. Já em 'infelizmente' (B) e 'deslealdade' (C), os afixos são independentes ('infeliz' e 'felizmente' existem no idioma, configurando derivação prefixal e sufixal)."
  },
  {
    "id": 202,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Derivação Regressiva (Deverbal)",
    "question": "A derivação regressiva (ou deverbal) consiste na formação de substantivos abstratos a partir de verbos, geralmente com a redução da terminação verbal para as vogais temáticas -a, -o, -e. Assinale o vocábulo formado por DERIVAÇÃO REGRESSIVA:",
    "options": [
      "O pescador (derivado do verbo pescar)",
      "A lealdade (derivado do adjetivo leal)",
      "O antebraço (derivado do substantivo braço)",
      "O debate (derivado do verbo debater)"
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. 'O debate' é substantivo abstrato que indica ação, formado pela regressão do verbo 'debater' (perda da desinência infinitiva -r e fixação da vogal -e). Em (B), 'pescador' é derivação sufixal (-dor); em (C), 'lealdade' é derivação sufixal (-dade); em (D), 'antebraço' é derivação prefixal (ante-)."
  },
  {
    "id": 203,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Derivação Imprópria (Conversão)",
    "question": "A DERIVAÇÃO IMPRÓPRIA ocorre quando uma palavra muda de classe gramatical no contexto da oração sem que haja qualquer alteração em sua estrutura morfológica. Assinale a frase em que se constata a ocorrência de derivação imprópria:",
    "options": [
      "O servidor realizou um trabalho rápido e eficiente durante a sessão.",
      "Eles discordaram profundamente das propostas apresentadas em plenário.",
      "A comissão permanente elaborou um parecer extremamente detalhado.",
      "O 'sim' dos parlamentares foi decisivo para a promulgação da lei."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O vocábulo 'sim' é originalmente um advérbio de afirmação. Precedido pelo artigo definido 'o' ('O sim dos parlamentares'), foi substantivado (passou a funcionar como substantivo comum), configurando típico caso de derivação imprópria ou conversão."
  },
  {
    "id": 204,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Composição por Justaposição vs Aglutinação",
    "question": "Na formação de palavras por COMPOSIÇÃO, unem-se dois ou mais radicais. Quando os elementos componentes se unem mantendo a integridade fonética e gráfica de cada um, ocorre:",
    "options": [
      "Aglutinação (ex: planalto, vinagre, pernilongo).",
      "Hibridismo morfológico greco-latino.",
      "Justaposição (ex: passatempo, pé-de-galinha, girassol).",
      "Reduplicação silábica imitativa onomatopeica."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Justaposição une palavras sem perda fonética de seus elementos (passa + tempo = passatempo; gira + sol = girassol; embora dobre o 's' para manter o som, não há supressão fonética). Na aglutinação, há perda/fusão fonética (plano + alto = planalto; vinho + acre = vinagre)."
  },
  {
    "id": 205,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Composição por Aglutinação",
    "question": "Assinale a alternativa em que AMBAS as palavras foram formadas pelo processo de COMPOSIÇÃO POR AGLUTINAÇÃO:",
    "options": [
      "Guarda-roupa e couve-flor.",
      "Beija-flor e pontapé.",
      "Planalto (plano + alto) e vinagre (vinho + acre).",
      "Segunda-feira e micro-ondas."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Em 'planalto' (plano + alto) e 'vinagre' (vinho + acre), houve alteração fonética e perda de elementos mórficos originais, caracterizando aglutinação. Todas as outras opções trazem termos compostos por justaposição."
  },
  {
    "id": 206,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Identificação do Radical",
    "question": "O RADICAL é o elemento mórfico fundamental e indivisível que contém o significado básico da palavra e é comum às palavras de uma mesma família (cognatas). Identifique a palavra que NÃO pertence à mesma família cognata das demais:",
    "options": [
      "Cabelo, cabeceira, cabeçalho e cabeçudo.",
      "Pedreiro, pedregulho, apedrejar e pedra.",
      "Livraria, livreiro, livrinho e livro.",
      "Terráqueo, terrestre, aterrar e terra."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 'Cabelo' tem raiz etimológica ligada a pelos capilares (latim 'capillus'). Já 'cabeceira', 'cabeçalho' e 'cabeçudo' derivam do radical de 'cabeça' (latim 'capitia'). As opções A, B e C reúnem palavras legitimamente cognatas com o mesmo radical compartilhado."
  },
  {
    "id": 207,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Desinências Nominais de Gênero e Número",
    "question": "Na morfologia da Língua Portuguesa, as desinências nominais indicam gênero (masculino/feminino) e número (singular/plural). Na palavra 'MENINAS', os morfemas '-A-' e '-S' classificam-se, respectivamente, como:",
    "options": [
      "Vogal temática e sufixo aumentativo.",
      "Desinência nominal de gênero feminino e desinência nominal de número plural.",
      "Radical flexionado e consoante eufônica de ligação.",
      "Afixo derivacional e desinência verbal de pessoa."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Na estrutura 'MENIN-A-S': 'menin-' é o radical; '-a-' é a desinência nominal de gênero feminino; '-s' é a desinência nominal de número plural."
  },
  {
    "id": 208,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Vogal Temática Verbal e Tema",
    "question": "A VOGAL TEMÁTICA liga o radical às desinências e indica a conjugação verbal (1ª -a, 2ª -e, 3ª -i). O radical somado à vogal temática constitui o:",
    "options": [
      "Afixo composto.",
      "Cognato absoluto.",
      "Morfema zero.",
      "Tema."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Na morfologia verbal: Radical + Vogal Temática = TEMA. Exemplo: no verbo 'cantar', 'cant-' é o radical e '-a-' é a vogal temática da 1ª conjugação. O tema é 'canta-'."
  },
  {
    "id": 209,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Vogais e Consoantes de Ligação",
    "question": "Vogais e consoantes de ligação são elementos fonéticos eufônicos inseridos entre morfemas unicamente para facilitar a pronúncia, desprovidos de significado gramatical próprio. Há uma CONSOANTE DE LIGAÇÃO na palavra:",
    "options": [
      "Infelizmente (in + feliz + mente)",
      "Desleal (des + leal)",
      "Cafeteira (café + -t- + eira)",
      "Pedrada (pedra + ada)"
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Em 'café' + '-eira', a junção direta geraria o cacófato 'cafeeira'. Inseriu-se a consoante eufônica '-t-' (cafeteira) exclusivamente para fluidez fonética. Outros exemplos: pau-l-ada, cha-l-eira."
  },
  {
    "id": 210,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Hibridismo",
    "question": "O processo de formação de palavras em que ocorre a junção de elementos mórficos originários de IDIOMAS DIFERENTES é denominado:",
    "options": [
      "Neologismo fonético espontâneo.",
      "Hibridismo (ex: televisão: tele grego + visão latim; burocracia: bureau francês + cracia grego).",
      "Siglonimização e acrônimo.",
      "Onomatopeia imitativa de ruídos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Hibridismo é a formação de uma palavra com radicais ou afixos de línguas distintas. Exemplos clássicos: Televisão (tele = grego, visão = latim), Burocracia (bureau = francês, cracia = grego), Automóvel (auto = grego, móvel = latim)."
  },
  {
    "id": 211,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Onomatopeia",
    "question": "Assinale a alternativa que apresenta vocábulos formados por ONOMATOPEIA (reprodução aproximada de sons ou ruídos da natureza e de objetos):",
    "options": [
      "Amanhecer, entardecer e anoitecer.",
      "Fidalgo, aguardente e pernalta.",
      "Couve-flor, guarda-chuva e girassol.",
      "Tic-tac, zunzum, miau e coaxar."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A onomatopeia consiste na criação de vocábulos que buscam imitar sons ou ruídos reais: tic-tac (relógio), zunzum (zumbido), miau (gato), coaxar (sapo), pingue-pongue."
  },
  {
    "id": 212,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Derivação Prefixal com Prefixo Negativo",
    "question": "Os prefixos 'in-' (latim) e 'a-' (grego) denotam privação ou negação. Assinale a opção em que AMBAS as palavras apresentam prefixos com valor semântico de NEGAÇÃO:",
    "options": [
      "Importar e adjunto.",
      "Inativo e atípico.",
      "Progresso e antebraço.",
      "Submarino e supersensível."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. 'Inativo' = não ativo (in- negativo latino); 'Atípico' = não típico (a- de privação grego). Em (B), 'importar' traz o 'in-' com sentido de movimento para dentro; em (C), 'pro-' denota para a frente; em (D), 'sub-' significa debaixo."
  },
  {
    "id": 213,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Sufixos Formadores de Substantivos Abstratos",
    "question": "Os sufixos nominalizadores transformam verbos ou adjetivos em substantivos. O sufixo presente em 'ORGANIZAÇÃO' (-ção) indica precipuamente a noção de:",
    "options": [
      "Ação ou resultado de uma ação.",
      "Lugar ou estabelecimento comercial.",
      "Profissão ou agente executor.",
      "Grau diminutivo pejorativo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O sufixo '-ção' (organiza + ção, promulga + ção, delibera + ção) é um sufixo nominalizador deverbal que exprime o ato, ação ou o resultado da ação do verbo."
  },
  {
    "id": 214,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Siglas e Acrônimos",
    "question": "No vocabulário administrativo e legislativo, as palavras formadas pela combinação das letras ou sílabas iniciais de uma denominação composta (ex: MERCOSUL, UNESCO, EMBRAPA) que podem ser pronunciadas como uma palavra comum denominam-se:",
    "options": [
      "Estrangeirismos arcaicos.",
      "Derivações parassintéticas truncadas.",
      "Acrônimos.",
      "Arcaísmos de composição por justaposição."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Acrônimo é a sigla que se pronuncia como uma palavra contínua e natural da língua (ex: Embrapa, Mercosul, Petrobras, Unesco). Diferencia-se das siglas puras que exigem soletração letra a letra (ex: CPF, OAB, IPTU)."
  },
  {
    "id": 215,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Neologismo",
    "question": "O processo linguístico pelo qual novos termos são criados ou importados para suprir a necessidade de nomear novos conceitos científicos, tecnológicos ou socioculturais (ex: 'deletar', 'tuitar', 'printar') é chamado de:",
    "options": [
      "Solecismo de regência.",
      "Pleonasmo de reforço.",
      "Neologismo.",
      "Ambiguidade estilística."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Neologismo é a criação de palavras novas ou a atribuição de novos significados a termos preexistentes na língua, refletindo inovações da sociedade e tecnologia."
  },
  {
    "id": 216,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Palavra Primitiva vs Derivada",
    "question": "Em relação à relação morfológica entre primitivo e derivado, assinale o par em que a segunda palavra é DERIVADA da primeira:",
    "options": [
      "Lei -> Legalizar.",
      "História -> Histórico (ambas são primitivas).",
      "Vento -> Ventania (ambas são formadas por composição).",
      "Flor -> Floricultura (formada unicamente por hibridismo)."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. 'Lei' é vocábulo primitivo (não se origina de outra palavra na língua portuguesa). 'Legalizar' é derivada de 'legal' (sua vez derivada de lei) por sufixação (-izar)."
  },
  {
    "id": 217,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Abreviatura vs Sigla vs Redução (Abreviação Vocabular)",
    "question": "O processo de ABREVIAÇÃO VOCABULAR (ou redução) consiste na eliminação de uma parte da palavra a fim de economizar tempo e esforço na comunicação falada ou escrita. Assinale o exemplo de abreviação vocabular:",
    "options": [
      "OAB (Ordem dos Advogados do Brasil).",
      "Passatempo (de passa + tempo).",
      "Amanhecer (de a + manhã + ecer).",
      "Foto (de fotografia), moto (de motocicleta) e fone (de telefone)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Abreviação vocabular (ou redução) é a redução de uma palavra longa mantendo o significado original: foto (fotografia), moto (motocicleta), fone (telefone), quilo (quilograma), cine (cinema)."
  },
  {
    "id": 218,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Desinência Modo-Temporal Verbal",
    "question": "Na forma verbal 'ESTUDÁVAMOS', o segmento mórfico '-VA-' classifica-se como:",
    "options": [
      "Desinência número-pessoal (indica primeira pessoa do plural).",
      "Desinência modo-temporal (indica pretérito imperfeito do modo indicativo).",
      "Vogal de ligação eufônica.",
      "Sufixo adverbializatório de intensidade."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Em 'estud-á-va-mos': 'estud-' é o radical; '-a-' é a vogal temática; 'estuda-' é o tema; '-va-' é a desinência modo-temporal (DMT) do pretérito imperfeito do indicativo; '-mos' é a desinência número-pessoal (DNP) de 1ª pessoa do plural."
  },
  {
    "id": 219,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Análise Estrutural Completa de Vocábulo",
    "question": "Assinale a alternativa em que a divisão mórfica do vocábulo 'DESALINHAMENTO' e a identificação de seus elementos estão inteiramente corretas:",
    "options": [
      "Desalinha- (radical único) + -mento (desinência de número).",
      "Des- (afixo flexional) + alinhamento (palavra composta por aglutinação).",
      "Des- (prefixo) + alinh- (radical) + -a- (vogal temática) + -mento (sufixo derivacional formador de substantivo).",
      "De- (prefixo) + salinha (radical) + -mento (sufixo aumentativo)."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. 'Desalinhamento' estrutura-se por: Prefixo 'des-' (sentido de negação/inversão) + Radical 'alinh-' (de linha) + Vogal temática '-a-' + Sufixo nominalizador '-mento' (formador de substantivo abstrato que indica ação ou resultado)."
  },
  {
    "id": 220,
    "category": "portugues",
    "day": "w2_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Identificação Geral dos Processos em Concurso",
    "question": "Relacione as colunas quanto ao processo de formação de palavras:\n(1) Justaposição\n(2) Aglutinação\n(3) Parassíntese\n(4) Derivação Imprópria\n\n( ) Envergonhar\n( ) Guarda-noturno\n( ) O olhar triste da testemunha\n( ) Pernalta\n\nA sequência correta de preenchimento, de cima para baixo, é:",
    "options": [
      "3 — 1 — 4 — 2",
      "1 — 3 — 2 — 4",
      "3 — 2 — 1 — 4",
      "4 — 1 — 3 — 2"
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Envergonhar: en- + vergonh- + -ar (parassíntese: 3); Guarda-noturno: guarda + noturno sem perda (justaposição: 1); O olhar triste: 'olhar' substantivado pelo artigo 'o' (derivação imprópria: 4); Pernalta: perna + alta com perda da vogal 'a' (aglutinação: 2). Sequência: 3, 1, 4, 2."
  }
,
{
  "id": 221,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Funções Típicas do Poder Legislativo",
  "question": "O Poder Legislativo Municipal, exercido pela Câmara de Vereadores, possui funções essenciais atribuídas diretamente pelo ordenamento constitucional. São consideradas funções TÍPICAS do Poder Legislativo Municipal:",
  "options": [
    "Administrar os serviços públicos de saúde e saneamento básico em colaboração direta com os secretários municipais.",
    "Julgar litígios judiciais entre servidores públicos e a prefeitura, substituindo a competência da vara cível da comarca.",
    "Promover a desapropriação compulsória de imóveis urbanos que não cumpram a função social da propriedade sem participação do Executivo.",
    "Legislar sobre assuntos de interesse local e exercer a fiscalização contábil, financeira, orçamentária e patrimonial da administração pública local."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. O Poder Legislativo tem como funções típicas precípuas: (1) Legislar (elaborar normas jurídicas locais) e (2) Fiscalizar (controle externo contábil, financeiro, orçamentário e operacional do Executivo e dos seus próprios órgãos, com auxílio do Tribunal de Contas)."
},
{
  "id": 222,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Funções Atípicas da Câmara Municipal",
  "question": "A teoria da separação de poderes no Brasil admite o exercício de funções atípicas por todos os Poderes da República. No âmbito da Câmara Municipal, constitui exemplo legítimo de FUNÇÃO ATÍPICA DE NATUREZA JULGADORA:",
  "options": [
    "Processar e julgar mandados de segurança impetrados por cidadãos contra atos do Presidente da Casa Legislativa.",
    "Condenar criminalmente servidores municipais à pena restritiva de liberdade por crimes de peculato e corrupção.",
    "Julgar o Prefeito, o Vice-Prefeito e os próprios Vereadores por infrações político-administrativas tipificadas em lei.",
    "Julgar as ações populares de nulidade de contratos administrativos de licitação firmados pelo Poder Executivo."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. A Câmara Municipal exerce função atípica de julgar ao processar e julgar o Prefeito e os próprios Vereadores por infrações político-administrativas (ex.: infrações descritas no Decreto-Lei nº 201/67 e na Lei Orgânica Municipal)."
},
{
  "id": 223,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Imunidade Material dos Vereadores (Art. 29, VIII CF)",
  "question": "Nos termos do Art. 29, VIII da Constituição Federal de 1988 e das leis orgânicas municipais, os Vereadores gozam de inviolabilidade (imunidade material) por suas opiniões, palavras e votos:",
  "options": [
    "No exercício do mandato e na circunscrição do Município.",
    "Em todo o território nacional, independentemente de conexão com o exercício do mandato parlamentar.",
    "Apenas dentro do recinto físico do plenário e das comissões temáticas da Câmara de Vereadores.",
    "Exclusivamente durante os períodos de sessões extraordinárias convocadas com quórum qualificado de dois terços."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 29, VIII da CF/88: 'inviolabilidade dos Vereadores por suas opiniões, palavras e votos no exercício do mandato e na circunscrição do Município'. A imunidade material do vereador possui limitação territorial estrita à circunscrição do município."
},
{
  "id": 224,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Mesa Diretora e Iniciativa Privativa de Leis",
  "question": "A Mesa Diretora é o órgão colegiado responsável pela direção dos trabalhos legislativos e dos serviços administrativos da Câmara. É matéria de INICIATIVA PRIVATIVA da Mesa Diretora da Câmara Municipal propor projeto de lei que disponha sobre:",
  "options": [
    "A organização administrativa da Câmara, criação e extinção de seus cargos e a fixação da respectiva remuneração.",
    "O Plano Plurianual (PPA), as Diretrizes Orçamentárias (LDO) e o Orçamento Anual (LOA) do Município.",
    "O Plano Diretor de Desenvolvimento Urbano e o zoneamento territorial municipal.",
    "A criação de secretarias municipais e atribuições dos órgãos da administração direta do Poder Executivo."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. A organização dos serviços da Câmara, a criação, transformação ou extinção de seus cargos, empregos e funções e a fixação da respectiva remuneração são de competência privativa da Mesa Diretora da Câmara (Art. 51, IV c/c Art. 29 da CF/88 e Lei Orgânica)."
},
{
  "id": 225,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Atribuições do Presidente da Câmara Municipal",
  "question": "No desempenho de suas funções regimentais e institucionais, compete privativamente ao Presidente da Câmara Municipal de Vereadores:",
  "options": [
    "Sancionar projetos de lei de autoria exclusiva de parlamentares sem encaminhamento prévio ao Prefeito Municipal.",
    "Vetar parcialmente projetos de lei aprovados pelo Plenário por motivo de inconstitucionalidade material.",
    "Suspender unilateralmente a vigência de decretos do Poder Executivo sem deliberação do Plenário.",
    "Representar a Câmara em juízo e fora dele, bem como promulgar leis quando o Prefeito descumprir o prazo legal após a rejeição do veto pelo Plenário."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. O Presidente da Câmara é o representante judicial e extrajudicial do Poder Legislativo local. Além disso, se o Prefeito não promulgar a lei no prazo de 48 horas após a derrubada do veto, cabe ao Presidente da Câmara promulgá-la (e, se este não o fizer em igual prazo, ao Vice-Presidente)."
},
{
  "id": 226,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Comissões Parlamentares de Inquérito (CPIs)",
  "question": "De acordo com a Constituição Federal (Art. 58, § 3º) e a legislação parlamentar, as Comissões Parlamentares de Inquérito (CPIs) no âmbito municipal serão criadas mediante requerimento de:",
  "options": [
    "Maioria absoluta dos membros da Câmara, para apuração ampla e irrestrita de qualquer ato da gestão municipal sem prazo determinado.",
    "Dois terços dos parlamentares presentes, com competência para decretar a indisponibilidade patrimonial e prisão preventiva dos investigados.",
    "Metade mais um dos vereadores, dependendo de prévia autorização homologatória do juiz de direito da comarca local.",
    "Pelo menos um terço dos membros da Câmara, para apuração de fato determinado e por prazo certo, com poderes de investigação próprios das autoridades judiciais."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Requisitos da CPI: requerimento de 1/3 dos membros da Casa, apuração de fato determinado, prazo certo e poderes de investigação próprios das autoridades judiciais. Atenção: CPI não tem reserva de jurisdição (não pode determinar interceptação telefônica, busca domiciliar nem decretar prisão fora de flagrante)."
},
{
  "id": 227,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Comissões Permanentes vs Temporárias",
  "question": "Na estrutura organizacional do Poder Legislativo, as comissões parlamentares classificam-se em permanentes e temporárias. Sobre as COMISSÕES PERMANENTES, assinale a afirmativa correta:",
  "options": [
    "São constituídas exclusivamente para representar a Câmara Municipal em eventos protocolares e congressos fora do estado.",
    "Subsistem através das legislaturas e têm por objetivo analisar o mérito e a constitucionalidade das proposições afetas à sua respectiva área temática.",
    "Extinguem-se automaticamente assim que concluem a emissão de parecer sobre o projeto de lei orçamentária do ano corrente.",
    "São compostas exclusivamente pelos líderes partidários da base de apoio formal ao Prefeito Municipal."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Comissões Permanentes são órgãos técnicos colegiados estáveis que perduram pelas legislaturas e apreciam projetos de acordo com as áreas temáticas (Constituição e Justiça, Finanças e Orçamento, Obras Públicas, Educação e Saúde)."
},
{
  "id": 228,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Processo de Cassação por Infração Político-Administrativa",
  "question": "No processo de cassação do mandato do Prefeito ou de Vereador perante a Câmara Municipal por infrações político-administrativas (Decreto-Lei nº 201/67 e LOM), a deliberação final que decide pela cassação exige o quórum qualificado de:",
  "options": [
    "Maioria simples dos vereadores votantes na sessão extraordinária de julgamento.",
    "Maioria absoluta dos membros componentes do Poder Legislativo Municipal.",
    "Dois terços (2/3) dos membros da Câmara Municipal, assegurados o contraditório e a ampla defesa ao acusado.",
    "Unanimidade dos vereadores que compõem a comissão processante destacada para o caso."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 5º, VI do DL 201/67 e disposições das Leis Orgânicas Municipais: o mandato do Prefeito ou Vereador somente será cassado se decorrer de decisão tomada por no mínimo 2/3 (dois terços) dos membros da Câmara Municipal."
},
{
  "id": 229,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Perda e Extinção do Mandato de Vereador",
  "question": "Em relação à perda e extinção do mandato parlamentar na Câmara Municipal, a declaração de perda do mandato será feita DE OFÍCIO PELA MESA DIRETORA (sem necessidade de votação do Plenário) quando o Vereador:",
  "options": [
    "Proceder de modo incompatível com a dignidade da Câmara ou incidir em quebra comprovada do decoro parlamentar.",
    "Deixar de comparecer, em cada sessão legislativa, à terça parte (1/3) das sessões ordinárias da Casa, salvo licença ou missão autorizada.",
    "Sofrer acusação formal formulada em CPI ainda sem julgamento do mérito judicial.",
    "Votar contra a orientação partidária do seu líder em projeto de lei de diretrizes orçamentárias."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. A falta a 1/3 das sessões ordinárias anuais (sem licença justificada) ou a perda/suspensão dos direitos políticos gera EXTINÇÃO/PERDA DECLARADA DE OFÍCIO pela Mesa Diretora. Já a quebra de decoro ou condenação criminal com trânsito em julgado exige deliberação do Plenário por maioria absoluta."
},
{
  "id": 230,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Quórum Regimental: Maioria Simples vs Absoluta vs Qualificada",
  "question": "O quórum de deliberação é a quantidade mínima de votos exigida para que a Câmara Municipal aprove legitimamente determinado ato legislativo. Assinale a correta correlação entre a matéria e o seu respectivo quórum constitucional:",
  "options": [
    "Aprovação de Emenda à Lei Orgânica Municipal — Exige quórum qualificado de dois terços (2/3) dos membros em dois turnos de votação.",
    "Aprovação de Lei Ordinária Municipal — Exige quórum qualificado de três quintos (3/5) de todos os eleitores cadastrados.",
    "Rejeição de veto do Prefeito Municipal — Exige maioria simples dos presentes na ordem do dia.",
    "Aprovação do Regimento Interno da Câmara — Exige maioria simples dos vereadores presentes na abertura da sessão."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. A Emenda à Lei Orgânica exige votação em dois turnos com interstício mínimo de 10 dias e aprovação por 2/3 dos membros da Câmara (Art. 29, caput da CF/88). Lei ordinária exige maioria simples. Rejeição de veto exige maioria absoluta. Regimento interno exige maioria absoluta."
},
{
  "id": 231,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Iniciativa Legislativa Popular no Município",
  "question": "A Constituição Federal de 1988 consagrou a iniciativa popular de projetos de lei como expressão da democracia direta e participativa. No âmbito dos Municípios, a iniciativa popular de projetos de lei de interesse específico do município exige a manifestação de:",
  "options": [
    "Pelo menos 1% (um por cento) do eleitorado nacional distribuído em pelo menos cinco municípios limítrofes.",
    "Pelo menos 10% (dez por cento) dos servidores públicos municipais da administração direta e autárquica.",
    "Pelo menos 20% (vinte por cento) dos moradores inscritos no cadastro imobiliário de IPTU da cidade.",
    "Pelo menos 5% (cinco por cento) do eleitorado municipal, mediante projeto articulado subscrito pelos cidadãos."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 29, XIII da CF/88: 'iniciativa popular de projetos de lei de interesse específico do Município, da cidade ou de bairros, através de manifestação de, pelo menos, cinco por cento do eleitorado'."
},
{
  "id": 232,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Fases do Processo Legislativo Municipal",
  "question": "O rito procedimental pelo qual uma proposição percorre os órgãos da Câmara até transformar-se em lei compõe o processo legislativo. A fase constitutiva do processo legislativo compreende as seguintes etapas em ordem cronológica:",
  "options": [
    "Elaboração de minuta no gabinete do vereador e divulgação oficiosa nas redes sociais da Câmara.",
    "Homologação liminar pelo Ministério Público Estadual e publicação no Diário da Justiça Eleitoral.",
    "Deliberação parlamentar (discussão e votação em Plenário) e deliberação executiva (sanção ou veto do Prefeito).",
    "Parecer vinculante do Tribunal de Justiça Estadual e assinatura do Presidente da República."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O processo legislativo desdobra-se em: (1) Fase introdutória (iniciativa/protocolo); (2) Fase constitutiva (deliberação parlamentar em comissões e plenário + deliberação executiva com sanção ou veto); (3) Fase complementar (promulgação e publicação)."
},
{
  "id": 233,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Veto do Prefeito e Quórum de Rejeição",
  "question": "Recebido o projeto de lei aprovado pela Câmara, o Prefeito Municipal dispõe do prazo de 15 (quinze) dias úteis para sancioná-lo ou vetá-lo. Caso decida pelo VETO, para que a Câmara Municipal REJEITE o veto e mantenha o texto original, é necessária deliberação por:",
  "options": [
    "Maioria simples dos vereadores que comparecerem à sessão em que o veto for apreciado.",
    "Maioria absoluta dos membros da Câmara Municipal, em escrutínio aberto, dentro do prazo legal de 30 dias.",
    "Quórum qualificado obrigatório e unânime de todos os líderes de bancada formalmente constituídos.",
    "Três quintos (3/5) dos membros titulares da comissão temática permanente de legislação e justiça."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 66, § 4º da CF/88 aplicado por simetria aos Municípios: o veto só pode ser rejeitado pelo voto da maioria absoluta dos vereadores (e não por maioria simples). O silêncio do Prefeito após 15 dias úteis importa em sanção tácita."
},
{
  "id": 234,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Sessões Extraordinárias da Câmara",
  "question": "A convocação extraordinária da Câmara Municipal é permitida em situações de urgência ou interesse público relevante. Durante uma Sessão Legislativa Extraordinária, a Câmara de Vereadores deliberará:",
  "options": [
    "Livremente sobre qualquer projeto pendente de votação ordinária, inclusive moções e homenagens cívicas.",
    "Exclusivamente sobre a destituição de membros da Mesa Diretora por voto de censura administrativa.",
    "Sobre matérias ordinárias mediante percepção obrigatória de verba pecuniária extraordinária dobrada por sessão.",
    "Somente sobre a matéria para a qual foi expressamente convocada, vedado o pagamento de parcela indenizatória em razão da convocação."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 57, § 7º da CF/88 e legislação municipal: na sessão legislativa extraordinária, a Câmara somente delibera sobre a matéria para a qual foi convocada (princípio da especificidade da pauta) e é vedado o pagamento de parcela indenizatória pela convocação (Art. 57, § 7º)."
},
{
  "id": 235,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Controle Externo da Câmara e Parecer do TCE",
  "question": "A fiscalização financeira e orçamentária do Município será exercida pela Câmara Municipal mediante controle externo, auxiliada pelo Tribunal de Contas do Estado. Acerca do parecer prévio emitido pelo Tribunal de Contas, assinale a opção correta:",
  "options": [
    "Possui eficácia vinculante automática e imediata, não podendo o Poder Legislativo discordar de suas conclusões técnicas.",
    "Tem natureza técnica e opinativa, deixando de prevalecer unicamente por decisão fundamentada de dois terços (2/3) dos membros da Câmara.",
    "Pode ser rejeitado livremente pela maioria simples dos vereadores presentes em sessão ordinária única.",
    "Depende de homologação prévia por decreto do Chefe do Poder Executivo para produzir efeitos de inelegibilidade."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 31, § 2º da CF/88: o parecer prévio emitido pelo órgão competente sobre as contas que o Prefeito deve prestar anualmente só deixará de prevalecer por decisão de dois terços dos membros da Câmara Municipal."
},
{
  "id": 236,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Princípio da Simetria Constitucional no Processo Legislativo",
  "question": "O Princípio da Simetria Constitucional exige que os entes federados adotem as regras básicas de organização e processo legislativo traçadas pela Constituição Federal. Em observância a esse princípio, é DEFESO (proibido) à Câmara Municipal:",
  "options": [
    "Rejeitar projetos de lei de iniciativa do Chefe do Poder Executivo que criem obrigações orçamentárias.",
    "Criar Comissões Parlamentares de Inquérito para apurar irregularidades em contratos de transporte público.",
    "Apresentar emenda parlamentar a projeto do Executivo que acarrete aumento de despesa em matérias de iniciativa reservada ao Prefeito.",
    "Apreciar vetos totais ou parciais apostos pelo Executivo em projetos de lei originados de emendas constitucionais."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 63, I da CF/88: não será admitido aumento da despesa prevista nos projetos de iniciativa exclusiva do Chefe do Poder Executivo. O princípio da simetria veda que vereadores aumentem despesa em projetos de iniciativa reservada do Prefeito."
},
{
  "id": 237,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Espécies Normativas: Decreto Legislativo vs Resolução",
  "question": "Dentre os atos do processo legislativo previstos no ordenamento jurídico, diferenciam-se o DECRETO LEGISLATIVO e a RESOLUÇÃO da Câmara. A respeito dessa distinção técnica, assinale a opção correta:",
  "options": [
    "O Decreto Legislativo destina-se apenas a organizar o regimento interno, ao passo que a Resolução altera a Lei Orgânica Municipal.",
    "O Decreto Legislativo disciplina matéria de competência exclusiva da Câmara de efeitos externos (ex.: julgamento das contas do Prefeito), enquanto a Resolução disciplina matéria de economia interna (ex.: Regimento Interno).",
    "A Resolução depende obrigatoriamente de sanção e promulgação pelo Prefeito Municipal para entrar em vigor.",
    "O Decreto Legislativo é ato administrativo infralegal expedido privativamente pelos Secretários Municipais."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Decretos Legislativos tratam de competências privativas/exclusivas da Câmara que geram efeitos externos (ex: aprovação de contas do prefeito, concessão de licença ao prefeito, sustação de atos normativos do Executivo). Resoluções tratam de matéria estritamente interna (ex: Regimento Interno, estrutura administrativa dos gabinetes)."
},
{
  "id": 238,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Suplência e Convocação de Vereador",
  "question": "Em consonância com as regras eleitorais e regimentais do Poder Legislativo Municipal, a convocação do suplente de Vereador dar-se-á nos casos de:",
  "options": [
    "Ausência justificada do titular a uma única sessão ordinária por motivos de saúde temporária.",
    "Voto divergente do titular em relação às deliberações firmadas em convenção partidária municipal.",
    "Morte, renúncia, cassação do titular ou licença por período contínuo superior ao fixado no Regimento Interno e Lei Orgânica.",
    "Instauração de sindicância administrativa preliminar sem afastamento cautelar determinado por juiz."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O suplente de vereador é convocado nos casos de vacância definitiva (morte, renúncia, perda/cassação de mandato) ou de licença do titular por período prolongado estabelecido na Lei Orgânica/Regimento Interno (geralmente superior a 120 dias ou para assumir cargo de Secretário Municipal)."
},
{
  "id": 239,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Natureza Jurídica do Regimento Interno da Câmara",
  "question": "O Regimento Interno da Câmara Municipal é a norma jurídica mestra que estrutura seu funcionamento. Sob a ótica do Direito Constitucional e Administrativo, o Regimento Interno:",
  "options": [
    "É veiculado sob a forma de Lei Ordinária, sujeitando-se obrigatoriamente ao veto político do Prefeito Municipal.",
    "Constitui decreto governamental expedido pelo Governador do Estado para padronizar as câmaras municipais.",
    "É veiculado sob a forma de Resolução, constituindo matéria interna corporis e auto-organizatória, insuscetível de veto pelo Chefe do Poder Executivo.",
    "Exige referendo popular compulsório a cada eleição municipal para manter sua eficácia normativa interna."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O Regimento Interno é veiculado por Resolução, ato normativo primário de competência privativa da Câmara que corporifica sua autonomia institucional (auto-organização parlamentar). Não passa pelo crivo de sanção ou veto do Prefeito."
},
{
  "id": 240,
  "category": "legislacao",
  "day": "w2_d2",
  "discipline": "Técnico Legislativo",
  "topic": "Publicidade e Transparência dos Atos Parlamentares (Lei 12.527/2011)",
  "question": "A Lei de Acesso à Informação (LAI - Lei nº 12.527/2011) e o Art. 37 da CF/88 impõem o princípio da publicidade aos órgãos legislativos. No âmbito da Câmara de Vereadores, constitui exigência de TRANSPARÊNCIA ATIVA:",
  "options": [
    "A exigência de que todo cidadão justifique documentalmente o motivo de seu interesse para obter cópia da ata da sessão.",
    "A divulgação em portal oficial na internet, independentemente de requerimentos, da execução orçamentária, folhas de pagamento, licitações e votações nominais.",
    "O fornecimento de informações contábeis restrito àqueles que comprovarem domicílio eleitoral no município há mais de cinco anos.",
    "A cobrança de taxa de protocolo prévia para acesso aos dados de remuneração dos cargos em comissão da Casa Legislativa."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. A transparência ativa consiste no dever do órgão público (incluindo as Câmaras Municipais) de disponibilizar espontaneamente na internet, sem necessidade de solicitação prévia, relatórios de despesas, salários, editais, contratos e deliberações plenárias (Art. 8º da Lei nº 12.527/2011)."
},
{
  "id": 241,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Sintaxe do Verbo Haver (Impessoalidade)",
  "question": "Nas provas da banca INBRASP, a sintaxe do verbo 'HAVER' é alvo frequente de cobrança gramatical. Assinale a frase em que a concordância do verbo destacado está INTEIRAMENTE CORRETA segundo a norma culta:",
  "options": [
    "Houve manifestações calorosas dos munícipes durante a apreciação das emendas orçamentárias.",
    "Houveram muitos pedidos de esclarecimento apresentados pelos vereadores da oposição.",
    "Haverão de existir soluções viáveis para equilibrar os limites de gastos da Câmara Municipal.",
    "Devem haverem critérios transparentes na concessão de diárias aos técnicos legislativos."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. O verbo HAVER, com sentido de 'existir', 'acontecer' ou tempo decorrido, é impessoal: não possui sujeito e deve permanecer obrigatoriamente na 3ª pessoa do singular ('Houve manifestações', 'Havia muitos pedidos', 'Deve haver critérios')."
},
{
  "id": 242,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Verbo Haver vs. Verbo Existir",
  "question": "Ao contrário de 'haver' (quando impessoal), o verbo 'EXISTIR' é pessoal e concorda normalmente com o seu sujeito gramatical. Assinale a alternativa que apresenta a correta concordância de ambos os verbos:",
  "options": [
    "Haviam muitas divergências entre os parlamentares, mas existia pontos de consenso sobre o piso salarial.",
    "Havia muitas divergências entre os parlamentares, mas existia pontos de consenso sobre o piso salarial.",
    "Haviam muitas divergências entre os parlamentares, mas existiam pontos de consenso sobre o piso salarial.",
    "Havia muitas divergências entre os parlamentares, mas existiam pontos de consenso sobre o piso salarial."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. 'Haver' (no sentido de existir) não vai para o plural ('Havia muitas divergências' - 'muitas divergências' é objeto direto). Já 'existir' é verbo intransitivo e possui sujeito ('pontos de consenso'), devendo concordar no plural ('existiam pontos de consenso')."
},
{
  "id": 243,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Locuções Verbais com Verbos Impessoais",
  "question": "Nas locuções verbais em que o verbo principal é o verbo 'HAVER' (no sentido de existir), o verbo auxiliar herda a impessoalidade, permanecendo invariável. Assinale a opção que observa corretamente essa regra:",
  "options": [
    "Podem haver irregularidades graves nos relatórios fiscais do exercício pretérito.",
    "Pode haver irregularidades graves nos relatórios fiscais do exercício pretérito.",
    "Devem haverem mecanismos mais rígidos de controle preventivo dos gastos públicos.",
    "Vão haverem novas audiências públicas na Câmara Municipal nesta legislatura."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Quando 'haver' for o verbo principal de uma locução verbal e estiver no sentido de existir, ele transmite sua impessoalidade ao verbo auxiliar, que deve ficar no singular: 'Pode haver irregularidades', 'Deve haver mecanismos', 'Vai haver audiências'."
},
{
  "id": 244,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Voz Passiva Sintética (Partícula Apassivadora 'se')",
  "question": "Quando associado a verbos transitivos diretos (VTD), o vocábulo 'SE' atua como partícula apassivadora, exigindo a concordância do verbo com o sujeito paciente. Assinale o exemplo que atende com exatidão a esse preceito:",
  "options": [
    "Aprovaram-se as diretrizes orçamentárias prioritárias para o próximo exercício financeiro.",
    "Aprovou-se as diretrizes orçamentárias prioritárias para o próximo exercício financeiro.",
    "Verificou-se muitas incoerências técnicas durante a instrução probatória do processo.",
    "Constatou-se várias incorreções graves nos cálculos atuariais do regime de previdência."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Em 'Aprovaram-se as diretrizes', o verbo 'aprovar' é VTD acompanhado da partícula apassivadora 'se'. 'As diretrizes orçamentárias' é o sujeito paciente (na voz passiva analítica: 'As diretrizes orçamentárias foram aprovadas'). Logo, o verbo deve ir ao plural."
},
{
  "id": 245,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Índice de Indeterminação do Sujeito ('se')",
  "question": "Quando o vocábulo 'SE' atua como ÍNDICE DE INDETERMINAÇÃO DO SUJEITO (acompanhando verbos transitivos indiretos, intransitivos ou de ligação), o verbo fica invariavelmente na 3ª pessoa do singular. Assinale a frase que exemplifica esse caso:",
  "options": [
    "Precisam-se de novos técnicos legislativos capacitados para atuar nas comissões temáticas.",
    "Precisa-se de novos técnicos legislativos capacitados para atuar nas comissões temáticas.",
    "Tratam-se de propostas orçamentárias de relevante interesse comunitário para Meruoca.",
    "Necessitam-se de certidões negativas de débito para a homologação da licitação."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Em 'Precisa-se de novos técnicos', o verbo 'precisar' é transitivo indireto (exige a preposição 'de'). O 'se' é índice de indeterminação do sujeito e 'de novos técnicos' é objeto indireto. Nesse caso, o verbo jamais vai para o plural: 'Precisa-se de...', 'Trata-se de...', 'Necessita-se de...'."
},
{
  "id": 246,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Correlação Verbal (Subjuntivo e Indicativo)",
  "question": "A adequada correlação entre os tempos e modos verbais confere coerência e precisão aos textos legislativos. Assinale a alternativa que apresenta a CORRETA CORRELAÇÃO verbal segundo a norma gramatical:",
  "options": [
    "Se o relator apresentasse o parecer tempestivamente, o Plenário votará a matéria hoje.",
    "Se o relator apresentar o parecer tempestivamente, o Plenário votava a matéria hoje.",
    "Caso o relator apresente o parecer tempestivamente, o Plenário votaria a matéria hoje.",
    "Se o relator apresentasse o parecer tempestivamente, o Plenário votaria a matéria hoje."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. A clássica correlação condicional hipotética exige: Pretérito imperfeito do subjuntivo ('apresentasse') articulado ao Futuro do pretérito do indicativo ('votaria'). Já o futuro do subjuntivo ('se apresentar') articula-se ao futuro do presente ('votará')."
},
{
  "id": 247,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Pretérito Mais-Que-Perfeito do Indicativo",
  "question": "Na oração 'Quando o Presidente abriu a sessão solene, a comissão já TERMINARA a leitura da ata', a forma verbal em destaque expressa:",
  "options": [
    "Uma ação habitual e contínua no presente com efeitos projetados para o futuro.",
    "Uma ação passada concluída anteriormente a outro fato também passado.",
    "Uma hipótese incerta condicionada à ocorrência de um evento contingente.",
    "Um fato futuro tomado em relação a um momento imediatamente contemporâneo."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. O pretérito mais-que-perfeito do indicativo (terminara, fizera, falara, concluíra) denota uma ação passada que ocorreu antes de outro evento igualmente passado (equivale à forma composta 'já havia terminado')."
},
{
  "id": 248,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Pretérito Perfeito vs. Pretérito Imperfeito",
  "question": "Assinale a alternativa em que o verbo destacado no pretérito imperfeito do indicativo expressa uma ação habitual, costumeira ou repetitiva no passado:",
  "options": [
    "Naquela época, os munícipes COMPARECIAM semanalmente à Câmara para acompanhar as votações.",
    "Ontem à tarde, o Prefeito Municipal ASSINOU o decreto de exoneração do assessor parlamentar.",
    "A comissão processante ENCERROU os trabalhos de oitiva no prazo impreterível fixado em edital.",
    "Após a leitura do expediente, o Presidente DECLAROU aberta a ordem do dia para votações."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. O pretérito imperfeito ('compareciam') indica ações habituais, contínuas ou de duração no passado. As outras alternativas trazem verbos no pretérito perfeito ('assinou', 'encerrou', 'declarou'), que exprimem ações pontuais e integralmente finalizadas."
},
{
  "id": 249,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Conjugação do Verbo PÔR e Seus Derivados",
  "question": "Os verbos derivados de 'PÔR' (como dispor, compor, propor, sobrepor) seguem rigorosamente o mesmo modelo de flexão do verbo primitivo. Assinale a frase com a flexão correta do verbo derivado:",
  "options": [
    "Quando o técnico legislativo propor a alteração do protocolo, a Mesa analisará a minuta.",
    "Se os vereadores comporem uma comissão especial, os fatos serão devidamente esclarecidos.",
    "Caso a assessoria jurídica não se opor à tramitação, o projeto seguirá para as comissões.",
    "Quando o técnico legislativo propuser a alteração do protocolo, a Mesa analisará a minuta."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. No futuro do subjuntivo de pôr temos 'quando eu puser, quando tu puseres, quando ele puser'. Logo, os derivados flexionam-se: 'propuser' (e nunca 'propor'), 'compuserem' (e nunca 'comporem'), 'opuser' (e nunca 'opor')."
},
{
  "id": 250,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Conjugação do Verbo VER vs. VIR",
  "question": "A confusão entre as formas dos verbos 'VER' e 'VIR' no futuro do subjuntivo é recorrente em certames da banca INBRASP. Assinale a opção que emprega CORRETAMENTE a forma verbal correspondente ao verbo 'VER':",
  "options": [
    "Se o servidor ver qualquer irregularidade nas notas fiscais, deverá comunicá-la ao setor competente.",
    "Quando o vereador vim à tribuna, apresentará as reivindicações dos moradores locais.",
    "Se o servidor vir qualquer irregularidade nas notas fiscais, deverá comunicá-la ao setor competente.",
    "Caso você ver o procurador jurídico no plenário, solicite o parecer sobre o substitutivo."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. No futuro do subjuntivo, o verbo VER conjuga-se: quando eu vir, quando tu vires, quando ele vir (e não 'se ele ver'). Já o verbo VIR conjuga-se: quando eu vier, quando tu vieres, quando ele vier."
},
{
  "id": 251,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Verbos Abundantes e Emprego do Particípio Duplo",
  "question": "Os verbos abundantes possuem dois particípios: um regular (terminado em -ado ou -ido) e outro irregular (forma reduzida). Quanto ao seu emprego correto com os verbos auxiliares, assinale a opção correta:",
  "options": [
    "O relatório fora IMPRESSO pela gráfica e o secretário havia IMPRIMIDO o comprovante no gabinete.",
    "O relatório fora imprimido pela gráfica e o secretário havia impresso o comprovante no gabinete.",
    "O documento oficial foi aceitado pelo diretor e a secretária tinha aceite os protocolos diários.",
    "A comissão tinha entregue os pareceres após o decreto ter sido entregado pelo prefeito municipal."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Regra áurea dos particípios duplos: (1) Com os auxiliares TER ou HAVER usa-se a forma regular terminada em -ado/-ido ('havia imprimido', 'tinha aceitado', 'havia entregado'); (2) Com os auxiliares SER ou ESTAR usa-se a forma irregular reduzida ('foi impresso', 'foi aceito', 'foi entregue')."
},
{
  "id": 252,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Conjugação de Verbos em -IAR (Regra do MARIO)",
  "question": "A maioria dos verbos terminados em -IAR é regular (ex.: criar $\\rightarrow$ eu crio; avaliar $\\rightarrow$ eu avalio). Todavia, os verbos do mnemônico 'MARIO' mudam o 'i' para 'ei' nas formas rizotônicas do presente. Pertence a esse grupo de conjugação especial o verbo:",
  "options": [
    "Copiar (eu copeio, tu copeias, ele copeia, eles copeiam).",
    "Confiar (eu confeio, tu confeias, ele confeia, eles confeiam).",
    "Ansiar (eu anseio, tu anseias, ele anseia, eles anseiam).",
    "Ampliar (eu ampleio, tu ampleias, ele ampleia, eles ampleiam)."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Mnemônico MARIO: Medir/Mediar, Ansiar, Remediar, Incendiar e Odiar. Esses verbos recebem 'ei' nas formas rizotônicas do presente do indicativo e do subjuntivo (eu anseio, remedeio, incendeio, odeio). Os demais verbos em -iar são regulares (eu copio, confio, amplio)."
},
{
  "id": 253,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Infinitivo Pessoal (Flexionado)",
  "question": "O infinitivo pessoal (ou flexionado) recebe desinências número-pessoais (-es, -mos, -des, -em). O emprego do infinitivo flexionado é OBRIGATÓRIO quando:",
  "options": [
    "O infinitivo possui sujeito próprio, claro e distinto do sujeito da oração principal.",
    "O verbo funciona como verbo principal de uma locução verbal regida por preposição de.",
    "O infinitivo integra uma locução verbal com verbo auxiliar modal como dever ou poder.",
    "A oração é introduzida pela preposição 'a' precedendo verbo que indica movimento contínuo."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. O infinitivo deve ser obrigatoriamente flexionado quando possuir sujeito próprio e explícito, diferente do sujeito da oração principal (ex.: 'O Presidente pediu para OS VEREADORES VOTAREM o projeto com urgência'). Em locuções verbais, o infinitivo não se flexiona ('Eles devem comparecer')."
},
{
  "id": 254,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Formação do Modo Imperativo",
  "question": "A formação do modo imperativo obedece a regras precisas derivadas do presente do indicativo e do presente do subjuntivo. Sobre a formação do IMPERATIVO AFIRMATIVO, é correto afirmar que:",
  "options": [
    "Todas as formas derivam exclusivamente do pretérito perfeito do indicativo sem as desinências número-pessoais.",
    "As formas de 'tu' e 'vós' derivam do presente do indicativo sem a letra 's' final, enquanto as demais formas vêm do presente do subjuntivo.",
    "As formas de 'você' e 'vocês' são extraídas do pretérito imperfeito do indicativo com o acréscimo de desinência modal.",
    "O imperativo afirmativo e o imperativo negativo possuem idêntica formação morfológica em todas as pessoas gramaticais."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. No Imperativo Afirmativo: 'tu' e 'vós' vêm do Presente do Indicativo cortando o 's' final (Tu cantas $\\rightarrow$ Canta tu; Vós cantais $\\rightarrow$ Cantai vós). As pessoas 'você', 'nós' e 'vocês' vêm diretamente do Presente do Subjuntivo sem alterações (Cante você, Cantemos nós, Cantem vocês)."
},
{
  "id": 255,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Formação do Modo Imperativo Negativo",
  "question": "Na redação de atos oficiais e recomendações, o uso do imperativo negativo exige observância de sua matriz morfológica. O IMPERATIVO NEGATIVO forma-se a partir de:",
  "options": [
    "Todas as pessoas extraídas do presente do indicativo sem o 's' final das segundas pessoas.",
    "Formas do futuro do pretérito modificadas pela junção de partículas adverbiais de intensidade.",
    "Infinitivo pessoal antecedido da partícula negativa sem desinências flexionais de número.",
    "Todas as pessoas extraídas diretamente do presente do subjuntivo, antecedidas da palavra de negação."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. O Imperativo Negativo tem formação 100% regular e unificada: todas as pessoas gramaticais (não cantes tu, não cante você, não cantemos nós, não canteis vós, não cantem vocês) são cópias exatas do Presente do Subjuntivo, antecedidas por palavra negativa ('não', 'nunca', 'jamais')."
},
{
  "id": 256,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Verbos Defectivos",
  "question": "Os verbos defectivos são aqueles que não possuem conjugação completa em todas as formas, modos ou pessoas gramaticais. Constitui exemplo clássico de VERBO DEFECTIVO na língua portuguesa o verbo:",
  "options": [
    "Correr (que se conjuga em todas as pessoas do presente do indicativo: corro, corres, corre).",
    "Escrever (que possui conjugação integral e abundante em todos os tempos do modo subjuntivo).",
    "Falir (que não possui as formas da primeira, segunda e terceira pessoas do singular do presente do indicativo).",
    "Partir (que funciona como modelo canônico da terceira conjugação regular em -ir)."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Verbos defectivos não se conjugam em determinadas formas. O verbo FALIR, por exemplo, no presente do indicativo, só possui a 1ª e 2ª pessoas do plural ('nós falimos', 'vós falis'), não possuindo as formas rizotônicas 'eu fali/falo/falo' (para evitar ambiguidade ou por tradição eufônica)."
},
{
  "id": 257,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Verbos Pronominais Essenciais vs Acidentais",
  "question": "Os verbos pronominais conjugam-se com pronomes oblíquos átonos da mesma pessoa do sujeito. Classifica-se como PRONOMINAL ESSENCIAL (aquele que só existe acompanhado do pronome) o verbo:",
  "options": [
    "Lavar-se (pronominal acidental, pois existe a forma ativa transitiva direta 'lavar o carro').",
    "Vestir-se (pronominal acidental, pois existe a forma transitiva direta 'vestir a toga').",
    "Ferir-se (pronominal acidental, pois existe a forma transitiva direta 'ferir o adversário').",
    "Queixar-se (não existe o verbo 'queixar' na acepção de reclamar sem o pronome)."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Verbos pronominais essenciais são aqueles que trazem o pronome oblíquo fundido à sua própria existência sem função sintática autônoma: queixar-se, arrepender-se, suicidar-se, zangar-se, atrever-se. Os acidentais podem ser empregados sem o pronome (lavar, ferir, pentear)."
},
{
  "id": 258,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Transitividade Verbal Contextual: Aspirar",
  "question": "A regência verbal estuda a relação de dependência entre o verbo e seus complementos. O verbo 'ASPIRAR' apresenta dupla transitividade conforme o sentido pretendido. Assinale o uso em que 'aspirar' é TRANSITIVO INDIRETO (com preposição 'a'):",
  "options": [
    "Muitos candidatos dedicados aspiram ao cargo público de Técnico Legislativo da Câmara.",
    "O paciente internado na unidade hospitalar aspirava o ar puro da serra pela manhã.",
    "O aspirador de pó industrial aspirou todo o resíduo acumulado no carpete do plenário.",
    "Durante o trajeto na mata nativa, os atletas aspiraram a fumaça tóxica da queimada."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. O verbo ASPIRAR possui dois regimes clássicos: (1) Sentido de 'sorver/inalar/respirar' = Transitivo Direto sem preposição ('aspirou o ar'); (2) Sentido de 'almejar/desejar/pretender' = Transitivo Indireto com a preposição 'a' ('aspiram ao cargo público')."
},
{
  "id": 259,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Regência Verbal: Assistir",
  "question": "O verbo 'ASSISTIR' assume diferentes regências de acordo com o contexto comunicativo. Assinale a alternativa em que 'assistir' é empregado como TRANSITIVO INDIRETO no sentido de 'presenciar / ver':",
  "options": [
    "A equipe de enfermagem da assistência social assistiu os idosos durante a campanha de vacinação.",
    "O médico plantonista do município assistiu o paciente acidentado com extrema presteza.",
    "Os cidadãos interessados assistiram à sessão plenária da Câmara Municipal com entusiasmo.",
    "O técnico legislativo assistiu o vereador na elaboração da justificativa do projeto de lei."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O verbo ASSISTIR: (1) No sentido de 'ver/presenciar' é Transitivo Indireto com preposição 'a' ('assistiram à sessão' - crase obrigatória); (2) No sentido de 'ajudar/socorrer' é preferencialmente Transitivo Direto sem preposição ('assistiu o paciente', 'assistiu o vereador'); (3) No sentido de 'caber/pertencer' é VTI com 'a' ('assiste ao cidadão esse direito')."
},
{
  "id": 260,
  "category": "portugues",
  "day": "w2_d2",
  "discipline": "Língua Portuguesa",
  "topic": "Regência Verbal: Obedecer e Visar",
  "question": "A norma culta exige atenção rigorosa à regência de determinados verbos de uso cotidiano no serviço público. Assinale a frase que respeita plenamente as normas de regência verbal:",
  "options": [
    "Todos os servidores públicos da Câmara devem obedecer às disposições do regimento interno.",
    "Todos os servidores públicos da Câmara devem obedecer as disposições do regimento interno.",
    "O projeto de lei complementar visa a promoção geral de incentivos fiscais no comércio.",
    "O assessor parlamentar visou ao documento oficial com carimbo institucional de protocolo."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. O verbo OBEDECER é estritamente Transitivo Indireto e rege a preposição 'a' ('obedecer a + as disposições = obedecer às disposições do regimento'). Já o verbo 'visar' no sentido de mirar ou apor visto é VTD ('visou o documento'). No sentido de almejar, rege 'a' ('visa à promoção')."
}
,
{
  "id": 261,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Espécies Normativas (CF/88 Art. 59)",
  "question": "O processo legislativo brasileiro compreende a elaboração de atos normativos com diferentes alcances e requisitos formais. De acordo com o rol taxativo expresso no artigo 59 da Constituição Federal de 1988, compreende a elaboração de:",
  "options": [
    "Instruções Normativas, Circulares Interministeriais, Decretos Executivos, Leis Ordinárias e Resoluções.",
    "Emendas à Constituição, Leis Complementares, Leis Ordinárias, Leis Delegadas, Medidas Provisórias, Decretos Legislativos e Resoluções.",
    "Portarias de Gabinete, Leis Orgânicas Municipais, Decretos-Leis, Provimentos e Tratados Comerciais.",
    "Regimentos Internos, Pareceres Jurídicos Vinculantes, Resoluções de Conselho, Súmulas e Leis Ordinárias."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. O art. 59 da CF/88 estabelece taxativamente as espécies normativas que integram o processo legislativo: I - emendas à Constituição; II - leis complementares; III - leis ordinárias; IV - leis delegadas; V - medidas provisórias; VI - decretos legislativos; VII - resoluções. Atos como portarias, instruções normativas e circulares são atos infralegais da Administração, não compondo o processo legislativo constitucional."
},
{
  "id": 262,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Emendas à Constituição: Procedimento e Limitações",
  "question": "Em relação ao procedimento de aprovação e formalização das Emendas à Constituição (CF/88, art. 60), assinale a alternativa juridicamente CORRETA:",
  "options": [
    "A proposta de emenda deve ser submetida à sanção ou veto motivado do Presidente da República no prazo de 15 dias úteis.",
    "A emenda constitucional exige para sua aprovação votação em turno único com quórum qualificado de maioria absoluta dos votos.",
    "Qualquer cidadão ou parlamentar isolado possui legitimidade autônoma para propor diretamente uma Emenda Constitucional.",
    "Aprovada em dois turnos por três quintos dos votos dos membros de cada Casa do Congresso Nacional, a emenda é promulgada pelas Mesas da Câmara dos Deputados e do Senado Federal, sem participação executiva de sanção ou veto."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Conforme o art. 60, §§ 2º e 3º da CF/88: a proposta será discutida e votada em cada Casa do Congresso Nacional, em dois turnos, considerando-se aprovada se obtiver, em ambos, três quintos dos votos dos respectivos membros. A emenda à Constituição será promulgada pelas Mesas da Câmara dos Deputados e do Senado Federal, com o respectivo número de ordem. Não existe fase de sanção ou veto pelo Poder Executivo em emendas constitucionais."
},
{
  "id": 263,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Iniciativa Privativa de Leis",
  "question": "No âmbito da organização municipal, em observância ao princípio da simetria constitucional com o artigo 61, § 1º da CF/88, são de iniciativa PRIVATIVA do Prefeito Municipal os projetos de lei que disponham sobre:",
  "options": [
    "Criação de cargos, funções ou empregos públicos na administração direta e autárquica do Poder Executivo, bem como a fixação ou aumento de sua remuneração.",
    "Organização interna dos gabinetes parlamentares e criação de cargos e comissões do Poder Legislativo Municipal.",
    "Fixação do subsídio dos Vereadores e do Presidente da Câmara para a legislatura subsequente.",
    "Elaboração e reforma das disposições do Regimento Interno da Câmara Municipal de Vereadores."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. A iniciativa de leis que versem sobre criação de cargos, funções ou empregos na administração pública direta e autárquica do Executivo, aumento de remuneração de seus servidores, regime jurídico e organização administrativa dos seus órgãos é competência privativa do Chefe do Poder Executivo (CF, art. 61, § 1º, II). As alternativas B, C e D versam sobre matérias de competência privativa da própria Câmara Municipal."
},
{
  "id": 264,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Leis Complementares versus Leis Ordinárias",
  "question": "Acerca das distinções formais e materiais entre Leis Complementares e Leis Ordinárias no processo legislativo, assinale a afirmativa CORRETA:",
  "options": [
    "A lei complementar possui hierarquia normativa superior à lei ordinária, podendo revogar qualquer matéria mesmo quando não reservada a ela.",
    "As leis ordinárias exigem quórum de dois terços dos membros da Casa Legislativa para sua aprovação final.",
    "As leis complementares são reservadas para matérias expressamente taxadas na Constituição e dependem da aprovação por maioria absoluta, enquanto as leis ordinárias tratam da matéria comum residual e exigem apenas maioria simples.",
    "O Chefe do Poder Executivo não pode vetar projetos de lei complementar, cabendo apenas o veto em leis ordinárias."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. A diferença entre Lei Complementar (LC) e Lei Ordinária (LO) reside no critério material (a LC só pode tratar de matérias expressamente previstas no texto constitucional) e no critério formal (a LC é aprovada por MAIORIA ABSOLUTA, conforme o art. 69 da CF/88, enquanto a LO é aprovada por MAIORIA SIMPLES, nos termos do art. 47 da CF/88). Não há hierarquia formal entre elas segundo o STF, mas sim campos materiais de competência distintos."
},
{
  "id": 265,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Fases do Processo Legislativo: Fase Integrativa",
  "question": "A doutrina constitucional e a técnica legislativa dividem o processo legislativo em três fases fundamentais: introdutória (iniciativa), constitutiva (deliberação parlamentar e manifestação executiva) e integrativa de eficácia. Integram tipicamente a fase INTEGRATIVA de eficácia da lei:",
  "options": [
    "A leitura da proposição no Pequeno Expediente e sua distribuição às Comissões Técnicas.",
    "A promulgação e a publicação no Diário Oficial.",
    "A emissão de parecer pela Comissão de Constituição e Justiça e a votação em Plenário.",
    "A apresentação de emendas de bancada e o despacho de admissibilidade da Mesa Diretora."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. A fase integrativa da lei é aquela que confere executoriedade e vigência ao diploma legal formalmente aprovado. É composta pela PROMULGAÇÃO (atestado oficial da existência da lei e ordem de seu cumprimento) e pela PUBLICAÇÃO (ato que torna o texto público para gerar eficácia e presunção de conhecimento erga omnes, em obediência ao princípio da publicidade)."
},
{
  "id": 266,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Veto Executivo: Prazo, Motivos e Rejeição",
  "question": "Aprovado um projeto de lei pela Câmara Municipal, este é enviado ao Prefeito para sanção. Caso o Prefeito decida vetá-lo, o regime constitucional e legal do veto estabelece que:",
  "options": [
    "O veto deve ser formalizado no prazo de 15 (quinze) dias úteis, motivado por inconstitucionalidade (veto jurídico) ou por contrariedade ao interesse público (veto político), comunicando os motivos em até 48 horas ao Presidente da Câmara.",
    "O veto pode ser tácito, de modo que a ausência de manifestação do Chefe do Executivo em 15 dias importa em rejeição automática do projeto.",
    "O veto parcial pode incidir livremente sobre palavras isoladas, expressões avulsas ou orações intermediárias dentro de um artigo de lei.",
    "A Câmara só pode rejeitar o veto do Prefeito se obtiver unanimidade absoluta de votos de todos os parlamentares em sessão secreta."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Nos termos do art. 66, §§ 1º e 2º da CF/88 e das Leis Orgânicas Municipais: o veto é sempre expresso e motivado (não existe veto tácito), devendo ser exercido no prazo de 15 dias ÚTEIS. O veto parcial só pode abranger texto integral de artigo, parágrafo, inciso ou alínea (vedado vetar palavras ou expressões isoladas). Os motivos devem ser comunicados ao Presidente da Casa Legislativa dentro de 48 horas."
},
{
  "id": 267,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Sanção Tácita e Sanção Expressa",
  "question": "No processo de formação das leis, a manifestação de concordância do Chefe do Poder Executivo com o projeto aprovado pelo Legislativo denomina-se 'Sanção'. Sobre as formas de sanção, é correto afirmar:",
  "options": [
    "A sanção expressa torna dispensável a promulgação e a publicação da nova lei.",
    "A sanção pode ser presumida caso o Prefeito assine um veto sem indicar os motivos.",
    "Apenas o Presidente da República pode praticar sanção tácita, sendo vedada essa figura aos governadores e prefeitos.",
    "O silêncio do Chefe do Executivo após o transcurso integral do prazo constitucional de 15 dias úteis sem sanção expressa nem veto importa em sanção tácita."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 66, § 3º da CF/88: 'Decorrido o prazo de quinze dias, o silêncio do Presidente da República [ou do Prefeito, por simetria] importará em sanção'. Portanto, enquanto o veto deve ser sempre expresso e motivado, a sanção pode ser expressa (declaração formal positiva) ou tácita (decorrente da inércia após 15 dias úteis)."
},
{
  "id": 268,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Derrubada de Veto e Promulgação Supletiva",
  "question": "A Câmara Municipal de Meruoca, reunida em sessão plenária, apreciou o veto do Prefeito a determinado projeto de lei e o rejeitou pelo voto da maioria absoluta dos seus membros. Nessa hipótese, conforme as regras constitucionais aplicáveis ao processo legislativo:",
  "options": [
    "O projeto de lei perde o objeto e deve ser arquivado imediatamente pelo Diretor Legislativo.",
    "O Prefeito pode interpor novo veto sobre a mesma matéria, reiniciando o ciclo de deliberação parlamentar.",
    "O projeto será enviado ao Prefeito para promulgação; se este não o fizer dentro de 48 horas, o Presidente da Câmara o promulgará, e, se este não o fizer em igual prazo, caberá ao Vice-Presidente fazê-lo.",
    "A lei será promulgada compulsoriamente pelo Juiz de Direito Diretor do Foro da Comarca de Meruoca."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Conforme art. 66, §§ 5º e 7º da CF/88 e Leis Orgânicas municipais: se o veto for rejeitado, o projeto é enviado ao Chefe do Executivo para que o promulgue em 48 horas. Não o fazendo nesse prazo, abre-se a competência sucessiva/supletiva: o Presidente da Câmara o promulgará e, caso este também se omita em igual prazo (48 horas), caberá ao Vice-Presidente da Câmara fazê-lo."
},
{
  "id": 269,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Classificação das Emendas Parlamentares",
  "question": "No decorrer dos debates parlamentares, os vereadores têm a faculdade de sugerir alterações aos projetos em tramitação por meio de 'Emendas'. A emenda que tem por finalidade suprimir total ou parcialmente texto de artigo, parágrafo, inciso ou alínea da proposição principal denomina-se:",
  "options": [
    "Emenda Supressiva.",
    "Emenda Aditiva.",
    "Emenda Modificativa.",
    "Emenda Aglutinativa."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Classificação técnica regimental das emendas: (1) Supressiva: visa a eliminar parte do texto da proposição; (2) Aditiva: acrescenta dispositivos ou novas previsões ao texto; (3) Modificativa: altera a redação de dispositivo sem criar novo assunto ou suprimir a regra; (4) Aglutinativa: resulta da fusão de proposições ou emendas correlatas."
},
{
  "id": 270,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Conceito e Tramitação de Substitutivo",
  "question": "Na tramitação regimental de proposições legislativas nas Câmaras Municipais, a denominação 'Substitutivo' corresponde a:",
  "options": [
    "Um recurso interposto pelo autor contra o arquivamento sumário determinado pela CCJ.",
    "Um tipo de voto em separado apresentado por parlamentar vencido no âmbito das comissões temáticas.",
    "Um requerimento de urgência assinado pela Mesa para inverter a Ordem do Dia.",
    "Uma proposição legislativa apresentada por parlamentar ou comissão para substituir integralmente o texto de um projeto de lei já em tramitação sobre a mesma matéria."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Substitutivo é o projeto de lei apresentado por um parlamentar, bancada ou comissão competente com a finalidade de substituir integralmente uma proposição principal em andamento. Havendo aprovação do substitutivo, a proposição original e as emendas a ela apresentadas ficam automaticamente prejudicadas."
},
{
  "id": 271,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Atuação da Comissão de Constituição e Justiça (CCJ)",
  "question": "As Comissões Permanentes exercem controle preventivo e técnico essencial sobre as proposições. Sobre a atuação da Comissão de Constituição e Justiça (CCJ) ou comissão equivalente na Câmara Municipal, assinale a afirmativa CORRETA:",
  "options": [
    "A CCJ analisa exclusivamente a oportunidade financeira e a viabilidade orçamentária dos projetos de lei tributários.",
    "Compete à CCJ manifestar-se obrigatoriamente sobre o aspecto constitucional, legal, regimental e a técnica legislativa das proposições antes de sua votação de mérito.",
    "Se a CCJ aprovar o parecer pela inconstitucionalidade, a proposição é compulsoriamente remetida para sanção do Prefeito.",
    "A CCJ possui atribuição jurisdicional para julgar os crimes de responsabilidade e cassar o mandato de parlamentares."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. A Comissão de Constituição, Justiça e Redação Final (CCJ) atua como órgão de controle de juridicidade preventiva: aprecia a constitucionalidade (se a matéria ofende a CF ou a Lei Orgânica), a legalidade (se contraria leis gerais), o respeito ao regimento e a boa técnica legislativa (LC nº 95/98)."
},
{
  "id": 272,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Poder Terminativo das Comissões",
  "question": "O artigo 58, § 2º, I da CF/88 faculta aos regimentos regimentar a prerrogativa de as Comissões deliberarem em caráter conclusivo (ou terminativo) sobre determinadas proposições. Isso significa que:",
  "options": [
    "A decisão da comissão tem natureza de sentença judicial irrecorrível perante o Supremo Tribunal Federal.",
    "O projeto é sancionado imediatamente na própria sala da comissão sem que o Chefe do Executivo tome conhecimento.",
    "A comissão aprova ou rejeita o projeto com efeito definitivo, dispensando a competência do Plenário, salvo se houver recurso de determinado número de membros da Casa Legislativa exigindo a deliberação plenária.",
    "A proposição só pode ser arquivada mediante homologação prévia do Tribunal de Contas dos Municípios."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Conforme o art. 58, § 2º, I da CF/88, às comissões cabe 'discutir e votar projeto de lei que dispensar, na forma do regimento, a competência do Plenário, salvo se houver recurso de um décimo dos membros da Casa'. Este é o chamado poder terminativo ou poder conclusivo das comissões."
},
{
  "id": 273,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Decreto Legislativo versus Resolução",
  "question": "No exercício das atribuições privativas do Poder Legislativo Municipal, a Câmara expede atos normativos que não dependem de sanção do Prefeito. A espécie normativa adequada para disciplinar matéria de competência privativa da Câmara que produz efeitos EXTERNOS (como julgar as contas anuais do Prefeito ou conceder honrarias e títulos de cidadania) é:",
  "options": [
    "O Decreto Legislativo.",
    "A Portaria Administrativa.",
    "O Projeto de Lei Delegada.",
    "O Despacho Terminativo."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. A distinção clássica no processo legislativo municipal estabelece: (1) DECRETO LEGISLATIVO: matéria de competência exclusiva/privativa da Câmara que produz efeitos EXTERNOS à Casa (ex.: julgamento das contas do Prefeito, concessão de título de cidadão honorário, autorização para o Prefeito ausentar-se do Município por período superior a 15 dias); (2) RESOLUÇÃO: matéria privativa da Câmara com efeitos INTERNOS (Regimento Interno, organização da Secretaria, criação de cargos do Legislativo)."
},
{
  "id": 274,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Matérias Disciplinadas por Resolução",
  "question": "A Resolução é a proposição legislativa destinada a regular matérias de competência privativa da Câmara Municipal que produzem efeitos político-administrativos interna corporis. Constitui matéria típica de RESOLUÇÃO da Câmara:",
  "options": [
    "A instituição da planta genérica de valores e alíquotas do IPTU municipal.",
    "A desafetação e doação onerosa de bens imóveis dominicais do Município.",
    "A fixação das diretrizes orçamentárias anuais do Poder Executivo (LDO).",
    "A criação, transformação ou extinção dos cargos do quadro de servidores da Câmara Municipal e a alteração do seu Regimento Interno."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. As Resoluções da Câmara tratam de sua vida e administração interna: regimento interno, estrutura administrativa do Legislativo, concessão de licença a vereador, regulamentação de seus serviços internos. Matérias tributárias, patrimoniais municipais gerais e orçamentárias (IPTU, alienação de imóveis, LDO) exigem Lei Formal (ordinária ou complementar)."
},
{
  "id": 275,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Quóruns Parlamentares: Maioria Simples versus Maioria Absoluta",
  "question": "A fixação de quórum é elemento essencial para a validade das deliberações parlamentares. Em conformidade com o artigo 47 da CF/88, salvo determinação legal em sentido diverso, as deliberações da Câmara serão tomadas por maioria de votos, presente a maioria absoluta de seus membros. Essa definição refere-se à:",
  "options": [
    "Maioria Qualificada de Dois Terços.",
    "Maioria Simples (ou Relativa).",
    "Unanimidade Regimental Suplementar.",
    "Maioria Constitucional de Três Quintos."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. A regra geral do processo legislativo é a MAIORIA SIMPLES (ou relativa): exige a presença em sessão da maioria absoluta dos membros da Casa (quórum de instalação) e a votação favorável da maioria dos presentes (quórum de aprovação). Já a maioria absoluta exige o voto favorável do primeiro número inteiro acima da metade do total de membros que compõem a Casa, independentemente dos presentes."
},
{
  "id": 276,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Princípio da Irrepetibilidade (CF/88 Art. 67)",
  "question": "Um projeto de lei de autoria parlamentar foi rejeitado em Plenário na Câmara Municipal. Em relação à possibilidade de reapresentação dessa mesma matéria na mesma Sessão Legislativa (mesmo ano de trabalhos), a regra constitucional da irrepetibilidade (CF/88, art. 67) estabelece que:",
  "options": [
    "É terminantemente proibida sob qualquer pretexto até a realização da legislatura seguinte (quatro anos depois).",
    "Pode ser reapresentado livremente pelo mesmo vereador autor decorridos apenas sete dias da rejeição anterior.",
    "Somente poderá ser objeto de novo projeto de lei mediante a assinatura e proposta formal da maioria absoluta dos membros da Casa Legislativa.",
    "Depende de parecer favorável emitido previamente pelo Tribunal de Contas ou pelo Ministério Público Estadual."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Conforme o art. 67 da CF/88: 'A matéria constante de projeto de lei rejeitado somente poderá ser objeto de novo projeto, na mesma sessão legislativa, mediante proposta da maioria absoluta dos membros de qualquer das Casas do Congresso Nacional'. Essa salvaguarda impede que parlamentares sobrecarreguem repetitivamente os trabalhos com propostas já rejeitadas, salvo consenso qualificado."
},
{
  "id": 277,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Regime de Urgência no Processo Legislativo",
  "question": "O Regimento Interno prevê hipóteses em que determinada proposição pode tramitar em regime de 'Urgência Especial'. A principal consequência procedimental do deferimento do regime de urgência é:",
  "options": [
    "A promulgação instantânea da lei antes de qualquer votação plenária.",
    "A autorização para que o projeto seja sancionado sem leitura do seu texto.",
    "A anulação de todas as emendas e pareceres aprovados anteriormente pelas comissões.",
    "A dispensa de exigências e prazos regimentais ordinários para que a proposição seja incluída prontamente na Ordem do Dia e deliberada pelo Plenário."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. O regime de urgência tem o objetivo de conferir celeridade à tramitação de matérias inadiáveis ou de grave interesse coletivo. Ele autoriza a dispensa de prazos de interstício, distribuição imediata em avulsos e pronta inclusão na Ordem do Dia, reduzindo etapas intermediárias sem suprimir a soberania da deliberação plenária."
},
{
  "id": 278,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Iniciativa Popular no Âmbito Municipal",
  "question": "A Constituição Federal de 1988, em seu artigo 29, inciso XIII, consagra o exercício direto da cidadania no processo legislativo municipal por meio da iniciativa popular de projetos de lei de interesse específico do Município, da cidade ou de bairros. Para que a iniciativa popular municipal seja válida, exige-se a manifestação de, pelo menos:",
  "options": [
    "5% (cinco por cento) do eleitorado do Município.",
    "1% (um por cento) dos cidadãos residentes no bairro.",
    "10% (dez por cento) do total de votantes da última eleição majoritária.",
    "15% (quinze por cento) dos eleitores alistados no Estado."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 29, XIII da CF/88: 'iniciativa popular de projetos de lei de interesse específico do Município, da cidade ou de bairros, através de manifestação de, pelo menos, cinco por cento do eleitorado'. Em nível federal (CF art. 61, § 2º) a regra é 1% do eleitorado nacional distribuído por pelo menos 5 estados com não menos de 0,3% em cada um."
},
{
  "id": 279,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Fase da Redação Final (LC nº 95/1998)",
  "question": "Após a aprovação do projeto de lei em plenário, acompanhado de emendas que modificaram trechos de sua redação originária, a matéria é encaminhada para a confecção da 'Redação Final'. Nessa fase regulamentar:",
  "options": [
    "Podem ser apresentadas novas emendas de mérito que criem despesas públicas adicionais.",
    "O relator tem o poder de rejeitar integralmente o mérito aprovado pela maioria do Plenário.",
    "É defeso efetuar qualquer alteração substancial de mérito, restringindo-se os trabalhos à escorreita adequação gramatical, clareza, precisão e técnica legislativa em harmonia com as deliberações plenárias.",
    "O projeto adquire status definitivo de lei sancionada, dispensando o envio ao Executivo."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. A fase de Redação Final (regida pelos preceitos da Lei Complementar nº 95/1998 e regimentos internos) é estritamente de consolidação formal do que já foi deliberado e aprovado. É vedada qualquer alteração de mérito, permitindo-se apenas correções vernáculas, ajustes de concordância, numeração de artigos e técnica legislativa."
},
{
  "id": 280,
  "category": "legislacao",
  "day": "w2_d3",
  "discipline": "Processo Legislativo",
  "topic": "Retirada de Proposição pelo Autor",
  "question": "Um parlamentar protocolou na Secretaria da Câmara Municipal um Projeto de Lei Ordinária. Dias depois, antes que a matéria fosse submetida à votação em Plenário, ele decide retirá-la definitivamente de tramitação. Segundo as regras gerais do processo legislativo regimental:",
  "options": [
    "Uma proposição legislativa, após protocolada, torna-se patrimônio público inalienável e não pode ser retirada em hipótese alguma.",
    "O autor pode solicitar a retirada da proposição; se a deliberação em Plenário ainda não tiver sido iniciada, o deferimento é prerrogativa regimental do Presidente ou do autor; se já iniciada a votação, dependerá da concordância do Plenário.",
    "A retirada da proposição exige obrigatoriamente concordância prévia e homologação por decreto do Prefeito Municipal.",
    "O autor pode retirar a proposição inclusive depois que o projeto for sancionado e publicado como lei oficial."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Conforme praxe e normas regimentais: a retirada de proposição é de iniciativa de seu autor. Antes de ser submetida à deliberação plenária (ou antes de receber parecer contrário de comissão terminativa), a retirada pode ser deferida de plano pelo Presidente. Contudo, se a matéria já estiver sob deliberação/votação no Plenário, a retirada só poderá ocorrer se o próprio Plenário autorizar."
},
{
  "id": 281,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Word 365: Quebras de Página versus Quebras de Seção",
  "question": "No Microsoft Word 365, ao preparar a minuta de um relatório técnico para a Mesa Diretora, o servidor necessita que as páginas 1 e 2 fiquem em orientação 'Retrato' e a página 3 fique em orientação 'Paisagem' para acomodar uma tabela extensa. Para permitir essa divergência de orientação de página no mesmo documento, deve-se inserir:",
  "options": [
    "Uma Quebra de Linha Manual com o atalho Shift + Enter.",
    "Uma Quebra de Página Simples com o atalho Ctrl + Enter.",
    "Uma Quebra de Seção do tipo 'Próxima Página'.",
    "Um Marcador de Recuo Negativo na Régua Horizontal."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. No MS Word, formatações de nível de página (orientação Retrato/Paisagem, cabeçalhos/rodapés diferentes, margens distintas e número de colunas) são atributos vinculados à SEÇÃO. Uma Quebra de Página simples apenas empurra o texto para a página seguinte na mesma seção. Para alterar a orientação de uma página isolada, é obrigatório inserir uma Quebra de Seção (Menu Layout -> Quebras -> Quebras de Seção -> Próxima Página)."
},
{
  "id": 282,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Word 365: Teclas de Atalho Oficiais (Português)",
  "question": "No Microsoft Word configurado no padrão de idioma Português do Brasil, as teclas de atalho padrão utilizadas para 'Salvar as alterações no documento', 'Alinhar o texto no modo Justificado' e 'Desfazer a última ação' são, respectivamente:",
  "options": [
    "Ctrl + B, Ctrl + J e Ctrl + Z.",
    "Ctrl + S, Ctrl + U e Ctrl + D.",
    "Ctrl + G, Ctrl + A e Ctrl + Z.",
    "Ctrl + S, Ctrl + J e Ctrl + Y."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Nos programas do Microsoft Office em Português: Ctrl + B = Salvar (no Word em inglês seria Ctrl + S); Ctrl + J = Alinhamento Justificado (Justify); Ctrl + Z = Desfazer (Undo). Vale lembrar que Ctrl + S em português sublinha o texto no Word."
},
{
  "id": 283,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Word: Recurso de Mala Direta",
  "question": "O recurso 'Mala Direta' (Mail Merge) disponível na guia 'Correspondências' do Microsoft Word é especialmente indicado para qual finalidade no setor administrativo:",
  "options": [
    "Enviar spam em lote para listas públicas de e-mails de forma anônima e indetectável.",
    "Traduzir documentos legislativos inteiros automaticamente para dialetos regionais.",
    "Comprimir arquivos pesados no formato ZIP antes de anexá-los ao correio eletrônico.",
    "Gerar automaticamente lotes de documentos personalizados (como ofícios, convites, cartas e etiquetas) a partir de um modelo fixo integrado a uma lista ou tabela de dados (como planilha Excel ou contatos Outlook)."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. A Mala Direta do Word permite criar cartas, ofícios, certificados ou etiquetas personalizadas em escala. Ela combina um 'documento principal' (texto base com campos de mesclagem como «Nome», «Cargo», «Endereço») com uma 'fonte de dados' (como uma planilha do Excel ou lista de contatos)."
},
{
  "id": 284,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Excel 365: Função SOMA e Sintaxe de Intervalos",
  "question": "Em uma planilha do Microsoft Excel 365, o usuário deseja somar todos os valores numéricos contidos no intervalo contínuo que vai da célula B2 até a célula B12. A sintaxe correta da fórmula que realiza essa operação é:",
  "options": [
    "=TOTAL(B2..B12)",
    "=SOMA(B2:B12)",
    "=SOMA(B2;B12)",
    "=SOMATÓRIO(B2 a B12)"
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. No Excel, o operador de intervalo contínuo é representado pelos dois pontos (:). Portanto, `=SOMA(B2:B12)` soma todas as células de B2 até B12. Atenção para a pegadinha: se usasse o ponto e vírgula (`=SOMA(B2;B12)`), somaria unicamente a célula B2 e a célula B12 isoladamente."
},
{
  "id": 285,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Excel 365: Função MÉDIA",
  "question": "Considere as seguintes células em uma planilha do Excel: A1 = 10, A2 = 20, A3 = 30 e A4 = 40. Ao preencher a célula A5 com a fórmula `=MÉDIA(A1:A4)`, o valor numérico retornado será:",
  "options": [
    "25",
    "100",
    "20",
    "50"
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. A função `=MÉDIA()` calcula a média aritmética simples dos valores contidos no intervalo: (10 + 20 + 30 + 40) / 4 = 100 / 4 = 25."
},
{
  "id": 286,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Excel: Referências Relativas, Absolutas e Mistas",
  "question": "No Microsoft Excel, ao copiar uma fórmula que contém a expressão `$E$5` de uma célula para outra, o comportamento das coordenadas da célula referenciada será caracterizado como:",
  "options": [
    "Referência Relativa: a coluna E e a linha 5 serão automaticamente deslocadas.",
    "Referência Mista: a coluna E permanece fixa, mas a linha 5 muda livremente.",
    "Referência Absoluta: nem a coluna E nem a linha 5 sofrerão qualquer alteração ao serem copiadas para outra posição, mantendo-se estáticas.",
    "Referência Inválida: o Excel exibirá o código de erro #REF! por uso incorreto de caracteres especiais."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O caractere cifrão (`$`) é o operador de fixação (ancoragem) no Excel. Quando colocado antes da letra da coluna e antes do número da linha (`$E$5`), cria-se uma REFERÊNCIA ABSOLUTA, que nunca muda ao ser copiada ou arrastada. Se houvesse cifrão em apenas um dos componentes (ex: `$E5` ou `E$5`), seria uma referência mista."
},
{
  "id": 287,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Excel 365: Função Lógica SE",
  "question": "Um técnico elaborou a seguinte fórmula no Excel para avaliar o cumprimento de metas de atendimento da Câmara: `=SE(D4>=100; \"Meta Atingida\"; \"Meta Pendente\")`. Sabendo-se que o valor registrado na célula D4 é exatamente 100, o resultado exibido na célula da fórmula será:",
  "options": [
    "Meta Pendente",
    "Meta Atingida",
    "#NOME?",
    "VERDADEIRO"
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. A função SE tem a estrutura: `=SE(condição; valor_se_verdadeiro; valor_se_falso)`. A condição testada é `D4 >= 100`. Como D4 vale 100, o teste relacional `100 >= 100` é VERDADEIRO (maior ou igual). Logo, o Excel executa o segundo argumento e exibe a mensagem 'Meta Atingida'."
},
{
  "id": 288,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Excel 365: Função CONT.SE",
  "question": "Deseja-se saber quantas vezes a palavra 'Deferido' aparece na coluna de status dos processos legislativos, no intervalo de C2 até C80. A função do Microsoft Excel especificamente concebida para realizar contagens baseadas em um critério específico é:",
  "options": [
    "=SOMAR(C2:C80; \"Deferido\")",
    "=CONTAR(C2:C80 = Deferido)",
    "=LOCALIZAR.SE(C2:C80; \"Deferido\")",
    "=CONT.SE(C2:C80; \"Deferido\")"
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. A função `=CONT.SE(intervalo; critérios)` conta o número de células dentro de um intervalo que atendem à condição estipulada. No caso em questão, `=CONT.SE(C2:C80; \"Deferido\")` conta com precisão as ocorrências da palavra. A função CONTAR() contaria apenas células com números, e SOMASE() somaria valores numéricos com base em critérios."
},
{
  "id": 289,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Excel 365: Função PROCV",
  "question": "A função `=PROCV(valor_procurado; matriz_tabela; núm_índice_coluna; [procurar_intervalo])` é uma das mais cobradas em provas de concurso. A respeito do seu funcionamento no Excel, é correto afirmar:",
  "options": [
    "O PROCV efetua uma pesquisa vertical, buscando o valor_procurado estritamente na PRIMEIRA coluna à esquerda da matriz_tabela e retornando o valor correspondente na mesma linha a partir do número da coluna indicado.",
    "O PROCV só funciona se a tabela estiver disposta na horizontal e com células em ordem decrescente.",
    "O PROCV serve para calcular o produto vetorial entre duas matrizes tridimensionais.",
    "Caso o valor procurado não seja encontrado, o PROCV sempre substitui o erro pelo número zero automaticamente."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. PROCV significa 'Procura Vertical'. Ela pesquisa um valor na PRIMEIRA coluna de um intervalo ou matriz e retorna um valor situado na mesma linha, extraído da coluna definida pelo argumento 'núm_índice_coluna'. Se não encontrar uma correspondência exata (quando configurado com FALSO ou 0 no último parâmetro), retorna o erro `#N/D`."
},
{
  "id": 290,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft PowerPoint 365: Efeitos de Transição versus Efeitos de Animação",
  "question": "No Microsoft PowerPoint 365, ao preparar uma apresentação para a Sessão Solene da Câmara de Meruoca, o operador precisa configurar efeitos visuais. A distinção conceitual e prática entre 'Transições' e 'Animações' no PowerPoint reside no fato de que:",
  "options": [
    "As Transições são aplicadas a gráficos do Excel inseridos, enquanto as Animações só funcionam em textos sem formatação.",
    "As Animações referem-se à troca de um slide para outro na tela, enquanto as Transições se aplicam apenas ao áudio da apresentação.",
    "As Transições são os efeitos visuais que ocorrem durante a passagem de um slide para o slide seguinte, enquanto as Animações são os movimentos e efeitos visuais aplicados a elementos individuais (textos, imagens, ícones) dentro do próprio slide.",
    "As Transições são recursos exclusivos da versão web, e as Animações só existem na versão instalada para desktop."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Conceito clássico de PowerPoint: TRANSIÇÃO é o efeito de passagem de tela entre um slide e outro (ex: Esmaecer, Empurrão, Cortina). ANIMAÇÃO é o efeito aplicado aos objetos específicos contidos no slide (ex: Surgir, Zoom, Rotação em uma caixa de texto ou foto)."
},
{
  "id": 291,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft PowerPoint: Slide Mestre",
  "question": "Para garantir uma identidade visual consistente em toda a apresentação (adicionar o brasão do Município de Meruoca, número de página e cor institucional de título em todos os slides de uma só vez), o recurso correto a ser utilizado no Microsoft PowerPoint é:",
  "options": [
    "O Editor de Estilos Rápidos da Barra de Status.",
    "O Modo de Exibição do Slide Mestre.",
    "O Painel de Seleção de Formas Vetoriais.",
    "A Ferramenta de Gravação de Macros de Áudio."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. O 'Slide Mestre' (guia Exibir -> Slide Mestre) é o slide principal da hierarquia de apresentação que armazena informações sobre o tema, layout, fontes, cores e logotipos. Quaisquer alterações feitas no slide mestre são automaticamente replicadas em todos os slides da apresentação que utilizam aquele modelo."
},
{
  "id": 292,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft PowerPoint: Atalhos para Iniciar Apresentação (F5 versus Shift+F5)",
  "question": "Durante a realização de uma palestra na Câmara de Vereadores, o técnico está editando o slide número 14 no PowerPoint e precisa iniciar a exibição em tela cheia exatamente a partir desse slide atual (slide 14), sem voltar para o início. O atalho de teclado correspondente a essa ação é:",
  "options": [
    "F5",
    "Ctrl + F5",
    "Alt + F5",
    "Shift + F5"
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. No Microsoft PowerPoint: F5 = Inicia a apresentação a partir do PRIMEIRO slide (slide 1); Shift + F5 = Inicia a apresentação a partir do SLIDE ATUAL em que o usuário está posicionado; Esc = Encerra a apresentação em tela cheia."
},
{
  "id": 293,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Google Docs: Colaboração em Tempo Real",
  "question": "No Google Docs (Documentos Google), integrado ao ecossistema Google Workspace, a coautoria simultânea de arquivos apresenta a seguinte característica funcional:",
  "options": [
    "O documento é bloqueado pelo primeiro usuário com 'lock' exclusivo, impedindo qualquer outra pessoa de visualizar o arquivo até o término da sessão.",
    "As edições de outros usuários só são refletidas após reinicialização completa do navegador web.",
    "Vários usuários autorizados podem editar o documento de forma simultânea e síncrona na nuvem, sendo as alterações salvas automaticamente em tempo real e visualizadas com cursores coloridos identificando cada participante.",
    "O Google Docs exige que os usuários salvem as versões intermediárias periodicamente clicando em um ícone de disquete físico."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O Google Docs é nativo em nuvem e destaca-se pela coautoria em tempo real: múltiplos usuários trabalham no mesmo arquivo simultaneamente, cada qual identificado por um cursor com sua cor e avatar/nome, com salvamento contínuo automático nos servidores do Google (Google Drive)."
},
{
  "id": 294,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Google Workspace / Drive: Níveis de Permissão de Compartilhamento",
  "question": "Ao compartilhar um arquivo no Google Drive com membros de uma equipe de trabalho, o proprietário pode conceder permissões diferenciadas. A permissão que autoriza o usuário a visualizar o documento e propor alterações por meio de anotações e balões laterais, mas que NÃO lhe concede poder de alterar diretamente o texto original sem a anuência do autor, é a de:",
  "options": [
    "Comentarista.",
    "Leitor.",
    "Editor.",
    "Proprietário Delegado."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Os níveis principais de compartilhamento no Google Drive são: (1) LEITOR: pode apenas visualizar e baixar o arquivo, sem adicionar comentários ou editar; (2) COMENTARISTA: pode visualizar e sugerir alterações/comentários em balões laterais, mas não altera o texto original diretamente; (3) EDITOR: tem controle total sobre o conteúdo do documento, podendo alterar textos, excluir trechos e aceitar ou rejeitar sugestões."
},
{
  "id": 295,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Google Sheets: Histórico de Versões e Segurança",
  "question": "Em uma planilha de controle financeiro desenvolvida no Google Sheets (Planilhas Google), um funcionário apagou acidentalmente fórmulas complexas na tarde de ontem. O recurso nativo do Google Workspace que permite recuperar com precisão o estado anterior da planilha é:",
  "options": [
    "O Modo de Limpeza Automática de Cache do Chrome.",
    "A Barra de Status com Desfazer Limitado a três cliques.",
    "O Formatador de Células em Cascata.",
    "O Histórico de Versões (Menu Arquivo -> Histórico de versões -> Ver histórico de versões)."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. O Google Workspace mantém um registro detalhado de todas as alterações feitas em um documento através do 'Histórico de versões' (atalho Ctrl+Alt+Shift+H). Ele permite navegar por todas as versões anteriores, ver exatamente quem fez cada edição e restaurar a versão selecionada a qualquer momento com segurança."
},
{
  "id": 296,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Manipulação de Textos no Pacote Office: Área de Transferência",
  "question": "Ao selecionar um texto em um editor como o Microsoft Word e acionar a combinação de teclas `Ctrl + X`, o texto em questão:",
  "options": [
    "É formatado com efeito de sublinhado duplo e caixa alta.",
    "É recortado, isto é, retirado de sua posição original e enviado para a Área de Transferência, podendo ser inserido em outro local por meio do comando `Ctrl + V`.",
    "É duplicado na linha de baixo instantaneamente sem ser copiado para a memória.",
    "É permanentemente excluído sem possibilidade de ser colado posteriormente."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. A operação 'Recortar' (`Ctrl + X`) remove o conteúdo selecionado de seu local de origem e o armazena temporariamente na Área de Transferência (Clipboard) do sistema operacional, permitindo que seja colado (`Ctrl + V`) no mesmo aplicativo ou em outro documento."
},
{
  "id": 297,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Excel: Precedência de Operadores Matemáticos",
  "question": "No Microsoft Excel, a ordem de execução dos operadores em uma fórmula matemática segue estritamente a hierarquia algébrica padrão. Considere a fórmula inserida em uma célula: `=2 + 3 * 4 ^ 2`. O resultado que será calculado e exibido pelo Excel é:",
  "options": [
    "50",
    "80",
    "400",
    "38"
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. A precedência de operadores no Excel é: 1º Parênteses; 2º Potenciação (`^`); 3º Multiplicação (`*`) e Divisão (`/`); 4º Adição (`+`) e Subtração (`-`). Resolução passo a passo da fórmula `=2 + 3 * 4 ^ 2`: primeiro calcula a potência `4 ^ 2 = 16`; em seguida a multiplicação `3 * 16 = 48`; por último a adição `2 + 48 = 50`."
},
{
  "id": 298,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Google Drive: Sincronização Local com 'Drive para Computador'",
  "question": "O aplicativo oficial 'Google Drive para computador' (antigo Backup and Sync / Drive File Stream) oferece aos usuários a capacidade de:",
  "options": [
    "Executar jogos de computador e renderização 3D offline sem placa gráfica dedicada.",
    "Substituir o disco rígido físico por uma conexão de fibra óptica sem sistema operacional.",
    "Bloquear chamadas telefônicas no smartphone corporativo conectado via Bluetooth.",
    "Acessar e gerenciar arquivos e pastas do Google Drive diretamente a partir do Explorador de Arquivos do Windows como se fossem uma unidade de disco local, integrando a sincronização em nuvem."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. O aplicativo 'Google Drive para computador' cria uma unidade virtual no Explorador de Arquivos do Windows (geralmente com letra própria, como G:). Isso permite aos usuários abrir, editar e organizar seus arquivos da nuvem diretamente pelos softwares instalados no Windows (como abrir um arquivo .docx no Microsoft Word direto da nuvem), mantendo a sincronização transparente."
},
{
  "id": 299,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Microsoft Word 365: Ferramenta Pincel de Formatação",
  "question": "No Microsoft Word 365, o ícone que reproduz o desenho de um pincel na guia 'Página Inicial' (Pincel de Formatação / Format Painter) destina-se a:",
  "options": [
    "Desenhar vetores e figuras geométricas livres no cabeçalho do documento.",
    "Copiar a formatação (tipo de fonte, tamanho, cor, negrito, espaçamento) de um trecho de texto já formatado e aplicá-la rapidamente a outro trecho selecionado.",
    "Localizar e substituir automaticamente palavras com erros de concordância verbal.",
    "Exportar o texto para impressoras térmicas matriciais de alta velocidade."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. O Pincel de Formatação copia unicamente o ESTILO e a FORMATAÇÃO (fonte, tamanho, cor, espaçamento, bordas) de uma seleção e a replica em outro texto. Dica prática para a prova: com um clique único no pincel, aplica-se uma vez; dando DUPLO CLIQUE no ícone do pincel, ele fica travado, permitindo aplicar a formatação repetidamente em vários trechos até que se pressione a tecla Esc."
},
{
  "id": 300,
  "category": "informatica",
  "day": "w2_d3",
  "discipline": "Informática",
  "topic": "Segurança no Pacote Office: Modo de Exibição Protegido e Macros",
  "question": "Ao abrir um arquivo de texto (.docx) ou pasta de trabalho (.xlsx) que foi recebido como anexo de e-mail de remetente desconhecido ou baixado da internet, o Microsoft Office costuma exibi-lo no 'Modo de Exibição Protegido'. O objetivo primordial desse mecanismo defensivo é:",
  "options": [
    "Bloquear a conexão de internet de toda a repartição pública até que o arquivo seja deletado.",
    "Criptografar compulsoriamente os arquivos do usuário com chave privada para exigir senha de acesso.",
    "Abrir o documento em ambiente de leitura isolada (sandbox) com recursos de edição e execução de macros desabilitados, mitigando riscos de infecção por malwares antes da verificação do usuário.",
    "Excluir automaticamente o arquivo do computador caso o usuário não possua assinatura corporativa da Microsoft."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O Modo de Exibição Protegido (Protected View) é um recurso de segurança do Microsoft Office que abre documentos potencialmente inseguros (da internet, anexos de e-mail ou locais inseguros) em modo somente leitura com elementos ativos (como macros VBA e conexões de dados) bloqueados. Isso reduz os riscos de ataques cibernéticos causados por documentos adulterados."
},
  {
    "id": 301,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Sessões Plenárias: Tipologias e Finalidades",
    "question": "De acordo com as regras regimentais típicas das Câmaras Municipais e os princípios do Processo Legislativo, as sessões plenárias dividem-se em ordinárias, extraordinárias, solenes e secretas. Sobre a Sessão Extraordinária, é correto afirmar que:",
    "options": [
      "Destina-se exclusivamente à discussão e votação das matérias constantes do ato de sua convocação, sendo vedada a deliberação sobre assunto estranho à pauta.",
      "Ocorre em dias e horários pré-determinados no Regimento Interno, independentemente de convocação especial prévia.",
      "Gera obrigatoriamente o pagamento de parcela indenizatória aos vereadores em valor equivalente a 50% do subsídio mensal.",
      "Pode deliberar sobre qualquer matéria de interesse do Município, inclusive projetos apresentados verbalmente na hora da sessão."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme os princípios constitucionais (CF/88 art. 57, § 7º aplicável por simetria aos Municípios) e normas regimentais, na sessão legislativa extraordinária a Câmara Municipal delibera EXCLUSIVAMENTE sobre a matéria para a qual foi convocada. Além disso, a Emenda Constitucional nº 50/2006 vedou expressamente o pagamento de qualquer parcela indenizatória em razão de convocação extraordinária."
  },
  {
    "id": 302,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Quórum de Abertura e Instalação de Sessão Plenária",
    "question": "Para que uma Sessão Ordinária da Câmara Municipal de Meruoca possa ser legalmente aberta e tenha início a sua fase deliberativa, exige-se via de regra o quórum de presença de:",
    "options": [
      "Dois terços (2/3) de todos os membros que compõem a Câmara Municipal.",
      "Maioria absoluta dos membros da Câmara Municipal (metade mais um dos vereadores).",
      "Pelo menos um terço (1/3) dos vereadores para abertura e deliberação indistinta.",
      "Apenas o Presidente e o Primeiro Secretário da Mesa Diretora, independente do número de presentes."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Em regra de processo legislativo e direito parlamentar municipal, a abertura da sessão ordinária ou o início da Ordem do Dia (fase de deliberação e votação) exige a presença da MAIORIA ABSOLUTA dos membros da Casa (primeiro número inteiro superior à metade do total de vereadores). Sem quórum mínimo, a sessão não pode deliberar."
  },
  {
    "id": 303,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Fases da Sessão Plenária: Expediente vs. Ordem do Dia",
    "question": "A sessão ordinária da Câmara Municipal é estruturada em momentos distintos. A fase destinada prioritariamente à leitura de correspondências recebidas, apresentação de proposições e breves pronunciamentos de vereadores, antes das votações, denomina-se:",
    "options": [
      "Ordem do Dia.",
      "Tribuna Livre Comunitária.",
      "Pequeno Expediente (ou Expediente).",
      "Explicação Pessoal Final."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A sessão plenária ordinária divide-se classicamente em: 1) Expediente (ou Pequeno/Grande Expediente), destinado a comunicações da Mesa, leitura de ofícios, apresentação de matérias e discursos; 2) Ordem do Dia, que é a fase deliberativa onde as proposições da pauta são discutidas e votadas; e 3) Explicações Pessoais, destinada às considerações finais dos vereadores."
  },
  {
    "id": 304,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Convocação Extraordinária da Câmara Municipal",
    "question": "A convocação extraordinária da Câmara Municipal fora do período ordinário de funcionamento ou em situações de urgência e interesse público relevante pode ser promovida legitimamente por:",
    "options": [
      "Qualquer cidadão eleitor do Município mediante abaixo-assinado com 50 assinaturas.",
      "Exclusivamente pelo Delegado de Polícia da comarca local em razão de inquérito penal.",
      "Pelo Juiz de Direito da Vara Única da Comarca com anuência do Ministério Público.",
      "Pelo Prefeito Municipal, pelo Presidente da Câmara ou por requerimento da maioria dos vereadores."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A convocação extraordinária da Câmara Municipal decorre de preceito constitucional e das Leis Orgânicas municipais: pode ser realizada pelo Prefeito (em caso de urgência relevante), pelo Presidente da Câmara ou pela maioria dos membros do Legislativo. Autoridades externas ou cidadãos isolados não detêm legitimidade para convocar sessões extraordinárias da Casa Legislativa."
  },
  {
    "id": 305,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Instrumentos Parlamentares: Pedido de Vista",
    "question": "Durante a tramitação de uma matéria colocada em discussão na Ordem do Dia, um vereador manifesta a necessidade de examinar mais detidamente o texto do projeto antes de proferir seu voto. O instrumento regimental cabível para essa finalidade é o:",
    "options": [
      "Pedido de Vista.",
      "Recurso de Agravo Regimental.",
      "Destaque para Votação em Separado.",
      "Voto em Separado da Oposição."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Pedido de Vista é a prerrogativa regimental conferida ao parlamentar (seja em Comissão ou em Plenário) para obter acesso aos autos da proposição por prazo determinado, a fim de analisar a matéria detalhadamente antes de sua votação definitiva."
  },
  {
    "id": 306,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Proposições: Emendas Modificativas, Supressivas e Aditivas",
    "question": "No processo legislativo municipal, as emendas parlamentares apresentadas a um projeto de lei classificam-se conforme sua finalidade material. A emenda que visa eliminar parte do texto de um artigo ou parágrafo é classificada como:",
    "options": [
      "Emenda Modificativa.",
      "Emenda Supressiva.",
      "Emenda Aditiva.",
      "Emenda Aglutinativa."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Conforme a técnica legislativa clássica e os Regimentos Internos: a) Emenda Supressiva: elimina qualquer parte de uma proposição; b) Emenda Aditiva: acrescenta algo novo ao texto; c) Emenda Modificativa: altera a redação sem criar ou extinguir substancialmente o dispositivo; d) Emenda Substitutiva: substitui integralmente a proposição (substitutivo) ou artigo."
  },
  {
    "id": 307,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Atribuições do Presidente da Câmara e Voto de Minerva",
    "question": "No exercício das funções da Presidência da Câmara Municipal, o Presidente da Mesa Diretora possui regras especiais quanto ao direito de voto no Plenário. Em regra geral, o Presidente vota quando:",
    "options": [
      "Desejar manifestar sua opinião partidária em qualquer discussão preliminar.",
      "A votação envolver matéria contábil de fornecedores de pequeno valor.",
      "Houver empate na votação pública (voto de desempate/Minerva) ou em matérias que exijam quórum qualificado (como 2/3).",
      "O Prefeito Municipal enviar mensagem com pedido expresso de manifestação presidencial."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Por expressa tradição parlamentar e previsão regimental, o Presidente da Câmara não vota nas deliberações ordinárias para manter a imparcialidade na condução dos trabalhos, VOTANDO APENAS: 1) para desempatar a votação (voto de Minerva); 2) em votações secretas (quando existentes); 3) quando a matéria exigir quórum de dois terços (2/3) ou maioria absoluta, onde sua presença e voto contam para o quórum qualificado."
  },
  {
    "id": 308,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Lideranças Partidárias e Colégio de Líderes",
    "question": "A representação partidária no âmbito do Poder Legislativo organiza-se por meio de lideranças. Sobre o papel dos Líderes Partidários e do Colégio de Líderes, assinale a afirmativa correta:",
    "options": [
      "O Líder partidário perde o direito de discursar nas sessões se não for membro da Mesa Diretora.",
      "O Colégio de Líderes substitui as Comissões Permanentes e pode aprovar leis sem necessidade de plenário.",
      "Os Líderes são nomeados diretamente pelo Prefeito Municipal para representá-lo na bancada dos vereadores.",
      "O Líder é o porta-voz autorizado de sua bancada partidária, podendo fazer uso da palavra pela liderança e orientar o voto de seus liderados nas deliberações."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O Líder é o parlamentar formalmente indicado pela agremiação ou bloco partidário para expressar o posicionamento oficial da bancada, orientar a votação em plenário, participar de reuniões de definição de pauta no Colégio de Líderes e discursar no tempo destinado à liderança partidária."
  },
  {
    "id": 309,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Maioria e Minoria na Composição da Câmara",
    "question": "O princípio da proporcionalidade partidária, previsto no Art. 58, § 1º da Constituição Federal e aplicável às Câmaras Municipais, assegura que:",
    "options": [
      "A composição das Comissões Permanentes deve reproduzir, tanto quanto possível, a representação proporcional dos partidos ou blocos parlamentares que participam da Casa.",
      "Todos os partidos com representação na Câmara devem ocupar obrigatoriamente um cargo na Mesa Diretora de forma rotativa a cada 6 meses.",
      "O partido da Minoria tem o direito de indicar o Presidente da Câmara, independentemente da vontade do Plenário.",
      "A Mesa Diretora deve ser composta exclusivamente por vereadores pertencentes à bancada de sustentação do Prefeito."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. O Art. 58, § 1º da CF/88 estabelece que na constituição da Mesa e de cada Comissão é assegurada, tanto quanto possível, a representação proporcional dos partidos ou dos blocos parlamentares com assento na Casa Legislativa. Esse postulado garante o pluralismo democrático e a voz da minoria."
  },
  {
    "id": 310,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Sistema Eleitoral para Vereadores: Sistema Proporcional",
    "question": "No Brasil, a eleição para os cargos do Poder Executivo (Prefeito e Governador) segue o Sistema Majoritário, enquanto a eleição para o cargo de Vereador da Câmara Municipal obedece estritamente ao:",
    "options": [
      "Sistema Distrital Puro, dividindo-se o Município em circunscrições de bairro.",
      "Sistema Proporcional de Lista Aberta, no qual as vagas conquistadas pelo partido dependem da soma dos votos da legenda e dos seus candidatos.",
      "Sistema Majoritário Simples em turno único, elegendo-se quem obtiver mais votos absolutos independentemente do partido.",
      "Sistema de Sufrágio Censitário Obrigatório com lista partidária pré-ordenada e fechada."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A eleição para Vereador (assim como para Deputado Estadual e Federal) no Brasil segue o SISTEMA PROPORCIONAL DE LISTA ABERTA (CF/88, art. 29, II e Código Eleitoral). As vagas são distribuídas aos partidos de acordo com o Quociente Eleitoral e o Quociente Partidário, sendo eleitos os candidatos mais votados dentro de cada legenda que atingirem a cláusula de barreira individual."
  },
  {
    "id": 311,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Cálculo do Quociente Eleitoral (QE)",
    "question": "Em uma eleição municipal para a Câmara de Vereadores com 9 cadeiras disponíveis, foram apurados exatamente 18.000 votos válidos (soma dos votos nominais e de legenda). Sabendo que o Quociente Eleitoral (QE) é obtido pela divisão do total de votos válidos pelo número de lugares a preencher (desprezada a fração se igual ou inferior a meio, ou arredondada para um se superior), qual é o Quociente Eleitoral dessa eleição?",
    "options": [
      "1.500 votos.",
      "1.800 votos.",
      "2.000 votos.",
      "2.250 votos."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Aplicação direta da regra do Código Eleitoral (Art. 106): QE = Total de Votos Válidos / Número de Vagas a Preencher. No caso: QE = 18.000 / 9 = 2.000 votos. Logo, cada partido precisa de 2.000 votos para conquistar diretamente uma vaga."
  },
  {
    "id": 312,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Cálculo do Quociente Partidário (QP)",
    "question": "Considerando uma eleição em que o Quociente Eleitoral (QE) foi fixado em 2.000 votos, determinado partido político obteve um total de 6.400 votos válidos (entre votos nominais em seus candidatos e votos de legenda). Conforme o Código Eleitoral (Art. 107), o Quociente Partidário (QP) desse partido é igual a:",
    "options": [
      "1 cadeira.",
      "2 cadeiras.",
      "4 cadeiras.",
      "3 cadeiras (desprezada a fração restante)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O Quociente Partidário (QP) define quantas vagas o partido obtém diretamente pela primeira fase de distribuição: QP = Votação do Partido / QE. Calculando: QP = 6.400 / 2.000 = 3,2. O Art. 107 do Código Eleitoral determina que se despreza a fração! Portanto, o QP é igual a 3 cadeiras. A fração restante (0,2 ou 400 votos) concorre na distribuição das sobras."
  },
  {
    "id": 313,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Cláusula de Barreira Individual do Candidato a Vereador",
    "question": "Para que um candidato a Vereador seja considerado eleito pelas vagas conquistadas pelo seu partido por meio do Quociente Partidário, a legislação eleitoral brasileira (Lei nº 9.504/97 e Código Eleitoral com alterações recentes) exige que o candidato tenha obtido votação nominal mínima de pelo menos:",
    "options": [
      "10% do Quociente Eleitoral (QE).",
      "5% do total de eleitores inscritos no Município.",
      "20% dos votos totais da legenda partidária.",
      "50% da votação do candidato mais votado do Município."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme o Art. 108 do Código Eleitoral (incluído pela Reforma Eleitoral - Lei 13.165/2015), estarão eleitos os candidatos que tenham obtido votos em número igual ou superior a 10% (dez por cento) do Quociente Eleitoral, na ordem da votação nominal que cada um tenha recebido. Essa é a chamada cláusula de barreira/desempenho individual para evitar o efeito 'puxador extremo' de candidatos sem representatividade própria."
  },
  {
    "id": 314,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Distribuição das Sobras Eleitorais",
    "question": "Quando as vagas de vereador não são integralmente preenchidas pelo Quociente Partidário, as vagas restantes ('sobras') são distribuídas pelo critério das maiores médias. A fórmula da média de cada partido participante é obtida por:",
    "options": [
      "Média = Votos Válidos do Município / Número Total de Partidos Concorrentes.",
      "Média = Número de Votos Válidos do Partido / (Número de Vagas Já Obtidas pelo Partido + 1).",
      "Média = Idade do Candidato Mais Velho + Votos Nominais da Coligação.",
      "Média = Quociente Eleitoral * 2 / Total de Vagas da Câmara."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Conforme o Art. 109, I do Código Eleitoral, a média de cada agremiação para disputar as sobras é calculada dividindo-se o número de votos válidos atribuídos a cada partido pelo número de lugares por ele já obtidos mais 1: Média = Votos_Partido / (Vagas_Obtidas + 1). O partido que alcançar a maior média fica com a vaga, repetindo-se a operação até esgotarem as sobras."
  },
  {
    "id": 315,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Fidelidade Partidária e Perda do Mandato Eletivo",
    "question": "O mandato de vereador conquistado no sistema proporcional pertence ao partido político. Conforme jurisprudência pacífica do TSE e do STF, o vereador que se desfiliar do partido sem justa causa perderá o mandato. Constitui hipótese legítima de JUSTA CAUSA para desfiliação partidária:",
    "options": [
      "Desacordo pessoal entre o vereador e o tesoureiro do diretório municipal.",
      "Convite financeiramente mais vantajoso oferecido por liderança do Poder Executivo.",
      "Mudança substancial ou desvio reiterado do programa partidário, ou grave discriminação política pessoal comprovada.",
      "Vontade unilateral do vereador expressa por notificação simples no cartório de títulos."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A Lei dos Partidos Políticos (Lei 9.096/95, art. 22-A) e a Resolução TSE nº 22.610/2007 preveem taxativamente as hipóteses de justa causa: 1) mudança substancial ou desvio reiterado do programa partidário; 2) grave discriminação política pessoal; e 3) mudança de partido efetuada durante a 'janela partidária' (nos 30 dias que antecedem o prazo de filiação no ano da eleição do término do mandato)."
  },
  {
    "id": 316,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Comissões Parlamentares de Inquérito (CPIs) Municipais",
    "question": "A criação de Comissão Parlamentar de Inquérito (CPI) no âmbito da Câmara Municipal constitui importante instrumento de fiscalização da minoria parlamentar. Para a sua instauração válida, a CF/88 (art. 58, § 3º) e a Lei Orgânica exigem simultaneamente:",
    "options": [
      "Autorização prévia do Tribunal de Contas e concordância formal do Prefeito Municipal.",
      "Votação unânime de todos os vereadores presentes e prazo indeterminado de atuação.",
      "Aval da Procuradoria Jurídica do Município e homologação judicial pelo Juiz de Direito da Comarca.",
      "Requerimento de pelo menos um terço (1/3) dos membros da Câmara, indicação de fato determinado e fixação de prazo certo de funcionamento."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. São três os requisitos cumulativos e indispensáveis para a instauração de CPI (CF/88 art. 58, § 3º e jurisprudência vinculante do STF): 1) requerimento de no mínimo 1/3 (um terço) dos membros da Casa; 2) apuração de fato determinado de interesse público; e 3) funcionamento por prazo certo. Presentes os requisitos, a instalação é direito público subjetivo das minorias, independendo de aprovação do plenário."
  },
  {
    "id": 317,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Julgamento das Contas do Prefeito e Quórum Qualificado",
    "question": "O controle externo da Câmara Municipal sobre as contas anuais prestadas pelo Chefe do Poder Executivo é exercido com o auxílio do Tribunal de Contas competente. Sobre o Parecer Prévio emitido pela Corte de Contas, a CF/88 (art. 31, § 2º) estabelece que ele:",
    "options": [
      "Só deixará de prevalecer por decisão de dois terços (2/3) dos membros da Câmara Municipal.",
      "Tem caráter meramente opinativo simples, bastando a maioria dos presentes na sessão para derrubá-lo.",
      "É irrecorrível e vincula a Câmara, impedindo qualquer deliberação política em sentido contrário.",
      "Depende de homologação posterior pelo Ministério Público de Contas para produzir efeitos perante a Câmara."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme o Art. 31, § 2º da Constituição Federal: 'O parecer prévio, emitido pelo órgão competente sobre as contas que o Prefeito deve anualmente prestar, só deixará de prevalecer por decisão de dois terços dos membros da Câmara Municipal'. É uma das regras mais cobradas pela banca INBRASP em concursos legislativos."
  },
  {
    "id": 318,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Inviolabilidade e Imunidade Material do Vereador",
    "question": "Em relação ao estatuto dos congressistas e parlamentares, a Constituição Federal estende aos Vereadores a prerrogativa da imunidade material (Art. 29, VIII). De acordo com o texto constitucional, os vereadores gozam de inviolabilidade por suas opiniões, palavras e votos:",
    "options": [
      "Em todo o território nacional, sob quaisquer circunstâncias de sua vida pessoal e partidária.",
      "No exercício do mandato e na circunscrição do respectivo Município.",
      "Apenas dentro do recinto físico do Plenário da Câmara durante as sessões solenes.",
      "Exclusivamente durante o período eleitoral oficial regulamentado pelo TSE."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A CF/88, em seu Art. 29, VIII, assegura expressamente a inviolabilidade dos Vereadores por suas opiniões, palavras e votos NO EXERCÍCIO DO MANDATO e NA CIRCUNSCRIÇÃO DO MUNICÍPIO. Atenção: vereador NÃO possui imunidade formal/processual ampla (foro por prerrogativa federal geral ou imunidade prisional ampla de parlamentar federal), limitando-se à inviolabilidade material territorialmente demarcada."
  },
  {
    "id": 319,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Registro e Ata das Sessões Legislativas",
    "question": "Ao término de cada sessão plenária da Câmara Municipal, os trabalhos legislativos, debates, presenças e votações ocorridas são formalmente consignados em documento oficial denominado Ata da Sessão. A respeito da Ata, é correto afirmar:",
    "options": [
      "A Ata é elaborada com valor sigiloso, sendo vedado o acesso aos cidadãos e à imprensa local.",
      "A Ata só precisa ser redigida uma vez por ano, ao final da sessão legislativa anual de dezembro.",
      "A Ata é lida e submetida à apreciação do Plenário na sessão ordinária seguinte, podendo os vereadores solicitar retificações antes de sua aprovação e assinatura.",
      "A elaboração da Ata compete ao Prefeito Municipal, que a assina e publica no Diário Oficial."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A Ata da sessão é lavrada pela Secretaria da Câmara sob supervisão da Mesa Diretora. Na sessão subsequente, a Ata é colocada em discussão e votação para que os vereadores possam requerer correções ou retificações quanto a falas ou registros de votos, sendo em seguida assinada pela Mesa e disponibilizada publicamente."
  },
  {
    "id": 320,
    "category": "especificos",
    "day": "w2_d4",
    "discipline": "Técnico Legislativo",
    "topic": "Atos da Presidência da Câmara: Decretos, Resoluções e Portarias",
    "question": "A competência administrativa interna da Câmara Municipal manifesta-se por meio de diferentes espécies normativas e atos regimentais. Para nomear servidor efetivo aprovado em concurso público ou conceder diárias de viagem a vereadores e servidores, o ato administrativo típico expedido pelo Presidente da Câmara é a:",
    "options": [
      "Lei Complementar Municipal.",
      "Emenda à Lei Orgânica.",
      "Medida Provisória Legislativa.",
      "Portaria da Presidência."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Os atos de administração interna e de gestão de pessoal no âmbito da Câmara (como nomeação, exoneração, concessão de férias, licenças e autorização de diárias) são formalizados por meio de PORTARIA expedida pelo Presidente da Câmara. Resoluções e Decretos Legislativos tratam de matérias de competência privativa do Plenário."
  },
  {
    "id": 321,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Razão e Proporção: Divisão Simples",
    "question": "Em um concurso promovido pela Câmara Municipal, a razão entre o número de candidatos inscritos para o cargo de Técnico Legislativo e o número de vagas ofertadas é de 45 para 1. Sabendo que foram abertas exatamente 4 vagas para o cargo, o número total de candidatos inscritos nessa seleção foi de:",
    "options": [
      "180 candidatos.",
      "160 candidatos.",
      "200 candidatos.",
      "140 candidatos."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A razão entre inscritos (x) e vagas (v) é expressa pela proporção: x / v = 45 / 1. Como v = 4, temos: x / 4 = 45 / 1  =>  x = 4 * 45 = 180 candidatos inscritos."
  },
  {
    "id": 322,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Divisão em Partes Diretamente Proporcionais",
    "question": "Dois servidores da Câmara Municipal, Carlos e Mariana, digitalizaram juntos um total de 240 processos legislativos. A divisão do trabalho foi feita em partes diretamente proporcionais ao tempo de serviço de cada um no órgão: Carlos trabalha há 3 anos na Câmara e Mariana há 5 anos. Quantos processos Mariana digitalizou?",
    "options": [
      "90 processos.",
      "150 processos.",
      "120 processos.",
      "160 processos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Na divisão em partes diretamente proporcionais aos números 3 e 5, a soma das partes é: 3 + 5 = 8 partes. Cada parte (constante de proporcionalidade k) vale: k = 240 / 8 = 30 processos. Logo, Mariana, que tem proporção 5, digitalizou: 5 * 30 = 150 processos. (Carlos digitalizou 3 * 30 = 90)."
  },
  {
    "id": 323,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Divisão em Partes Inversamente Proporcionais",
    "question": "A chefia do setor administrativo dividiu uma gratificação de R$ 1.800,00 entre dois técnicos em partes inversamente proporcionais ao número de dias que cada um faltou no mês. O técnico A teve 2 faltas e o técnico B teve 4 faltas. O valor recebido pelo técnico A foi de:",
    "options": [
      "R$ 600,00.",
      "R$ 900,00.",
      "R$ 1.200,00.",
      "R$ 1.400,00."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Dividir em partes inversamente proporcionais a 2 e 4 equivale a dividir em partes diretamente proporcionais aos inversos 1/2 e 1/4. Multiplicando pelo MMC (4) para eliminar as frações: 1/2 * 4 = 2 partes para A; 1/4 * 4 = 1 parte para B. Total de partes = 2 + 1 = 3 partes. O valor de cada parte é 1.800 / 3 = R$ 600,00. Logo, o técnico A recebe 2 * 600 = R$ 1.200,00 (e o técnico B recebe 1 * 600 = R$ 600,00)."
  },
  {
    "id": 324,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Regra de Três Simples Direta: Consumo de Materiais",
    "question": "O setor de reprografia da Câmara Municipal consome 6 resmas de papel A4 a cada 15 dias úteis de trabalho ordinário. Mantido exatamente o mesmo padrão diário de consumo, quantas resmas de papel serão consumidas em um período de 45 dias úteis?",
    "options": [
      "12 resmas.",
      "15 resmas.",
      "24 resmas.",
      "18 resmas."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Trata-se de uma regra de três simples direta (quanto mais dias trabalhados, maior a quantidade de resmas consumidas): 6 resmas ---- 15 dias; x resmas ---- 45 dias. Multiplicando cruzado: 15 * x = 6 * 45  =>  15x = 270  =>  x = 270 / 15 = 18 resmas."
  },
  {
    "id": 325,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Regra de Três Simples Inversa: Tempo e Equipe",
    "question": "Uma equipe composta por 4 arquivistas consegue organizar todo o acervo histórico de leis municipais em exatamente 15 dias de trabalho. Se a equipe fosse reforçada e contasse com 6 arquivistas com a mesma capacidade operacional dos primeiros, em quantos dias o mesmo acervo seria organizado?",
    "options": [
      "10 dias.",
      "8 dias.",
      "12 dias.",
      "9 dias."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. É uma regra de três simples INVERSA (ao aumentar o número de arquivistas, o tempo necessário para executar o serviço diminui): 4 arquivistas ---- 15 dias; 6 arquivistas ---- x dias. Multiplicando em linha: 6 * x = 4 * 15  =>  6x = 60  =>  x = 60 / 6 = 10 dias."
  },
  {
    "id": 326,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Regra de Três Composta: Produção de Relatórios",
    "question": "Trabalhando 6 horas por dia durante 8 dias, 3 redatores legislativos elaboram as atas de 72 sessões plenárias. Quantas atas de sessões plenárias seriam elaboradas por 4 redatores, trabalhando 8 horas por dia durante 5 dias, mantida a mesma produtividade individual?",
    "options": [
      "75 atas.",
      "80 atas.",
      "90 atas.",
      "60 atas."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Montando a regra de três composta identificando as grandezas: Redatores (R), Horas/dia (H), Dias (D) e Atas (A - produto final): R1=3, H1=6, D1=8, A1=72; R2=4, H2=8, D2=5, A2=x. Comparando as grandezas em relação a Atas: Mais redatores = mais atas (direta); Mais horas/dia = mais atas (direta); Mais dias = mais atas (direta). Logo: 72 / x = (3/4) * (6/8) * (8/5)  =>  72 / x = (3 * 6 * 8) / (4 * 8 * 5) = 144 / 160 = 9 / 10. Multiplicando cruzado: 9 * x = 72 * 10  =>  9x = 720  =>  x = 80 atas."
  },
  {
    "id": 327,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Porcentagem: Cálculo de Desconto Comercial",
    "question": "A Câmara de Meruoca realizou processo licitatório para compra de novos computadores cujo valor total tabelado era de R$ 45.000,00. A empresa vencedora ofereceu um desconto de 12% sobre o valor da tabela. Qual foi o valor final pago pela aquisição dos equipamentos?",
    "options": [
      "R$ 40.500,00.",
      "R$ 38.600,00.",
      "R$ 39.600,00.",
      "R$ 41.200,00."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Calculando o desconto de 12% sobre 45.000: Desconto = 45.000 * 0,12 = R$ 5.400,00. Valor final = 45.000 - 5.400 = R$ 39.600,00. (Ou diretamente: 45.000 * 0,88 = R$ 39.600,00)."
  },
  {
    "id": 328,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Porcentagem: Variação Percentual",
    "question": "No mês de janeiro, o número de atendimentos presenciais ao público na ouvidoria da Câmara foi de 250 pessoas. No mês de fevereiro, esse número subiu para 325 atendimentos. Qual foi o percentual de aumento verificado de janeiro para fevereiro?",
    "options": [
      "25%.",
      "28%.",
      "35%.",
      "30%."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A variação absoluta foi de: 325 - 250 = 75 atendimentos. A taxa percentual de aumento em relação ao valor inicial (janeiro) é: Taxa = (Variação / Valor_Inicial) * 100 = (75 / 250) * 100 = 0,30 * 100 = 30% de aumento."
  },
  {
    "id": 329,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Porcentagem: Aumentos Sucessivos",
    "question": "O salário de um servidor público municipal sofreu dois reajustes salariais sucessivos: o primeiro de 10% no início do ano e o segundo de 20% no segundo semestre. O reajuste acumulado real sobre o salário inicial do servidor foi de:",
    "options": [
      "32%.",
      "30%.",
      "31%.",
      "33%."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em aumentos sucessivos, multiplica-se os fatores de correção: Fator 1 = 1 + 0,10 = 1,10; Fator 2 = 1 + 0,20 = 1,20. Fator acumulado = 1,10 * 1,20 = 1,32. Subtraindo a base 1: 1,32 - 1 = 0,32 = 32% de aumento acumulado. Dica clássica: aumentos sucessivos nunca são a soma direta (10 + 20 = 30% é a pegadinha da banca)."
  },
  {
    "id": 330,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Juros Simples: Cálculo de Juros",
    "question": "Um servidor realizou uma aplicação financeira no valor de R$ 8.000,00 em regime de juros simples, a uma taxa de 1,5% ao mês, durante um período de 10 meses. O valor total dos juros rendidos por essa aplicação foi de:",
    "options": [
      "R$ 1.000,00.",
      "R$ 1.200,00.",
      "R$ 1.400,00.",
      "R$ 960,00."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Fórmula do juro simples: J = C * i * t, onde C = 8.000, i = 1,5% = 0,015 ao mês e t = 10 meses. J = 8.000 * 0,015 * 10 = 8.000 * 0,15 = R$ 1.200,00 de juros."
  },
  {
    "id": 331,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Juros Simples: Cálculo do Montante",
    "question": "Um empréstimo consignado de R$ 12.000,00 foi contratado à taxa de juros simples de 2% ao mês para ser quitado integralmente ao final de 8 meses em parcela única. Qual será o montante total (capital + juros) a ser pago na liquidação do empréstimo?",
    "options": [
      "R$ 13.600,00.",
      "R$ 14.120,00.",
      "R$ 13.920,00.",
      "R$ 14.400,00."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Cálculo dos juros simples: J = C * i * t = 12.000 * 0,02 * 8 = 12.000 * 0,16 = R$ 1.920,00. O montante final é a soma do capital inicial com os juros: M = C + J = 12.000 + 1.920 = R$ 13.920,00."
  },
  {
    "id": 332,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Juros Simples: Determinação do Tempo",
    "question": "Durante quanto tempo um capital de R$ 5.000,00 deve permanecer aplicado a uma taxa de juros simples de 2,5% ao mês para que gere um montante de R$ 6.500,00?",
    "options": [
      "8 meses.",
      "10 meses.",
      "14 meses.",
      "12 meses."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Juros gerados: J = Montante - Capital = 6.500 - 5.000 = R$ 1.500,00. Pela fórmula J = C * i * t: 1.500 = 5.000 * 0,025 * t  =>  1.500 = 125 * t  =>  t = 1.500 / 125 = 12 meses."
  },
  {
    "id": 333,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Média Aritmética Simples e Ponderada",
    "question": "Na avaliação de desempenho de um estagiário na Câmara, foram aplicadas 4 avaliações com notas de 0 a 10. Suas três primeiras notas foram 7,0; 8,0 e 6,0. Para que sua média aritmética final seja exatamente 8,0, qual nota ele precisa tirar na quarta avaliação?",
    "options": [
      "11,0 (impossível na escala de 0 a 10).",
      "9,0.",
      "10,0.",
      "8,5."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Para a média de 4 notas ser 8,0, a soma das quatro notas deve ser: Soma = 4 * 8,0 = 32,0 pontos. A soma das três primeiras notas é: 7,0 + 8,0 + 6,0 = 21,0 pontos. Logo, a quarta nota necessária seria: 32,0 - 21,0 = 11,0 pontos. Como a escala de avaliação vai até 10,0, é matematicamente impossível atingir essa média final."
  },
  {
    "id": 334,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Equações do 1º Grau aplicadas ao Serviço Público",
    "question": "Em uma sessão plenária extraordinária, o dobro do número de vereadores presentes somado a 5 resulta em 23 vereadores. Quantos vereadores estavam presentes nessa sessão?",
    "options": [
      "8 vereadores.",
      "9 vereadores.",
      "10 vereadores.",
      "11 vereadores."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Montando a equação do 1º grau: sendo 'x' o número de vereadores presentes: 2x + 5 = 23  =>  2x = 23 - 5  =>  2x = 18  =>  x = 18 / 2 = 9 vereadores presentes."
  },
  {
    "id": 335,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Equações do 1º Grau",
    "question": "O almoxarifado da Câmara comprou 50 unidades de materiais de expediente entre pastas organizadoras e canetas esferográficas, totalizando uma despesa de R$ 160,00. Cada pasta custou R$ 5,00 e cada caneta custou R$ 2,00. Quantas pastas organizadoras foram compradas?",
    "options": [
      "15 pastas.",
      "25 pastas.",
      "20 pastas.",
      "30 pastas."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Seja 'p' o número de pastas e 'c' o número de canetas. Sistema: 1) p + c = 50; 2) 5p + 2c = 160. Da primeira equação: c = 50 - p. Substituindo na segunda: 5p + 2(50 - p) = 160  =>  5p + 100 - 2p = 160  =>  3p = 160 - 100  =>  3p = 60  =>  p = 20 pastas organizadoras (e 30 canetas)."
  },
  {
    "id": 336,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Conversão de Unidades de Tempo e Medida",
    "question": "Uma gravação audiovisual de uma sessão solene da Câmara Municipal durou exatamente 2 horas, 45 minutos e 30 segundos. Convertendo todo esse tempo exclusivamente para segundos, obtém-se:",
    "options": [
      "9.750 segundos.",
      "10.230 segundos.",
      "9.850 segundos.",
      "9.930 segundos."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Conversão passo a passo: 1 hora = 3.600 segundos  =>  2 horas = 2 * 3.600 = 7.200 segundos; 1 minuto = 60 segundos  =>  45 minutos = 45 * 60 = 2.700 segundos; Mais os 30 segundos adicionais: Total = 7.200 + 2.700 + 30 = 9.930 segundos."
  },
  {
    "id": 337,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "RLM: Conectivos Lógicos e Tabela Verdade da Conjunção",
    "question": "Considerando as proposições simples p: 'O projeto de lei foi aprovado em plenário' (Verdadeira) e q: 'O Prefeito vetou o projeto' (Falsa), o valor lógico da proposição composta 'O projeto de lei foi aprovado E o Prefeito vetou o projeto' (p ^ q) é:",
    "options": [
      "Falso, pois na conjunção ('E') a proposição composta só é verdadeira quando todas as proposições componentes forem simultaneamente verdadeiras.",
      "Verdadeiro, pois basta que uma das proposições seja verdadeira para validar a conjunção.",
      "Inconclusivo, pois depende da publicação oficial no Diário da Câmara.",
      "Verdadeiro, pois a conjunção assume sempre o valor da proposição que veio primeiro."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Pela tabela-verdade do conectivo da conjunção (operador lógico 'E' / ^): V ^ F = F. A conjunção exige a veracidade cumulativa e simultânea de ambas as proposições para ser verdadeira. Havendo ao menos uma proposição falsa, o resultado lógico é impreterivelmente FALSO."
  },
  {
    "id": 338,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "RLM: Negação da Proposição Condicional (Se... então)",
    "question": "Na lógica sentencial clássica, a negação lógica da proposição condicional 'Se o servidor cumpre a meta, então recebe o elogio funcional' equivale logicamente a:",
    "options": [
      "Se o servidor não cumpre a meta, então não recebe o elogio funcional.",
      "O servidor cumpre a meta e não recebe o elogio funcional.",
      "Se o servidor recebe o elogio funcional, então cumpriu a meta.",
      "O servidor não cumpre a meta ou recebe o elogio funcional."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A regra de ouro da negação da condicional (P -> Q) é a 'Regra do MANÉ': Mantém a primeira (P) E nega a segunda (~Q): ~(P -> Q) = P ^ ~Q. Portanto: 'O servidor cumpre a meta E não recebe o elogio funcional'."
  },
  {
    "id": 339,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Sequências Numéricas e Padrões Lógicos",
    "question": "Observe a sequência lógica de números inteiros: 3, 7, 15, 31, 63, ... Mantendo-se o mesmo padrão aritmético de formação, o próximo termo dessa sequência é:",
    "options": [
      "95.",
      "125.",
      "127.",
      "129."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O padrão de formação pode ser visto de duas formas congruentes: 1) Cada termo é o dobro do anterior somado a 1: 3 * 2 + 1 = 7; 7 * 2 + 1 = 15; 15 * 2 + 1 = 31; 31 * 2 + 1 = 63; Próximo = 63 * 2 + 1 = 126 + 1 = 127. (Ou pelas potências de 2 subtraídas de 1: 2^2-1=3, 2^3-1=7, 2^4-1=15, 2^5-1=31, 2^6-1=63, 2^7-1=128-1=127)."
  },
  {
    "id": 340,
    "category": "matematica",
    "day": "w2_d4",
    "discipline": "Matemática / RLM",
    "topic": "Interpretação de Gráficos e Conjuntos Numéricos",
    "question": "Em uma pesquisa com os 30 servidores da Câmara Municipal, constatou-se que 18 servidores têm curso de capacitação em Processo Legislativo e 14 têm capacitação em Gestão Pública. Sabendo que 6 servidores possuem ambos os cursos, quantos servidores não possuem nenhum desses dois cursos?",
    "options": [
      "2 servidores.",
      "3 servidores.",
      "5 servidores.",
      "4 servidores."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Utilizando o Diagrama de Venn e a teoria dos conjuntos: Total de servidores = 30; Interseção (ambos os cursos) = 6; Somente Processo Legislativo = 18 - 6 = 12; Somente Gestão Pública = 14 - 6 = 8; Total de servidores com pelo menos um curso = 12 + 6 + 8 = 26 servidores. Servidores sem nenhum dos cursos = 30 - 26 = 4 servidores."
  }
,
  {
    "id": 341,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Estrutura dos Atos Normativos: Parte Preliminar",
    "question": "Conforme a Lei Complementar nº 95/1998, que dispõe sobre a elaboração, redação e alteração das leis, a estrutura formal de uma lei compreende três partes básicas: a parte preliminar, a parte normativa e a parte final. Integram obrigatoriamente a PARTE PRELIMINAR de uma lei:",
    "options": [
      "A epígrafe, a ementa, o preâmbulo, o enunciado do objeto e a indicação do âmbito de aplicação.",
      "As disposições transitórias, a cláusula de revogação expressa e a data de vigência.",
      "O texto articulado dos capítulos, a tabela de anexos e os pareceres das comissões.",
      "A assinatura dos líderes partidários e a exposição de motivos assinada pelo relator."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme o Art. 3º, I da LC nº 95/1998, a parte preliminar compreende a epígrafe, a ementa, o preâmbulo, o enunciado do objeto e a indicação do âmbito de aplicação das disposições normativas. A parte normativa contém os artigos do texto legal e a parte final contém a vigência e revogação."
  },
  {
    "id": 342,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Numeração e Articulação dos Artigos",
    "question": "A respeito das regras de articulação dos atos normativos disciplinadas na Lei Complementar nº 95/1998 (Art. 10), a numeração ordinal e cardinal dos ARTIGOS deve obedecer à seguinte regra:",
    "options": [
      "A numeração dos artigos será ordinal do Art. 1º ao Art. 10, passando a cardinal a partir do Art. 11.",
      "A numeração dos artigos será ordinal do Art. 1º ao Art. 9º e cardinal a partir do Art. 10.",
      "Todos os artigos de leis e decretos devem ser grafados compulsoriamente em algarismos romanos.",
      "A numeração dos artigos será sempre cardinal desde o início (Artigo 1, Artigo 2, etc.), vedado o uso de ordinais."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. De acordo com o Art. 10, I da LC nº 95/1998: 'os artigos serão designados pela forma ordinal do primeiro ao nono e pela forma cardinal a partir do dez' (Art. 1º, Art. 2º... Art. 9º; Art. 10, Art. 11, etc.). Essa é uma das regras mais cobradas em provas de técnico legislativo."
  },
  {
    "id": 343,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Desdobramento de Artigos em Parágrafos",
    "question": "O artigo de uma lei municipal pode ser desdobrado em parágrafos para regulamentar aspectos complementares ou exceções à regra geral do 'caput'. Segundo a LC nº 95/1998, a correta indicação do parágrafo único e dos parágrafos múltiplos é:",
    "options": [
      "O parágrafo único deve ser grafado pelo símbolo '§ 1º' com a expressão 'Único' entre parênteses.",
      "Havendo múltiplos parágrafos, todos são grafados por algarismos cardinais com a palavra 'Parágrafo' por extenso.",
      "Quando houver apenas um parágrafo, será indicada a expressão por extenso 'Parágrafo único.'; havendo múltiplos parágrafos, usa-se o símbolo '§' seguido de numeração ordinal do 1º ao 9º e cardinal a partir do 10.",
      "O símbolo '§' só pode ser utilizado se houver mais de dez parágrafos no mesmo artigo."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Conforme o Art. 10, III da LC nº 95/1998: os parágrafos serão indicados pelo símbolo '§', seguido de numeração ordinal até o nono e cardinal a partir do dez. Quando existir apenas um parágrafo no artigo, a denominação é OBRIGATORIAMENTE por extenso: 'Parágrafo único.' (sendo vedado utilizar '§ único' ou '§ 1º único')."
  },
  {
    "id": 344,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Desdobramento em Incisos, Alíneas e Itens",
    "question": "Na hierarquia formal de desdobramento e estruturação dos dispositivos de uma proposição legislativa, a Lei Complementar nº 95/1998 estabelece que:",
    "options": [
      "As alíneas se desdobram em incisos e os incisos se desdobram em itens numéricos.",
      "Os artigos se desdobram diretamente em itens arábicos e estes se desdobram em letras maiúsculas.",
      "Os parágrafos se desdobram em letras maiúsculas e os incisos em algarismos ordinais por extenso.",
      "Os artigos e parágrafos desdobram-se em incisos (algarismos romanos); os incisos em alíneas (letras minúsculas); e as alíneas em itens (algarismos arábicos)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A hierarquia expressa no Art. 10, incisos II, IV e V da LC nº 95/1998 é: 1) Os artigos e os parágrafos desdobram-se em INCISOS (indicados por algarismos romanos: I, II, III...); 2) Os incisos desdobram-se em ALÍNEAS (indicadas por letras minúsculas: a, b, c...); 3) As alíneas desdobram-se em ITENS (indicados por algarismos arábicos: 1, 2, 3...)."
  },
  {
    "id": 345,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Pontuação na Articulação Legislativa",
    "question": "Quanto às normas de pontuação dos dispositivos legais reguladas pela Lei Complementar nº 95/1998 (Art. 10), assinale a alternativa que descreve o emprego gramatical CORRETO:",
    "options": [
      "O texto do artigo (ou parágrafo) que se desdobrar em incisos deve terminar com dois-pontos (:); os incisos e alíneas terminam com ponto e vírgula (;), exceto o último, que termina com ponto final (.).",
      "Todos os incisos e alíneas devem terminar impreterivelmente com ponto final, independentemente de haver continuidade do rol.",
      "O caput do artigo nunca pode terminar com dois-pontos, devendo ser empregado sempre ponto e vírgula.",
      "As alíneas devem terminar sempre com vírgula simples para indicar que pertencem à mesma oração subordinada."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme o Art. 10, VI da LC nº 95/1998: a) o texto do artigo ou parágrafo que se desdobra em incisos finaliza com dois-pontos (:); b) os incisos, alíneas e itens terminam com ponto e vírgula (;), à exceção do último do rol, que se encerra com ponto final (.); c) quando a alínea ou inciso se desdobrar, terminará por dois-pontos."
  },
  {
    "id": 346,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Regras de Alteração de Leis: Inserção de Novos Artigos",
    "question": "Ao elaborar um projeto de lei que pretenda incluir novos artigos entre o Art. 15 e o Art. 16 de uma lei municipal vigente, o redator legislativo deve seguir a sistemática da LC nº 95/1998 para evitar a rennumeração de toda a lei. O procedimento correto de acréscimo é:",
    "options": [
      "Renomear o Art. 16 para Art. 17 e empurrar todos os artigos seguintes para a numeração seguinte.",
      "Identificar os novos artigos com o número do artigo imediatamente anterior seguido de letras maiúsculas em ordem alfabética.",
      "Utilizar números fracionários ou decimais acompanhados de vírgula.",
      "Inserir os novos dispositivos como anexos sem numeração ao final do texto consolidado."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. De acordo com o Art. 12, III, 'b' da LC nº 95/1998, é expressamente vedada a renumeração de artigos existentes. Para a inserção de novos dispositivos entre artigos já existentes, utiliza-se o número do artigo anterior acrescido de letras maiúsculas, em ordem alfabética: Art. 15-A, Art. 15-B, Art. 15-C. (O mesmo se aplica a parágrafos: § 1º-A; e a incisos: I-A)."
  },
  {
    "id": 347,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Proibição de Reaproveitamento de Numeração Revogada",
    "question": "Suponha que o Art. 8º da Lei Orgânica do Município de Meruoca tenha sido formalmente revogado há dois anos. Em novo projeto de lei, um vereador propõe introduzir nova norma e designá-la como 'Art. 8º'. À luz da LC nº 95/1998, essa prática é:",
    "options": [
      "Permitida, desde que o novo assunto tenha pertinência temática com a matéria original.",
      "Válida e recomendada para economizar espaço e evitar o acúmulo de dispositivos com sufixos alfabéticos.",
      "Expressamente vedada, pois é proibido reaproveitar o número de dispositivo revogado, vetado ou declarado inconstitucional para matéria diversa.",
      "Facultativa, ficando a critério discricionário do Presidente da Comissão de Legislação e Justiça."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Conforme o Art. 12, III, 'b' e 'c' da LC nº 95/1998, é vedado o reaproveitamento do número de dispositivo revogado, vetado ou declarado inconstitucional para tratar de matéria diferente, a fim de preservar a segurança jurídica e o histórico da evolução legislativa."
  },
  {
    "id": 348,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Cláusula de Revogação: Expressa vs. Genérica",
    "question": "Uma das alterações mais relevantes impostas pela LC nº 95/1998 no Direito Positivo brasileiro refere-se à CLÁUSULA DE REVOGAÇÃO (Art. 9º). A respeito desse tema, assinale a conduta estritamente obrigatória:",
    "options": [
      "É obrigatório o uso da cláusula genérica 'revogam-se as disposições em contrário' ao final de toda lei.",
      "A lei nova deve deixar a revogação tácita a cargo do Poder Judiciário, sendo desnecessário declarar revogações.",
      "As revogações devem ser feitas de modo velado para não prejudicar direitos adquiridos de terceiros.",
      "A cláusula de revogação deve enunciar expressamente todas as leis ou dispositivos que estão sendo revogados, sendo vedada a fórmula genérica 'revogam-se as disposições em contrário'."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O Art. 9º da LC nº 95/1998 estabelece taxativamente: 'A cláusula de revogação deverá enunciar expressamente as leis ou disposições legais revogadas'. O parágrafo único do mesmo artigo veda expressamente o uso de cláusulas vagas e indeterminadas do tipo 'revogam-se as disposições em contrário'."
  },
  {
    "id": 349,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Cláusula de Vigência e Contagem do Prazo de Vacatio Legis",
    "question": "Segundo o Art. 8º da LC nº 95/1998, a cláusula de vigência deve indicar de forma expressa e clara o prazo para que a lei comece a produzir efeitos. Quando a lei estabelece um período de vacância (vacatio legis) fixado em dias corridos, a contagem do prazo opera-se:",
    "options": [
      "Incluindo-se a data da publicação e a do último dia do prazo, entrando a lei em vigor no dia subsequente à sua consumação integral.",
      "Excluindo-se o dia da publicação e contando-se apenas os dias úteis forenses da comarca.",
      "Iniciando-se 15 dias após a circulação física do primeiro exemplar impresso.",
      "Computando-se os prazos em meses lunares de 28 dias a partir da assinatura do Prefeito."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme o Art. 8º, § 1º da LC nº 95/1998 (redação dada pela LC 107/2001): 'A contagem do prazo para entrada em vigor das leis que estabeleçam período de vacância far-se-á com a inclusão da data da publicação e do último dia do prazo, entrando em vigor no dia subsequente à sua consumação integral'."
  },
  {
    "id": 350,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Uso da Expressão 'Entra em Vigor na Data de sua Publicação'",
    "question": "A fórmula 'esta Lei entra em vigor na data de sua publicação' é frequentemente encontrada no encerramento de diplomas legais. Nos termos das diretrizes da LC nº 95/1998, essa fórmula:",
    "options": [
      "Deve ser adotada compulsoriamente em todos os códigos e diplomas orçamentários do Município.",
      "É recomendada apenas para leis de pequena repercussão, que não demandem prazo de adaptação dos cidadãos ou da Administração Pública.",
      "Foi banida do ordenamento e enseja a nulidade absoluta do ato legislativo.",
      "Só pode ser utilizada caso o texto legal tenha menos de três artigos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. De acordo com o Art. 8º, 'caput' da LC nº 95/1998: a cláusula 'entra em vigor na data de sua publicação' deve ser reservada para as leis de pequena repercussão. Leis de grande alcance, códigos e normas que imponham novas obrigações materiais devem prever vacatio legis adequada para ampla divulgação e conhecimento."
  },
  {
    "id": 351,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Redação de Leis: Clareza, Precisão e Ordem Direta",
    "question": "As disposições normativas devem ser redigidas com clareza, precisão e ordem lógica. O Art. 11 da LC nº 95/1998 estabelece diretrizes de redação oficial. Para a obtenção de CLAREZA e PRECISÃO, o texto legal deve:",
    "options": [
      "Empregar adjetivos superlativos e figuras de linguagem poéticas para embelezar o preâmbulo.",
      "Usar frases longas e subordinadas com múltiplas negações para dificultar interpretações ambíguas.",
      "Usar frases curtas em ordem direta, vocabulário corrente em sentido comum, evitando preciosismos e neologismos desnecessários.",
      "Evitar a repetição de termos técnicos, substituindo-os a cada parágrafo por sinônimos inventados."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O Art. 11, I da LC nº 95/1998 impõe: a) usar palavras e expressões em seu sentido comum (salvo termo técnico próprio da área); b) usar frases curtas e concisas em ordem direta; c) construir as orações na forma positiva; d) manter a uniformidade de tempo verbal e de terminologia ao longo de todo o ato normativo."
  },
  {
    "id": 352,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Uso de Siglas e Nomenclaturas em Proposições",
    "question": "Ao redigir um projeto de lei que cite órgãos ou entidades públicas municipais e estaduais por meio de siglas (como TCM, SAAE, SUS), a técnica legislativa oficial exige que:",
    "options": [
      "As siglas sejam utilizadas isoladamente desde a ementa, sem necessidade de escrita por extenso.",
      "As siglas sejam grafadas sempre em letras minúsculas acompanhadas de asterisco no rodapé.",
      "O uso de qualquer sigla em texto de lei seja expressamente proibido pela Constituição.",
      "Na primeira menção no texto normativo, a denominação do órgão ou entidade seja escrita por extenso, acompanhada da respectiva sigla entre parênteses."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Conforme o Art. 11, II, 'f' da LC nº 95/1998, para assegurar a precisão do texto legal: 'indicar, expressamente, o dispositivo objeto de remissão (...) e grafar por extenso as referências a números e percentuais (...); e indicar a primeira menção de entidades e órgãos com o nome por extenso seguido da respectiva sigla entre parênteses'."
  },
  {
    "id": 353,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Consolidação de Leis: Conceito e Limites",
    "question": "A consolidação de leis consiste na integração de todas as leis vigentes sobre determinada matéria em um único diploma legal. Segundo a LC nº 95/1998 (Art. 13), o projeto de lei de consolidação:",
    "options": [
      "Tem por objetivo reunir normas afins, revogando expressamente os atos originais e preservando o conteúdo substantivo das regras consolidadas.",
      "Pode criar novos tributos e penalidades mais graves sem prévia discussão em comissão temática.",
      "Extingue os direitos subjetivos concedidos por leis municipais anteriores a 1988.",
      "Dispensa a aprovação pelo Plenário da Câmara, sendo publicado por despacho monocrático da Mesa."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme o Art. 13 da LC nº 95/1998, a consolidação consiste na reunião de atos normativos sobre determinado assunto em um único texto, eliminando duplicidades e contradições. É vedada qualquer alteração de mérito substantivo da lei consolidada que retire direitos ou crie novas obrigações não previstas nas leis originais."
  },
  {
    "id": 354,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Alterações Permitidas no Processo de Consolidação",
    "question": "No processo de consolidação de leis municipais pela Câmara Municipal, a LC nº 95/1998 permite que sejam efetuadas certas adaptações formais no texto integrado. Entre as alterações permitidas na consolidação, inclui-se:",
    "options": [
      "A criação de novos cargos comissionados para a estrutura do Poder Legislativo.",
      "A declaração de nulidade de contratos administrativos celebrados no exercício anterior.",
      "A supressão de dispositivos já declarados inconstitucionais pelo STF ou TJ e a atualização de termos gramaticais obsoletos.",
      "A alteração dos quóruns regimentais de maioria qualificada previstos na Lei Orgânica."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O Art. 14 da LC nº 95/1998 autoriza expressamente, na consolidação: a) supressão de dispositivos declarados inconstitucionais pelo Judiciário com efeito erga omnes; b) supressão de dispositivos implicitamente revogados; c) adequação de terminologias e linguagem gramatical arcaica; d) uniformização do tempo verbal e fusão de dispositivos repetitivos."
  },
  {
    "id": 355,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Ementa dos Atos Normativos",
    "question": "A ementa é o elemento formal que sintetiza o conteúdo da lei. De acordo com as disposições da LC nº 95/1998 (Art. 5º), a ementa de um ato normativo deve:",
    "options": [
      "Conter no máximo cinco palavras e ser impressa em caracteres itálicos no rodapé da folha.",
      "Reproduzir a justificação política do projeto com a biografia do parlamentar proponente.",
      "Alinhar-se à esquerda do texto com tamanho de fonte superior ao do título principal da lei.",
      "Ser grafada de forma concisa e indicar, com clareza e precisão, o objeto principal sobre o qual versa a lei."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O Art. 5º da LC nº 95/1998 preconiza: 'A ementa será grafada por meio de caracteres que a realcem e alinhar-se-á à direita da página, explicitando, de modo conciso, o objeto da lei'. Ela funciona como o resumo temático oficial do diploma."
  },
  {
    "id": 356,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Unicidade do Objeto e Proibição de 'Jabutis'",
    "question": "O Art. 7º da LC nº 95/1998 estabelece que o primeiro artigo do texto legal indicará o objeto da lei e o seu âmbito de aplicação. O mesmo artigo preconiza o Princípio da Unicidade do Objeto. Isso significa que:",
    "options": [
      "Cada lei tratará de um único objeto, não devendo conter matéria estranha ao seu objeto principal ou a este não vinculada por afinidade.",
      "Uma lei municipal só pode possuir um único artigo substantivo em todo o seu corpo normativo.",
      "O Município só pode aprovar uma única lei tributária por ano legislativo ordinário.",
      "As leis ordinárias não podem ser alteradas por leis complementares sob pena de bitributação."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme o Art. 7º, II da LC nº 95/1998: 'a lei não conterá matéria estranha a seu objeto ou a este não vinculada por afinidade, pertinência ou conexão'. Essa regra visa banir os chamados 'jabutis' ou 'contrabandos legislativos' (inserção de temas totalmente alheios à ementa original do projeto)."
  },
  {
    "id": 357,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Epígrafe de Leis e Decretos",
    "question": "Na técnica legislativa, a EPÍGRAFE localiza-se no topo do documento normativo. A sua correta formação formal é constituída por:",
    "options": [
      "Pelo nome de batismo do autor do projeto e seu domicílio eleitoral.",
      "Pelo título designativo da espécie normativa, número oficial do ato e ano de sua promulgação (ex.: LEI Nº 1.234, DE 11 DE SETEMBRO DE 2026).",
      "Por uma citação jurisprudencial de tribunal superior que fundamente a legalidade da matéria.",
      "Pela indicação do partido político que detém a maioria dos assentos na Câmara."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Conforme o Art. 4º da LC nº 95/1998: 'A epígrafe, grafada em caracteres maiúsculos, propiciará identificação numérica e figurará a espécie normativa, número e data do ato' (exemplo clássico: LEI Nº 450, DE 11 DE SETEMBRO DE 2026)."
  },
  {
    "id": 358,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Agrupamento de Artigos em Capítulos e Títulos",
    "question": "Quando uma proposição legislativa possui grande extensão ou complexidade temática (como a Lei Orgânica ou o Regimento Interno), seus artigos podem ser agrupados hierarquicamente. A ordem hierárquica ascendente de agrupamento prevista na LC nº 95/1998 (Art. 10, VII) é:",
    "options": [
      "Artigos -> Parágrafos -> Itens -> Alíneas -> Capítulos.",
      "Artigos -> Títulos -> Livros -> Seções -> Subseções.",
      "Artigos -> Subseções -> Seções -> Capítulos -> Títulos -> Livros -> Partes.",
      "Artigos -> Alíneas -> Seções -> Anexos -> Decretos."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Conforme o Art. 10, VII da LC nº 95/1998: os artigos podem ser agrupados sucessivamente em: Subseções; as subseções em Seções; as seções em Capítulos; os capítulos em Títulos; os títulos em Livros; e os livros em Partes (Parte Geral e Parte Especial)."
  },
  {
    "id": 359,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Indicação de Prazos e Datas na Técnica Legislativa",
    "question": "A respeito da padronização e precisão textual na redação de leis conforme a LC nº 95/1998, as referências a datas e valores nos textos normativos devem ser expressas da seguinte maneira:",
    "options": [
      "As datas devem ser abreviadas em padrão numérico com barras (ex.: 11/09/26) para poupar linhas no diário.",
      "Os valores monetários devem ser escritos exclusivamente em numerais arábicos, dispensando-se a escrita por extenso.",
      "Os valores monetários e datas devem ser registrados em moeda estrangeira conversível pelo Banco Central.",
      "Para expressar datas, utiliza-se a forma por extenso (ex.: 11 de setembro de 2026), grafando-se '1º' para o primeiro dia do mês; e valores monetários são expressos em algarismos seguidos de sua menção por extenso entre parênteses."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O Art. 11, II da LC nº 95/1998 estabelece expressamente a obrigatoriedade de grafar datas por extenso (com '1º de...' para o primeiro dia do mês) e indicar valores monetários em algarismos seguidos da forma por extenso entre parênteses, garantindo exatidão probatória."
  },
  {
    "id": 360,
    "category": "especificos",
    "day": "w2_d5",
    "discipline": "Técnica Legislativa",
    "topic": "Aplicabilidade da LC 95/98 no Âmbito Municipal",
    "question": "Em relação ao alcance federativo da Lei Complementar nº 95/1998, é juridicamente correto afirmar que suas regras e preceitos de técnica legislativa vinculam:",
    "options": [
      "Todos os entes federados (União, Estados, Distrito Federal e Municípios), por expressa determinação do Art. 59, parágrafo único da Constituição Federal.",
      "Exclusivamente o Congresso Nacional, não se aplicando às Câmaras Municipais nem às Assembleias Legislativas.",
      "Apenas as capitais de Estado e cidades com mais de duzentos mil eleitores.",
      "Exclusivamente os projetos de iniciativa privativa do Poder Judiciário e Ministério Público."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme o Art. 59, parágrafo único da CF/88 e o Art. 1º da própria LC nº 95/1998, as normas de técnica legislativa para elaboração, redação e consolidação das leis aplicam-se à União, aos Estados, ao Distrito Federal e a todos os MUNICÍPIOS brasileiros, constituindo parâmetro cogente de legalidade e boa prática legislativa."
  },
  {
    "id": 361,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Identificação do Sujeito da Oração",
    "question": "Na oração 'Aprovaram os vereadores meruoquenses o novo plano de cargos da administração municipal', o sujeito da forma verbal 'Aprovaram' classifica-se como:",
    "options": [
      "Indeterminado, pois o verbo encontra-se flexionado na 3ª pessoa do plural.",
      "Sujeito Simples, cujo núcleo substantivo é 'vereadores', posposto ao verbo.",
      "Oração sem sujeito, por tratar de matéria de interesse público.",
      "Sujeito Composto, formado pelos termos 'vereadores' e 'plano de cargos'."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Colocando a oração na ordem direta: 'Os vereadores meruoquenses [sujeito simples, núcleo: vereadores] aprovaram [verbo] o novo plano de cargos da administração municipal [objeto direto]'. A inversão sintática (sujeito posposto) é uma das armadilhas mais comuns da banca INBRASP para tentar induzir o candidato a marcar sujeito indeterminado."
  },
  {
    "id": 362,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Sujeito Oculto (Desinencial) vs. Indeterminado",
    "question": "Assinale a alternativa em que o sujeito da oração classifica-se tecnicamente como SUJEITO INDETERMINADO:",
    "options": [
      "Durante a sessão matutina, comparecemos pontualmente à reunião de lideranças partidárias.",
      "O Presidente e o Secretário assinaram a resolução legislativa de imediato.",
      "Precisa-se de assessores jurídicos qualificados para a Comissão de Redação Final.",
      "Choveu torrencialmente em Meruoca na madrugada da última terça-feira."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Na frase 'Precisa-se de assessores jurídicos...', temos um Verbo Transitivo Indireto ('precisar de algo') acompanhado do pronome 'se' como ÍNDICE DE INDETERMINAÇÃO DO SUJEITO. Como o verbo é transitivo indireto (com preposição 'de'), a oração não admite voz passiva e o sujeito é INDETERMINADO. Nas outras: A tem sujeito desinencial (nós); B tem sujeito composto; D é oração sem sujeito (fenômeno da natureza)."
  },
  {
    "id": 363,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Oração Sem Sujeito e Concordância com Verbo 'Haver'",
    "question": "O verbo 'HAVER' é classificado como impessoal (oração sem sujeito) quando empregado no sentido de existir, ocorrer ou indicar tempo decorrido, devendo permanecer obrigatoriamente na 3ª pessoa do singular. Assinale a frase que exemplifica a correta regência e concordância sintática desse verbo:",
    "options": [
      "Haviam muitos munícipes presentes no plenário durante a votação das contas públicas.",
      "Houveram várias dúvidas regimentais suscitadas pelos técnicos legislativos durante os debates.",
      "Se não houvessem tantas emendas supressivas, o projeto de lei já teria sido promulgado.",
      "Houve muitos debates produtivos entre os vereadores antes da deliberação final da matéria."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. No sentido de existir ou ocorrer, o verbo HAVER não possui sujeito e NÃO se flexiona no plural: 'Houve muitos debates' (e não 'houveram'). 'Muitos debates' é objeto direto da oração. As opções A, B e C estão incorretas porque flexionaram indevidamente o verbo impessoal no plural ('haviam', 'houveram', 'houvessem')."
  },
  {
    "id": 364,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Transitividade Verbal Direta e Indireta (VTDI)",
    "question": "Considere a frase: 'O Presidente da Câmara comunicou o cancelamento da sessão extraordinária aos vereadores da comarca'. O verbo 'comunicar', no contexto da oração, classifica-se sintaticamente como:",
    "options": [
      "Verbo Transitivo Direto e Indireto (VTDI), regendo 'o cancelamento da sessão' como Objeto Direto e 'aos vereadores da comarca' como Objeto Indireto.",
      "Verbo Transitivo Indireto (VTI), pois exige obrigatoriamente duas preposições sucessivas.",
      "Verbo Intransitivo (VI), sendo todos os seus complementos meros adjuntos adverbiais de modo.",
      "Verbo de Ligação (VL), expressando um estado transitório do sujeito parlamentar."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Quem comunica, comunica algo (Objeto Direto: 'o cancelamento da sessão extraordinária' - sem preposição) a alguém (Objeto Indireto: 'aos vereadores da comarca' - com preposição 'a'). Trata-se tipicamente de um Verbo Transitivo Direto e Indireto (VTDI ou bitransitivo)."
  },
  {
    "id": 365,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Predicado Verbal, Nominal e Verbo-Nominal",
    "question": "O predicado classifica-se conforme a natureza de seu(s) núcleo(s). Assinale a alternativa que contém um PREDICADO VERBO-NOMINAL:",
    "options": [
      "Os técnicos legislativos analisaram detidamente as emendas apresentadas ao projeto.",
      "Os novos vereadores da legislatura chegaram entusiasmados à primeira sessão plenária.",
      "A Lei Orgânica de Meruoca é fundamental para a organização político-administrativa do Município.",
      "O expediente parlamentar transcorreu sem nenhuma interrupção regimental."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O predicado verbo-nominal possui dois núcleos: um verbo significativo (de ação) e um nome (predicativo). Na oração 'chegaram entusiasmados à primeira sessão', o predicado é formado pelo verbo de ação 'chegaram' (núcleo verbal) + o adjetivo 'entusiasmados' (predicativo do sujeito, núcleo nominal). Em A temos predicado verbal; em C predicado nominal (verbo de ligação 'é' + predicativo 'fundamental'); em D predicado verbal."
  },
  {
    "id": 366,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Complemento Nominal vs. Adjunto Adnominal",
    "question": "Na oração 'A leitura do parecer das comissões esclareceu todas as dúvidas regimentais', o termo destacado 'do parecer das comissões' exerce a função sintática de:",
    "options": [
      "Objeto Direto Preposicionado da forma verbal 'esclareceu'.",
      "Adjunto Adverbial de Instrumento dos trabalhos de votação.",
      "Complemento Nominal, pois completa o sentido do substantivo abstrato de ação 'leitura' com valor paciente/passivo (o parecer foi lido).",
      "Agente da Passiva com função predicativa de causa originária."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A distinção de ouro: 'leitura' é um substantivo abstrato transitivo derivado do verbo 'ler'. O termo preposicionado 'do parecer' tem sentido PACIENTE / PASSIVO (o parecer é lido por alguém, sofre a ação da leitura). Termo preposicionado completando substantivo abstrato com sentido passivo é sempre COMPLEMENTO NOMINAL. Se tivesse sentido ativo (ex.: 'A leitura do vereador'), seria adjunto adnominal."
  },
  {
    "id": 367,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Adjunto Adnominal em Substantivo Abstrato",
    "question": "Diferenciando o Adjunto Adnominal do Complemento Nominal, assinale a opção em que o termo preposicionado em destaque exerce função de ADJUNTO ADNOMINAL:",
    "options": [
      "A obediência às leis municipais é dever inescusável de todos os munícipes.",
      "A confiança no Poder Legislativo foi restabelecida com as audiências públicas transparentes.",
      "O apoio aos servidores concursados foi aprovado por unanimidade pelos vereadores.",
      "A manifestação da Mesa Diretora encerrou a polêmica sobre o quórum de votação."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Em 'A manifestação da Mesa Diretora', a Mesa Diretora é quem PRATICA a ação de manifestar-se (sentido ATIVO / agente). Termo preposicionado ligado a substantivo abstrato com valor ativo é ADJUNTO ADNOMINAL. Nas opções A, B e C os termos possuem sentido paciente ('às leis' = as leis são obedecidas; 'no Poder Legislativo' = o Poder recebe a confiança; 'aos servidores' = os servidores recebem apoio), sendo todos Complementos Nominais."
  },
  {
    "id": 368,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Identificação do Agente da Passiva",
    "question": "Na frase 'O projeto de lei de diretrizes orçamentárias foi sancionado pelo Prefeito Municipal dentro do prazo regimental', o termo 'pelo Prefeito Municipal' classifica-se sintaticamente como:",
    "options": [
      "Agente da Passiva.",
      "Objeto Indireto.",
      "Adjunto Adverbial de Instrumento.",
      "Complemento Nominal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A oração está na voz passiva analítica (verbo auxiliar 'foi' + particípio 'sancionado'). O termo preposicionado 'pelo Prefeito Municipal' representa o ser que executa a ação verbal na oração passiva, classificando-se como AGENTE DA PASSIVA. Passando para a voz ativa: 'O Prefeito Municipal sancionou o projeto de lei...'."
  },
  {
    "id": 369,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Identificação de Adjuntos Adverbiais",
    "question": "No trecho 'Ontem à tarde, o relator apresentou o parecer favorável na sala das comissões com extrema clareza', os termos destacados expressam, respectivamente, circunstâncias adverbiais de:",
    "options": [
      "Causa, finalidade e consequência lógica.",
      "Tempo, lugar e modo.",
      "Instrumento, intensidade e companhia.",
      "Dúvida, oposição e concessão."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Análise das circunstâncias dos adjuntos adverbiais: 1) 'Ontem à tarde' indica a circunstância temporal em que o fato ocorreu (Tempo); 2) 'na sala das comissões' indica a localização física do ato (Lugar); 3) 'com extrema clareza' indica a maneira/forma como o relator apresentou o parecer (Modo)."
  },
  {
    "id": 370,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Aposto Explicativo vs. Vocativo",
    "question": "A respeito dos termos 'Aposto' e 'Vocativo' na sintaxe da língua portuguesa, assinale a afirmativa correta:",
    "options": [
      "O Vocativo mantém estreita dependência sintática com o verbo da oração, exercendo função de sujeito em frases imperativas.",
      "O Aposto explicativo deve vir necessariamente sem vírgulas para não fragmentar a continuidade da frase.",
      "O Vocativo é um termo de chamamento ou interpelação, sintaticamente independente da oração, devendo ser sempre isolado por sinal de pontuação (vírgula).",
      "O Aposto especificativo é aquele que vem sempre entre parênteses para explicar um conceito filosófico."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O VOCATIVO não pertence nem ao sujeito nem ao predicado; é um termo independente utilizado para chamar, invocar ou interpelar o interlocutor ('Senhor Presidente, peço a palavra pela ordem'). Deve vir OBRIGATORIAMENTE isolado por vírgula (ou outro sinal de pontuação enfático). O aposto explicativo, por sua vez, amplia ou resume um termo de natureza substantiva."
  },
  {
    "id": 371,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Classificação do Aposto Especificativo",
    "question": "Em 'O Município de Meruoca situa-se na Região Noroeste do Estado do Ceará', a expressão destacada 'de Meruoca' exerce função sintática de:",
    "options": [
      "Adjunto Adverbial de Origem e Procedência.",
      "Complemento Nominal do verbo situar-se.",
      "Objeto Indireto do substantivo próprio Ceará.",
      "Aposto Especificativo (ou Individualizador)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O APOSTO ESPECIFICATIVO (ou individualizador) restringe e individualiza um substantivo genérico ('Município', 'cidade', 'rio', 'rua', 'poeta') por meio de um nome próprio, ligando-se a ele sem pausa e geralmente com preposição ('cidade de Sobral', 'Município de Meruoca', 'rua das Flores'). Não é separado por vírgulas."
  },
  {
    "id": 372,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Pronome Apassivador vs. Índice de Indeterminação do Sujeito",
    "question": "Analise as duas construções sintáticas a seguir:\nI. 'Publicaram-se os novos editais do concurso legislativo.'\nII. 'Necessita-se de servidores dedicados na assessoria parlamentar.'\nQuanto à função da partícula 'SE', é correto afirmar que:",
    "options": [
      "Em I, o 'SE' é Partícula Apassivadora e 'os novos editais do concurso legislativo' é o Sujeito Paciente; em II, o 'SE' é Índice de Indeterminação do Sujeito e o sujeito é indeterminado.",
      "Em ambas as frases, o 'SE' funciona exclusivamente como pronome reflexivo recíproco.",
      "Em I, o termo 'os novos editais' é objeto direto e o sujeito é indeterminado.",
      "Em II, o 'SE' é conjunção subordinativa condicional de valor conformativo."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Regra capital da sintaxe: Em I, o verbo 'publicar' é Transitivo Direto. Com VTD + se, forma-se a voz passiva sintética (ou pronominal), onde o pronome 'se' é APASSIVADOR e o termo seguinte é o SUJEITO PACIENTE (que concorda com o verbo: 'os editais foram publicados' = 'publicaram-se os editais'). Em II, o verbo 'necessitar' é Transitivo Indireto (rege preposição 'de'). VTI + se resulta em ÍNDICE DE INDETERMINAÇÃO DO SUJEITO, mantendo o verbo obrigatoriamente no singular."
  },
  {
    "id": 373,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Objeto Direto Preposicionado",
    "question": "O objeto direto preposicionado ocorre quando um verbo transitivo direto tem seu complemento introduzido por preposição, não por exigência de regência verbal, mas por razões estilísticas, de ênfase ou para evitar ambiguidade. Assinale a oração que apresenta esse recurso sintático:",
    "options": [
      "O técnico legislativo redigiu a ata da sessão plenária com agilidade.",
      "Os vereadores amam a Meruoca e defendem os interesses de sua população com fervor.",
      "O relatório das contas anuais foi encaminhado ao tribunal competente no prazo legal.",
      "A assembleia dos servidores municipais reivindicou melhorias nos planos de saúde."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O verbo 'amar' é Transitivo Direto ('quem ama, ama algo ou alguém'). Na frase 'amam a Meruoca', a preposição 'a' foi inserida antes do substantivo para expressar respeito cívico e realce afetivo, configurando classicamente um OBJETO DIRETO PREPOSICIONADO. Nas outras alternativas, os verbos 'redigir', 'encaminhar' e 'reivindicar' possuem objetos diretos comuns sem preposição ou objetos indiretos regenciais."
  },
  {
    "id": 374,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Objeto Pleonástico",
    "question": "Na oração 'Aos vereadores da oposição, não lhes restou alternativa senão apresentar a emenda supressiva', o pronome oblíquo 'lhes' retoma enfaticamente o termo prévio 'Aos vereadores da oposição'. Essa repetição estilística e sintática classifica o termo como:",
    "options": [
      "Aposto Resumitivo Substantivado.",
      "Predicativo do Objeto Indireto.",
      "Objeto Indireto Pleonástico.",
      "Adjunto Adverbial de Meio."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O termo 'Aos vereadores da oposição' é um Objeto Indireto já anteposto. A forma pronominal 'lhes' é inserida para duplicar/retomar esse mesmo objeto indireto com finalidade de ênfase e clareza, caracterizando a figura sintática do OBJETO INDIRETO PLEONÁSTICO."
  },
  {
    "id": 375,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Função Sintática do Pronome Relativo 'QUE'",
    "question": "No período 'O projeto de lei que moderniza a estrutura administrativa da Câmara foi elogiado por todos os servidores', o pronome relativo 'que' exerce, dentro da oração subordinada adjetiva, a função sintática de:",
    "options": [
      "Objeto Direto do verbo modernizar.",
      "Complemento Nominal do substantivo lei.",
      "Adjunto Adverbial de Instrumento.",
      "Sujeito da forma verbal 'moderniza'."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Para descobrir a função do pronome relativo 'que', substitui-se o pronome pelo seu antecedente ('o projeto de lei'): 'O projeto de lei [sujeito] moderniza [verbo] a estrutura administrativa [objeto direto]'. Portanto, o pronome relativo 'que' funciona sintaticamente como SUJEITO da oração subordinada adjetiva."
  },
  {
    "id": 376,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Predicativo do Objeto",
    "question": "Assinale a alternativa em que o termo em destaque funciona sintaticamente como PREDICATIVO DO OBJETO:",
    "options": [
      "O Plenário da Câmara considerou a proposta de emenda inconstitucional.",
      "O experiente consultor jurídico redigiu o parecer preliminar com zelo.",
      "A Mesa Diretora permaneceu atenta às reivindicações dos munícipes presentes.",
      "Os manifestantes saíram apressados após a votação final do projeto."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Na oração 'O Plenário [sujeito] considerou [verbo transitivo direto] a proposta de emenda [objeto direto] inconstitucional [predicativo do objeto]'. O adjetivo 'inconstitucional' expressa um atributo ou juízo de valor conferido pelo sujeito ao objeto direto 'a proposta de emenda', caracterizando o Predicativo do Objeto. Em C temos predicativo do sujeito ('atenta'); em D temos predicativo do sujeito ('apressados')."
  },
  {
    "id": 377,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Pontuação do Vocativo no Texto Oficial",
    "question": "Em redação oficial e técnica parlamentar, o vocativo deve ser rigorosamente demarcado pela pontuação. Assinale a frase redigida em estrita conformidade com a norma-padrão da língua portuguesa:",
    "options": [
      "Senhor Presidente solicito a palavra pela ordem, para esclarecer o voto da bancada.",
      "Solicito a palavra pela ordem, Senhor Presidente, para esclarecer o voto da bancada.",
      "Solicito a palavra pela ordem Senhor Presidente para esclarecer o voto da bancada.",
      "Solicito a palavra, pela ordem Senhor Presidente, para esclarecer o voto da bancada."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O vocativo 'Senhor Presidente' interpela diretamente o destinatário da fala. Quando intercalado no meio da oração, deve vir obrigatoriamente ISOLADO POR DUAS VÍRGULAS (uma antes e outra depois): 'Solicito a palavra pela ordem, Senhor Presidente, para esclarecer...'. Em A faltou a vírgula após o vocativo inicial; em C e D a pontuação ficou truncada."
  },
  {
    "id": 378,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Diferenciação de Adjunto Adnominal e Predicativo",
    "question": "Considere os dois enunciados a seguir:\nI. 'O vereador indignado discursou contra o aumento das taxas municipais.'\nII. 'O vereador discursou indignado contra o aumento das taxas municipais.'\nDo ponto de vista sintático-semântico, os termos destacados desempenham, respectivamente, os papéis de:",
    "options": [
      "Adjunto Adverbial de Modo em I; e Objeto Direto Qualificador em II.",
      "Complemento Nominal em I; e Adjunto Adnominal em II.",
      "Adjunto Adnominal em I (característica atribuída de forma direta e inerente ao substantivo); e Predicativo do Sujeito em II (estado transitório associado ao momento da ação de discursar).",
      "Vocativo Invocatório em I; e Aposto Explicativo em II."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Em I, 'indignado' é termo que integra o sintagma nominal ('O vereador indignado'), funcionando como ADJUNTO ADNOMINAL (qualidade vista como duradoura ou específica do sujeito). Em II, 'indignado' funciona como PREDICATIVO DO SUJEITO (estado psicológico momentâneo e circunstancial do vereador no instante em que proferia o discurso), integrando o predicado verbo-nominal."
  },
  {
    "id": 379,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Termos Acessórios - Aposto Resumitivo / Recapitulativo",
    "question": "Na oração 'Projetos de lei, requerimentos verbais, indicações e moções de pesar, NADA impediu o avanço da pauta prioritária da sessão', a palavra destacada 'NADA' exerce a função sintática de:",
    "options": [
      "Objeto Indireto Recíproco do verbo impedir.",
      "Adjunto Adverbial de Negação Absoluta.",
      "Complemento Nominal do substantivo pauta.",
      "Aposto Resumitivo (ou Recapitulativo)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O APOSTO RESUMITIVO (ou recapitulativo) é exercido por um pronome indefinido (como 'tudo', 'nada', 'ninguém') que sintetiza em uma única palavra uma enumeração anterior de termos. Na oração, 'NADA' resume os múltiplos sujeitos enumerados ('projetos de lei, requerimentos, indicações...'), concordando o verbo no singular."
  },
  {
    "id": 380,
    "category": "portugues",
    "day": "w2_d5",
    "discipline": "Língua Portuguesa",
    "topic": "Sintaxe: Análise Sintática Global de Período",
    "question": "No excerto oficial 'A Comissão de Constituição e Justiça aprovou o parecer favorável do relator unanimemente', o termo sublinhado 'o parecer favorável do relator' classifica-se sintaticamente como:",
    "options": [
      "Sujeito Paciente da oração passiva truncada.",
      "Objeto Direto da forma verbal transitiva direta 'aprovou'.",
      "Complemento Nominal da Comissão de Constituição.",
      "Predicativo do Sujeito do ato decisório."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Identificando os termos na oração: 'A Comissão de Constituição e Justiça' = Sujeito Simples; 'aprovou' = Verbo Transitivo Direto; 'o parecer favorável do relator' = OBJETO DIRETO (complemento sem preposição que sofre a ação de aprovar); 'unanimemente' = Adjunto Adverbial de Modo."
  }
,
  {
    "id": 381,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Atos Administrativos: Conceito e Distinções",
    "question": "No âmbito do Direito Administrativo, a atuação do Poder Público desdobra-se em fatos e atos. Assinale a alternativa que apresenta a correta distinção entre ato administrativo e fato administrativo:",
    "options": [
      "O ato administrativo é a manifestação unilateral de vontade da Administração que visa produzir efeitos jurídicos imediatos sob regime de direito público; já o fato administrativo é qualquer acontecimento material da realidade que independe de manifestação volitiva voltada diretamente à produção de tais efeitos, mas repercute no mundo jurídico.",
      "O fato administrativo depende obrigatoriamente de um processo de deliberação solene em diário oficial; o ato administrativo prescinde de vontade humana e decorre sempre de eventos da natureza.",
      "Todo fato administrativo constitui um ato administrativo bilateral praticado exclusivamente sob o regime de direito privado comum.",
      "Ato e fato administrativo são termos estritamente sinônimos no ordenamento pátrio, designando indistintamente a celebração de contratos bilaterais pela Câmara Municipal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme doutrina consagrada (Hely Lopes Meirelles e Di Pietro), o ato administrativo é uma declaração de vontade do Estado (ou de quem lhe faça as vezes) que produz efeitos jurídicos imediatos regidos pelo direito público. Já o fato administrativo é uma ocorrência fática material (como o decurso do tempo, a morte de um servidor ou a colisão de uma viatura) que pode gerar consequências jurídicas reflexas, sem constituir em si uma declaração intencional de vontade jurídica da Administração."
  },
  {
    "id": 382,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Elementos do Ato: Competência (Sujeito)",
    "question": "Sobre o elemento 'Competência' (sujeito) como requisito de validade dos atos administrativos, é CORRETO afirmar:",
    "options": [
      "A competência é plenamente renunciável e pode ser alienada pelo agente público titular caso haja prévia autorização em decreto executivo.",
      "A competência decorre sempre de expressa previsão legal, sendo, em regra, inderrogável, improrrogável e de exercício obrigatório pelo titular legalmente investido.",
      "Qualquer matéria pode ser objeto de delegação administrativa entre órgãos, inclusive a edição de atos de caráter normativo e a decisão de recursos administrativos.",
      "A incompetência do agente público é considerada sempre vício material insanável, vedando de forma absoluta qualquer hipótese de convalidação administrativa."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O princípio da legalidade determina que a competência é sempre fixada em lei, configurando poder-dever irrenunciável, inderrogável e de exercício obrigatório. A alternativa A erra ao permitir renúncia; a C erra porque o art. 13 da Lei 9.784/1999 veda expressamente a delegação de atos normativos, decisão de recursos e matérias de competência exclusiva (mneumônico CENORA); e a D erra pois o vício de competência, desde que não seja razão de competência exclusiva, admite convalidação (ratificação)."
  },
  {
    "id": 383,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Elementos do Ato: Finalidade e Desvio de Poder",
    "question": "O Presidente da Câmara Municipal remove ex officio um servidor estável para atuar em setor distante como forma de represália pessoal por divergências políticas. Essa conduta vicia o ato administrativo no elemento:",
    "options": [
      "Competência, configurando excesso de poder por extrapolação de atribuições formais.",
      "Forma, por ter sido publicado em portaria legislativa comum e não em decreto legislativo.",
      "Finalidade, configurando desvio de poder (ou desvio de finalidade), o que acarreta a nulidade absoluta do ato praticado.",
      "Objeto, haja vista que a remoção de servidores públicos é conduta originariamente ilícita no serviço público."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A finalidade do ato administrativo é elemento sempre vinculado e visa ao interesse público e ao fim específico pretendido pela lei. O uso da remoção funcional como sanção ou vingança pessoal caracteriza típico DESVIO DE PODER (ou desvio de finalidade), espécie de abuso de poder que atinge o elemento finalidade e torna o ato nulo de pleno direito (vício insanável)."
  },
  {
    "id": 384,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Elementos do Ato: Forma e Motivação",
    "question": "A respeito do requisito 'Forma' e do dever de motivação no âmbito dos atos administrativos, assinale a opção correta:",
    "options": [
      "No Direito Administrativo vige o princípio do informalismo absoluto, sendo a forma escrita dispensável mesmo para atos punitivos e exonerações.",
      "A forma é a exteriorização material da vontade administrativa, e a motivação consiste na exposição expressa dos fundamentos de fato e de direito que justificaram a prática do ato.",
      "Motivo e motivação são expressões sinônimas que se referem exclusivamente ao estado psicológico subjetivo do gestor público.",
      "A ausência de motivação em atos vinculados acarreta sempre sua conversão automática em ato discricionário confirmatório."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A FORMA é a maneira pela qual o ato se exterioriza (em regra, escrita e solene para garantir controle e publicidade). A MOTIVAÇÃO é a formalização discursiva e expressa das razões fáticas e jurídicas que embasaram o ato. Motivo é o pressuposto fático e legal; motivação é a sua declaração formal no texto do ato."
  },
  {
    "id": 385,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Teoria dos Motivos Determinantes",
    "question": "A Teoria dos Motivos Determinantes preconiza que:",
    "options": [
      "O administrador público não se vincula aos motivos que declarou formalmente, podendo alterá-los a qualquer tempo durante o processo judicial.",
      "Os motivos determinantes aplicam-se exclusivamente aos atos negociais bilaterais subordinados ao Código Civil.",
      "Apenas os atos expressamente vinculados se subordinam aos motivos fáticos da realidade, ficando os atos discricionários imunes à verificação fática.",
      "A validade do ato administrativo condiciona-se à veracidade e compatibilidade fática e jurídica dos motivos expressamente declarados pela autoridade, mesmo quando a lei não exigia motivação obrigatória."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Pela Teoria dos Motivos Determinantes, quando a autoridade pública declara formalmente os motivos que justificaram o ato, a validade deste fica indissociavelmente vinculada à existência real e legal desses motivos. Se demonstrada a inexistência ou falsidade dos fatos alegados, o ato será nulo, mesmo que se tratasse originalmente de ato discricionário cuja motivação prévia não fosse legalmente obrigatória (como na exoneração ad nutum de cargo comissionado)."
  },
  {
    "id": 386,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Elementos do Ato: Objeto, Motivo e Mérito Administrativo",
    "question": "Nos atos administrativos discricionários, o denominado 'mérito administrativo' (conveniência e oportunidade da Administração) reside fundamentalmente nos elementos:",
    "options": [
      "Competência e Forma.",
      "Competência e Finalidade.",
      "Finalidade e Forma.",
      "Motivo e Objeto."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Enquanto a Competência, a Finalidade e a Forma são elementos obrigatoriamente VINCULADOS em qualquer ato administrativo, a margem de escolha discricionária outorgada por lei ao administrador (juízo de oportunidade e conveniência — mérito administrativo) concentra-se nos elementos MOTIVO (valoração da situação fática autorizadora) e OBJETO (escolha do conteúdo ou medida cabível)."
  },
  {
    "id": 387,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Atributos do Ato: Presunção de Legitimidade e Veracidade",
    "question": "Em relação ao atributo da presunção de legitimidade e veracidade dos atos administrativos, assinale a afirmativa INCORRETA:",
    "options": [
      "Trata-se de uma presunção juris et de jure (absoluta), não admitindo produção de prova em contrário pelo particular prejudicado.",
      "Presume-se que o ato foi editado em estrita conformidade com o ordenamento jurídico (legitimidade) e que os fatos relatados pela Administração são verdadeiros (veracidade).",
      "Opera a inversão do ônus da prova, incumbindo ao administrado comprovar a existência de ilegalidade ou falsidade na atuação administrativa.",
      "Está presente em todos os atos administrativos, desde o momento de sua edição, conferindo-lhes imediata eficácia e operabilidade."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A presunção de legitimidade e veracidade é juris tantum (relativa), e NÃO juris et de jure (absoluta). Ela admite sim prova em contrário; no entanto, em razão da presunção, inverte-se o ônus da prova, cabendo ao particular comprovar que o ato é ilegal ou que os fatos declarados não condizem com a verdade."
  },
  {
    "id": 388,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Atributos do Ato: Autoexecutoriedade",
    "question": "A autoexecutoriedade é o atributo que permite à Administração Pública compelir materialmente o administrado ao cumprimento do ato sem a necessidade de prévia intervenção judicial. Sobre esse atributo, é correto assinalar que:",
    "options": [
      "Está presente de forma irrestrita em todos os atos da Administração, autorizando inclusive a cobrança forçada de créditos e multas sem processo de execução fiscal.",
      "Exige sempre autorização expressa do Ministério Público estadual antes de qualquer medida de polícia administrativa.",
      "Impede que o Poder Judiciário faça qualquer controle a posteriori sobre a proporcionalidade da medida executada pela Administração.",
      "Existe unicamente quando expressamente prevista em lei ou quando exigida por situação de urgência e iminente risco ao interesse público."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A autoexecutoriedade NÃO existe em todos os atos administrativos (por exemplo, a cobrança de multas administrativas exige execução fiscal perante o Judiciário). Segundo a melhor doutrina, a autoexecutoriedade manifesta-se em duas hipóteses: 1) quando houver expressa autorização legal; ou 2) em situações de urgência que demandem atuação imediata para salvaguardar a ordem, saúde ou segurança públicas."
  },
  {
    "id": 389,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Atributos do Ato: Tipicidade",
    "question": "O atributo do ato administrativo segundo o qual o ato deve corresponder a figuras previamente definidas pela lei para produzir determinados efeitos, funcionando como garantia contra arbitrariedades e impedindo a edição de atos inominados impositivos, denomina-se:",
    "options": [
      "Imperatividade.",
      "Tipicidade.",
      "Exigibilidade.",
      "Inalienabilidade."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A TIPICIDADE (atributo formulado e destacado pela Profª Maria Sylvia Zanella Di Pietro) define que o ato administrativo deve corresponder a figuras predefinidas em lei aptas a produzir determinados efeitos jurídicos. Impede que a Administração crie atos inominados para impor obrigações coercitivas unilaterais fora dos moldes da lei."
  },
  {
    "id": 390,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Atributos do Ato: Imperatividade",
    "question": "A imperatividade é o atributo pelo qual os atos administrativos se impõem a terceiros independentemente de sua concordância. Esse atributo NÃO está presente em:",
    "options": [
      "Atos punitivos sancionatórios, como a aplicação de multa de trânsito.",
      "Atos de fiscalização de posturas municipais e interdição de estabelecimentos.",
      "Atos negociais (como a concessão de licença a pedido) e atos puramente enunciativos (como certidões e atestados).",
      "Atos normativos impositivos de deveres de observância compulsória geral."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A imperatividade (decorrente do poder extroverso do Estado) impõe obrigações a terceiros unilateralmente. Por isso, ela NÃO se faz presente nos atos negociais (nos quais o particular solicita voluntariamente um benefício ou autorização, como licença e alvará) nem nos atos enunciativos (que apenas atestam uma situação preexistente, como certidões, certidões de tempo de serviço e atestados)."
  },
  {
    "id": 391,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Classificação dos Atos: Formação da Vontade (Complexo vs Composto)",
    "question": "Em matéria de formação da vontade administrativa, a investidura de determinadas autoridades depende da indicação pelo Chefe do Executivo e da aprovação pelo Poder Legislativo, conjugando vontades de órgãos independentes para a formação de um único ato. Trata-se de um ato administrativo:",
    "options": [
      "Simples.",
      "Subjetivo.",
      "Composto.",
      "Complexo."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. O ATO COMPLEXO nasce da conjugação de vontades de órgãos diferentes e independentes que se fundem para formar um único ato (ex.: nomeação de Ministro do STF com aprovação do Senado, concessão de aposentadoria sujeita a registro pelo Tribunal de Contas). Já o ATO COMPOSTO é praticado por um único órgão e apenas depende da homologação/aprovação ou visto (ato acessório) de outro órgão."
  },
  {
    "id": 392,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Classificação dos Atos: Destinatários",
    "question": "Quanto aos destinatários, os atos administrativos classificam-se em gerais e individuais. Constitui exemplo de ato administrativo geral:",
    "options": [
      "Um decreto regulamentar que disciplina o horário de funcionamento das repartições municipais.",
      "A portaria de demissão disciplinar aplicada a um servidor específico após regular PAD.",
      "A certidão de tempo de contribuição previdenciária expedida em nome de determinado servidor.",
      "O termo de posse individual de um novo Técnico Legislativo aprovado em concurso."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Atos gerais (ou normativos) possuem destinatários indeterminados, comando abstrato e eficácia erga omnes, prevalecendo sobre os atos individuais. O decreto que regulamenta o horário de funcionamento das repartições do Município atinge a coletividade indiscriminada de servidores e cidadãos, sendo genuinamente um ato geral."
  },
  {
    "id": 393,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Espécies de Atos: Licença vs Autorização",
    "question": "No que concerne às espécies de atos negociais, a diferenciação técnica clássica entre 'Licença' e 'Autorização' reside no fato de que:",
    "options": [
      "A licença é ato bilateral e oneroso regulado pelo Direito Comercial; a autorização é um contrato de adesão trabalhista.",
      "A licença decorre do poder disciplinar interno, enquanto a autorização é expressão exclusiva do poder judicante dos tribunais.",
      "A autorização gera direito adquirido imutável ao administrado, não podendo jamais ser cancelada pelo poder público.",
      "A licença é ato administrativo unilateral, vinculado e definitivo, gerando direito subjetivo ao administrado que preenche os requisitos legais; já a autorização é ato unilateral, discricionário e precário, revogável a qualquer tempo sem direito a indenização."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Distinção essencial em provas de concurso: a LICENÇA é vinculada e confere direito subjetivo ao particular que cumpre as exigências legais (ex.: licença para construir, licença para dirigir). A AUTORIZAÇÃO é ato discricionário e precário, concedido no interesse predominante do particular, podendo a Administração revogá-lo discricionariamente por razões de conveniência e oportunidade sem indenização (ex.: autorização para uso de calçada por quiosque)."
  },
  {
    "id": 394,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Espécies de Atos: Atos Ordinatórios",
    "question": "Os atos ordinatórios destinam-se a disciplinar a rotina interna dos órgãos e a conduta funcional dos agentes públicos subalternos, decorrendo do poder hierárquico. São espécies de atos ordinatórios, EXCETO:",
    "options": [
      "Instruções e Circulares internas.",
      "Portarias de designação funcional e Ordens de Serviço.",
      "Memorandos e Avisos administrativos.",
      "Alvarás de autorização e licenças de funcionamento comercial."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Alvarás de autorização e licenças de funcionamento são espécies de ATOS NEGOCIAIS, voltados a conferir faculdades aos particulares mediante manifestação externa da Administração. Já instruções, circulares, portarias, ordens de serviço e memorandos são típicos ATOS ORDINATÓRIOS de circulação interna disciplinar."
  },
  {
    "id": 395,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Espécies de Atos: Atos Enunciativos - Pareceres",
    "question": "No tocante aos atos enunciativos, os pareceres técnicos e jurídicos emitidos por órgãos de consultoria da Câmara Municipal classificam-se quanto à sua força vinculante. Quando a lei obriga o gestor a solicitar o parecer, porém não o obriga a decidir estritamente de acordo com a conclusão do parecerista, trata-se de um parecer:",
    "options": [
      "Facultativo.",
      "Obrigatório (ou preceptivo).",
      "Vinculante.",
      "Arbitrário."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Classificação dos pareceres: 1) FACULTATIVO: a autoridade não é obrigada a pedir e nem a seguir a conclusão; 2) OBRIGATÓRIO (preceptivo): a lei exige expressamente a consulta prévia (solicitação do parecer), mas a autoridade mantém a liberdade de decidir de modo divergente se motivar adequadamente; 3) VINCULANTE: a lei exige a consulta prévia e impõe a obrigação de seguir e acatar as conclusões do parecer."
  },
  {
    "id": 396,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Vícios dos Atos: Excesso de Poder vs Usurpação de Função",
    "question": "Considere duas situações hipotéticas no âmbito legislativo municipal: I. Um servidor efetivo do setor financeiro, com investidura legal, pratica ato de competência privativa do Diretor-Geral da Câmara. II. Um cidadão comum, sem qualquer vínculo funcional ou nomeação, assume uma mesa no plenário e assina termos oficiais fingindo ser servidor público. As situações I e II configuram, respectivamente:",
    "options": [
      "Usurpação de função em I; e Excesso de poder em II.",
      "Desvio de finalidade em I; e Função de fato em II.",
      "Fato da administração em I; e Ato bilateral em II.",
      "Excesso de poder em I; e Usurpação de função em II."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. No caso I, o agente é servidor regularmente investido, mas age além dos limites da sua competência legal: isso configura EXCESSO DE PODER (vício de competência). No caso II, o sujeito não tem investidura nem vínculo com a Administração, praticando ato fingindo ser agente público: isso configura USURPAÇÃO DE FUNÇÃO (crime tipificado no Código Penal e conduta juridicamente inexistente perante o Estado)."
  },
  {
    "id": 397,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Vícios dos Atos: Inexistência do Motivo",
    "question": "Uma servidora pública municipal teve sua licença-prêmio indeferida sob a motivação oficial expressa de que 'a servidora faltou injustificadamente por 15 dias durante o período aquisitivo'. Comprovado nos autos do recurso que a servidora nunca teve nenhuma falta, o ato administrativo padece de vício insanável no elemento:",
    "options": [
      "Competência, por ausência de autorização ministerial.",
      "Forma, pois deveria ter sido publicado em veículo de imprensa particular.",
      "Motivo, em virtude da falsidade e inexistência fática do pressuposto alegado.",
      "Finalidade mediata, visto que a concessão de licenças independe de histórico funcional."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O MOTIVO é o pressuposto de fato e de direito que autoriza a prática do ato. Se a Administração fundamenta seu ato em um fato materialmente inexistente ou falso (supostas faltas inexistentes), há vício fatal de motivo. Pela Teoria dos Motivos Determinantes, a falsidade do motivo enseja a anulação/nulidade do ato denegatório."
  },
  {
    "id": 398,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Atributos do Ato: Exigibilidade vs Executoriedade",
    "question": "A doutrina moderna desdobra a autoexecutoriedade em duas vertentes: exigibilidade e executoriedade. Constitui exemplo de manifestação da 'exigibilidade' do ato administrativo:",
    "options": [
      "A apreensão física de mercadorias deterioradas em estabelecimento comercial irregular.",
      "A demolição compulsória imediata de um imóvel em ruínas que ameaça desabar sobre pedestres.",
      "O uso moderado da força policial para desocupar um prédio público invadido.",
      "A cominação de multa pecuniária pela autoridade sanitária para induzir indiretamente o infrator ao cumprimento da obrigação."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A EXIGIBILIDADE atua pela coerção indireta (meios indiretos que compelem o administrado a cumprir a ordem sob ameaça de sanção, como a imposição de multas diárias). A EXECUTORIEDADE (coerção direta) autoriza a Administração a praticar diretamente a conduta material sobre as coisas ou pessoas sem mediação (como apreender mercadorias, demolir obra irregular ou interditar estabelecimento)."
  },
  {
    "id": 399,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Classificação dos Atos: Perfeição, Validade e Eficácia",
    "question": "Um ato administrativo que completou todo o seu ciclo de formação interna, está em perfeita conformidade com as exigências da lei, porém encontra-se submetido a uma condição suspensiva futura para que passe a produzir seus efeitos práticos, é tecnicamente classificado como:",
    "options": [
      "Perfeito, válido, mas ineficaz.",
      "Imperfeito, inválido e nulo de pleno direito.",
      "Perfeito, nulo e eficaz provisoriamente.",
      "Inexistente, revogável e exaurido."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Análise dos planos do ato administrativo: 1) PERFEIÇÃO: completou o ciclo de formação; 2) VALIDADE: obedece a todos os requisitos de legalidade; 3) EFICÁCIA: aptidão atual para produzir efeitos. Se o ato cumpriu as etapas e a lei, mas aguarda termo inicial ou condição suspensiva, ele é PERFEITO, VÁLIDO, porém ainda INEFICAZ."
  },
  {
    "id": 400,
    "category": "administrativo",
    "day": "w3_d1",
    "discipline": "D. Administrativo",
    "topic": "Espécies de Atos: Atos Punitivos no Poder Disciplinar",
    "question": "A aplicação de penalidade disciplinar de suspensão a um servidor da Câmara Municipal após a conclusão de processo administrativo disciplinar constitui espécie de ato punitivo interno fundado diretamente no poder:",
    "options": [
      "Regulamentar.",
      "Normativo originário.",
      "Disciplinar.",
      "De polícia judiciária."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O PODER DISCIPLINAR é a prerrogativa conferida à Administração Pública para apurar infrações e aplicar sanções aos servidores públicos e àqueles sujeitos a vínculo especial e específico com o Estado (como concessionárias e contratados). Difere do poder de polícia, que impõe restrições a particulares em geral sem vínculo jurídico específico."
  },
  {
    "id": 401,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Coordenação: Oração Coordenada Sindética Adversativa",
    "question": "No excerto 'O projeto de lei continha excelentes propostas para a saúde de Meruoca, PORÉM o plenário da Câmara rejeitou seu texto base', a oração introduzida pela conjunção destacada classifica-se como:",
    "options": [
      "Oração Coordenada Sindética Conclusiva.",
      "Oração Coordenada Sindética Explicativa.",
      "Oração Coordenada Sindética Adversativa.",
      "Oração Subordinada Adverbial Concessiva."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A conjunção 'porém' estabelece uma relação de oposição/contraste entre orações sintaticamente independentes, configurando típica ORAÇÃO COORDENADA SINDÉTICA ADVERSATIVA (conectivos adversativos: mas, porém, contudo, todavia, entretanto, no entanto)."
  },
  {
    "id": 402,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Coordenação: Oração Coordenada Sindética Conclusiva",
    "question": "Assinale a alternativa que apresenta uma Oração Coordenada Sindética Conclusiva:",
    "options": [
      "Os prazos regimentais foram rigorosamente obedecidos; PORTANTO, a deliberação legislativa é válida.",
      "Os vereadores compareceram ao plenário E debateram com entusiasmo as emendas.",
      "Não atrase o envio dos relatórios, POIS o Tribunal de Contas iniciará a auditoria amanhã.",
      "ORA defendia a aprovação imediata da matéria, ORA postulava pedido de vistas regimental."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A oração 'PORTANTO, a deliberação legislativa é válida' exprime dedução e encerramento lógico decorrente do fato anterior, sendo Coordenada Sindética Conclusiva (conectivos: logo, portanto, por conseguinte, por isso, pois posposto ao verbo). Na alternativa B temos aditiva; na C temos explicativa ('pois' anteposto); na D temos alternativas correlativas."
  },
  {
    "id": 403,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Conjunções Coordenativas: Emprego e Sentido do Conectivo 'Pois'",
    "question": "Quanto à sintaxe e ao valor semântico da conjunção 'pois' no período composto, assinale a afirmativa correta:",
    "options": [
      "Quando colocada após o verbo da oração (entre vírgulas), a conjunção 'pois' possui valor conclusivo; quando anteposta ao verbo, introduz oração explicativa ou causal.",
      "A conjunção 'pois' assume exclusivamente sentido adversativo quando empregada no início do período oracional.",
      "O conectivo 'pois' é uma conjunção estritamente proporcional equivalente a 'à medida que'.",
      "O termo 'pois' funciona como conjunção subordinativa concessiva em qualquer contexto formal."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Regra clássica da gramática normativa (Cunha & Cintra, Bechara): quando a conjunção 'pois' vem após o verbo da oração que encabeça (posposta ao verbo e isolada por vírgulas), ela tem valor CONCLUSIVO (ex.: 'Estudou com afinco; obterá, pois, a vaga'). Quando vem antes do verbo (anteposta), tem valor EXPLICATIVO ou CAUSAL (ex.: 'Entre depressa, pois vai chover')."
  },
  {
    "id": 404,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação: Oração Subordinada Substantiva Subjetiva",
    "question": "Na oração 'É indispensável QUE TODOS OS EDIS PARTICIPEM DA VOTAÇÃO', a oração destacada em maiúsculas exerce a função sintática de:",
    "options": [
      "Objeto Direto da oração principal.",
      "Predicativo do Objeto Indireto.",
      "Complemento Nominal do adjetivo indispensável.",
      "Sujeito da oração principal (Oração Subordinada Substantiva Subjetiva)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Analisando a oração principal: 'É indispensável' possui verbo de ligação ('É') e predicativo do sujeito ('indispensável'), mas falta o sujeito da oração! Pergunta-se: O que é indispensável? Resposta: 'que todos os edis participem da votação' (ou 'A participação de todos os edis é indispensável'). Logo, a oração funciona como SUJEITO da oração principal, classificando-se como Subordinada Substantiva Subjetiva."
  },
  {
    "id": 405,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação: Oração Subordinada Substantiva Objetiva Direta",
    "question": "No período 'O parecerista constatou QUE O PROJETO ATENDIA AOS LIMITES DA LEI DE RESPONSABILIDADE FISCAL', a oração em destaque classifica-se como:",
    "options": [
      "Subordinada Substantiva Objetiva Indireta.",
      "Subordinada Adjetiva Restritiva.",
      "Subordinada Substantiva Objetiva Direta.",
      "Subordinada Adverbial Conformativa."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O verbo da oração principal 'constatou' é Transitivo Direto (VTD) e não exige preposição: 'O parecerista constatou ISTO'. O termo 'isto' substitui a oração inteira, que funciona como complemento verbal sem preposição (Objeto Direto), sendo, portanto, Oração Subordinada Substantiva Objetiva Direta, encabeçada pela conjunção integrante 'que'."
  },
  {
    "id": 406,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação: Completiva Nominal vs Objetiva Indireta",
    "question": "Considere as orações: I. 'A comissão tinha a convicção DE QUE AS CONTAS SERIAM APROVADAS.' II. 'O Presidente da Mesa necessitava DE QUE OS SECRETÁRIOS CONFERISSEM O QUÓRUM.' Os segmentos destacados exercem, respectivamente, as funções de:",
    "options": [
      "Objeto Indireto em I; e Complemento Nominal em II.",
      "Aposto Explicativo em I; e Sujeito Oracional em II.",
      "Objeto Direto Preposicionado em I; e Adjunto Adnominal em II.",
      "Complemento Nominal em I; e Objeto Indireto em II."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Em I, a oração subordinada 'de que as contas seriam aprovadas' completa o sentido de um NOME substantivo abstrato ('convicção'), funcionando como COMPLEMENTO NOMINAL (Oração Subordinada Substantiva Completiva Nominal). Em II, a oração 'de que os secretários conferissem o quórum' completa o sentido de um VERBO transitivo indireto ('necessitava'), funcionando como OBJETO INDIRETO (Oração Subordinada Substantiva Objetiva Indireta)."
  },
  {
    "id": 407,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação: Oração Subordinada Substantiva Predicativa",
    "question": "Na frase 'A principal meta da comissão parlamentar é QUE A AUDITORIA CONCLUA O RELATÓRIO NO PRAZO', a oração subordinada classifica-se como:",
    "options": [
      "Subordinada Substantiva Predicativa.",
      "Subordinada Substantiva Subjetiva.",
      "Subordinada Substantiva Apositiva.",
      "Subordinada Adverbial Consecutiva."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A estrutura da oração principal apresenta Sujeito ('A principal meta da comissão parlamentar') + Verbo de Ligação ('é'). O termo que se segue a um verbo de ligação para caracterizar o sujeito é o PREDICATIVO DO SUJEITO. Como essa atribuição é feita por meio de uma oração encabeçada por conjunção integrante, temos uma Oração Subordinada Substantiva Predicativa."
  },
  {
    "id": 408,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação: Oração Subordinada Substantiva Apositiva",
    "question": "Assinale a alternativa que apresenta uma Oração Subordinada Substantiva Apositiva:",
    "options": [
      "Todos os cidadãos sabem que a publicidade administrativa é imperativa.",
      "A exigência dos vereadores consistia nisto: QUE AS REUNIÕES FOSSEM TRANSMITIDAS AO VIVO.",
      "Convém que o parecer da assessoria chegue antes da abertura dos trabalhos.",
      "O edital foi publicado pelos servidores para que os licitantes comparecessem."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A Oração Subordinada Substantiva Apositiva exerce a função sintática de aposto de um termo da oração principal, explicando-o de forma específica. Geralmente vem pontuada com dois-pontos ou travessões (ex.: '...consistia nisto: que as reuniões fossem transmitidas ao vivo')."
  },
  {
    "id": 409,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação: Orações Adjetivas (Explicativa vs Restritiva)",
    "question": "Considere os enunciados: I. 'Os vereadores de Meruoca, QUE ESTUDARAM O REGIMENTO INTERNO, votaram favoravelmente ao parecer.' II. 'Os vereadores de Meruoca QUE ESTUDARAM O REGIMENTO INTERNO votaram favoravelmente ao parecer.' Quanto ao sentido e à pontuação, é correto afirmar:",
    "options": [
      "Em I, a oração entre vírgulas é restritiva e indica que apenas uma parcela dos vereadores estudou o regimento.",
      "Em II, a ausência de vírgulas torna a oração explicativa e generalizante a todos os vereadores do plenário.",
      "Em I, a oração é explicativa, indicando que todos os vereadores de Meruoca estudaram o regimento; em II, a oração é restritiva, indicando que apenas aqueles vereadores que estudaram o regimento votaram favoravelmente.",
      "As duas construções possuem idêntico valor semântico e gramatical, sendo a vírgula de uso meramente optativo e facultativo."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Clássica questão de bancas sobre orações adjetivas: 1) ADJETIVA EXPLICATIVA (com vírgulas): atribui uma qualidade ou circunstância inerente a todo o grupo (sentido generalizante / totalitário); 2) ADJETIVA RESTRITIVA (sem vírgulas): restringe, recorta e delimita o sentido do substantivo antecedente a apenas uma parte dos indivíduos (apenas aqueles que estudaram, e não a totalidade)."
  },
  {
    "id": 410,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação Adverbial: Causal vs Consecutiva",
    "question": "No período 'A solenidade atraiu tantas pessoas da comunidade QUE O AUDITÓRIO DA CÂMARA FICOU COMPLETAMENTE LOTADO', a oração destacada estabelece com a oração principal uma relação de:",
    "options": [
      "Causa da atração das pessoas.",
      "Consequência (efeito decorrente da grande quantidade de presentes).",
      "Concessão à realização da solenidade.",
      "Finalidade almejada pela Mesa Diretora."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A presença do termo intensificador na oração principal ('tantas pessoas') associado à conjunção subordinativa 'que' ('tanto... que', 'tão... que', 'tal... que') estabelece nítida relação de CONSEQUÊNCIA (efeito gerado pela intensidade da causa anterior). Trata-se de uma Oração Subordinada Adverbial Consecutiva."
  },
  {
    "id": 411,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação Adverbial: Concessiva e Conectivos Concessivos",
    "question": "Assinale a alternativa que contém uma oração subordinada adverbial concessiva:",
    "options": [
      "CONQUANTO HOUVESSE INTENSA PRESSÃO DA BANCADA DE OPOSIÇÃO, o presidente manteve a votação da ordem do dia.",
      "Logo que o sinal sonoro soou, os parlamentares ingressaram no recinto do plenário.",
      "Caso o projeto não seja protocolado até as 17 horas, a matéria será arquivada.",
      "À medida que as semanas transcorriam, a preparação dos candidatos tornava-se mais consistente."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A oração 'CONQUANTO houvesse intensa pressão...' introduz uma ressalva/obstáculo incapaz de anular ou impedir a realização da ação principal, caracterizando Oração Subordinada Adverbial Concessiva. 'Conquanto' é conectivo estritamente concessivo (sinônimo de embora, ainda que, se bem que, posto que). B é temporal; C é condicional; D é proporcional."
  },
  {
    "id": 412,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Conjunções Subordinativas: Polissemia do Conectivo 'Como'",
    "question": "A conjunção 'como' pode assumir diferentes valores sintáticos e semânticos. Analise o período: 'COMO NÃO HAVIA QUÓRUM REGIMENTAL MÍNIMO, a sessão ordinária foi declarada suspensa pelo Presidente'. Nesse contexto, o conectivo 'como' introduz uma oração subordinada adverbial:",
    "options": [
      "Comparativa.",
      "Conformativa.",
      "Causal.",
      "Consecutiva."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Quando o conectivo 'como' inicia o período antes da oração principal, equivalendo semanticamente a 'já que', 'visto que' ou 'porquanto', ele introduz oração subordinada adverbial CAUSAL ('Já que não havia quórum mínimo, a sessão foi suspensa'). Não se trata de comparação nem conformidade."
  },
  {
    "id": 413,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação Adverbial: Oração Condicional e Locuções",
    "question": "Em 'A emenda aditiva será incorporada ao texto final do projeto, DESDE QUE OBTENHA DOIS TERÇOS DOS VOTOS DOS VEREADORES', a oração sublinhada expressa ideia de:",
    "options": [
      "Tempo cronológico simultâneo.",
      "Condição indispensável para a ocorrência da oração principal.",
      "Concessão mitigada com verbo no subjuntivo.",
      "Proporcionalidade mútua de eventos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. A locução 'desde que' seguida de verbo no modo subjuntivo ('obtenha') estabelece uma CONDIÇÃO obrigatória para que a emenda seja incorporada. Trata-se de uma Oração Subordinada Adverbial Condicional (equivalente a 'caso obtenha', 'se obtiver'). Note que 'desde que' com indicativo teria valor temporal, o que não ocorre na frase."
  },
  {
    "id": 414,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação Adverbial: Conformativa",
    "question": "No trecho 'A prestação de contas da Mesa Diretora foi elaborada CONSOANTE DETERMINA A LEI DE RESPONSABILIDADE FISCAL', o termo destacado introduz uma oração subordinada adverbial:",
    "options": [
      "Concessiva.",
      "Conclusiva.",
      "Conformativa.",
      "Consecutiva."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. O conectivo 'consoante' é conjunção subordinativa conformativa por excelência (sinônimo perfeito de 'conforme', 'segundo', 'de acordo com'). Expressa concordância ou conformidade com uma regra ou padrão exterior, classificando-se a oração como Subordinada Adverbial Conformativa."
  },
  {
    "id": 415,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação Adverbial: Proporcional ('À medida que')",
    "question": "A respeito das locuções proporcionais e temporais, assinale a opção gramaticalmente CORRETA:",
    "options": [
      "A locução 'à medida em que' é a forma culta padrão consagrada pela gramática para indicar proporção simultânea.",
      "A locução correta para indicar gradação proporcional é 'à medida que' (ou 'à proporção que'), devendo-se evitar a forma híbrida e incorreta 'à medida em que'.",
      "As locuções 'à medida que' e 'na medida em que' são perfeitamente sinônimas e intercambiáveis com valor causal em qualquer redação oficial.",
      "O conectivo 'ao passo que' expressa obrigatoriamente tempo pontual futuro pretérito."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Pegadinha frequente de concurso: 1) 'À MEDIDA QUE' indica PROPORÇÃO (gradação simultânea); 2) 'NA MEDIDA EM QUE' indica CAUSA (equivalente a visto que, já que); 3) A forma 'à medida em que' é considerada erro gramatical grosseiro (mistura indevida das duas locuções anteriores)."
  },
  {
    "id": 416,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Subordinação Adverbial: Finalidade ('A fim de que')",
    "question": "No trecho 'O Presidente convocou a reunião extraordinária A FIM DE QUE OS PARLAMENTARES DEBATESSEM O PLANO DIRETOR', a oração sublinhada traduz uma circunstância de:",
    "options": [
      "Finalidade (objetivo ou meta visada pela convocação).",
      "Causa pretérita da reunião.",
      "Consequência imediata da fala do Presidente.",
      "Condição preliminar à realização do debate."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A locução conjuntiva 'a fim de que' (grafada separadamente na indicação de objetivo) introduz uma Oração Subordinada Adverbial FINAL, denotando a intenção, propósito ou objetivo que move a ação expressa na oração principal."
  },
  {
    "id": 417,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Período Composto: Orações Reduzidas",
    "question": "Na oração 'TERMINADA A LEITURA DA ATA, o Presidente abriu a fase de pronunciamento dos líderes partidários', a oração destacada é classificada como:",
    "options": [
      "Oração subordinada substantiva apositiva de gerúndio.",
      "Oração coordenada assindética explicativa.",
      "Oração subordinada adverbial temporal reduzida de particípio.",
      "Oração subordinada adjetiva restritiva de infinitivo."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Desenvolvendo a oração: 'Assim que terminou a leitura da ata / Quando terminou a leitura da ata, o Presidente abriu a fase...'. Por não possuir conectivo explícito e ter seu verbo flexionado no particípio ('terminada'), trata-se de uma ORAÇÃO SUBORDINADA ADVERBIAL TEMPORAL REDUZIDA DE PARTICÍPIO."
  },
  {
    "id": 418,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Morfossintaxe: Distinção entre Pronome Relativo e Conjunção Integrante",
    "question": "Observe as duas frases extraídas de pronunciamentos oficiais: I. 'Os assessores informaram QUE AS DILIGÊNCIAS JÁ HAVIAM SIDO REALIZADAS.' II. 'As diligências QUE A COMISSÃO REALIZOU trouxeram novos fatos aos autos.' A palavra 'que' presente em I e II classifica-se, respectivamente, como:",
    "options": [
      "Pronome relativo em I; e Conjunção integrante em II.",
      "Conjunção integrante em I; e Pronome relativo em II.",
      "Conjunção consecutiva em I; e Conjunção explicativa em II.",
      "Pronome indefinido em I; e Partícula expletiva de realce em II."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Em I, o 'que' introduz uma oração subordinada substantiva objetiva direta completando o verbo 'informaram' (pode ser substituído por 'isto': 'informaram isto'); logo, é CONJUNÇÃO INTEGRANTE. Em II, o 'que' retoma o substantivo antecedente 'diligências' ('as quais a comissão realizou'), funcionando como elo de subordinação adjetiva; logo, é PRONOME RELATIVO."
  },
  {
    "id": 419,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Morfossintaxe: Funções da Palavra 'SE' no Período Composto",
    "question": "Assinale a frase em que o vocábulo 'se' atua como CONJUNÇÃO INTEGRANTE introduzindo oração subordinada substantiva:",
    "options": [
      "O servidor perguntou ao Diretor SE HAVERIA EXPEDIENTE REGULAR DURANTE O FERIADO MUNICIPAL.",
      "Se o quórum qualificado não for alcançado, a sessão não poderá deliberar a matéria.",
      "Aprovou-se a resolução administrativa sem nenhum voto contrário na Casa.",
      "Vive-se com muita tranquilidade nos distritos serranos de Meruoca."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Em A, o 'se' introduz oração subordinada substantiva objetiva direta completando o verbo 'perguntou' ('perguntou isto'); logo, atua como CONJUNÇÃO INTEGRANTE. Em B, 'se' é conjunção condicional; em C, 'se' é pronome apassivador ('a resolução foi aprovada'); em D, 'se' é índice de indeterminação do sujeito."
  },
  {
    "id": 420,
    "category": "portugues",
    "day": "w3_d1",
    "discipline": "Língua Portuguesa",
    "topic": "Período Composto: Período Misto (Coordenação e Subordinação)",
    "question": "No período 'O relator concluiu o voto, MAS advertiu que o texto da lei necessitava de aprimoramento', temos:",
    "options": [
      "Um período composto exclusivamente por orações coordenadas assindéticas sem conectivos.",
      "Um período composto por coordenação (oração coordenada sindética adversativa 'mas advertiu') e por subordinação (oração subordinada substantiva objetiva direta 'que o texto da lei necessitava de aprimoramento').",
      "Um período simples constituído de uma única oração absoluta com adjuntos adverbiais compostos.",
      "Um período composto exclusivamente por orações subordinadas adjetivas restritivas correlatas."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Estrutura analítica do período: 1) 'O relator concluiu o voto' = Oração principal / coordenada assindética; 2) 'MAS advertiu' = Oração Coordenada Sindética Adversativa em relação à primeira; 3) 'que o texto da lei necessitava de aprimoramento' = Oração Subordinada Substantiva Objetiva Direta subordinada ao verbo transitivo direto 'advertiu'. Trata-se de um período misto composto por coordenação e subordinação."
  }
,
  {
    "id": 421,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Invalidação: Anulação dos Atos Administrativos",
    "question": "A respeito do instituto da anulação do ato administrativo, com base na jurisprudência sumulada do Supremo Tribunal Federal (Súmulas 346 e 473) e na Lei Federal nº 9.784/1999, é CORRETO afirmar:",
    "options": [
      "A anulação decorre exclusivamente de juízo discricionário de conveniência e oportunidade, produzindo efeitos prospectivos (ex nunc) a partir da decisão que a decreta.",
      "A Administração Pública não pode anular seus próprios atos ilegais quando já tiverem decorrido mais de 30 dias de sua publicação, cabendo apenas a via jurisdicional.",
      "O Poder Judiciário tem competência originária para anular ex officio, sem qualquer provocação da parte interessada, os atos administrativos editados pela Câmara Municipal.",
      "A anulação é a declaração de invalidade de ato administrativo que padece de vício de legalidade, operando efeitos retroativos (ex tunc), podendo ser declarada pela própria Administração (autotutela) ou pelo Poder Judiciário mediante provocação."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A ANULAÇÃO incide sobre atos ilegais (com vício de conformidade jurídica). Por desconstituir uma ilegalidade originária, opera efeitos retroativos (ex tunc), fulminando o ato desde o seu nascimento. Pode ser pronunciada pela própria Administração fundada no princípio da autotutela (Súmulas 346 e 473 do STF) ou pelo Poder Judiciário, desde que provocado (o Judiciário não anula ex officio atos administrativos)."
  },
  {
    "id": 422,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Invalidação: Prazo Decadencial para Anulação",
    "question": "O direito da Administração de anular os atos administrativos de que decorram efeitos favoráveis para os destinatários decai em:",
    "options": [
      "Cinco anos, contados da data em que foram praticados, salvo comprovada má-fé do administrado.",
      "Dois anos da ciência do ato pelo Tribunal de Contas do Estado.",
      "Dez anos impreterivelmente, não comportando qualquer exceção relativa a dolo ou má-fé.",
      "Três anos para atos da administração direta e um ano para os da administração indireta."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Nos termos expressos do art. 54 da Lei Federal nº 9.784/1999 (norma geral de processo administrativo aplicável por simetria): 'O direito da Administração de anular os atos administrativos de que decorram efeitos favoráveis para os destinatários decai em cinco anos, contados da data em que foram praticados, salvo comprovada má-fé'. Havendo má-fé do beneficiário, o ato pode ser anulado a qualquer tempo."
  },
  {
    "id": 423,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Extinção: Revogação dos Atos Administrativos",
    "question": "Quanto ao instituto da revogação do ato administrativo, assinale a afirmativa juridicamente correta:",
    "options": [
      "A revogação pode ser determinada pelo Poder Judiciário no exercício de sua função jurisdicional típica, sempre que considerar o ato inoportuno para a coletividade.",
      "A revogação incide apenas sobre atos vinculados, sendo terminantemente vedada a revogação de atos administrativos discricionários.",
      "A revogação extingue o ato com efeitos retroativos à data de sua emissão originária (efeitos ex tunc), desfazendo todas as relações pretéritas já consolidadas.",
      "A revogação atinge atos plenamente válidos e legais que, por razões supervenientes de conveniência e oportunidade, tornaram-se desinteressantes para a Administração, produzindo efeitos ex nunc (não retroativos)."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A REVOGAÇÃO fundamenta-se no mérito administrativo (conveniência e oportunidade da Administração perante um ato perfeito e válido). Seus efeitos são estritamente prospectivos (ex nunc, não retroagem). É prerrogativa privativa da própria Administração: o Poder Judiciário jamais pode revogar atos administrativos do Poder Executivo ou Legislativo (só pode revogar seus próprios atos em gestão administrativa interna)."
  },
  {
    "id": 424,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Extinção: Atos Irrevogáveis",
    "question": "A doutrina de Direito Administrativo elenca hipóteses em que o ato administrativo NÃO pode ser objeto de revogação. São espécies de atos irrevogáveis, EXCETO:",
    "options": [
      "Atos consumados ou exauridos que já produziram integralmente todos os seus efeitos.",
      "Atos que geraram direito adquirido, nos termos da garantia constitucional.",
      "Atos vinculados, nos quais a Administração não dispõe de margem de escolha de mérito.",
      "Atos discricionários contínuos, como a permissão ou autorização precária de uso de bem público."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A autorização e a permissão de uso de bem público são atos discricionários e precários, sendo a essência deles a possibilidade de REVOGAÇÃO a qualquer momento pelo Poder Público por razões de oportunidade e conveniência. Já os atos consumados, vinculados, enunciativos, que integram procedimento preclusivo e os que geraram direito adquirido são formalmente IRREVOGÁVEIS."
  },
  {
    "id": 425,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Extinção: Cassação do Ato Administrativo",
    "question": "A Câmara Municipal de Meruoca concedeu alvará de funcionamento a uma empresa com a condição expressa de respeitar os limites acústicos e de segurança contra incêndio. Posteriormente, constatou-se que o estabelecimento passou a realizar shows pirotécnicos sem isolamento acústico, violando frontalmente as obrigações impostas. A extinção desse ato administrativo em razão do descumprimento culposo das condições pelo beneficiário configura:",
    "options": [
      "Revogação tácita.",
      "Caducidade normativa.",
      "Cassação.",
      "Contraposição."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A CASSAÇÃO ocorre quando o destinatário do ato descumpre as condições legais ou regulamentares que eram indispensáveis para a continuidade e fruição daquele benefício ou autorização. É uma forma de extinção com caráter sancionatório pelo descumprimento superveniente de deveres pelo particular."
  },
  {
    "id": 426,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Extinção: Caducidade do Ato Administrativo",
    "question": "A retirada do ato administrativo do ordenamento jurídico decorrente da edição de uma nova legislação que tornou inviável ou proibida a manutenção daquela situação anteriormente deferida denomina-se:",
    "options": [
      "Caducidade.",
      "Anulação ficta.",
      "Renúncia expressa.",
      "Desapropriação indireta."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A CADUCIDADE (ou decaimento) consiste na extinção do ato administrativo válido em virtude da superveniência de norma jurídica superior com a qual o ato ou direito tornou-se incompatível (ex.: autorização válida para explorar atividade em determinado local que passa a ser declarada área de proteção ambiental rigorosa por lei nova)."
  },
  {
    "id": 427,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Extinção: Contraposição e Renúncia",
    "question": "Considere as seguintes formas de desfazimento de atos: I. A nomeação de um novo Diretor para um cargo em comissão extingue automaticamente a nomeação do ocupante anterior. II. Um servidor público regularmente investido formula pedido escrito abrindo mão formalmente de sua promoção funcional. As situações I e II exemplificam, respectivamente:",
    "options": [
      "Caducidade em I; e Cassação em II.",
      "Convalidação em I; e Reforma em II.",
      "Anulação em I; e Revogação unilateral em II.",
      "Contraposição (ou derrubada) em I; e Renúncia em II."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A CONTRAPOSIÇÃO (ou derrubada) ocorre quando a edição de um novo ato, fundado em competência diversa, gera efeitos diametralmente opostos aos do ato primitivo, extinguindo-o implicitamente (ex.: a nomeação extingue a investidura anterior). A RENÚNCIA ocorre quando o próprio titular ou beneficiário do ato abre mão voluntariamente do direito ou prerrogativa conferida pelo ato administrativo."
  },
  {
    "id": 428,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Convalidação: Requisitos e Pressupostos de Validade",
    "question": "Nos termos do art. 55 da Lei Federal nº 9.784/1999, 'em decisão na qual se evidencie não acarretarem lesão ao interesse público nem prejuízo a terceiros, os atos que apresentarem defeitos sanáveis poderão ser convalidados pela própria Administração'. A respeito da convalidação, é correto afirmar:",
    "options": [
      "A convalidação opera efeitos prospectivos (ex nunc), passando o ato a ter eficácia válida apenas após a assinatura do termo de saneamento.",
      "Podem ser objeto de convalidação os atos que padecem de desvio de finalidade e os que versam sobre objeto juridicamente ilícito.",
      "A convalidação opera efeitos retroativos (ex tunc), convalidando o ato desde o momento originário de sua prática no mundo jurídico.",
      "Qualquer ato nulo de pleno direito deve ser compulsoriamente convalidado para preservar a despesa pública."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A CONVALIDAÇÃO (ou saneamento) é o ato pelo qual a Administração corrige um defeito sanável de um ato anterior. Ela produz efeitos RETROATIVOS (ex tunc), validando os efeitos desde a data originária em que foi praticado. Para ser convalidado, exige-se que: 1) não haja lesão ao interesse público; 2) não haja prejuízo a terceiros; 3) o defeito seja sanável (apenas Competência e Forma)."
  },
  {
    "id": 429,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Convalidação: Vícios Sanáveis (Regra FO-CO)",
    "question": "Em conformidade com a doutrina consolidada de Direito Administrativo (Hely Lopes Meirelles, Di Pietro e Carvalho Filho), a convalidação de atos administrativos somente é juridicamente admitida quando o vício residir nos elementos:",
    "options": [
      "Motivo e Objeto, desde que haja parecer ministerial favorável.",
      "Finalidade e Motivo, em face do interesse da coletividade.",
      "Competência (desde que não privativa/exclusiva) e Forma (desde que não exigida como essencialidade de validade pela lei).",
      "Objeto e Finalidade, quando houver dolo comprovado de terceiro."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Regra áurea e macete clássico dos concursos ('FO-CO'): somente são sanáveis os vícios de FORMA e COMPETÊNCIA. Mas atenção aos limites: a competência só pode ser convalidada (ratificada) se NÃO for privativa ou exclusiva nem envolver matéria em razão da pessoa ou órgão; a forma só pode ser convalidada se a solenidade omitida não constituir a própria essência e substância de validade legal do ato."
  },
  {
    "id": 430,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Convalidação: Formas de Saneamento (Ratificação, Reforma e Conversão)",
    "question": "A doutrina reconhece diferentes modalidades de aproveitamento e preservação dos atos administrativos. A hipótese em que a Administração retira do ato apenas a sua parte viciada ou ilegal, mantendo incólume a parcela válida e aproveitável do seu conteúdo, denomina-se:",
    "options": [
      "Reforma.",
      "Conversão.",
      "Ratificação.",
      "Revogação cominatória."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Modalidades de saneamento: 1) RATIFICAÇÃO: a autoridade competente supre a falta de competência daquele que praticou originariamente o ato sanável; 2) REFORMA: a Administração suprime a parcela ilegal/viciada do ato, conservando a parte válida; 3) CONVERSÃO: o ato inválido é transformado retroativamente em outra espécie de ato administrativo válido."
  },
  {
    "id": 431,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Classificação: Vinculação vs Discricionariedade",
    "question": "A respeito da distinção entre atos administrativos vinculados e discricionários, assinale a afirmativa correta:",
    "options": [
      "No ato vinculado, a lei confere ao administrador ampla liberdade para decidir se pratica ou não o ato segundo critérios subjetivos de conveniência.",
      "Nos atos discricionários, o administrador atua sem nenhuma vinculação à lei ou à Constituição, possuindo poder absoluto de comando.",
      "No ato vinculado, a lei estabelece de forma objetiva e estrita todos os requisitos e comportamentos a serem adotados pela autoridade, inexistindo margem de liberdade ou opção de mérito.",
      "O ato discricionário não admite controle de legalidade perante o Poder Judiciário sob nenhuma hipótese."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. No ATO VINCULADO (ou regrado), a lei prevê detalhadamente a conduta a ser adotada diante do fato concreto; preenchidos os requisitos, o agente tem o dever de expedir o ato (direito subjetivo do administrado). No ATO DISCRICIONÁRIO, a lei outorga uma margem legítima de escolha de oportunidade e conveniência, sempre dentro dos limites estabelecidos pela própria lei."
  },
  {
    "id": 432,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Controle dos Atos: Limites do Controle Jurisdicional sobre Atos Discricionários",
    "question": "O controle exercido pelo Poder Judiciário sobre os atos administrativos discricionários editados pela Câmara Municipal:",
    "options": [
      "Pode substituir a escolha discricionária de mérito da Mesa Diretora por outra opção que o magistrado julgue mais conveniente ao interesse público.",
      "Restringe-se à verificação da legalidade, legitimidade, veracidade dos motivos declarados e conformidade aos princípios da razoabilidade e proporcionalidade, sendo vedada a substituição do mérito administrativo pelo juiz.",
      "É totalmente proibido pelo princípio da separação dos poderes estabelecido no art. 2º da Constituição Federal.",
      "Abrange exclusivamente a fixação de valores pecuniários das diárias parlamentares."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Princípio basilar do Direito Público: o Poder Judiciário NÃO pode reexaminar o MÉRITO administrativo (oportunidade e conveniência legítimas), sob pena de invasão indevida na esfera administrativa. Contudo, o Judiciário PODE e DEVE controlar a legalidade, o desvio de finalidade, a veracidade dos motivos (Teoria dos Motivos Determinantes) e os excessos que violem a razoabilidade e a proporcionalidade."
  },
  {
    "id": 433,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Teoria das Nulidades: Distinção entre Nulo e Anulável",
    "question": "No regime das nulidades dos atos administrativos no Direito brasileiro, assinale a correta correspondência:",
    "options": [
      "O ato nulo possui defeito leve sanável e pode ser ratificado com efeitos prospectivos.",
      "O ato anulável é aquele que possui vício insanável no motivo ou no objeto, impondo-se a obrigatoriedade de revogação.",
      "O ato nulo apresenta vício grave e insanável, não admitindo convalidação, gerando nulidade de pleno direito; já o ato anulável ostenta vício sanável, podendo ser convalidado pela Administração se presentes os requisitos legais.",
      "Não existe a categoria de atos anuláveis no Direito Administrativo, sendo todos os atos viciados considerados inexistentes."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. A doutrina majoritária e a Lei 9.784/1999 (art. 55) consagram a dicotomia: 1) ATOS NULOS: possuem vícios graves e insanáveis (finalidade ilícita, objeto proibido, motivo falso, competência exclusiva violada), devendo ser anulados de ofício, sem admitir convalidação; 2) ATOS ANULÁVEIS: possuem defeitos sanáveis (competência não exclusiva e forma secundária), permitindo a convalidação pela Administração."
  },
  {
    "id": 434,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Teoria das Nulidades: Ato Inexistente",
    "question": "O ato administrativo que ostenta uma aparência de ato estatal, mas foi praticado por alguém que não possui qualquer investidura pública nem competência legal atribuída (usurpador de função), ou cujo objeto é física ou juridicamente impossível (como a nomeação de pessoa falecida), é qualificado pela doutrina como ato:",
    "options": [
      "Revogável por conveniência.",
      "Inexistente.",
      "Convalidável por ratificação.",
      "Anulável a pedido das partes."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O ATO INEXISTENTE é aquele que apresenta uma aberração jurídica tão extrema que sequer atinge o plano da existência do negócio jurídico (ex.: conduta de usurpador de função pública ou nomeação de pessoa comprovadamente morta). Ele não produz nenhum efeito jurídico, não goza de presunção de legitimidade e não depende de prazo decadencial para anulação."
  },
  {
    "id": 435,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Autotutela: Exigência de Contraditório na Anulação",
    "question": "De acordo com a Súmula Vinculante nº 5 do STF e a jurisprudência pacífica dos Tribunais Superiores, a anulação de ato administrativo pela própria Administração que afete a esfera de direitos individuais de terceiros:",
    "options": [
      "Deve ser sempre precedida de processo administrativo no qual se assegurem o contraditório e a ampla defesa ao administrado interessado.",
      "Prescinde de contraditório ou defesa, tendo em vista a supremacia absoluta do interesse público sobre o privado.",
      "Só pode ser realizada após autorização expressa do Tribunal de Contas da União.",
      "Gera direito automático e incondicional à indenização por lucros cessantes em favor do infrator."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Conforme expressa jurisprudência vinculante e pacificada (STF e STJ): embora a Administração possa anular seus próprios atos ilegais com fulcro no poder de autotutela, quando essa anulação atingir a esfera de direitos ou interesses individuais de terceiros (como a cassação de pensão ou anulação de nomeação de servidor), é INDISPENSÁVEL a prévia instauração de processo administrativo com contraditório e ampla defesa."
  },
  {
    "id": 436,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Invalidação: Proteção aos Terceiros de Boa-Fé",
    "question": "Considere que a nomeação de um determinado servidor público para a Câmara Municipal foi posteriormente anulada pelo fato de ter sido praticada por autoridade incompetente. Os atos praticados por esse servidor perante terceiros de boa-fé enquanto esteve em exercício funcional de fato:",
    "options": [
      "São integralmente nulos e desfeitos, devendo todos os cidadãos atendidos refazer seus requerimentos.",
      "São preservados e mantidos como válidos em relação aos terceiros de boa-fé, com esteio na Teoria da Aparência e no Princípio da Segurança Jurídica.",
      "São convertidos automaticamente em atos judiciais de jurisdição voluntária.",
      "Dependem de convalidação individual expressa pelo Presidente da República."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Aplicação da Teoria do Funcionário de Fato e do princípio da segurança jurídica: ainda que a investidura do servidor seja anulada retroativamente, os atos por ele praticados perante os cidadãos e administrados de boa-fé são PRESERVADOS e reputam-se válidos perante terceiros, evitando prejuízos desproporcionais à coletividade."
  },
  {
    "id": 437,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Convalidação: Vício de Forma Sanável vs Insanável",
    "question": "Em relação ao vício de forma no ato administrativo, é correto asseverar que:",
    "options": [
      "Todo e qualquer vício de forma é considerado insanável pela legislação pátria.",
      "O vício de forma é convalidável quando a lei não houver exigido solenidade específica como condição indispensável à validade e eficácia do ato.",
      "A forma oral é convalidável mediante publicação de extrato após 10 anos da conduta.",
      "A ausência de forma solene prescrita expressamente sob pena de nulidade pode ser suprida pelo decurso de prazo bienal."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O vício de FORMA é sanável (convalidável) desde que a solenidade omitida ou defeituosa não seja exigida pela lei como requisito 'ad solemnitatem' (essência de validade absoluta do ato). Se a forma era meramente secundária ou instrumental, a Administração pode supri-la ou regularizá-la retroativamente."
  },
  {
    "id": 438,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Saneamento dos Atos: Conversão de Atos Administrativos",
    "question": "Quando a Administração Pública aproveita um ato que seria originariamente nulo em determinada categoria, aproveitando seus elementos para qualificá-lo validamente sob outra roupagem jurídica (como aproveitar uma licença nula concedida de forma precária convertendo-a em autorização administrativa), opera-se o fenômeno da:",
    "options": [
      "Conversão do ato administrativo.",
      "Cassação mandatória.",
      "Caducidade de competência.",
      "Revogação tácita."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. A CONVERSÃO é o aproveitamento de um ato inválido numa categoria jurídica que passa a ser recepcionado como ato válido sob outra espécie ou figura legal compatível com a vontade estatal e os elementos fáticos existentes."
  },
  {
    "id": 439,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Extinção: Diferenciação entre Cassação e Revogação",
    "question": "A diferença fundamental entre a Revogação e a Cassação reside no fato de que:",
    "options": [
      "A revogação decorre de ilegalidade original; a cassação decorre de mérito discricionário do administrado.",
      "A revogação decorre de reavaliação de oportunidade e conveniência pela Administração; a cassação é ato cominatória/sancionatório motivado pelo descumprimento superveniente de deveres pelo particular.",
      "A revogação produz efeitos ex tunc; a cassação produz efeitos exclusivamente moratórios.",
      "A cassação é competência privativa do Poder Judiciário; a revogação cabe apenas ao Tribunal de Contas."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Na REVOGAÇÃO, o particular não praticou nenhuma falta nem cometeu nenhuma irregularidade: a Administração simplesmente não deseja mais manter o ato por conveniência pública. Na CASSAÇÃO, o desfazimento do ato é imputado exclusivamente à culpa do particular, que descumpriu as condições legais pré-estabelecidas para desfrutar daquele ato."
  },
  {
    "id": 440,
    "category": "administrativo",
    "day": "w3_d2",
    "discipline": "D. Administrativo",
    "topic": "Invalidação: Desvio de Poder / Desvio de Finalidade",
    "question": "O desvio de finalidade (ou desvio de poder) é vício que atinge o elemento finalidade do ato administrativo. Uma vez comprovado o desvio de finalidade em um ato administrativo praticado pelo Presidente de uma Câmara Municipal, o ato deve ser:",
    "options": [
      "Convalidado por ato do plenário legislativo em 30 dias.",
      "Anulado, por se tratar de vício grave de legalidade insanável no ordenamento jurídico.",
      "Convertido em ato de cortesia política sem valor normativo.",
      "Revogado com efeitos prospectivos para salvaguardar as finanças públicas."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. O DESVIO DE FINALIDADE acarreta a NULIDADE ABSOLUTA do ato administrativo (art. 2º, 'e', da Lei nº 4.717/1965 — Lei da Ação Popular). O vício de finalidade é radicalmente INSANÁVEL, impondo-se a sua ANULAÇÃO retroativa (ex tunc), jamais cabendo convalidação ou mera revogação."
  },
  {
    "id": 441,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Conversão de Comprimento (km para metros)",
    "question": "Para uma obra de reforma da fiação da Câmara de Meruoca, foram adquiridos 3 rolos de cabeamento de rede com 0,45 km de comprimento cada um. Se na primeira etapa da obra foram utilizados 820 metros de cabo, quantos metros de cabeamento ainda restam?",
    "options": [
      "430 metros.",
      "1.350 metros.",
      "530 metros.",
      "680 metros."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Passo a passo: 1) Cada rolo tem 0,45 km = 0,45 × 1.000 = 450 metros. 2) O total adquirido em 3 rolos foi: 3 × 450 m = 1.350 metros. 3) Foram utilizados 820 metros. 4) Restante: 1.350 - 820 = 530 metros."
  },
  {
    "id": 442,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Unidades de Superfície e Hectares",
    "question": "O Município de Meruoca desapropriou um terreno plano de 2,4 hectares para a construção de um complexo de apoio administrativo. Sabendo que 1 hectare (ha) equivale a 10.000 m² e que 35% dessa área total será destinada ao estacionamento público, qual será a área destinada ao estacionamento?",
    "options": [
      "6.800 m².",
      "7.200 m².",
      "8.400 m².",
      "9.600 m²."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Passo a passo: 1) Área total do terreno em metros quadrados: 2,4 ha = 2,4 × 10.000 m² = 24.000 m². 2) Área do estacionamento: 35% de 24.000 m² = 0,35 × 24.000 = 8.400 m²."
  },
  {
    "id": 443,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Volume e Capacidade (m³ e Litros)",
    "question": "O reservatório de água do edifício da Câmara Municipal possui formato de paralelepípedo retângulo com as seguintes dimensões internas: 4 metros de comprimento, 2,5 metros de largura e 1,8 metro de altura. Sabendo que 1 m³ de volume comporta exatamente 1.000 litros de água, qual é a capacidade máxima total desse reservatório em litros?",
    "options": [
      "14.500 litros.",
      "20.000 litros.",
      "16.200 litros.",
      "18.000 litros."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Passo a passo: 1) Volume em m³ = Comprimento × Largura × Altura = 4 × 2,5 × 1,8 = 10 × 1,8 = 18 m³. 2) Conversão para litros: 1 m³ = 1.000 litros. Portanto: 18 × 1.000 = 18.000 litros."
  },
  {
    "id": 444,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Massa (kg e Toneladas)",
    "question": "Em uma campanha de reciclagem de papéis de arquivos obsoletos da Câmara de Meruoca, foram arrecadados 2,8 toneladas de papel. Esse material foi dividido e acondicionado igualmente em sacas de 35 kg cada. Quantas sacas completas foram necessárias para embalar todo o papel reciclado?",
    "options": [
      "75 sacas.",
      "90 sacas.",
      "85 sacas.",
      "80 sacas."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Passo a passo: 1) Sabendo que 1 tonelada (t) = 1.000 kg, temos: 2,8 t = 2,8 × 1.000 = 2.800 kg de papel. 2) Dividindo o total pelo peso de cada saca: 2.800 / 35. 2.800 ÷ 35 = 80 sacas completas."
  },
  {
    "id": 445,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Unidades de Tempo e Conversões Decimais",
    "question": "Uma sessão plenária extraordinária da Câmara iniciou-se às 09h 15min e encerrou-se exatamente às 12h 03min. Qual foi a duração total dessa sessão plenária expressa em minutos?",
    "options": [
      "172 minutos.",
      "158 minutos.",
      "168 minutos.",
      "148 minutos."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Passo a passo: 1) Intervalo de 09h 15min até 12h 00min: faltam 45 minutos para 10h + 2 horas completas (10h às 12h) = 2h 45min. 2) De 12h 00min até 12h 03min: mais 3 minutos. Total = 2 horas e 48 minutos. 3) Convertendo 2h 48min para minutos: (2 × 60) + 48 = 120 + 48 = 168 minutos."
  },
  {
    "id": 446,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema Monetário Brasileiro: Troco e Cédulas",
    "question": "Um servidor comprou materiais de expediente para o setor legislativo totalizando R$ 346,80. Para efetuar o pagamento, entregou no caixa 4 cédulas de R$ 100,00. O troco recebido pelo servidor foi de:",
    "options": [
      "R$ 54,20.",
      "R$ 55,20.",
      "R$ 52,20.",
      "R$ 53,20."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Passo a passo: 1) Valor entregue: 4 × R$ 100,00 = R$ 400,00. 2) Valor da compra: R$ 346,80. 3) Troco = 400,00 - 346,80 = R$ 53,20."
  },
  {
    "id": 447,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema Monetário: Juros Simples e Parcelamento",
    "question": "Um equipamento eletrônico de som para o plenário custa R$ 4.000,00 à vista. A loja oferece o plano de pagamento a prazo em 4 parcelas mensais iguais com taxa de juros simples de 2,5% ao mês sobre o valor inicial à vista. Qual será o valor de cada uma das 4 parcelas?",
    "options": [
      "R$ 1.050,00.",
      "R$ 1.200,00.",
      "R$ 1.150,00.",
      "R$ 1.100,00."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Passo a passo: 1) Juros simples: J = C × i × t. Capital (C) = 4.000; taxa (i) = 2,5% ao mês = 0,025; tempo (t) = 4 meses. 2) J = 4.000 × 0,025 × 4 = 4.000 × 0,10 = R$ 400,00 de juros totais. 3) Montante a pagar = C + J = 4.000 + 400 = R$ 4.400,00. 4) Valor de cada uma das 4 parcelas iguais: 4.400 / 4 = R$ 1.100,00."
  },
  {
    "id": 448,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema Monetário: Descontos e Orçamento",
    "question": "Em uma licitação para compra de papel A4, a empresa vencedora ofereceu um lote de 50 caixas no valor total de R$ 1.800,00. Caso a Câmara efetue o pagamento em parcela única até 5 dias úteis, a empresa concede um desconto promocional de 8%. Qual será o valor final a ser pago com o desconto aplicado?",
    "options": [
      "R$ 1.680,00.",
      "R$ 1.640,00.",
      "R$ 1.656,00.",
      "R$ 1.624,00."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Passo a passo: 1) Valor do desconto de 8% sobre R$ 1.800,00: 0,08 × 1.800 = R$ 144,00. 2) Valor final com desconto: 1.800,00 - 144,00 = R$ 1.656,00 (ou diretamente: 1.800 × 0,92 = R$ 1.656,00)."
  },
  {
    "id": 449,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Capacidade em Mililitros (ml) e Litros",
    "question": "Para uma audiência pública na Câmara foram compradas garrafas de água mineral com capacidade de 350 ml cada. Se no total foram servidos 42 litros de água durante a audiência, quantas garrafas completas de 350 ml foram consumidas?",
    "options": [
      "110 garrafas.",
      "120 garrafas.",
      "130 garrafas.",
      "140 garrafas."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Passo a passo: 1) Converter litros para mililitros: 1 L = 1.000 ml, logo 42 litros = 42 × 1.000 = 42.000 ml. 2) Dividir pelo volume de cada garrafa: 42.000 ÷ 350 = 4.200 ÷ 35 = 120 garrafas."
  },
  {
    "id": 450,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Conversão de Área (m² para cm² e ladrilhos)",
    "question": "O piso de uma sala de reuniões de 24 m² será totalmente revestido com placas cerâmicas quadradas de 40 cm de lado. Desconsiderando perdas e rejuntes, quantas placas cerâmicas completas serão necessárias para cobrir todo o piso dessa sala?",
    "options": [
      "160 placas.",
      "120 placas.",
      "150 placas.",
      "180 placas."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Passo a passo: 1) Área de cada placa quadrada: 40 cm = 0,4 m. Área = 0,4 m × 0,4 m = 0,16 m² (ou 40 × 40 = 1.600 cm²). 2) Área total da sala: 24 m² = 24 × 10.000 = 240.000 cm². 3) Quantidade de placas = 24 / 0,16 = 2.400 / 16 = 150 placas."
  },
  {
    "id": 451,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Perímetro e Cálculo de Custo Linear",
    "question": "Um terreno retangular pertencente ao patrimônio da Câmara de Meruoca possui 45 metros de comprimento e 25 metros de largura. A administração pretende cercar todo o seu contorno com grade de proteção metálica. Se o metro linear da grade instalada custa R$ 85,00, qual será o custo total para cercar o perímetro desse terreno?",
    "options": [
      "R$ 9.650,00.",
      "R$ 10.850,00.",
      "R$ 12.450,00.",
      "R$ 11.900,00."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Passo a passo: 1) O perímetro de um retângulo é 2 × (comprimento + largura) = 2 × (45 + 25) = 2 × 70 = 140 metros. 2) Custo total = 140 m × R$ 85,00/m = R$ 11.900,00."
  },
  {
    "id": 452,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema Monetário: Diárias e Operações Fundamentais",
    "question": "Dois servidores da Câmara de Meruoca viajaram em missão oficial para Fortaleza para participar de treinamento sobre o Processo Legislativo. Cada servidor tem direito a uma diária de R$ 220,00 por dia completo e R$ 110,00 por meia diária. Sabendo que a missão durou 3 dias completos e 1 meia diária para cada um dos dois servidores, qual foi o valor total pago em diárias pela Câmara?",
    "options": [
      "R$ 1.620,00.",
      "R$ 770,00.",
      "R$ 1.480,00.",
      "R$ 1.540,00."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Passo a passo: 1) Diárias por servidor: 3 dias completos = 3 × 220 = R$ 660,00; mais 1 meia diária = R$ 110,00. Total por servidor = 660 + 110 = R$ 770,00. 2) Como foram 2 servidores: 2 × R$ 770,00 = R$ 1.540,00."
  },
  {
    "id": 453,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Escalas e Conversão de Unidades",
    "question": "Em uma planta arquitetônica da nova sede da Câmara desenhada na escala 1 : 250, a extensão da fachada principal mede 12 cm no papel. Qual é a medida real dessa fachada em metros?",
    "options": [
      "25 metros.",
      "30 metros.",
      "35 metros.",
      "300 metros."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Passo a passo: 1) Na escala 1 : 250, cada 1 cm no mapa representa 250 cm na realidade. 2) Medida real em cm = 12 × 250 = 3.000 cm. 3) Convertendo centímetros para metros: 1 metro = 100 cm, logo 3.000 cm = 3.000 ÷ 100 = 30 metros."
  },
  {
    "id": 454,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Capacidade e Custo de Combustível",
    "question": "O veículo oficial da Câmara Municipal tem rendimento médio de 12,5 km por litro de gasolina. Em uma semana de vistorias parlamentares na zona rural de Meruoca, o veículo percorreu 450 km. Se o litro da gasolina custa R$ 5,80, qual foi o gasto total com combustível nessa semana?",
    "options": [
      "R$ 208,80.",
      "R$ 198,60.",
      "R$ 215,40.",
      "R$ 226,20."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Passo a passo: 1) Quantidade de litros consumidos = Distância / Rendimento = 450 ÷ 12,5 = 36 litros. 2) Custo total = 36 litros × R$ 5,80/litro = R$ 208,80."
  },
  {
    "id": 455,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Horas Decimais para Minutos",
    "question": "Um servidor levou 3,4 horas para redigir a ata detalhada de uma sessão solene. Essa duração de 3,4 horas equivale exatamente a:",
    "options": [
      "3 horas e 40 minutos.",
      "3 horas e 24 minutos.",
      "3 horas e 15 minutos.",
      "3 horas e 4 minutos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Pegadinha clássica em concursos: 3,4 horas NÃO é 3 horas e 40 minutos! Temos 3 horas inteiras + 0,4 de uma hora. Como 1 hora tem 60 minutos, 0,4 hora = 0,4 × 60 minutos = 24 minutos. Portanto, 3,4 horas equivale exatamente a 3 horas e 24 minutos."
  },
  {
    "id": 456,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Massa (Gramas e Miligramas)",
    "question": "Para o tratamento de desinfecção dos reservatórios do prédio do Legislativo, a vigilância sanitária recomenda utilizar 2,5 mg de cloro ativo para cada 1 litro de água. Para desinfetar uma caixa d'água contendo 8.000 litros de água, quantos gramas de cloro ativo serão necessários?",
    "options": [
      "200 gramas.",
      "20 gramas.",
      "2 gramas.",
      "2.000 gramas."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Passo a passo: 1) Quantidade total de cloro em miligramas: 8.000 litros × 2,5 mg/L = 20.000 mg. 2) Conversão de mg para gramas: 1 g = 1.000 mg. Logo, 20.000 mg = 20.000 ÷ 1.000 = 20 gramas."
  },
  {
    "id": 457,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema Monetário: Percentuais sobre Remuneração",
    "question": "O salário inicial de um Técnico Legislativo de Meruoca é fixado no edital em R$ 1.800,00. Após a conclusão do estágio probatório e cumprimento dos critérios do Plano de Cargos e Carreiras, o servidor receberá uma gratificação de desempenho de 22% sobre seu vencimento básico, acrescida de um adicional de qualificação de 15% (também incidente sobre o vencimento básico). Com esses dois benefícios, qual passará a ser a remuneração bruta total desse servidor?",
    "options": [
      "R$ 2.466,00.",
      "R$ 2.412,00.",
      "R$ 2.380,00.",
      "R$ 2.520,00."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Passo a passo: 1) Soma dos percentuais de acréscimo: 22% + 15% = 37% sobre o vencimento básico. 2) Valor total dos adicionais: 0,37 × 1.800 = R$ 666,00. 3) Remuneração bruta = Vencimento básico + adicionais = 1.800 + 666 = R$ 2.466,00."
  },
  {
    "id": 458,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Superfície, Capacidade e Rendimento",
    "question": "O plenário da Câmara possui 4 paredes que precisam ser pintadas. Duas paredes medem 12 m por 3,5 m cada, e as outras duas medem 8 m por 3,5 m cada. O pintor informou que cada lata de tinta de 3,6 litros rende 40 m² de pintura com duas demãos. Quantas latas de tinta de 3,6 L, no mínimo, a administração precisará comprar para pintar todo o plenário?",
    "options": [
      "4 latas.",
      "3 latas.",
      "5 latas.",
      "6 latas."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Passo a passo: 1) Área das duas primeiras paredes: 2 × (12 × 3,5) = 2 × 42 = 84 m². 2) Área das outras duas paredes: 2 × (8 × 3,5) = 2 × 28 = 56 m². 3) Área total = 84 + 56 = 140 m². 4) Rendimento por lata = 40 m². 5) Número de latas = 140 ÷ 40 = 3,5 latas. Como a compra deve ser de latas inteiras, serão necessárias no mínimo 4 latas completas."
  },
  {
    "id": 459,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema Monetário: Comparação À Vista vs A Prazo",
    "question": "Para a aquisição de 10 novos computadores, a Câmara recebeu duas propostas: Proposta I: Pagamento à vista com 12% de desconto sobre o valor de tabela de R$ 35.000,00. Proposta II: Pagamento em duas parcelas de R$ 16.000,00 (uma entrada e outra após 30 dias). A economia obtida pela Câmara ao optar pela Proposta I em relação à Proposta II é de:",
    "options": [
      "R$ 1.200,00.",
      "R$ 1.500,00.",
      "R$ 1.800,00.",
      "R$ 2.200,00."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Passo a passo: 1) Proposta I (à vista): Desconto de 12% em R$ 35.000 = 0,12 × 35.000 = R$ 4.200,00. Valor pago = 35.000 - 4.200 = R$ 30.800,00. 2) Proposta II: 2 parcelas de R$ 16.000 = R$ 32.000,00. 3) Diferença (economia): 32.000,00 - 30.800,00 = R$ 1.200,00."
  },
  {
    "id": 460,
    "category": "matematica",
    "day": "w3_d2",
    "discipline": "Matemática / RLM",
    "topic": "Sistema de Medidas: Vazão, Volume e Tempo",
    "question": "Uma torneira com defeito em um dos banheiros da Câmara fica gotejando e perde 15 ml de água por minuto. Se o defeito demorou 8 horas para ser reparado pela equipe de manutenção, qual foi a quantidade total de água desperdiçada nesse período?",
    "options": [
      "7,2 litros.",
      "8,5 litros.",
      "6,4 litros.",
      "9,0 litros."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Passo a passo: 1) Tempo decorrido em minutos: 8 horas = 8 × 60 = 480 minutos. 2) Quantidade de água desperdiçada em ml: 480 minutos × 15 ml/minuto = 7.200 ml. 3) Convertendo ml para litros: 1 L = 1.000 ml. Logo, 7.200 ÷ 1.000 = 7,2 litros."
  }

,
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
      "Internet é a rede mundial pública; Intranet é a rede privada interna de uma organização com acesso restrito; Extranet é a extensão controlada da Intranet para parceiros externos via login.",
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
,
{
  "id": 491,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Contratacao Direta: Dispensa vs Inexigibilidade (Arts. 74-75)",
  "question": "Quanto à contratação direta na Lei nº 14.133/2021, a diferença essencial entre dispensa e inexigibilidade de licitação é que:",
  "options": [
    "Na dispensa a competição é viável, mas a lei autoriza não licitar (rol taxativo); na inexigibilidade a competição é inviável (rol exemplificativo).",
    "Na dispensa a competição é inviável e na inexigibilidade a competição é viável, invertendo a lógica da licitação.",
    "Ambas dispensam qualquer processo formal, bastando ordem verbal do prefeito para contratar.",
    "A dispensa exige sempre licitação prévia e a inexigibilidade é vedada aos municípios."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Arts. 74 e 75 da Lei 14.133/21. Dispensa (Art. 75): competir seria possível, mas a lei DISPENSA por conveniência (rol TAXATIVO, ex: pequeno valor, emergência). Inexigibilidade (Art. 74): competir é INVIÁVEL (fornecedor exclusivo, artista consagrado) — rol EXEMPLIFICATIVO. Pegadinha INBRASP nº 1 do tema."
},
{
  "id": 492,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Dispensa por Valor (Art. 75, I e II)",
  "question": "A dispensa de licitação em razão do pequeno valor (Art. 75, I e II da Lei nº 14.133/2021, valores atualizados por decreto federal) aplica-se a:",
  "options": [
    "Qualquer compra milionária, desde que o prefeito declare urgência verbal.",
    "Obras e serviços de engenharia até o limite superior e outros serviços e compras até o limite inferior, vedado o fracionamento para enquadrar a despesa.",
    "Obras acima de R$ 10 milhões e serviços contínuos de qualquer valor.",
    "Apenas à compra de café e material de limpeza, independentemente do valor."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 75, I (obras/engenharia/manutenção de veículos: teto maior) e II (outros serviços e compras: teto menor), atualizados anualmente por decreto. É VEDADO o fracionamento de despesa para fugir da licitação (soma-se o gasto anual do objeto). Números exatos mudam por decreto; a banca cobra a lógica dos dois patamares."
},
{
  "id": 493,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Inexigibilidade: Hipoteses (Art. 74)",
  "question": "São hipóteses de inexigibilidade de licitação previstas no Art. 74 da Lei nº 14.133/2021:",
  "options": [
    "Compra de bens comuns de prateleira e contratação de obra padrão por menor preço.",
    "Serviços de limpeza com dezenas de empresas aptas e fornecimento de papel A4.",
    "Fornecedor exclusivo, profissional do setor artístico consagrado e serviços técnicos especializados de natureza predominantemente intelectual.",
    "Locação de imóvel qualquer sem avaliação prévia e sem justificativa."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 74, I a V da Lei 14.133/21: I - fornecedor exclusivo (atestado); II - artista consagrado pela crítica ou público; III - serviços técnicos intelectuais (estudos, pareceres, projetos) com notória especialização; IV - objetos que devam ser contratados por credenciamento; V - aquisição/locação de imóvel com características específicas (com avaliação e justificativa). Bens comuns = pregão, jamais inexigibilidade."
},
{
  "id": 494,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Processo da Contratacao Direta (Art. 72)",
  "question": "O processo de contratação direta (dispensa ou inexigibilidade) exige, nos termos do Art. 72 da Lei nº 14.133/2021:",
  "options": [
    "Apenas um telefonema para a empresa amiga e pagamento adiantado sem recibo.",
    "Somente a nota de empenho, dispensados parecer, pesquisa de preços e publicidade.",
    "Autorização verbal do vereador presidente, sem qualquer documento escrito.",
    "Documento de formalização da demanda, estimativa de despesa com pesquisa de preços, parecer jurídico e técnico, demonstração de compatibilidade orçamentária e autorização da autoridade competente, tudo divulgado no PNCP."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 72 da Lei 14.133/21. Contratação direta NÃO é contratação informal: exige DFD, ETP quando cabível, TR, pesquisa de preços (Art. 23), parecer jurídico, razão da escolha do contratado, justificativa do preço e autorização — com divulgação no PNCP. Pegadinha: 'direta' dispensa a COMPETIÇÃO, não o PROCESSO."
},
{
  "id": 495,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Dispensa Emergencial (Art. 75, VIII)",
  "question": "A dispensa emergencial do Art. 75, VIII da Lei nº 14.133/2021 (emergência ou calamidade pública) caracteriza-se por:",
  "options": [
    "Ser cabível apenas para os bens e serviços necessários ao atendimento da emergência, com contratação pelo prazo máximo de 1 ano, vedada a prorrogação e a recontratação da mesma empresa no período seguinte.",
    "Permitir qualquer contratação pelo prazo de 10 anos, inclusive obras não relacionadas à emergência.",
    "Dispensar a comprovação da emergência, bastando a alegação genérica de pressa.",
    "Autorizar a contratação de empresa punida com inidoneidade sem qualquer restrição."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 75, VIII da Lei 14.133/21. Emergência real (não fabricada pela desídia do gestor): só o necessário, contrato de até 1 ANO, sem prorrogação, vedada recontratação da mesma empresa. A emergência deve ser demonstrada; a culpa do gestor pela falta de planejamento não gera emergência lícita (entendimento do TCU)."
},
{
  "id": 496,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Formalizacao do Contrato (Arts. 89-95)",
  "question": "Sobre a formalização dos contratos administrativos na Lei nº 14.133/2021, é correto afirmar que:",
  "options": [
    "Todo contrato pode ser verbal, inclusive obras de grande vulto, sem qualquer registro.",
    "A regra é o termo de contrato escrito, admitindo-se instrumento hábil substituto (carta-contrato, nota de empenho, autorização de compra) nas compras com entrega imediata e integral sem obrigações futuras.",
    "É vedado qualquer substituto do termo de contrato, mesmo para compras à vista de pequeno valor.",
    "O contrato verbal é a regra e o escrito é exceção para valores acima de R$ 1 bilhão."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Arts. 89 a 95 da Lei 14.133/21. Regra: termo escrito. Exceção: instrumento hábil (empenho, carta-contrato) em compras de entrega imediata/integral sem obrigação futura (ex: material de expediente à vista) e nos limites da dispensa por valor. Contrato verbal só em pequenas compras de pronto pagamento (Art. 95, §2º) e mesmo assim com justificativa."
},
{
  "id": 497,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Clausulas Necessarias (Art. 92)",
  "question": "O Art. 92 da Lei nº 14.133/2021 estabelece as cláusulas necessárias do contrato administrativo. Entre elas NÃO se inclui:",
  "options": [
    "O objeto e seus elementos característicos, com quantitativos e especificações.",
    "O preço, as condições de pagamento, os critérios de reajuste e a dotação orçamentária.",
    "A preferência pessoal do gestor pelo contratado e a dispensa de definir o objeto com precisão.",
    "Os prazos de execução e vigência, o modelo de gestão, os casos de extinção e as penalidades."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 92 da Lei 14.133/21 (rol com ~20 incisos): objeto detalhado, preço e pagamento, reajuste, prazos, crédito orçamentário, garantias, direitos/deveres, fiscalização, penalidades, extinção, foro. A opção A descreve vícios (pessoalidade e objeto impreciso), jamais cláusula válida — é a clássica questão de 'EXCETO' da banca."
},
{
  "id": 498,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Vigencia dos Contratos Continuos (Arts. 105-107)",
  "question": "Quanto à duração dos contratos de serviços e fornecimentos contínuos na Lei nº 14.133/2021, assinale a opção correta:",
  "options": [
    "São sempre de 30 dias improrrogáveis, devendo licitar todo mês.",
    "Podem durar 99 anos desde o início, sem qualquer limite ou justificativa.",
    "A prorrogação é automática e independe de previsão no edital ou de vantagem para a Administração.",
    "Podem ter vigência inicial de até 5 anos, prorrogável sucessivamente até o máximo de 10 anos, desde que atestada a vantajosidade e prevista a prorrogação no edital."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Arts. 105 a 107 da Lei 14.133/21. Contratos por escopo seguem o cronograma; contínuos (limpeza, vigilância): até 5 anos + prorrogações até 10. Exceções com prazos próprios: aluguel de equipamentos/programas e operação continuada de sistemas estruturantes. Prorrogação exige previsão, interesse público e preço vantajoso."
},
{
  "id": 499,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Alteracao Unilateral: Limites (Art. 125)",
  "question": "Nas alterações unilaterais do contrato pela Administração (Art. 125 da Lei nº 14.133/2021), os acréscimos ou supressões ficam limitados a:",
  "options": [
    "25% do valor inicial atualizado, em regra, e 50% no caso particular de reforma de edifício ou de equipamento.",
    "100% em qualquer caso, sem limite, a critério do fiscal do contrato.",
    "10% para acréscimos e 90% para supressões, sem distinção de objeto.",
    "Não há limite algum, podendo o contrato dobrar de valor por decisão unilateral."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 125 da Lei 14.133/21 (mesma lógica da Lei 8.666/93, Art. 65). Regra: até 25% para mais ou para menos. Exceção: até 50% em reforma de edifício ou equipamento. Supressões ACIMA do limite dependem de acordo (consensual). Ultrapassar unilateralmente gera nulidade do excesso."
},
{
  "id": 500,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Reajuste, Repactuacao e Reequilibrio (Arts. 124-136)",
  "question": "Sobre a manutenção do equilíbrio econômico-financeiro do contrato (Arts. 124 a 136 da Lei nº 14.133/2021), é correto afirmar que:",
  "options": [
    "As três figuras são sinônimas e podem ser usadas livremente a qualquer tempo, sem previsão contratual.",
    "O reajuste repõe a inflação por índice previsto (após 1 ano); a repactuação é própria de serviços com mão de obra dedicada (planilha de custos); o reequilíbrio cobre fato imprevisível ou de consequências incalculáveis.",
    "O reequilíbrio é vedado e o contratado assume todo prejuízo, mesmo em caso fortuito.",
    "O reajuste dispensa interregno mínimo e pode ser mensal por decisão do contratado."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Arts. 124-136 da Lei 14.133/21. Reajuste em sentido estrito: índice (IPCA etc.), após 12 meses do orçamento. Repactuação: demonstração analítica de custos (terceirização com dedicação exclusiva). Revisão/reequilíbrio: álea extraordinária (fato do príncipe, caso fortuito, força maior). Mnemônico: índice = reajuste; planilha = repactuação; imprevisível = reequilíbrio."
},
{
  "id": 501,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Fiscalizacao e Recebimento (Arts. 117 e 140)",
  "question": "Na execução contratual (Arts. 117 e 140 da Lei nº 14.133/2021), o recebimento do objeto ocorre em duas etapas:",
  "options": [
    "Verbal e definitivo, sem qualquer verificação, bastando a palavra do contratado.",
    "Somente definitivo após 10 anos do término da obra, sem etapa provisória.",
    "Provisório (verificação sumária pelo fiscal, em até 15 dias do comunicado, salvo prazo diverso) e definitivo (verificação da qualidade e quantidade, por servidor ou comissão designada).",
    "Automático na assinatura do contrato, antes mesmo da execução do objeto."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 140 da Lei 14.133/21. Recebimento provisório: conferência rápida (fiscal). Definitivo: aceite após testes/verificações (servidor ou comissão). Em obras/serviços de engenharia o definitivo exige comissão. O recebimento definitivo NÃO exclui a responsabilidade civil (solidez e segurança — Art. 140, §6º c/c Código Civil)."
},
{
  "id": 502,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Pagamento e Ordem Cronologica (Art. 141)",
  "question": "O Art. 141 da Lei nº 14.133/2021 determina que os pagamentos observem a ordem cronológica de exigibilidade por fonte de recursos. A quebra dessa ordem:",
  "options": [
    "É livre e pode ocorrer por simpatia do tesoureiro, sem qualquer justificativa.",
    "É obrigatória todo mês, pagando-se primeiro as empresas de amigos do gestor.",
    "Dispensa qualquer publicidade, podendo ser decidida oralmente.",
    "Somente é admitida mediante justificativa da autoridade competente, devidamente publicada, em casos de grave perturbação da ordem, emergência ou calamidade."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 141 da Lei 14.133/21 (regra da fila de pagamentos por fonte). Quebra só com justificativa formal e pública: risco de paralisação de serviço essencial, emergência, calamidade. Pagamento fora da ordem sem motivo configura improbidade/irregularidade grave apontada pelos Tribunais de Contas."
},
{
  "id": 503,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Garantias Contratuais (Arts. 96-102)",
  "question": "Sobre as garantias de execução contratual (Arts. 96 a 102 da Lei nº 14.133/2021), assinale a opção correta:",
  "options": [
    "O edital pode exigir garantia nas modalidades caução em dinheiro, seguro-garantia ou fiança bancária, limitada a 5% do valor inicial (até 10% mediante justificativa em obras de grande vulto).",
    "A garantia é sempre de 50% do contrato e só admite depósito em ouro.",
    "O contratado escolhe livremente não apresentar garantia, mesmo quando exigida no edital.",
    "O seguro-garantia cobre apenas o primeiro dia de obra e depois se extingue sozinho."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Arts. 96-102 da Lei 14.133/21. Modalidades à escolha do contratado: caução (dinheiro/títulos), seguro-garantia, fiança bancária (e título de capitalização foi incluído). Teto: 5%, até 10% com justificativa técnica em obras/serviços de grande vulto. Há ainda o seguro-garantia com cláusula de retomada (step in) em grandes obras."
},
{
  "id": 504,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Matriz de Riscos (Art. 22)",
  "question": "A matriz de riscos prevista no Art. 22 da Lei nº 14.133/2021 consiste em:",
  "options": [
    "Documento secreto que esconde os riscos da obra do Tribunal de Contas.",
    "Cláusula contratual que define a repartição objetiva de riscos entre contratante e contratado (ex: variação cambial, atraso de licenças), vedada a alocação de risco de caso fortuito ao contratado sem contrapartida.",
    "Planilha de apostas sobre qual empresa vai falir primeiro durante a execução.",
    "Lista de servidores que serão punidos se a obra atrasar, independentemente de culpa."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 22 da Lei 14.133/21. A matriz distribui riscos previsíveis (quem arca com cada evento) e integra o cálculo do equilíbrio econômico-financeiro: risco alocado ao contratado já está no preço (sem reequilíbrio por ele). Obrigatória em obras e serviços de engenharia de grande vulto."
},
{
  "id": 505,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Infracoes Administrativas (Art. 155)",
  "question": "O Art. 155 da Lei nº 14.133/2021 tipifica as infrações do licitante/contratado. Configura infração administrativa, entre outras condutas:",
  "options": [
    "Entregar o objeto antes do prazo com qualidade superior à exigida.",
    "Apresentar proposta com desconto maior que o dos concorrentes.",
    "Dar causa à inexecução parcial ou total do contrato, apresentar documentação falsa, fraudar a licitação e comportar-se de modo inidôneo.",
    "Comparecer pontualmente à sessão e assinar a ata de registro de preços."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 155, I a XII da Lei 14.133/21: inexecução parcial/total, retardamento, documentação falsa, fraude, inidoneidade, conluio. Cumprir bem e pontualmente jamais é infração — as demais opções descrevem conduta exemplar ou competitiva lícita."
},
{
  "id": 506,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Penalidades: Especies e Prazos (Art. 156)",
  "question": "As sanções aplicáveis ao responsável por infração (Art. 156 da Lei nº 14.133/2021) e seus alcances temporais são:",
  "options": [
    "Prisão perpétua do sócio e confisco de todos os bens da família.",
    "Apenas advertência verbal, sem qualquer outra consequência em qualquer caso.",
    "Multa única de R$ 1,00 simbólica para todas as infrações graves.",
    "Advertência, multa, impedimento de licitar e contratar (até 3 anos, no ente sancionador) e declaração de inidoneidade (3 a 6 anos, em todos os entes)."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Art. 156 da Lei 14.133/21. Escada: advertência (só inexecução parcial leve) → multa (mora/inexecução, cumulável) → impedimento (até 3 anos, no âmbito do ente: ex: só no Município de Meruoca) → inidoneidade (3 a 6 anos, em TODOS os entes, para fraudes e crimes). Mnemônico de alcance: Impedimento = local; Inidoneidade = nacional."
},
{
  "id": 507,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Reabilitacao do Punido (Art. 163)",
  "question": "A reabilitação do licitante punido com impedimento ou inidoneidade (Art. 163 da Lei nº 14.133/2021) exige cumulativamente:",
  "options": [
    "Reparação integral do dano, pagamento da multa, transcurso do prazo mínimo de 1 ano (impedimento) ou 3 anos (inidoneidade), cumprimento das condições e análise jurídica prévia.",
    "Apenas um pedido de desculpas por escrito ao prefeito, sem reparar nada.",
    "O decurso de 30 dias e a promessa verbal de não repetir.",
    "Sentença judicial transitada em julgado absolvendo em qualquer outro processo."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Art. 163 da Lei 14.133/21. Reabilitação NÃO é perdão automático: exige reparar o dano + pagar multa + esperar prazo mínimo (1 ano impedimento / 3 anos inidoneidade) + cumprir condições impostas + parecer jurídico. Só então o nome sai do CEIS/CNEP."
},
{
  "id": 508,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Extincao do Contrato: Hipoteses (Art. 137)",
  "question": "Constituem motivos para extinção do contrato administrativo (Art. 137 da Lei nº 14.133/2021):",
  "options": [
    "O simples desejo do contratado de receber mais, sem qualquer inadimplemento.",
    "Descumprimento ou cumprimento irregular das obrigações, atraso injustificado na execução, subcontratação vedada e razões de interesse público devidamente justificadas.",
    "A troca de prefeito, por si só, sem motivação relacionada ao contrato.",
    "O fato de outra empresa oferecer preço menor após a assinatura do contrato."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Art. 137 da Lei 14.133/21 (rol com ~9 incisos): inadimplemento, mora, alteração social que prejudique, caso fortuito/força maior, interesse público (com indenização do contratado de boa-fé). Troca de governo NÃO extingue contrato (princípio da continuidade e impessoalidade)."
},
{
  "id": 509,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Subcontratacao (Art. 122)",
  "question": "Quanto à subcontratação de partes do objeto (Art. 122 da Lei nº 14.133/2021), é correto afirmar que:",
  "options": [
    "É sempre livre e total, podendo o vencedor repassar 100% do contrato a terceiros sem avisar.",
    "É proibida em qualquer hipótese, mesmo parcial e prevista em edital.",
    "Somente é admitida se prevista no edital e no contrato, até o limite autorizado, vedada a subcontratação total e da parcela de maior relevância técnica.",
    "Dispensa qualquer responsabilidade do contratado original, que some após repassar."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Art. 122 da Lei 14.133/21. Subcontratação parcial e autorizada: exige previsão, limite e avaliação técnica; vedada a integral e a do 'coração' técnico do objeto. O contratado original continua INTEGRALMENTE responsável pela execução (não há novação)."
},
{
  "id": 510,
  "category": "administrativo",
  "day": "w3_d4",
  "discipline": "Lei 14.133/2021",
  "topic": "Nulidade do Contrato (Arts. 147-150)",
  "question": "Declarada a nulidade do contrato administrativo (Arts. 147 a 150 da Lei nº 14.133/2021), a consequência quanto aos efeitos já produzidos é que:",
  "options": [
    "O contratado perde tudo, mesmo de boa-fé, e ainda deve demolir o que construiu sem indenização.",
    "A nulidade nunca retroage e o contrato nulo continua válido para sempre.",
    "Os efeitos do contrato nulo são convertidos automaticamente em doação ao particular.",
    "A nulidade opera retroativamente, mas a Administração deve indenizar o contratado de boa-fé pelo que executou e pelo prejuízo da desmobilização, apurando-se a responsabilidade de quem deu causa."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Arts. 147-150 da Lei 14.133/21. Nulidade ex tunc (retroage), mas com indenização ao contratado de BOA-FÉ (o que executou + desmobilização + diferença de preço), sem prejuízo de apurar quem causou a nulidade (servidor/responsável responde). Vedado enriquecimento ilícito da Administração."
},
{
  "id": 511,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Verbo Haver Impessoal",
  "question": "Assinale a frase em que a concordância do verbo HAVER está em estrita conformidade com a norma-padrão:",
  "options": [
    "Havia muitas divergências entre os parlamentares durante a votação do veto.",
    "Haviam muitos requerimentos sobre a mesa da presidência ontem.",
    "Houveram intensos debates acerca da lei orçamentária na sessão.",
    "Hão muitas vagas para o cargo de técnico legislativo em Meruoca."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. HAVER com sentido de EXISTIR é impessoal: fica na 3ª pessoa do singular (Havia = existiam seriam... não!). 'Muitas divergências' é objeto direto, não sujeito. Em B, C e D o verbo foi indevidamente ao plural. Macete: troque por EXISTIR — se 'existir' iria ao plural, o 'haver' continua singular."
},
{
  "id": 512,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Verbo Fazer (Tempo e Clima)",
  "question": "Assinale a alternativa em que o verbo FAZER está corretamente flexionado segundo a norma culta:",
  "options": [
    "Fazem dez anos que o regimento interno da Câmara não é atualizado.",
    "Faz dez anos que o regimento interno da Câmara não é atualizado.",
    "Fizeram dias quentes em Meruoca durante todo o verão passado.",
    "Hão de fazer dois meses que a obra foi inaugurada."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. FAZER indicando tempo decorrido ou clima é impessoal (singular): 'Faz dez anos', 'Fez calor ontem'. Em B o verbo foi ao plural indevidamente; em C o correto seria 'Fez dias quentes' (ou 'Fizeram-se' em outra construção); em D há erro duplo. Macete: tempo e clima com FAZER nunca têm sujeito — singular sempre."
},
{
  "id": 513,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Sujeito Partitivo",
  "question": "Com sujeito partitivo (expressões como 'a maioria', 'a maior parte', 'parte de' seguidas de especificador no plural), a norma-padrão admite:",
  "options": [
    "Exclusivamente o plural, sendo erro grave usar o singular em qualquer caso.",
    "Exclusivamente o singular, sendo proibida a concordância com o especificador plural.",
    "Dupla concordância: o verbo pode ir ao singular (com o núcleo partitivo) ou ao plural (com o especificador) — 'A maioria dos vereadores aprovou/aprovaram o veto'.",
    "A flexão no dual, inexistente em português, com desinência própria."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Sujeito partitivo admite concordância SINGULAR (núcleo: 'A maioria... aprovou') ou PLURAL (atrativa com o especificador: '...aprovaram'). As duas estão certas — a banca INBRASP cobra exatamente essa faculdade. Atenção: se o partitivo vier com artigo definido + especificador, o plural é preferível, mas o singular continua válido."
},
{
  "id": 514,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Expressoes Percentuais",
  "question": "Quanto à concordância com expressões percentuais seguidas de especificador, a norma-padrão estabelece que:",
  "options": [
    "O verbo fica sempre no singular, mesmo com percentual plural e especificador plural.",
    "O verbo fica sempre no plural, mesmo com '1%' e especificador singular.",
    "Percentuais exigem verbo no futuro do pretérito em qualquer contexto.",
    "O verbo concorda com o número percentual ou, facultativamente, com o especificador — '10% da turma faltou/faltaram à sessão'."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Com percentuais + especificador há dupla possibilidade: concordância gramatical com o número ('10%... faltou') ou atrativa com o especificador ('...faltaram'). Com número no singular ('1% da turma'), o singular é obrigatório se não houver especificador plural divergente. A banca testa a faculdade, não a obrigação."
},
{
  "id": 515,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia com SE: Apassivadora vs Indice",
  "question": "Assinale a frase com concordância rigorosamente correta quanto ao emprego da partícula SE:",
  "options": [
    "Aprovaram-se as diretrizes orçamentárias prioritárias para o próximo exercício.",
    "Precisam-se de novos servidores para o arquivo da Câmara Municipal.",
    "Vende-se processos antigos arquivados na secretaria municipal.",
    "Aluga-se salas comerciais no centro de Meruoca."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Em A, 'aprovar' é VTD + SE apassivador: 'as diretrizes' é sujeito paciente → plural ('foram aprovadas'). Em B, 'precisar' é VTI: o SE é índice de indeterminação e o verbo deve ficar no SINGULAR ('Precisa-se') — o plural 'Precisam-se' está errado. Em C e D, VTD + SE apassivador exigem plural ('Vendem-se processos', 'Alugam-se salas'). Macete SE: teste 'foram + particípio' — deu certo, concorda; não deu, singular."
},
{
  "id": 516,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Sujeito Composto",
  "question": "Assinale a alternativa em que a concordância com sujeito composto está correta:",
  "options": [
    "O Presidente e o Relator da Comissão assinou o parecer técnico.",
    "O Presidente e o Relator da Comissão assinaram o parecer técnico.",
    "Vereadores e prefeito faltou à sessão solene de ontem.",
    "As atas e o relatório foi arquivado pela secretaria."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Sujeito composto ANTES do verbo → plural obrigatório ('assinaram'). As demais quebram a regra: B e C com singular, D com singular para dois núcleos. Exceção (núcleos sinônimos ou gradação) não se aplica aqui. Macete: dois sujeitos antes do verbo, verbo no plural sem choro."
},
{
  "id": 517,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia Nominal: Anexo, Obrigado, Mesmo, Só",
  "question": "Assinale a frase em que a concordância nominal está correta:",
  "options": [
    "Seguem anexo as planilhas de gastos do gabinete da presidência.",
    "Muito obrigado — disse a vereadora ao receber a homenagem.",
    "Seguem anexas as planilhas de gastos do gabinete da presidência.",
    "Eles mesmos redigiu a ata da sessão extraordinária."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. 'Anexo' como adjetivo varia ('anexas as planilhas'); invariável só como advérbio ('em anexo'). 'Obrigado' varia com quem fala ('obrigada' disse a vereadora → C errada). 'Mesmo' como reforço varia ('eles mesmos redigiram' → D errada duplamente). Macete: anexo/obrigado/mesmo/só se comportam como adjetivos — combinam com o nome."
},
{
  "id": 518,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Um e Outro, Nem Um Nem Outro",
  "question": "Quanto às expressões 'um e outro' e 'nem um nem outro', a norma-padrão determina que:",
  "options": [
    "Ambas exigem sempre o plural, sem exceção.",
    "Ambas exigem sempre o singular, sem exceção.",
    "O verbo fica no infinitivo impessoal em todos os casos.",
    "Com 'um e outro' o verbo vai ao singular ou ao plural ('Um e outro vereador faltou/faltaram'); com 'nem um nem outro' a regra geral é o singular ('Nem um nem outro compareceu')."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. 'Um e outro' = soma com ideia de reciprocidade/exclusão alternada → singular ou plural (facultativo). 'Nem um nem outro' = negação dos dois → singular (regra geral; plural só com ideia enfática de adição, raro em prova). A banca cobra a diferença entre as duas expressões."
},
{
  "id": 519,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: Sujeito Oracional",
  "question": "Quando o sujeito é uma oração (sujeito oracional), o verbo da oração principal fica:",
  "options": [
    "Na 3ª pessoa do singular — 'Falta aprovar dois projetos polêmicos antes do recesso'.",
    "No plural, concordando com o numeral dentro da oração sujeito.",
    "No infinitivo, sem flexão de pessoa.",
    "Na 1ª pessoa do plural, por deferência ao leitor."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Sujeito oracional ('aprovar dois projetos...') não tem número definido → verbo no singular ('Falta aprovar...', 'Convém analisar os vetos', 'Importa concluir as atas'). Pegadinha: o plural dentro da oração ('dois projetos') NÃO puxa o verbo. Macete: substitua a oração por ISSO — 'ISSO falta' (singular)."
},
{
  "id": 520,
  "category": "portugues",
  "day": "w3_d4",
  "discipline": "Língua Portuguesa",
  "topic": "Concordancia: É Proibido / São Necessários",
  "question": "Assinale a frase em que a concordância com as expressões 'é proibido', 'é necessário' e similares está correta:",
  "options": [
    "É proibida entrada de estranhos no plenário durante a votação.",
    "É proibido entrada de estranhos no plenário durante a votação.",
    "São necessário a assinatura dos dois secretários no autógrafo.",
    "É necessários paciência e diálogo na condução dos trabalhos."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Sem artigo antes do substantivo, a expressão fica INVARIÁVEL ('É proibido entrada', 'É necessário assinatura'). Com artigo, varia ('É proibida A entrada', 'São necessárias AS assinaturas'). Em B falta o artigo para variar; C e D invertem a regra. Macete: sem artigo, trava tudo no singular masculino."
}
,
{
  "id": 521,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Iniciativa Popular (CF, Art. 29, XIII)",
  "question": "A Constituição Federal assegura a iniciativa popular de projetos de lei de interesse específico do Município. Nesse contexto, assinale a alternativa CORRETA:",
  "options": [
    "A iniciativa popular exige subscrição de no mínimo dez por cento dos eleitores do Município.",
    "A iniciativa popular é vedada aos Municípios, cabendo apenas à União e aos Estados.",
    "A iniciativa popular depende de autorização prévia do Prefeito para ser exercida.",
    "A iniciativa popular manifesta-se por projetos subscritos por no mínimo cinco por cento do eleitorado municipal."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. CF/88, Art. 29, XIII: iniciativa popular mediante manifestação de pelo menos 5% do eleitorado. Distrator A troca o percentual; C nega o instituto; D cria autorização inexistente."
},
{
  "id": 522,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Iniciativa Privativa do Prefeito",
  "question": "No processo legislativo municipal, são de iniciativa privativa do Prefeito as leis que disponham sobre:",
  "options": [
    "Criação de cargos e funções na administração municipal e regime jurídico dos servidores.",
    "Organização dos serviços internos da Câmara e criação de seus cargos.",
    "Fixação dos subsídios dos Vereadores para a legislatura seguinte.",
    "Alteração do Regimento Interno da Câmara Municipal."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Simetria com CF, Art. 61, § 1º, II: cargos, funções, empregos, regime jurídico e organização administrativa do Executivo. B e D são da Mesa/Câmara; C é da Câmara (cada legislatura fixa para a subsequente)."
},
{
  "id": 523,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Iniciativa da Mesa Diretora",
  "question": "Compete privativamente à Mesa Diretora da Câmara a iniciativa de projetos de lei sobre:",
  "options": [
    "Aumento da remuneração dos servidores do Poder Executivo municipal.",
    "Criação de secretarias municipais e definição de suas atribuições.",
    "Organização dos serviços administrativos da Câmara e criação ou extinção de seus cargos.",
    "Instituição de impostos municipais sobre serviços de qualquer natureza."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. A Câmara organiza seus próprios serviços (função atípica administrativa). A e B são do Prefeito; D, embora municipal, não é iniciativa privativa da Mesa."
},
{
  "id": 524,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Emendas, Substitutivos e Pareceres",
  "question": "Durante a tramitação de um projeto de lei na Câmara, é CORRETO afirmar que:",
  "options": [
    "A emenda supressiva acrescenta dispositivo novo ao texto da proposição.",
    "O substitutivo altera integralmente a proposição, substituindo seu texto.",
    "O parecer das comissões substitui a votação em plenário.",
    "A emenda aditiva elimina parte do texto sem deliberação."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Supressiva ELIMINA; aditiva ACRESCENTA; modificativa ALTERA redação; substitutivo SUBSTITUI tudo. Parecer instrui, não substitui o plenário."
},
{
  "id": 525,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Sanção: Prazo e Silêncio",
  "question": "Aprovado um projeto de lei pela Câmara de Meruoca, o Prefeito terá 15 dias úteis para sancioná-lo ou vetá-lo. Decorrido esse prazo sem manifestação, é CORRETO afirmar que:",
  "options": [
    "O projeto é arquivado por decurso de prazo.",
    "O silêncio importa sanção tácita do projeto.",
    "O projeto retorna à Câmara para nova votação obrigatória.",
    "O veto é considerado automaticamente oposto."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Simetria com CF, Art. 66, § 3º: silêncio do Executivo em 15 dias úteis = sanção tácita. Não há arquivamento nem veto presumido."
},
{
  "id": 526,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Veto: Espécies e Motivos",
  "question": "O Prefeito poderá vetar projeto de lei aprovado pela Câmara quando o julgar inconstitucional ou contrário ao interesse público. Sobre o veto, assinale a alternativa CORRETA:",
  "options": [
    "O veto é sempre total, não se admitindo veto parcial.",
    "O veto parcial alcança apenas textos integrais, nunca palavras isoladas.",
    "O veto pode ser total ou parcial, abrangendo inclusive palavra ou expressão isolada.",
    "O veto dispensa motivação, por ser ato discricionário puro."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. CF, Art. 66, § 2º: veto total ou parcial (este, sobre texto integral de artigo, parágrafo, inciso ou alínea — e, na prática legislativa, palavra/expressão). Exige motivação: inconstitucionalidade ou interesse público."
},
{
  "id": 527,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Apreciação do Veto pela Câmara",
  "question": "Oposto o veto, a Câmara deverá apreciá-lo em 30 dias. É CORRETO afirmar que:",
  "options": [
    "O veto só pode ser rejeitado pelo voto da maioria absoluta dos membros da Câmara.",
    "O veto é derrubado por maioria simples dos vereadores presentes.",
    "Decorrido o prazo sem apreciação, o veto é automaticamente mantido.",
    "A apreciação do veto dispensa quórum mínimo de presença."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. CF, Art. 66, § 4º (simetria municipal): rejeição por maioria absoluta em 30 dias; não apreciado, SOBRESTA as demais deliberações (tranca a pauta) — jamais é mantido automaticamente."
},
{
  "id": 528,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Promulgação: Prazos e Competência",
  "question": "Rejeitado o veto pela Câmara, o projeto será enviado ao Prefeito para promulgação em 48 horas. Se ele não o fizer, é CORRETO afirmar que:",
  "options": [
    "O Presidente da Câmara promulgará a lei em igual prazo de 48 horas.",
    "A lei jamais entrará em vigor por falta de promulgação.",
    "Qualquer vereador poderá promulgar a lei imediatamente.",
    "O Tribunal de Contas promulgará a lei no lugar do Prefeito."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. CF, Art. 66, § 7º: omisso o Prefeito em 48h, promulga o Presidente da Câmara (e, se este falhar, o Vice). Sem promulgação não há executoriedade — por isso a Constituição define substitutos."
},
{
  "id": 529,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Fiscalização: Convocação e Sustação",
  "question": "No exercício da função fiscalizadora, a Câmara Municipal poderá:",
  "options": [
    "Convocar Secretários Municipais para prestar pessoalmente informações sobre assuntos de suas pastas.",
    "Demitir servidores do Poder Executivo por decisão de comissão.",
    "Anular atos do Prefeito por conveniência política, sem motivação.",
    "Sustar contratos administrativos regulares sem apontar ilegalidade."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Simetria com CF, Art. 50: convocação de auxiliares para informações (recusa injustificada = crime de responsabilidade). Sustação de atos/contratos exige ilegalidade apontada (com o TCE). Demissão e anulação imotivada extrapolam a competência do Legislativo."
},
{
  "id": 530,
  "category": "legislacao",
  "day": "w3_d5",
  "discipline": "Lei Orgânica de Meruoca",
  "topic": "Julgamento das Contas: Prefeito x Mesa",
  "question": "Quanto ao julgamento das contas no âmbito municipal, assinale a alternativa CORRETA:",
  "options": [
    "As contas do Prefeito são julgadas pelo Tribunal de Contas, sem qualquer participação da Câmara Municipal.",
    "As contas da Mesa da Câmara são julgadas pela própria Câmara, com total exclusão do Tribunal de Contas.",
    "Todas as contas municipais são julgadas pelo Prefeito, por ser o ordenador de despesas.",
    "As contas do Prefeito são julgadas pela Câmara, com parecer prévio do Tribunal de Contas; as da Mesa são julgadas diretamente pelo Tribunal."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. CF, Arts. 31 e 71: Prefeito = julgado pela Câmara (controle externo político, com parecer do TCE); Mesa/Câmara enquanto unidade gestora = julgada pelo TCE. Distrator A inverte; B exclui o TCE; D concentra tudo no Prefeito."
},
{
  "id": 531,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área do Retângulo",
  "question": "O plenário da Câmara possui formato retangular com 12 metros de comprimento por 9 metros de largura. A área total desse plenário é de:",
  "options": [
    "42 m².",
    "54 m².",
    "108 m².",
    "216 m²."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Área = 12 × 9 = 108 m². A soma 42 é o perímetro; 216 é o dobro da área; 54 é a metade."
},
{
  "id": 532,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Perímetro do Retângulo",
  "question": "Um terreno da Câmara mede 45 metros de comprimento por 25 metros de largura. Para cercá-lo totalmente, serão necessários:",
  "options": [
    "70 metros de cerca.",
    "1.125 metros de cerca.",
    "95 metros de cerca.",
    "140 metros de cerca."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Perímetro = 2 × (45 + 25) = 140 m. 1.125 é a área; 70 é metade do perímetro; 95 não corresponde a nenhuma operação válida."
},
{
  "id": 533,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área do Quadrado",
  "question": "Uma sala de arquivo quadrada possui 12 metros de lado. Sua área corresponde a:",
  "options": [
    "48 m².",
    "144 m².",
    "24 m².",
    "72 m²."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Área = 12² = 144 m². 48 é o perímetro; 24 e 72 são frações sem base no cálculo."
},
{
  "id": 534,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área do Triângulo",
  "question": "Um jardim triangular em frente à Câmara tem base de 10 metros e altura de 6 metros. Sua área é de:",
  "options": [
    "60 m².",
    "16 m².",
    "36 m².",
    "30 m²."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Área = (10 × 6) / 2 = 30 m². 60 esquece a divisão por 2 — erro clássico da banca; 16 soma base e altura; 36 não tem base no cálculo."
},
{
  "id": 535,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área do Círculo",
  "question": "Uma praça circular possui raio de 7 metros. Adotando π = 3,14, sua área é de:",
  "options": [
    "43,96 m².",
    "153,86 m².",
    "21,98 m².",
    "307,72 m²."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Área = 3,14 × 7² = 153,86 m². 43,96 é o comprimento da circunferência (2πr); 307,72 dobra o raio; 21,98 não tem base."
},
{
  "id": 536,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Volume do Paralelepípedo",
  "question": "Um depósito da Câmara mede 5 metros de comprimento, 4 metros de largura e 2,5 metros de altura. Seu volume é de:",
  "options": [
    "50 m³.",
    "45 m³.",
    "11,5 m³.",
    "100 m³."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Volume = 5 × 4 × 2,5 = 50 m³. 11,5 soma as medidas; 100 dobra o resultado."
},
{
  "id": 537,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Área e Rendimento (Piso)",
  "question": "Uma sala de 8 metros por 6 metros será revestida com placas que cobrem 16 m² cada. Serão necessárias:",
  "options": [
    "2 placas.",
    "4 placas.",
    "3 placas.",
    "6 placas."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Área = 48 m²; 48 / 16 = 3 placas exatas. 2 e 6 vêm de divisões erradas; 4 arredonda sem necessidade."
},
{
  "id": 538,
  "category": "matematica",
  "day": "w3_d5",
  "discipline": "Matemática / RLM",
  "topic": "Volume e Consumo (Caixa d'Água)",
  "question": "Uma caixa d'água de 2 m por 1,5 m por 1 m abastece um setor que consome 500 litros por dia. Sem reposição, a reserva dura:",
  "options": [
    "3 dias.",
    "5 dias.",
    "7 dias.",
    "6 dias."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Volume = 3 m³ = 3.000 litros; 3.000 / 500 = 6 dias. Exige a conversão m³→litros antes de dividir — pulo clássico da banca."
}
,
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
,
{
  "id": 569,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Mesa Diretora: Mandato",
  "question": "Quanto ao mandato dos membros da Mesa Diretora da Câmara Municipal, a regra regimental mais comum estabelece que:",
  "options": [
    "O mandato é vitalício, só se encerrando com a renúncia expressa do ocupante.",
    "O mandato é de dois anos, permitida a recondução para o mesmo cargo na eleição imediatamente subsequente, observada a Lei Orgânica.",
    "O mandato coincide com o do Prefeito e não admite qualquer recondução.",
    "Os membros da Mesa são escolhidos por sorteio a cada sessão ordinária."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Padrão regimental: mandato de 2 anos (metade da legislatura), com possibilidade de recondução nos termos da Lei Orgânica. Vitaliciedade e sorteio inexistem; coincidir com o prefeito não é regra."
},
{
  "id": 570,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Destituição de Membro da Mesa",
  "question": "A destituição de membro da Mesa Diretora que se omita ou exorbite de suas atribuições regimentais depende, em regra, de:",
  "options": [
    "Decisão judicial de primeira instância, sem participação da Câmara.",
    "Decreto do Prefeito determinando o afastamento imediato.",
    "Deliberação do Plenário pelo voto de dois terços dos vereadores, assegurada ampla defesa.",
    "Simples requerimento verbal de qualquer cidadão presente à sessão."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. A Mesa é eleita pela Câmara e só por ela pode ser destituída: quórum qualificado de 2/3 com contraditório e ampla defesa. Prefeito e Judiciário não destituem mesa diretora."
},
{
  "id": 571,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Presidente: Representação da Câmara",
  "question": "Entre as atribuições do Presidente da Câmara Municipal inclui-se:",
  "options": [
    "Nomear os Secretários Municipais do Poder Executivo.",
    "Julgar crimes comuns praticados por qualquer cidadão do Município.",
    "Representar a Câmara em juízo e fora dele, bem como dar posse a Prefeito, Vice e Vereadores.",
    "Arrecadar diretamente os tributos municipais e executar o orçamento."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. O Presidente é a face institucional do Legislativo: representa-o judicial e extrajudicialmente e preside a posse dos eleitos. Nomear secretários, julgar crimes e arrecadar são funções alheias ao cargo."
},
{
  "id": 572,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Presidente: Direção dos Trabalhos",
  "question": "Na direção dos trabalhos plenários, compete ao Presidente da Câmara, entre outras atribuições:",
  "options": [
    "Votar em todas as matérias com peso dobrado em relação aos demais vereadores.",
    "Proibir qualquer vereador de apresentar requerimentos durante a legislatura.",
    "Alterar sozinho o texto de leis já aprovadas antes da promulgação.",
    "Abrir, presidir e encerrar as sessões, manter a ordem e suspender a sessão quando necessário."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Poderes de polícia dos trabalhos: abrir/presidir/encerrar, manter a ordem, suspender. Voto sem peso dobrado, vedação de requerimentos e alteração unilateral de lei aprovada são incompatíveis com o cargo."
},
{
  "id": 574,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Sessões Ordinárias e Períodos Legislativos",
  "question": "As sessões legislativas ordinárias da Câmara Municipal realizam-se, por simetria com o modelo constitucional, em dois períodos anuais, compreendidos, em regra, entre:",
  "options": [
    "2 de fevereiro a 17 de julho e 1º de agosto a 22 de dezembro, com recessos em janeiro e parte de julho e dezembro.",
    "1º de janeiro a 31 de dezembro, sem qualquer recesso parlamentar.",
    "Apenas no mês de fevereiro de cada ano, em sessão única anual.",
    "Os dias de carnaval e as festas juninas, por tradição municipal."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Simetria com CF, Art. 57: 02/02–17/07 e 01/08–22/12. Recesso não significa paralisação total: comissões e convocações extraordinárias subsistem."
},
{
  "id": 575,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Sessões Extraordinárias",
  "question": "Sobre as sessões extraordinárias da Câmara Municipal, é CORRETO afirmar que:",
  "options": [
    "Ocorrem todos os dias úteis do ano, independentemente de convocação.",
    "Destinam-se a homenagens e comemorações, sem qualquer deliberação.",
    "Convocadas no recesso para matéria urgente e determinada, sem extra remuneratório.",
    "Podem tratar de qualquer assunto, ainda que estranho ao ato de convocação."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Extraordinária = recesso + matéria certa e urgente + sem extra remuneratório (CF, Art. 57, § 7º, por simetria). Homenagens são das solenes; a pauta vincula-se à convocação."
},
{
  "id": 576,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Sessões Solenes e Secretas",
  "question": "As sessões solenes e as sessões secretas distinguem-se porque:",
  "options": [
    "Ambas servem apenas para a votação do orçamento anual.",
    "As solenes são sempre secretas e as secretas são sempre solenes.",
    "Nenhuma delas admite a presença de vereadores, sendo realizadas só por servidores.",
    "As solenes destinam-se a atos cívicos e homenagens, sem deliberação; secretas: sigilo regimental decidido pelo Plenário."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Solene = celebração (posse, títulos, homenagens), sem voto. Secreta = sigilo regimental, decidida pelo Plenário. Confundi-las é a pegadinha clássica."
},
{
  "id": 577,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Abertura da Sessão e Quórum",
  "question": "Para a abertura das sessões plenárias e para as deliberações da Câmara, os quóruns regimentais típicos exigem, respectivamente:",
  "options": [
    "Unanimidade para abrir e maioria simples para deliberar.",
    "Um terço para abrir; maioria absoluta presente para deliberar.",
    "Apenas o Presidente presente para abrir e deliberar sozinho.",
    "Dois terços para abrir e unanimidade para qualquer deliberação."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Abertura com 1/3; deliberação com maioria absoluta presente decidindo por maioria de votos (CF, Art. 47, por simetria). Unanimidade e decisão solitária inexistem como regra."
},
{
  "id": 579,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Poder Conclusivo das Comissões",
  "question": "Em regra regimental, as comissões permanentes da Câmara podem deliberar de forma conclusiva, dispensando a votação em Plenário, quando:",
  "options": [
    "Se o Regimento autorizar, com recurso de um décimo para o Plenário.",
    "Em todas as matérias, esvaziando por completo as funções do Plenário.",
    "Apenas quando o Prefeito autorizar previamente cada deliberação.",
    "Jamais, pois toda matéria exige votação em Plenário sem exceção."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Simetria com CF, Art. 58, § 2º, I: poder conclusivo previsto no Regimento, com recurso de 1/10 para o Plenário. Não é geral nem depende do Prefeito; tampouco é vedado em absoluto."
},
{
  "id": 580,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "CPI: Poderes e Destino",
  "question": "As Comissões Parlamentares de Inquérito da Câmara Municipal possuem poderes de investigação próprios das autoridades judiciais e, ao final dos trabalhos, deverão:",
  "options": [
    "Condenar criminalmente os investigados, fixando penas de prisão.",
    "Arquivar sigilosamente o relatório, vedada qualquer divulgação.",
    "Encaminhar suas conclusões ao Ministério Público para as providências cabíveis, quando for o caso.",
    "Substituir o Tribunal de Contas no julgamento das contas do Prefeito."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. CPI investiga com poderes judiciais (quebra de sigilo mediante decisão, oitivas), mas não julga nem condena: remete ao MP. Arquivamento sigiloso obrigatório e substituição do TCE inexistem."
},
{
  "id": 583,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Processos de Votação",
  "question": "Quanto aos processos de votação no Plenário da Câmara, a regra regimental típica estabelece que:",
  "options": [
    "Toda votação é secreta, sem exceção, inclusive nas eleições da Mesa.",
    "A votação simbólica é a regra geral e a nominal realiza-se mediante requerimento aprovado pelo Plenário.",
    "A votação simbólica é proibida e todas as matérias exigem chamada nominal.",
    "O voto é sempre aberto por aclamação, vedado qualquer registro individual."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Simbólica (permanecem sentados/aprovado) como regra; nominal (chamada com registro) por requerimento. Votação sempre secreta ou sempre por aclamação contrariam o padrão."
},
{
  "id": 585,
  "category": "legislacao",
  "day": "w4_d1",
  "discipline": "Regimento Interno",
  "topic": "Legislatura e Sessão Legislativa",
  "question": "No Poder Legislativo municipal, distinguem-se legislatura e sessão legislativa porque:",
  "options": [
    "Ambas têm duração de trinta dias e se confundem integralmente.",
    "A legislatura dura um ano e a sessão legislativa dura quatro anos.",
    "Legislatura = mandato de 4 anos; sessão legislativa = cada ano de trabalhos.",
    "A sessão legislativa só existe em ano eleitoral."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Legislatura = 4 anos (mandato); sessão legislativa = cada ano civil de trabalhos (com os dois períodos e recessos). Inverter ou igualar os conceitos é o erro cobrado."
},
{
  "id": 588,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Assistir (Presenciar)",
  "question": "Assinale a frase em que o verbo ASSISTIR foi empregado com a regência correta no sentido de presenciar:",
  "options": [
    "Os vereadores assistiram à sessão solene de abertura dos trabalhos.",
    "Os vereadores assistiram a sessão solene de abertura dos trabalhos.",
    "Os vereadores assistiram na sessão solene de abertura dos trabalhos.",
    "Os vereadores assistiram para a sessão solene de abertura dos trabalhos."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Assistir = presenciar é VTI com preposição A. Como 'sessão' é palavra feminina determinada, soma-se o artigo: a + a = À (crase obrigatória). Sem crase, com EM ou PARA, a regência está errada."
},
{
  "id": 590,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Visar (Almejar vs Mirar)",
  "question": "Assinale a frase em que o verbo VISAR está corretamente empregado:",
  "options": [
    "O projeto visa o fortalecimento da agricultura familiar.",
    "O projeto visa ao fortalecimento da agricultura familiar.",
    "O atirador visou a o alvo antes de disparar.",
    "O servidor visou de assinar o documento oficial."
  ],
  "correctAnswer": 1,
  "commentary": "Gabarito: B. Almejar = VTI com A ('visa AO fortalecimento'); como 'fortalecimento' é masculino, não há crase. Mirar = VTD ('visou o alvo'); pôr visto = VTD ('visou o documento'). As demais violam cada regência."
},
{
  "id": 591,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Aspirar (Almejar vs Sorver)",
  "question": "Assinale a alternativa em que o verbo ASPIRAR está correto:",
  "options": [
    "O vereador aspira o cargo de presidente da Mesa.",
    "O paciente aspira a o oxigênio pelo cateter.",
    "A indústria aspira em novos mercados consumidores.",
    "O vereador aspira ao cargo de presidente da Mesa."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Almejar = VTI com A ('aspira AO cargo', sem crase por ser masculino); sorver/respirar = VTD ('aspira o oxigênio'). EM não rege nenhum dos sentidos."
},
{
  "id": 592,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Obedecer e Desobedecer",
  "question": "Os verbos OBEDECER e DESOBEDECER são transitivos indiretos. Assinale a frase correta:",
  "options": [
    "Os servidores obedeceram o regimento interno da Câmara.",
    "Os servidores obedeceram com o regimento interno da Câmara.",
    "Os servidores desobedeceram de todas as normas regimentais.",
    "Os servidores obedeceram ao regimento interno da Câmara."
  ],
  "correctAnswer": 3,
  "commentary": "Gabarito: D. Obedecer/desobedecer exigem preposição A (VTI): 'obedecer AO regimento'. Sem preposição ou com COM/DE, a regência está errada. Sem crase aqui porque 'regimento' é masculino."
},
{
  "id": 593,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência: Pagar e Perdoar (VTDI)",
  "question": "PAGAR e PERDOAR são bitransitivos: coisa sem preposição, pessoa com preposição. Assinale a frase correta:",
  "options": [
    "A Prefeitura pagou aos fornecedores as faturas em atraso.",
    "A Prefeitura pagou os fornecedores as faturas em atraso.",
    "O presidente perdoou a ofensa ao colega arrependido.",
    "O presidente perdoou o colega a ofensa sofrida."
  ],
  "correctAnswer": 0,
  "commentary": "Gabarito: A. Coisa = OD ('as faturas', sem preposição); pessoa = OI ('AOS fornecedores'). Em C/D os papéis se invertem: o correto seria 'perdoou AO colega A ofensa' (pessoa com A, coisa sem)."
},
{
  "id": 594,
  "category": "portugues",
  "day": "w4_d1",
  "discipline": "Língua Portuguesa",
  "topic": "Regência Nominal",
  "question": "A regência nominal estuda a preposição exigida pelos nomes. Assinale a alternativa em que a regência nominal está correta:",
  "options": [
    "O técnico mostrou-se obediente o regulamento da Câmara.",
    "A comissão está favorável com a aprovação do projeto.",
    "O técnico mostrou-se obediente ao regulamento da Câmara.",
    "Os vereadores são aptos em legislar sobre a matéria."
  ],
  "correctAnswer": 2,
  "commentary": "Gabarito: C. Obediente/favorável pedem A ('obediente AO', 'favorável À aprovação'); apto pede A ou PARA ('aptos A legislar'). COM e EM violam a regência desses nomes."
}
];

// =========================================================================
// CRONOGRAMA COMPLETO DAS 7 SEMANAS (31/08 a 18/10/2026)
// =========================================================================
const WEEKS_DATA = [
  {
    weekNumber: 1,
    title: "Semana 1 (31/08 a 06/09)",
    focus: "Constituição + Português + Fundamentos Administrativos",
    days: [
      {
        id: "w1_d1",
        dayLabel: "Segunda-feira",
        date: "31/08/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Português — Interpretação de Textos",
            details: "Situação comunicativa, pressuposto, inferência, ambiguidade, ironia, polissemia, intertextualidade e linguagem não verbal.",
            tasks: ["40m Teoria & Exemplos", "20m Esquemas & Anotações", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "D. Constitucional — Arts. 1º a 4º da CF/88",
            details: "Fundamentos da República, separação de poderes, objetivos fundamentais e princípios das relações internacionais.",
            tasks: ["40m Teoria & CF Seca", "20m Leitura dos Arts. 1º a 4º", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 questões de Português + 15 questões de Constitucional. Registro dos erros e pegadinhas.",
            tasks: ["15 Questões Português", "15 Questões Constitucional", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      
      {
        id: "w1_d2",
        dayLabel: "Terça-feira",
        date: "01/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "D. Constitucional — Art. 5º da CF/88",
            details: "Direitos individuais, direitos coletivos, garantias e introdução aos remédios constitucionais (HC, HD, MS, MI, AP).",
            tasks: ["40m Teoria Art. 5º", "20m Leitura dos Incisos", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Tipos e Gêneros Textuais",
            details: "Narrativo, descritivo, expositivo, argumentativo, instrucional, propaganda, editorial, cartaz, ofício, carta comercial.",
            tasks: ["40m Teoria dos Gêneros", "20m Diferenciação Prática", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 questões de Constitucional (Art. 5º) + 15 de Português. Registrar no caderno de erros.",
            tasks: ["15 Questões Art. 5º", "15 Questões Tipos Textuais", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w1_d3",
        dayLabel: "Quarta-feira",
        date: "02/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "D. Administrativo — Princípios e Organização",
            details: "Conceito, princípios expressos (LIMPE) e implícitos, administração direta vs. indireta, autarquias, fundações e empresas públicas.",
            tasks: ["40m Teoria Organização", "20m Esquema Direta/Indireta", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Informática — Ambientes & Hardware",
            details: "Windows 11, Ubuntu Linux, gerenciamento de arquivos/pastas, arquitetura básica de computadores, backup e restauração.",
            tasks: ["40m Teoria SO & Hardware", "20m Atalhos e Procedimentos", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 questões de Administrativo + 15 de Informática.",
            tasks: ["15 Questões D. Admin", "15 Questões Informática", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w1_d4",
        dayLabel: "Quinta-feira",
        date: "03/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Português — Fonologia, Ortografia & Acentuação",
            details: "Regras de acentuação (proparoxítonas e hiatos na INBRASP), novo acordo ortográfico, divisão silábica e emprego da crase.",
            tasks: ["40m Teoria & Regras de Acentuação", "20m Memorização e Casos de Crase", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "D. Constitucional — Arts. 6º a 11 (Direitos Sociais)",
            details: "Direitos sociais fundamentais, direitos dos trabalhadores, licença-maternidade/paternidade, FGTS, greve e liberdade sindical.",
            tasks: ["40m Leitura dos Arts. 6º–11 da CF", "20m Mnemônicos dos Direitos Sociais", "10m Recuperação Ativa"]
          },
          {
            badge: "Pílula Lei Seca • 25m",
            subject: "Lei Orgânica de Meruoca — Arts. 1º ao 15",
            details: "Leitura da lei seca: Princípios fundamentais do município, competências privativas e competências comuns com Estado/União.",
            tasks: ["15m Leitura dos Arts. 1º a 15", "10m Anotação de Competências Privativas"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões INBRASP + Caderno de Erros",
            details: "20 questões de Português (ortografia/crase) + 20 questões de D. Constitucional.",
            tasks: ["20 Questões Português", "20 Questões Constitucional", "30m Registro no Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w1_d5",
        dayLabel: "Sexta-feira",
        date: "04/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "D. Administrativo — Poderes Administrativos & Atributos",
            details: "Poder vinculado, discricionário, hierárquico, disciplinar, regulamentar e poder de polícia. Atributos do ato (PATI).",
            tasks: ["40m Teoria Poderes & Atributos", "20m Quadro Comparativo e Mnemônico PATI", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Informática — Algoritmos, Fluxogramas & Noções de Python",
            details: "Fundamentos de lógica de programação, pseudocódigos, estruturas condicionais (if/else), laços (for/while) e noções de Python (Edital pág. 21).",
            tasks: ["40m Teoria de Algoritmos & Fluxogramas", "20m Estruturas de Repetição & Python Básico", "10m Recuperação Ativa"]
          },
          {
            badge: "Pílula Lei Seca • 25m",
            subject: "Lei Orgânica de Meruoca — Arts. 16 ao 30",
            details: "Organização do Poder Legislativo Municipal, composição da Câmara, posse, suplência e prerrogativas dos Vereadores.",
            tasks: ["15m Leitura dos Arts. 16 a 30", "10m Destaque de Quóruns e Inviolabilidade"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões INBRASP + Caderno de Erros",
            details: "20 questões de Poderes Administrativos + 20 de Informática/Lógica.",
            tasks: ["20 Questões Poderes", "20 Questões Informática/Algoritmos", "30m Registro no Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w1_d6",
        dayLabel: "Sábado",
        date: "05/09/2026",
        blocks: [
          {
            badge: "Simulado 1 • 3h00",
            subject: "SIMULADO 1 — 40 Questões",
            details: "Simulação real: 20 Gerais + 20 Específicas, sem consulta, 4 alternativas por questão. Foco em cronometragem.",
            tasks: ["Realizar Simulado (3 horas)", "Preencher Cartão-Resposta", "Classificar Erros por Cores"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w1_d7",
        dayLabel: "Domingo",
        date: "06/09/2026",
        blocks: [
          {
            badge: "Revisão • 2h30",
            subject: "Correção Profunda do Simulado + Revisão CF",
            details: "Análise profunda de cada erro do Simulado 1. Revisão da CF/88 arts. 1º a 11 + 20 questões dos assuntos errados.",
            tasks: ["Correção Analítica Simulado", "Revisão CF Arts. 1º–11", "20 Questões de Reforço"]
          }
        ],
        targetQuestions: 20
      }
    ]
  },
  {
    weekNumber: 2,
    title: "Semana 2 (07/09 a 13/09)",
    focus: "Poder Legislativo + Processo Legislativo + Português + LC 95",
    days: [
      {
        id: "w2_d1",
        dayLabel: "Segunda-feira",
        date: "07/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "D. Constitucional — Organização do Estado",
            details: "União, Estados, Municípios e DF. Competências privativas, comuns e suplementares municipais (CF arts. 18–31).",
            tasks: ["40m Teoria Arts. 18–31", "20m Foco em Municípios", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Estrutura e Formação de Palavras",
            details: "Derivação (prefixal, sufixal, parassintética, regressiva, imprópria), composição e classes gramaticais.",
            tasks: ["40m Teoria Formação", "20m Exemplos e Prefixos", "10m Recuperação Ativa"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões + Caderno de Erros",
            details: "20 questões de Organização do Estado + 20 de Formação de Palavras.",
            tasks: ["20 Questões Const.", "20 Questões Port.", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w2_d2",
        dayLabel: "Terça-feira",
        date: "08/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Técnico Legislativo — O Poder Legislativo",
            details: "Funções típicas (legislar e fiscalizar) e atípicas (administrar e julgar), Legislativo municipal e representação parlamentar.",
            tasks: ["40m Teoria Poder Legislativo", "20m Atribuições e Funções", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Morfologia & Verbos",
            details: "Verbos, tempos e modos verbais, flexão verbal e nominal, formas nominais e correlação verbal.",
            tasks: ["40m Teoria Verbos", "20m Conjugação e Tempos", "10m Recuperação Ativa"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões + Caderno de Erros",
            details: "20 questões de Legislativo + 20 de Verbos e Regência.",
            tasks: ["20 Questões Legislativo", "20 Questões Verbos/Português", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w2_d3",
        dayLabel: "Quarta-feira",
        date: "09/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Processo Legislativo — Espécies & Proposições",
            details: "Espécies normativas (CF art. 59), iniciativa das leis, tramitação, projetos, emendas, substitutivos e pareceres.",
            tasks: ["40m Teoria Espécies Normativas", "20m Fluxo de Tramitação", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Informática — Pacote Office & Google Workspace",
            details: "Word/Docs (formatação, estilos), Excel/Sheets (fórmulas básicas, soma, média, SE), PowerPoint/Slides.",
            tasks: ["40m Teoria e Prática Office", "20m Fórmulas Excel", "10m Recuperação Ativa"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões + Caderno de Erros",
            details: "20 questões de Processo Legislativo + 20 de Office & Google Workspace.",
            tasks: ["20 Questões Proc. Leg.", "20 Questões Office/Workspace", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w2_d4",
        dayLabel: "Quinta-feira",
        date: "10/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Poder Legislativo — Sessões, Agenda & Representação Partidária",
            details: "Sessões plenárias (ordinárias, extraordinárias e solenes), Expediente vs Ordem do Dia, Partidos Políticos e Sistemas Eleitorais de Vereadores (quociente eleitoral e partidário - Edital pág. 24).",
            tasks: ["40m Teoria Sessões & Ordem do Dia", "20m Quociente Eleitoral e Partidos", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Matemática & RLM — Razão, Proporção, Porcentagem & Regra de Três",
            details: "Razão e proporção, grandezas diretamente e inversamente proporcionais, regra de três simples/composta e porcentagem no padrão INBRASP.",
            tasks: ["40m Métodos e Fórmulas", "20m Resolução de Questões", "10m Recuperação Ativa"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões + Caderno de Erros",
            details: "20 questões de Sessões/Sistemas Eleitorais + 20 de Matemática/RLM.",
            tasks: ["20 Questões Legislativo", "20 Questões Matemática/RLM", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      
      {
        id: "w2_d5",
        dayLabel: "Sexta-feira",
        date: "11/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Técnica Legislativa — LC 95/1998",
            details: "Estrutura dos atos normativos, articulação (artigo, parágrafo, inciso, alínea, item), redação, alteração e vigência.",
            tasks: ["40m Leitura da LC 95/98", "20m Regras de Articulação", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Sintaxe da Oração",
            details: "Termos da oração: sujeito, predicado, transitividade verbal, objetos, complementos, adjuntos e aposto.",
            tasks: ["40m Teoria Sintaxe", "20m Análise de Frases", "10m Recuperação Ativa"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões + Caderno de Erros",
            details: "20 questões de Técnica Legislativa (LC 95/98) + 20 de Sintaxe da Oração.",
            tasks: ["20 Questões LC 95/98", "20 Questões Sintaxe", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w2_d6",
        dayLabel: "Sábado",
        date: "12/09/2026",
        blocks: [
          {
            badge: "Simulado 2 • 3h00",
            subject: "SIMULADO 2 — 40 Questões",
            details: "Simulação completa no padrão oficial de prova. Foco em ritmo e segurança nas respostas.",
            tasks: ["Executar Simulado 2", "Marcar Tempo por Questão", "Classificar Desempenho"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w2_d7",
        dayLabel: "Domingo",
        date: "13/09/2026",
        blocks: [
          {
            badge: "Revisão • 2h30",
            subject: "Correção + Lei Seca CF Arts. 1º a 31",
            details: "Correção do Simulado 2 + Revisão completa dos arts. 1º–5º, 6º–11, 18–19 e 29–31 da CF.",
            tasks: ["Correção Simulado 2", "Leitura Lei Seca CF", "20 Questões dos Erros"]
          }
        ],
        targetQuestions: 20
      }
    ]
  },
  {
    weekNumber: 3,
    title: "Semana 3 (14/09 a 20/09)",
    focus: "Atos Administrativos + Lei 14.133 + Lei Orgânica de Meruoca",
    days: [
      {
        id: "w3_d1",
        dayLabel: "Segunda-feira",
        date: "14/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "D. Administrativo — Atos Administrativos (Parte 1)",
            details: "Conceito, requisitos/elementos (COMFIFOR), atributos (PATI), classificação e espécies.",
            tasks: ["40m Requisitos e Atributos", "20m Espécies de Atos", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Período Composto",
            details: "Coordenação (aditivas, adversativas, etc.) e subordinação (substantivas, adjetivas, adverbiais).",
            tasks: ["40m Teoria Conjunções", "20m Quadro de Conectivos", "10m Recuperação Ativa"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões + Caderno de Erros",
            details: "20 questões de Direito Administrativo (Atos Administrativos) + 20 de Língua Portuguesa (Período Composto).",
            tasks: ["20 Questões Atos Administrativos", "20 Questões Período Composto", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w3_d2",
        dayLabel: "Terça-feira",
        date: "15/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "D. Administrativo — Extinção de Atos",
            details: "Anulação, revogação, cassação, caducidade, convalidação (FO-CO), vinculação e discricionariedade.",
            tasks: ["40m Anulação vs Revogação", "20m Convalidação", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Matemática — Sistema Monetário & Medidas",
            details: "Unidades de medida (comprimento, área, massa, capacidade), conversão de unidades e cálculos financeiros.",
            tasks: ["40m Conversão de Unidades", "20m Resolução de Problemas", "10m Recuperação Ativa"]
          },
          {
            badge: "Treino de Alto Nível • 1h40",
            subject: "40 Questões + Caderno de Erros",
            details: "20 questões de Extinção e Convalidação de Atos + 20 de Sistema Monetário e Medidas.",
            tasks: ["20 Questões Extinção Atos", "20 Questões Medidas", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w3_d3",
        dayLabel: "Quarta-feira",
        date: "16/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Lei 14.133/2021 — Licitações (Parte 1)",
            details: "Princípios, agentes públicos, planejamento, modalidades (pregão, concorrência, concurso, leilão, diálogo competitivo) e critérios.",
            tasks: ["40m Modalidades e Critérios", "20m Agente de Contratação", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Informática — Redes & Internet",
            details: "Internet, Intranet, conceitos de navegação, navegadores (Chrome, Edge, Firefox), pesquisa avançada e protocolos básicos.",
            tasks: ["40m Teoria Redes", "20m Navegadores & Recursos", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "20 da Lei 14.133/2021 + 10 de Informática.",
            tasks: ["20 Questões Lei 14.133", "10 Questões Redes", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w3_d4",
        dayLabel: "Quinta-feira",
        date: "17/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Lei 14.133/2021 — Contratos & Sanções",
            details: "Contratação direta (inexigibilidade vs dispensa), contratos administrativos, alteração, fiscalização e sanções.",
            tasks: ["40m Inexigibilidade vs Dispensa", "20m Gestão Contratual", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Concordância Verbal & Nominal",
            details: "Regras gerais e casos especiais: verbos impessoais (haver, fazer), sujeito partitivo, porcentagem e concordância atrativa.",
            tasks: ["40m Regras de Concordância", "20m Casos Especiais", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "20 da Lei 14.133 + 10 de Concordância.",
            tasks: ["20 Questões Lei 14.133", "10 Questões Concordância", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w3_d5",
        dayLabel: "Sexta-feira",
        date: "18/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Lei Orgânica de Meruoca — Estrutura e Poderes",
            details: "Competências do Município, Poder Legislativo municipal, competências da Câmara, vereadores, inviolabilidade e processo legislativo municipal.",
            tasks: ["40m Leitura Lei Orgânica", "20m Ficha de Competências", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Matemática — Geometria Básica",
            details: "Perímetro, área de figuras planas (quadrado, retângulo, triângulo, círculo), volume de paralelepípedos.",
            tasks: ["40m Fórmulas Geométricas", "20m Exercícios de Área/Volume", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "20 de Lei Orgânica + 10 de Geometria.",
            tasks: ["20 Questões Lei Orgânica", "10 Questões Geometria", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w3_d6",
        dayLabel: "Sábado",
        date: "19/09/2026",
        blocks: [
          {
            badge: "Simulado 3 • 3h00",
            subject: "SIMULADO 3 — 40 Questões",
            details: "Simulação completa. Atenção especial às questões de Licitações e Lei Orgânica.",
            tasks: ["Executar Simulado 3", "Verificar Tempo", "Classificar Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w3_d7",
        dayLabel: "Domingo",
        date: "20/09/2026",
        blocks: [
          {
            badge: "Revisão • 2h30",
            subject: "Correção + Bateria Lei Orgânica & 14.133",
            details: "Correção do Simulado 3 + 30 questões direcionadas de Lei Orgânica e Lei 14.133. Último dia de inscrições no concurso!",
            tasks: ["Correção Simulado 3", "30 Questões LO & 14.133", "Checagem de Inscrição"]
          }
        ],
        targetQuestions: 30
      }
    ]
  },
  {
    weekNumber: 4,
    title: "Semana 4 (21/09 a 27/09)",
    focus: "Regimento Interno + Orçamento + LRF + LGPD",
    days: [
      {
        id: "w4_d1",
        dayLabel: "Segunda-feira",
        date: "21/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Regimento Interno da Câmara de Meruoca (Parte 1)",
            details: "Organização da Câmara, composição da Mesa Diretora, competências do Presidente, sessões legislativas (ordinárias, extraordinárias).",
            tasks: ["40m Leitura Regimento", "20m Esquema da Mesa Diretora", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Regência Verbal & Nominal + Crase",
            details: "Regência dos verbos comuns em concursos (visar, aspirar, assistir, obedecer), preposições obrigatórias e regras de crase.",
            tasks: ["40m Regência & Crase", "20m Casos Proibidos/Facultativos", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "20 do Regimento Interno + 10 de Regência/Crase.",
            tasks: ["20 Questões Regimento", "10 Questões Crase/Regência", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w4_d2",
        dayLabel: "Terça-feira",
        date: "22/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Regimento Interno da Câmara (Parte 2)",
            details: "Comissões, atribuições, proposições (requerimentos, indicações, moções, projetos), tramitação, quóruns de votação e plenário.",
            tasks: ["40m Proposições e Quóruns", "20m Prazos Regimentais", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "RLM — Lógica de Argumentação & Problemas",
            details: "Estrutura lógica, premissas e conclusões, problemas de contagem simples, diagramas de Venn e porcentagem aplicada.",
            tasks: ["40m Teoria e Diagramas", "20m Resolução Prática", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "20 do Regimento + 10 de RLM.",
            tasks: ["20 Questões Regimento", "10 Questões RLM", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w4_d3",
        dayLabel: "Quarta-feira",
        date: "23/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Orçamento Público — PPA, LDO e LOA",
            details: "Princípios orçamentários (anualidade, universalidade, unidade, exclusividade), PPA (4 anos), LDO (metas/diretrizes), LOA.",
            tasks: ["40m Teoria PPA/LDO/LOA", "20m Relação entre os Três", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Informática — Comunicação Digital & E-mail",
            details: "Correio eletrônico (Thunderbird, webmail, campos Cco/Cc), ferramentas de colaboração digital (WhatsApp, Telegram, Discord).",
            tasks: ["40m Ferramentas de Correio", "20m Protocolos SMTP/IMAP/POP", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 de Orçamento + 15 de Informática.",
            tasks: ["15 Questões Orçamento", "15 Questões Informática", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w4_d4",
        dayLabel: "Quinta-feira",
        date: "24/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "LRF — Lei Complementar 101/2000",
            details: "Responsabilidade fiscal, receitas públicas, despesas, limites de despesa com pessoal (Poder Legislativo), transparência e RREO/RGF.",
            tasks: ["40m Limites da LRF", "20m Gastos do Legislativo", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Colocação Pronominal",
            details: "Próclise (fatores atrativos), ênclise e mesóclise. Posição dos pronomes átonos nas locuções verbais.",
            tasks: ["40m Fatores de Próclise", "20m Regras Especiais", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 de LRF + 15 de Colocação Pronominal.",
            tasks: ["15 Questões LRF", "15 Questões Colocação", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w4_d5",
        dayLabel: "Sexta-feira",
        date: "25/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "LGPD — Lei 13.709/2018",
            details: "Dado pessoal, dado sensível, tratamento, princípios, bases legais, controlador, operador, encarregado (DPO) e direitos do titular.",
            tasks: ["40m Conceitos e Bases Legais", "20m Agentes de Tratamento", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Políticas Públicas — Conceitos e Ciclo",
            details: "Ciclo de políticas públicas (agenda, formulação, tomada de decisão, implementação, avaliação), controle e participação.",
            tasks: ["40m Ciclo de Políticas", "20m Fases de Avaliação", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 de LGPD + 15 de Políticas Públicas.",
            tasks: ["15 Questões LGPD", "15 Questões Políticas", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w4_d6",
        dayLabel: "Sábado",
        date: "26/09/2026",
        blocks: [
          {
            badge: "Simulado 4 • 3h00",
            subject: "SIMULADO 4 — 40 Questões",
            details: "Simulação de prova. Testar equilíbrio de tempo entre matérias gerais e específicas.",
            tasks: ["Executar Simulado 4", "Marcar Tempo", "Estatísticas de Acertos"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w4_d7",
        dayLabel: "Domingo",
        date: "27/09/2026",
        blocks: [
          {
            badge: "Revisão • 2h30",
            subject: "Correção + Revisão Regimento/LRF/LGPD",
            details: "Correção aprofundada do Simulado 4 e consolidação de Regimento + Orçamento/LRF + LGPD.",
            tasks: ["Correção Simulado 4", "Revisão de Artigos-Chave", "Caderno de Erros"]
          }
        ],
        targetQuestions: 20
      }
    ]
  },
  {
    weekNumber: 5,
    title: "Semana 5 (28/09 a 04/10)",
    focus: "Controle + Gestão Pública + Transparência + Políticas Públicas",
    days: [
      {
        id: "w5_d1",
        dayLabel: "Segunda-feira",
        date: "28/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Controle da Administração Pública",
            details: "Controle interno e externo (Legislativo auxiliado pelo TCE), tomada e prestação de contas, julgamento das contas do Prefeito.",
            tasks: ["40m Teoria do Controle", "20m Parecer Prévio do TCE", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Semântica & Sentido dos Vocábulos",
            details: "Sinonímia, antonímia, homonímia, paronímia, hiperonímia, hiponímia, sentido denotativo vs. conotativo.",
            tasks: ["40m Relações Semânticas", "20m Parônimos Frequentes", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 de Controle da Administração + 15 de Semântica.",
            tasks: ["15 Questões Controle", "15 Questões Semântica", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w5_d2",
        dayLabel: "Terça-feira",
        date: "29/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Responsabilidade Civil do Estado",
            details: "Art. 37, § 6º da CF/88, responsabilidade objetiva do Estado (teoria do risco administrativo), direito de regresso, excludentes.",
            tasks: ["40m Teoria da Resp. Civil", "20m Ação Regressiva e Dolo/Culpa", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Matemática — Estatística Básica",
            details: "Média aritmética simples e ponderada, moda, mediana, leitura e interpretação de gráficos e tabelas.",
            tasks: ["40m Média, Moda e Mediana", "20m Exercícios Práticos", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 de Responsabilidade Civil + 15 de Estatística.",
            tasks: ["15 Questões Resp. Civil", "15 Questões Estatística", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w5_d3",
        dayLabel: "Quarta-feira",
        date: "30/09/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Improbidade Administrativa — Lei 8.429/92",
            details: "Atos que causam enriquecimento ilícito (art. 9º), prejuízo ao erário (art. 10), atentam contra princípios (art. 11), dolo e sanções.",
            tasks: ["40m Hipóteses de Improbidade", "20m Sanções e Prazos", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Informática — Cloud Computing",
            details: "Conceitos de nuvem, modelos de serviço (IaaS, PaaS, SaaS), modelos de implantação (pública, privada, híbrida), provedores.",
            tasks: ["40m IaaS vs PaaS vs SaaS", "20m Modelos de Nuvem", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 de Improbidade + 15 de Cloud Computing.",
            tasks: ["15 Questões Improbidade", "15 Questões Cloud", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w5_d4",
        dayLabel: "Quinta-feira",
        date: "01/10/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Gestão Pública & Arquivística",
            details: "Planejamento estratégico na Câmara, gestão de processos, gestão de pessoas, gestão documental (protocolo, arquivo, guarda, eliminação).",
            tasks: ["40m Teoria de Gestão e Arquivos", "20m Fases da Gestão Documental", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Português — Figuras de Linguagem & Reescrita",
            details: "Metáfora, metonímia, antítese, paradoxo, eufemismo, hipérbole, ironia, paráfrase e reescritura de orações.",
            tasks: ["40m Figuras e Reescrita", "20m Questões de Substituição", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 de Gestão Pública/Arquivos + 15 de Figuras/Reescrita.",
            tasks: ["15 Questões Gestão", "15 Questões Português", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w5_d5",
        dayLabel: "Sexta-feira",
        date: "02/10/2026",
        blocks: [
          {
            badge: "Bloco 1 • 1h10",
            subject: "Governança, Compliance & Controle Social",
            details: "Agenda legislativa, indicadores de desempenho, transparência pública, LAI (Lei 12.527/11), ouvidoria e participação popular.",
            tasks: ["40m Teoria Governança e LAI", "20m Regras de Sigilo da LAI", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 2 • 1h10",
            subject: "Informática — Segurança da Informação",
            details: "Malware (vírus, worm, trojan, spyware, ransomware, phishing), ferramentas de proteção (antivírus, firewall) e boas práticas.",
            tasks: ["40m Ameaças e Golpes", "20m Ferramentas de Proteção", "10m Recuperação Ativa"]
          },
          {
            badge: "Bloco 3 & 4 • 1h40",
            subject: "30 Questões + Caderno de Erros",
            details: "15 de Governança/LAI + 15 de Segurança da Informação.",
            tasks: ["15 Questões LAI/Gov", "15 Questões Segurança", "30m Caderno de Erros"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w5_d6",
        dayLabel: "Sábado",
        date: "03/10/2026",
        blocks: [
          {
            badge: "Simulado 5 • Velocidade",
            subject: "SIMULADO 5 — 40 Questões (Treino de Agilidade)",
            details: "Tentar terminar entre 2h20 e 2h40 para criar margem de segurança no preenchimento do gabarito.",
            tasks: ["Executar Simulado 5", "Concluir em < 2h40", "Classificar Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w5_d7",
        dayLabel: "Domingo",
        date: "04/10/2026",
        blocks: [
          {
            badge: "Revisão • 2h30",
            subject: "Correção + Esvaziamento do Caderno de Erros",
            details: "Correção integral do Simulado 5 e revisão concentrada de todos os erros acumulados nas últimas 5 semanas.",
            tasks: ["Correção Simulado 5", "Revisão Geral do Caderno", "Reforço nos Pontos Fracos"]
          }
        ],
        targetQuestions: 20
      }
    ]
  },
  {
    weekNumber: 6,
    title: "Semana 6 (05/10 a 11/10)",
    focus: "Consolidação Máxima & Simulado Geral",
    days: [
      {
        id: "w6_d1",
        dayLabel: "Segunda-feira",
        date: "05/10/2026",
        blocks: [
          {
            badge: "Consolidação • 40 Questões",
            subject: "SUPER REVISÃO — Língua Portuguesa",
            details: "Interpretação, morfologia, sintaxe, concordância, regência, crase, pontuação e reescrita de frases.",
            tasks: ["Revisão Geral de Português", "40 Questões Português", "Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w6_d2",
        dayLabel: "Terça-feira",
        date: "06/10/2026",
        blocks: [
          {
            badge: "Consolidação • 40 Questões",
            subject: "SUPER REVISÃO — Constitucional & Proc. Legislativo",
            details: "CF arts. 1º–5º, 6º–11, 18–31, 37–41 + Tramitação de leis, comissões, sanção, veto e promulgação.",
            tasks: ["Revisão CF e Proc. Leg.", "40 Questões Constitucional/Proc.", "Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w6_d3",
        dayLabel: "Quarta-feira",
        date: "07/10/2026",
        blocks: [
          {
            badge: "Consolidação • 40 Questões",
            subject: "SUPER REVISÃO — Direito Administrativo & Lei 14.133",
            details: "Princípios, organização, atos, poderes, improbidade, controle e Lei 14.133/2021 de ponta a ponta.",
            tasks: ["Revisão Administrativo", "40 Questões Admin & 14.133", "Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w6_d4",
        dayLabel: "Quinta-feira",
        date: "08/10/2026",
        blocks: [
          {
            badge: "Consolidação • 40 Questões",
            subject: "SUPER REVISÃO — Lei Orgânica & Regimento Interno",
            details: "Competências de Meruoca, Mesa Diretora, tramitação regimental, quóruns e fiscalização parlamentar.",
            tasks: ["Fichas Lei Orgânica & Regimento", "40 Questões Leg. Municipal", "Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w6_d5",
        dayLabel: "Sexta-feira",
        date: "09/10/2026",
        blocks: [
          {
            badge: "Consolidação • 40 Questões",
            subject: "SUPER REVISÃO — Bloco Específico Completo",
            details: "LC 95/98, PPA/LDO/LOA, LRF, LGPD, LAI, gestão documental, governança e ética pública.",
            tasks: ["Revisão Tópicos Específicos", "40 Questões Variadas", "Caderno de Erros"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w6_d6",
        dayLabel: "Sábado",
        date: "10/10/2026",
        blocks: [
          {
            badge: "Simulado 6 • Oficial",
            subject: "SIMULADO 6 — PROVA COMPLETA (Condições Reais)",
            details: "Início pontual às 09h00, término às 12h00. 40 questões, caneta transparente, sem consultas e sem celular.",
            tasks: ["Executar Simulado 09h–12h", "Preencher Gabarito", "Auditoria de Acertos"]
          }
        ],
        targetQuestions: 40
      },
      {
        id: "w6_d7",
        dayLabel: "Domingo",
        date: "11/10/2026",
        blocks: [
          {
            badge: "Diagnóstico",
            subject: "DIAGNÓSTICO FINAL & TABELA DE DESEMPENHO",
            details: "Preencher tabela de aproveitamento por disciplina para orientar as revisões cirúrgicas da última semana.",
            tasks: ["Preencher Diagnóstico Final", "Mapear Pontos Críticos (<80%)", "Plano da Semana 7"]
          }
        ],
        targetQuestions: 20
      }
    ]
  },
  {
    weekNumber: 7,
    title: "Semana 7 (12/10 a 18/10)",
    focus: "Reta Final, Super Revisão & Prova Oficial (18/10)",
    days: [
      {
        id: "w7_d1",
        dayLabel: "Segunda-feira",
        date: "12/10/2026",
        blocks: [
          {
            badge: "Reta Final",
            subject: "Constitucional + Administrativo + 30 Questões",
            details: "Manhã: Arts. 1º a 31 da CF. Tarde: Atos e Poderes. Noite: 30 questões de fixação.",
            tasks: ["Manhã: Constitucional", "Tarde: Administrativo", "Noite: 30 Questões"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w7_d2",
        dayLabel: "Terça-feira",
        date: "13/10/2026",
        blocks: [
          {
            badge: "Reta Final",
            subject: "Lei Orgânica + Regimento Interno + 30 Questões",
            details: "Manhã: Competências e Prazos LO. Tarde: Comissões e Quóruns RI. Noite: 30 questões municipais.",
            tasks: ["Manhã: Lei Orgânica", "Tarde: Regimento Interno", "Noite: 30 Questões"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w7_d3",
        dayLabel: "Quarta-feira",
        date: "14/10/2026",
        blocks: [
          {
            badge: "Reta Final",
            subject: "Lei 14.133/2021 + Processo Legislativo + LC 95",
            details: "Manhã: Contratação direta e licitações. Tarde: Espécies e LC 95. Noite: 30 questões.",
            tasks: ["Manhã: Lei 14.133", "Tarde: Proc. Leg. + LC 95", "Noite: 30 Questões"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w7_d4",
        dayLabel: "Quinta-feira",
        date: "15/10/2026",
        blocks: [
          {
            badge: "Reta Final",
            subject: "Português + Informática + Matemática (Divulgação dos Locais)",
            details: "Manhã: Português. Tarde: Informática & Fórmulas de RLM. Noite: 30 questões. Conferir local e sala da prova!",
            tasks: ["Manhã: Português", "Tarde: Info + Matemática", "Conferir Local da Prova"]
          }
        ],
        targetQuestions: 30
      },
      {
        id: "w7_d5",
        dayLabel: "Sexta-feira",
        date: "16/10/2026",
        blocks: [
          {
            badge: "Super Revisão",
            subject: "CADERNO DE ERROS & FLASHCARDS (Zero Assunto Novo)",
            details: "Revisar unicamente o caderno de erros, artigos sublinhados e pegadinhas clássicas da banca.",
            tasks: ["Revisão Geral do Caderno de Erros", "Leitura de Flashcards", "Descanso Mental"]
          }
        ],
        targetQuestions: 0
      },
      {
        id: "w7_d6",
        dayLabel: "Sábado",
        date: "17/10/2026",
        blocks: [
          {
            badge: "Véspera",
            subject: "VÉSPERA DE PROVA — Leveza & Logística",
            details: "Máximo 2 horas de leitura relaxada (LO e Regimento). Separar: RG, canetas transparentes preta/azul, água e lanche leve. Dormir cedo.",
            tasks: ["Revisão Leve (máx 2h)", "Separar Documento & Canetas", "Dormir Cedo"]
          }
        ],
        targetQuestions: 0
      },
      {
        id: "w7_d7",
        dayLabel: "Domingo",
        date: "18/10/2026",
        blocks: [
          {
            badge: "DIA DA PROVA",
            subject: "PROVA OBJETIVA — CÂMARA DE MERUOCA (09h às 12h)",
            details: "Portões abrem às 08h00 e fecham às 08h40. Estratégia de 3 passagens (Fáceis -> Médias -> Difíceis). Sucesso e foco total!",
            tasks: ["08h00: Chegada ao Local", "09h00: Início da Prova", "11h40: Preencher Gabarito", "12h00: Conclusão"]
          }
        ],
        targetQuestions: 40
      }
    ]
  }
];

const DEFAULT_ERRORS = [
  {
    id: "err_q6_ms",
    date: new Date().toLocaleDateString('pt-BR'),
    disciplina: "D. Constitucional",
    assunto: "Questão 6 — Mandado de Segurança (Conceito e Cabimento)",
    tipo: "interpretacao",
    conceito: "O que errou: Identificação do remédio cabível.\n\nSe violou direito documentado (líquido e certo) e não envolve cadeia/locomoção (HC) nem dados pessoais em cadastros públicos (HD), a resposta sempre será Mandado de Segurança (Art. 5º, LXIX da CF/88).",
    pegadinha: "Regra de ouro: Direito líquido e certo contra autoridade pública não amparado por HC/HD = MANDADO DE SEGURANÇA.",
    revisado: false
  },
  {
    id: "err_q7_ms_prazo",
    date: new Date().toLocaleDateString('pt-BR'),
    disciplina: "D. Constitucional",
    assunto: "Questão 7 — Mandado de Segurança (Prazo Decadencial)",
    tipo: "esqueci",
    conceito: "O que errou: Prazo decadencial para impetração.\n\nO prazo para impetrar Mandado de Segurança é de exatamente 120 dias corridos contados da ciência oficial do ato impugnado (Lei 12.016/09, Art. 23).",
    pegadinha: "Regra de ouro: Passou de 120 dias, extingue-se o direito de impetrar MS (prazo decadencial improrrogável).",
    revisado: false
  },
  {
    id: "err_q15_juri",
    date: new Date().toLocaleDateString('pt-BR'),
    disciplina: "D. Constitucional",
    assunto: "Questão 15 — Tribunal do Júri (Art. 5º, XXXVIII, 'd')",
    tipo: "duvida",
    conceito: "O que errou: Competência do júri popular.\n\nO Tribunal do Júri julga única e exclusivamente crimes DOLOSOS CONTRA A VIDA (homicídio doloso, aborto, infanticídio e induzimento/auxílio ao suicídio).",
    pegadinha: "Regra de ouro: O Júri NÃO julga roubo, acidente de trânsito culposo nem corrupção de servidor público.",
    revisado: false
  },
  {
    id: "err_q20_editorial",
    date: new Date().toLocaleDateString('pt-BR'),
    disciplina: "Língua Portuguesa",
    assunto: "Questão 20 — Gênero Textual: Editorial",
    tipo: "interpretacao",
    conceito: "O que errou: Diferença entre Editorial e Artigo de Opinião.\n\nO Editorial expressa a opinião e o posicionamento institucional da empresa jornalística/órgão e NÃO leva assinatura individual.",
    pegadinha: "Regra de ouro: Se tem a visão institucional e não tem assinatura = EDITORIAL. Se é assinado por articulista/colunista = ARTIGO DE OPINIÃO.",
    revisado: false
  },
  {
    id: "err_q22_funcao_conotativa",
    date: new Date().toLocaleDateString('pt-BR'),
    disciplina: "Língua Portuguesa",
    assunto: "Questão 22 — Funções da Linguagem: Conotativa / Apelativa",
    tipo: "duvida",
    conceito: "O que errou: Identificação da função da linguagem em textos instrucionais e cartazes.\n\nA função Conotativa (ou Apelativa) é centrada no receptor, utilizando verbos no imperativo e vocativos para orientar, convencer ou ordenar uma ação ('Economize', 'Apague').",
    pegadinha: "Regra de ouro: Verbos no imperativo dando ordens, instruções ou conselhos = FUNÇÃO CONOTATIVA (APELATIVA).",
    revisado: false
  },
  {
    id: "err_q24_divulgacao_cientifica",
    date: new Date().toLocaleDateString('pt-BR'),
    disciplina: "Língua Portuguesa",
    assunto: "Questão 24 — Gênero Textual: Artigo de Divulgação Científica",
    tipo: "nao-sabia",
    conceito: "O que errou: Finalidade do artigo de divulgação científica.\n\nSua finalidade essencial é transmitir o conhecimento e descobertas científicas para a população leiga em geral, utilizando linguagem clara, acessível e informativa.",
    pegadinha: "Regra de ouro: Divulgação científica não é ficção nem texto jurídico; é traduzir a ciência complexa para o público geral.",
    revisado: false
  }
];

// Estado Geral da Aplicação
let appState = {
  theme: 'light',
  checkedTasks: {},
  dayQuestions: {},
  quizAnswers: {},
  bankVersion: 3,
  quizCategoryFilter: 'w4_d1',
  quizOrderMode: 'random', // 'random', 'interleaved', 'sequential'
  quizFilterStatus: 'all', // 'all', 'pending', 'wrong'
  quizShuffledOrder: {}, // armazena ordem embaralhada por chave de filtro para manter estabilidade
  currentFlashcardIndex: 0,
  flashcardFilter: 'all',
  masteredFlashcards: {},
  cadernoErros: [...DEFAULT_ERRORS],
  simulados: [
    { num: 1, date: "05/09/2026", acertos: 0, total: 40, tempo: "3h00" },
    { num: 2, date: "12/09/2026", acertos: 0, total: 40, tempo: "3h00" },
    { num: 3, date: "19/09/2026", acertos: 0, total: 40, tempo: "3h00" },
    { num: 4, date: "26/09/2026", acertos: 0, total: 40, tempo: "3h00" },
    { num: 5, date: "03/10/2026", acertos: 0, total: 40, tempo: "2h35" },
    { num: 6, date: "10/10/2026", acertos: 0, total: 40, tempo: "2h50" }
  ],
  diagnostico: {
    portugues: { acertos: 0, total: 40 },
    informatica: { acertos: 0, total: 20 },
    matematica: { acertos: 0, total: 20 },
    constitucional: { acertos: 0, total: 30 },
    administrativo: { acertos: 0, total: 30 },
    especificos: { acertos: 0, total: 40 },
    legislacao: { acertos: 0, total: 40 }
  },
  currentWeek: 3
};

// Inicialização Geral
document.addEventListener('DOMContentLoaded', () => {
  loadState();
  initTheme();
  setupNavigation();
  setupCountdown();
  renderWeekPills();
  renderDaysForWeek(appState.currentWeek);
  selectQuizDay(appState.quizCategoryFilter || 'w3_d5');
  renderFlashcard();
  renderCadernoErros();
  renderSimulados();
  renderDiagnostico();
  updateGlobalMetrics();
  setupTimer();
  setupErrorForm();
  initEditalVerticalizado();
});

// Persistência
function saveState() {
  localStorage.setItem('meruoca_study_state', JSON.stringify(appState));
  updateGlobalMetrics();
}

function loadState() {
  const saved = localStorage.getItem('meruoca_study_state');
  if (saved) {
    try {
      const parsed = JSON.parse(saved);
      appState = { ...appState, ...parsed };
      if (appState.bankVersion !== 3) {
        appState.bankVersion = 3;
        appState.quizAnswers = {};
        appState.quizShuffledOrder = {};
        saveState();
      }
      if (!appState.lastSeenDay || (appState.lastSeenDay !== 'w4_d1' && appState.lastSeenDay !== 'ouro')) {
        appState.quizCategoryFilter = 'w4_d1';
        appState.lastSeenDay = 'w4_d1';
      }
      if (!appState.currentWeek || appState.currentWeek === 1 || appState.currentWeek === 2) {
        appState.currentWeek = 3;
      }
      if (!appState.flashcardFilter || appState.flashcardFilter === 'dia4') {
        appState.flashcardFilter = 'all';
      }
      if (!appState.quizAnswers) appState.quizAnswers = {};
      if (!appState.quizOrderMode) appState.quizOrderMode = 'random';
      if (!appState.quizFilterStatus) appState.quizFilterStatus = 'all';
      if (!appState.quizShuffledOrder) appState.quizShuffledOrder = {};
      if (!appState.masteredFlashcards) appState.masteredFlashcards = {};
      if (!appState.cadernoErros || appState.cadernoErros.length === 0) {
        appState.cadernoErros = [...DEFAULT_ERRORS];
      } else {
        // Garantir que os 3 erros chave existam no array
        DEFAULT_ERRORS.forEach(defErr => {
          if (!appState.cadernoErros.some(e => e.id === defErr.id)) {
            appState.cadernoErros.unshift(defErr);
          }
        });
      }
    } catch (e) {
      console.error("Erro ao carregar dados do LocalStorage", e);
    }
  }
}

// Alternância de Tema
function initTheme() {
  document.documentElement.setAttribute('data-theme', appState.theme);
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.innerHTML = appState.theme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    themeToggle.addEventListener('click', () => {
      appState.theme = appState.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', appState.theme);
      themeToggle.innerHTML = appState.theme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
      saveState();
    });
  }
}

// Navegação
function setupNavigation() {
  const allNavBtns = document.querySelectorAll('.nav-btn, .mobile-nav-btn:not(#mobileMenuBtn)');
  const tabPanes = document.querySelectorAll('.tab-pane');
  const sidebar = document.getElementById('sidebar');
  const sidebarBackdrop = document.getElementById('sidebarBackdrop');
  const menuToggle = document.getElementById('menuToggle');
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');

  function openSidebar() {
    if (sidebar) sidebar.classList.add('open');
    if (sidebarBackdrop) sidebarBackdrop.classList.add('active');
  }

  function closeSidebar() {
    if (sidebar) sidebar.classList.remove('open');
    if (sidebarBackdrop) sidebarBackdrop.classList.remove('active');
  }

  allNavBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.dataset.tab;
      if (!tabId) return;

      // Sincronizar todos os botões com o mesmo data-tab
      allNavBtns.forEach(b => {
        if (b.dataset.tab === tabId) b.classList.add('active');
        else b.classList.remove('active');
      });

      // Alternar visualização da aba
      tabPanes.forEach(pane => pane.classList.remove('active'));
      const targetPane = document.getElementById(tabId);
      if (targetPane) {
        targetPane.classList.add('active');
      }

      // Fechar a sidebar móvel caso esteja aberta
      closeSidebar();

      // Scroll suave para o topo ao trocar de aba
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  });

  // Toggle do menu via botão superior
  if (menuToggle) {
    menuToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      if (sidebar && sidebar.classList.contains('open')) {
        closeSidebar();
      } else {
        openSidebar();
      }
    });
  }

  // Toggle do menu via botão "Mais" da bottom nav no mobile
  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (sidebar && sidebar.classList.contains('open')) {
        closeSidebar();
      } else {
        openSidebar();
      }
    });
  }

  // Fechar ao tocar no backdrop escuro
  if (sidebarBackdrop) {
    sidebarBackdrop.addEventListener('click', () => {
      closeSidebar();
    });
  }
}

// Countdown
function setupCountdown() {
  const examDate = new Date('2026-10-18T09:00:00-03:00').getTime();

  function update() {
    const now = new Date().getTime();
    const diff = examDate - now;

    if (diff <= 0) {
      document.getElementById('cdDays').innerText = "00";
      document.getElementById('cdHours').innerText = "00";
      document.getElementById('cdMins').innerText = "00";
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

    document.getElementById('cdDays').innerText = String(days).padStart(2, '0');
    document.getElementById('cdHours').innerText = String(hours).padStart(2, '0');
    document.getElementById('cdMins').innerText = String(mins).padStart(2, '0');
  }

  update();
  setInterval(update, 60000);
}

// =========================================================================
// MÓDULO FLASHCARDS 3D
// =========================================================================
function getFilteredFlashcards() {
  if (!appState.flashcardFilter || appState.flashcardFilter === 'all') return FLASHCARDS_DATA;
  if (appState.flashcardFilter === 'semana2') {
    return FLASHCARDS_DATA.filter(fc => (fc.day && fc.day.startsWith('w2_')) || fc.id >= 48);
  }
  if (appState.flashcardFilter === 'dia4') {
    return FLASHCARDS_DATA.filter(fc => fc.day === 'dia4' || (fc.id >= 38 && fc.id <= 47));
  }
  if (appState.flashcardFilter === 'dia3') {
    return FLASHCARDS_DATA.filter(fc => fc.day === 'dia3' || (fc.id >= 23 && fc.id <= 37));
  }
  return FLASHCARDS_DATA.filter(fc => fc.category === appState.flashcardFilter);
}

function filterFlashcards(cat) {
  appState.flashcardFilter = cat;
  appState.currentFlashcardIndex = 0;
  
  document.querySelectorAll('.flashcard-filter-btn').forEach(btn => {
    const onclickStr = btn.getAttribute('onclick') || '';
    const isActive = onclickStr.includes("'" + cat + "'");
    btn.classList.toggle('btn-primary', isActive);
    btn.classList.toggle('btn-secondary', !isActive);
  });
  
  renderFlashcard();
}

function renderFlashcard() {
  const cards = getFilteredFlashcards();
  const cardEl = document.getElementById('activeFlashcard');
  if (!cardEl || cards.length === 0) return;

  if (appState.currentFlashcardIndex >= cards.length) {
    appState.currentFlashcardIndex = 0;
  }

  const current = cards[appState.currentFlashcardIndex];
  cardEl.classList.remove('is-flipped');

  document.getElementById('fcTag').innerText = current.tag;
  document.getElementById('fcQuestion').innerText = current.question;
  document.getElementById('fcAnswer').innerText = current.answer;
  document.getElementById('fcExplanation').innerText = current.explanation;

  const curIdxEl = document.getElementById('fcCurrentIndex');
  const totCardsEl = document.getElementById('fcTotalCards');
  const masteredEl = document.getElementById('fcMasteredCount');

  if (curIdxEl) curIdxEl.innerText = `${appState.currentFlashcardIndex + 1}`;
  if (totCardsEl) totCardsEl.innerText = `${cards.length}`;
  if (masteredEl) masteredEl.innerText = `${Object.keys(appState.masteredFlashcards).length}`;
}

function flipFlashcard() {
  const selection = window.getSelection();
  if (selection && selection.toString().trim().length > 0) return;
  const card = document.getElementById('activeFlashcard');
  if (card) card.classList.toggle('is-flipped');
}

function copyCurrentFlashcard() {
  const cards = getFilteredFlashcards();
  if (!cards || cards.length === 0) return;
  const current = cards[appState.currentFlashcardIndex || 0];
  if (!current) return;

  const textToCopy = `🎴 Flashcard - ${current.tag}:\n\n❓ Pergunta: ${current.question}\n\n✅ Resposta: ${current.answer}\n\n💡 Explicação: ${current.explanation}`;

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(textToCopy).then(() => {
      showToast("📋 Conteúdo do Flashcard copiado!");
    }).catch(() => {
      fallbackCopyText(textToCopy);
    });
  } else {
    fallbackCopyText(textToCopy);
  }
}

function nextFlashcard() {
  const cards = getFilteredFlashcards();
  if (appState.currentFlashcardIndex < cards.length - 1) {
    appState.currentFlashcardIndex++;
  } else {
    appState.currentFlashcardIndex = 0;
  }
  renderFlashcard();
}

function prevFlashcard() {
  const cards = getFilteredFlashcards();
  if (appState.currentFlashcardIndex > 0) {
    appState.currentFlashcardIndex--;
  } else {
    appState.currentFlashcardIndex = cards.length - 1;
  }
  renderFlashcard();
}

function shuffleFlashcards() {
  const cards = getFilteredFlashcards();
  appState.currentFlashcardIndex = Math.floor(Math.random() * cards.length);
  renderFlashcard();
  showToast("🔀 Cartões embaralhados!");
}

function markCardMastery(isMastered) {
  const cards = getFilteredFlashcards();
  const current = cards[appState.currentFlashcardIndex];
  if (isMastered) {
    appState.masteredFlashcards[current.id] = true;
    showToast("🎉 Excelente! Marcado como Dominado.");
  } else {
    delete appState.masteredFlashcards[current.id];
    showToast("📌 Marcado para revisão.");
  }
  saveState();
  nextFlashcard();
}

function filterFlashcards(cat) {
  appState.flashcardFilter = cat;
  appState.currentFlashcardIndex = 0;
  renderFlashcard();
}

// =========================================================================
// MÓDULO QUIZ INTERATIVO (ALEATORIEDADE & ORDEM INTELIGENTE)
// =========================================================================

// Algoritmo Fisher-Yates para embaralhamento de alta qualidade
function shuffleArray(arr) {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

// Algoritmo para intercalar matérias balanceadamente (round-robin entre disciplinas)
function interleaveQuestionsByDiscipline(questions) {
  const groups = {};
  questions.forEach(q => {
    const disc = q.discipline || 'Geral';
    if (!groups[disc]) groups[disc] = [];
    groups[disc].push(q);
  });

  // Embaralhar internamente as questões de cada disciplina
  const disciplines = Object.keys(groups);
  disciplines.forEach(disc => {
    groups[disc] = shuffleArray(groups[disc]);
  });

  // Embaralhar a ordem inicial das disciplinas para não começar sempre com a mesma
  const shuffledDisciplines = shuffleArray(disciplines);

  const result = [];
  let remaining = questions.length;

  while (remaining > 0) {
    for (let i = 0; i < shuffledDisciplines.length; i++) {
      const disc = shuffledDisciplines[i];
      if (groups[disc] && groups[disc].length > 0) {
        result.push(groups[disc].shift());
        remaining--;
      }
    }
  }

  return result;
}

// Retorna as questões base do filtro ativo
function getFilteredBaseQuestions(filterKey) {
  if (filterKey === 'all') return QUIZ_QUESTIONS_DATA;
  if (filterKey === 'reforco_port') return QUIZ_QUESTIONS_DATA.filter(q => (q.id >= 361 && q.id <= 380) || (q.id >= 401 && q.id <= 420));
  if (filterKey === 'resgatao') return QUIZ_QUESTIONS_DATA.filter(q => (q.id >= 361 && q.id <= 380) || (q.id >= 401 && q.id <= 420) || (q.id >= 424 && q.id <= 520));
  if (filterKey === 'ouro') return QUIZ_QUESTIONS_DATA.filter(q => [362,363,364,367,368,370,372,375,378,380,401,402,403,404,405,406,409,410,411,413,418,419,511,512,513,514,515,516,517,518,519,520,424,425,428,429,431,432,433,435,436,439,440,441,442,443,444,445,447,449,450,455,457,459,460,461,463,465,469,471,473,474,477,478,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,481,483,484,485,486].includes(q.id));
  if (filterKey === 'dia2') return QUIZ_QUESTIONS_DATA.filter(q => q.day === 'dia2' || (q.id >= 1 && q.id <= 30));
  const byDay = QUIZ_QUESTIONS_DATA.filter(q => q.day === filterKey);
  if (byDay.length > 0) return byDay;
  return QUIZ_QUESTIONS_DATA.filter(q => q.category === filterKey);
}

// Retorna as questões organizadas conforme o modo de ordenação e com persistência de ordem
function getOrderedQuestions(filterKey) {
  const baseQuestions = getFilteredBaseQuestions(filterKey);
  const mode = appState.quizOrderMode || 'random';

  if (mode === 'sequential') {
    return [...baseQuestions].sort((a, b) => a.id - b.id);
  }

  const orderKey = `${filterKey}_${mode}`;
  const baseIds = baseQuestions.map(q => q.id);

  // Verificar se já temos uma ordem válida armazenada para este filtro e modo
  const storedIds = appState.quizShuffledOrder ? appState.quizShuffledOrder[orderKey] : null;
  const isOrderValid = Array.isArray(storedIds) && 
    storedIds.length === baseIds.length && 
    baseIds.every(id => storedIds.includes(id));

  if (isOrderValid) {
    const qMap = new Map(baseQuestions.map(q => [q.id, q]));
    return storedIds.map(id => qMap.get(id)).filter(Boolean);
  }

  // Se não existir ou for inválida, gerar nova ordem
  let orderedList = [];
  if (mode === 'interleaved') {
    orderedList = interleaveQuestionsByDiscipline(baseQuestions);
  } else {
    // modo 'random' padrão
    orderedList = shuffleArray(baseQuestions);
  }

  // Armazenar os IDs ordenados para manter estabilidade enquanto o usuário responde
  if (!appState.quizShuffledOrder) appState.quizShuffledOrder = {};
  appState.quizShuffledOrder[orderKey] = orderedList.map(q => q.id);
  saveState();

  return orderedList;
}

// Forçar um novo embaralhamento das questões ativas
function shuffleActiveQuiz() {
  const filterKey = appState.quizCategoryFilter || 'dia6';
  const mode = appState.quizOrderMode || 'random';

  if (!appState.quizShuffledOrder) appState.quizShuffledOrder = {};
  delete appState.quizShuffledOrder[`${filterKey}_random`];
  delete appState.quizShuffledOrder[`${filterKey}_interleaved`];

  saveState();
  renderQuiz();

  const modeLabel = mode === 'interleaved' ? 'intercaladas por disciplina' : 'embaralhadas aleatoriamente';
  showToast(`🔀 Questões ${modeLabel}!`);
}

// Alterar o modo de ordenação (random, interleaved, sequential)
function setQuizOrderMode(mode) {
  appState.quizOrderMode = mode;
  saveState();
  renderQuiz();

  if (mode === 'random') {
    showToast("🔀 Modo Aleatório ativado: questões embaralhadas!");
  } else if (mode === 'interleaved') {
    showToast("⚖️ Modo Intercalado ativado: matérias alternadas como na prova!");
  } else {
    showToast("🔢 Modo Sequencial ativado: ordem numérica padrão.");
  }
}

// Filtrar por status (todas, pendentes, erros)
function setQuizStatusFilter(status) {
  appState.quizFilterStatus = status;
  saveState();
  renderQuiz();
}

function renderQuiz() {
  const container = document.getElementById('quizQuestionsContainer');
  if (!container) return;

  const filterKey = appState.quizCategoryFilter || 'dia6';
  const allOrderedQuestions = getOrderedQuestions(filterKey);

  // Contagens para o bloco
  const totalInBlock = allOrderedQuestions.length;
  let totalAnswered = 0;
  let correctCount = 0;
  let wrongCount = 0;
  let pendingCount = 0;

  allOrderedQuestions.forEach(q => {
    const ans = appState.quizAnswers[q.id];
    if (ans && ans.confirmed) {
      totalAnswered++;
      if (ans.isCorrect) correctCount++;
      else wrongCount++;
    } else {
      pendingCount++;
    }
  });

  const accuracyPct = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;

  // Atualizar placar de pontuação
  const totalEl = document.getElementById('quizTotalCount');
  const corEl = document.getElementById('quizCorrectCount');
  const wrgEl = document.getElementById('quizWrongCount');
  const accEl = document.getElementById('quizAccuracyPct');

  if (totalEl) totalEl.innerText = `${totalInBlock}`;
  if (corEl) corEl.innerText = `${correctCount}`;
  if (wrgEl) wrgEl.innerText = `${wrongCount}`;
  if (accEl) accEl.innerText = `${accuracyPct}%`;

  // Atualizar botões de modo de ordenação
  const orderMode = appState.quizOrderMode || 'random';
  const btnRandom = document.getElementById('btnOrderRandom');
  const btnInterleaved = document.getElementById('btnOrderInterleaved');
  const btnSequential = document.getElementById('btnOrderSequential');

  if (btnRandom) btnRandom.classList.toggle('active', orderMode === 'random');
  if (btnInterleaved) btnInterleaved.classList.toggle('active', orderMode === 'interleaved');
  if (btnSequential) btnSequential.classList.toggle('active', orderMode === 'sequential');

  // Atualizar filtros de status
  const statusFilter = appState.quizFilterStatus || 'all';
  const btnStatusAll = document.getElementById('btnStatusAll');
  const btnStatusPending = document.getElementById('btnStatusPending');
  const btnStatusWrong = document.getElementById('btnStatusWrong');

  if (btnStatusAll) btnStatusAll.classList.toggle('active', statusFilter === 'all');
  if (btnStatusPending) btnStatusPending.classList.toggle('active', statusFilter === 'pending');
  if (btnStatusWrong) btnStatusWrong.classList.toggle('active', statusFilter === 'wrong');

  const cntAll = document.getElementById('quizStatusAllCount');
  const cntPending = document.getElementById('quizStatusPendingCount');
  const cntWrong = document.getElementById('quizStatusWrongCount');

  if (cntAll) cntAll.innerText = `${totalInBlock}`;
  if (cntPending) cntPending.innerText = `${pendingCount}`;
  if (cntWrong) cntWrong.innerText = `${wrongCount}`;

  // Filtrar as questões exibidas de acordo com o status selecionado
  let displayQuestions = allOrderedQuestions;
  if (statusFilter === 'pending') {
    displayQuestions = allOrderedQuestions.filter(q => !appState.quizAnswers[q.id]?.confirmed);
  } else if (statusFilter === 'wrong') {
    displayQuestions = allOrderedQuestions.filter(q => appState.quizAnswers[q.id]?.confirmed && !appState.quizAnswers[q.id]?.isCorrect);
  }

  // Estado vazio quando não houver questões no filtro
  if (displayQuestions.length === 0) {
    let emptyMsg = "Nenhuma questão encontrada para os filtros selecionados.";
    let emptyIcon = "fas fa-info-circle";
    let emptyAction = "";

    if (statusFilter === 'pending') {
      emptyMsg = "🎉 Parabéns! Você já respondeu todas as questões deste bloco!";
      emptyIcon = "fas fa-check-circle";
      emptyAction = `<button class="btn btn-secondary" onclick="setQuizStatusFilter('all')" style="margin-top: 12px;"><i class="fas fa-eye"></i> Ver Todas as Questões</button>`;
    } else if (statusFilter === 'wrong') {
      emptyMsg = "Excelente! Você não possui nenhum erro registrado neste bloco.";
      emptyIcon = "fas fa-medal";
      emptyAction = `<button class="btn btn-secondary" onclick="setQuizStatusFilter('all')" style="margin-top: 12px;"><i class="fas fa-eye"></i> Ver Todas as Questões</button>`;
    }

    container.innerHTML = `
      <div class="quiz-card" style="text-align: center; padding: 40px 20px;">
        <i class="${emptyIcon}" style="font-size: 2.5rem; color: var(--primary); margin-bottom: 14px;"></i>
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 8px;">${emptyMsg}</h3>
        <p style="font-size: 0.88rem; color: var(--text-muted); max-width: 500px; margin: 0 auto;">Alterne o filtro ou reembaralhe as questões para continuar praticando.</p>
        ${emptyAction}
      </div>
    `;
    return;
  }

  const letters = ['A', 'B', 'C', 'D'];

  container.innerHTML = displayQuestions.map((q, displayIdx) => {
    const ans = appState.quizAnswers[q.id] || { selected: null, confirmed: false, isCorrect: false };
    const isConfirmed = ans.confirmed;

    return `
      <div class="quiz-card" id="quiz_card_${q.id}">
        <div class="quiz-card-header">
          <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
            <span class="quiz-pos-badge">Questão ${displayIdx + 1} de ${displayQuestions.length}</span>
            <span class="quiz-id-badge">ID ${q.id}</span>
            <button class="btn btn-secondary" style="font-size: 0.72rem; padding: 2px 7px; border-radius: var(--radius-sm); margin-left: 4px;" onclick="copyQuizQuestion(${q.id})" title="Copiar questão para a área de transferência">
              <i class="fas fa-copy"></i> Copiar
            </button>
          </div>
          <span class="quiz-discipline-tag">${q.discipline} • ${q.topic}</span>
        </div>

        <div class="quiz-question-text">
          ${q.question}
        </div>

        <div class="quiz-options-list">
          ${q.options.map((opt, optIdx) => {
            let optClass = "";
            if (isConfirmed) {
              if (optIdx === q.correctAnswer) {
                optClass = "correct";
              } else if (ans.selected === optIdx && !ans.isCorrect) {
                optClass = "wrong";
              }
            } else if (ans.selected === optIdx) {
              optClass = "selected";
            }

            return `
              <div class="quiz-option ${optClass} ${isConfirmed ? 'disabled' : ''}" onclick="selectQuizOption(${q.id}, ${optIdx})">
                <span class="option-letter">${letters[optIdx]}</span>
                <span>${opt}</span>
              </div>
            `;
          }).join('')}
        </div>

        <div class="quiz-card-footer">
          <div>
            ${!isConfirmed ? `
              <button class="btn btn-primary" onclick="confirmQuizAnswer(${q.id})" ${ans.selected === null ? 'disabled style="opacity: 0.5; cursor: not-allowed;"' : ''}>
                <i class="fas fa-check"></i> Confirmar Resposta
              </button>
            ` : `
              <span style="font-size: 0.9rem; font-weight: 700; color: ${ans.isCorrect ? 'var(--success)' : 'var(--danger)'};">
                ${ans.isCorrect ? '✓ Resposta Correta! (+2,5 pts)' : '✗ Resposta Incorreta'}
              </span>
            `}
          </div>

          <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
            ${isConfirmed ? `
              <button class="btn btn-secondary" style="font-size: 0.8rem; padding: 6px 12px;" onclick="copyQuizQuestion(${q.id})" title="Copiar questão com resposta e gabarito">
                <i class="fas fa-copy"></i> Copiar Resposta & Gabarito
              </button>
            ` : ''}

            ${isConfirmed && !ans.isCorrect ? `
              <button class="btn btn-danger" style="font-size: 0.8rem; padding: 6px 12px;" onclick="addQuizErrorToBook(${q.id})">
                <i class="fas fa-plus-circle"></i> Adicionar ao Caderno de Erros
              </button>
            ` : ''}
          </div>
        </div>

        <div class="quiz-explanation-box ${isConfirmed ? 'show' : ''} ${ans.isCorrect ? 'correct-border' : 'wrong-border'}">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <strong><i class="fas fa-comment-dots" style="color: var(--primary);"></i> Gabarito Oficial Comentado (${letters[q.correctAnswer]}):</strong>
            <button class="btn btn-secondary" style="font-size: 0.72rem; padding: 2px 7px;" onclick="copyQuizQuestion(${q.id})" title="Copiar comentário">
              <i class="fas fa-copy"></i> Copiar
            </button>
          </div>
          <p style="margin-top: 4px;">${q.commentary}</p>
        </div>
      </div>
    `;
  }).join('');
}

function copyQuizQuestion(qId) {
  const q = QUIZ_QUESTIONS_DATA.find(item => item.id === qId);
  if (!q) return;
  const letters = ['A', 'B', 'C', 'D'];
  const ans = appState.quizAnswers[q.id];
  const isConfirmed = ans && ans.confirmed;

  let textToCopy = `📌 Questão ${q.id} - ${q.discipline} (${q.topic}):\n${q.question}\n\n`;
  textToCopy += q.options.map((opt, i) => `${letters[i]}) ${opt}`).join('\n');

  if (isConfirmed) {
    const correctLetter = letters[q.correctAnswer];
    const correctText = q.options[q.correctAnswer];
    textToCopy += `\n\n✅ Gabarito Oficial: (${correctLetter}) ${correctText}\n\n💡 Comentário: ${q.commentary}`;
  }

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(textToCopy).then(() => {
      showToast("📋 Questão e resposta copiadas com sucesso!");
    }).catch(() => {
      fallbackCopyText(textToCopy);
    });
  } else {
    fallbackCopyText(textToCopy);
  }
}

function fallbackCopyText(text) {
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.select();
  try {
    document.execCommand('copy');
    showToast("📋 Questão e resposta copiadas!");
  } catch (err) {
    showToast("Erro ao copiar.");
  }
  document.body.removeChild(ta);
}

function selectQuizOption(qId, optIdx) {
  if (appState.quizAnswers[qId] && appState.quizAnswers[qId].confirmed) return;
  appState.quizAnswers[qId] = {
    selected: optIdx,
    confirmed: false,
    isCorrect: false
  };
  saveState();
  renderQuiz();
}

function getQuestionDayKey(q) {
  if (q.day) {
    if (q.day === 'dia3') return 'w1_d3';
    if (q.day === 'dia4') return 'w1_d4';
    if (q.day === 'dia5') return 'w1_d5';
    if (q.day === 'dia6') return 'w1_d6';
    return q.day;
  }
  if (q.category === 'constitucional' && q.id <= 15) return 'w1_d1';
  if (q.category === 'portugues' && q.id <= 30) return 'w1_d2';
  return 'w1_d1';
}

function confirmQuizAnswer(qId) {
  const q = QUIZ_QUESTIONS_DATA.find(item => item.id === qId);
  if (!q) return;

  const current = appState.quizAnswers[qId];
  if (!current || current.selected === null) return;

  const isCorrect = current.selected === q.correctAnswer;
  appState.quizAnswers[qId] = {
    selected: current.selected,
    confirmed: true,
    isCorrect: isCorrect
  };

  const dayId = getQuestionDayKey(q);
  if (!appState.dayQuestions[dayId]) {
    appState.dayQuestions[dayId] = { done: 0, correct: 0 };
  }
  appState.dayQuestions[dayId].done++;
  if (isCorrect) appState.dayQuestions[dayId].correct++;

  saveState();
  renderQuiz();
  renderDaysForWeek(appState.currentWeek);

  if (isCorrect) {
    showToast(`✓ Parabéns! Questão ${qId} correta.`);
  } else {
    showToast(`✗ Questão ${qId} incorreta. Gabarito: ${['A','B','C','D'][q.correctAnswer]}`);
  }
}

function filterQuizCategory(cat) {
  appState.quizCategoryFilter = cat;
  renderQuiz();
}

const QUIZ_DAYS_CONFIG = {
          w4_d1: {
    title: "⭐ Semana 4 • Dia 1 — Segunda-feira (21/09/2026 - HOJE): Regimento & Regência (18 Questões)",
    desc: "12 questões de Regimento Interno (Mesa, Presidente, sessões e comissões) + 6 questões de Língua Portuguesa (Regência Verbal & Nominal). Formato enxuto, padrão réplica fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_04_DIA_01_21_09_2026.html",
    bookletLabel: "Abrir Caderno Hoje Impresso (PDF)"
  },
          simReal: {
    title: "⭐ SIMULADO REAL — Ipaporanga/CE 2026 (29 Questões verídicas INBRASP)",
    desc: "29 questões reais transcritas com nº QConcursos: 10 Português + 4 Matemática + 1 Informática + 14 Específicas (Administrativo, Constitucional, Arquivologia e Gestão). Cronometre 2h15. Gabarito oficial da banca.",
    bookletUrl: "provas/PROVA_REAL_INBRASP_2026_IPAPORANGA.html",
    bookletLabel: "Abrir Prova Real Impressa (PDF)"
  },
          w3_d5: {
    title: "⭐ Semana 3 • Dia 5 — Sexta-feira (18/09/2026 - HOJE): LO Processo Legislativo & Geometria (18 Questões)",
    desc: "10 questões de Lei Orgânica (iniciativa, tramitação, sanção, veto, promulgação e fiscalização) + 8 questões de Matemática (áreas, perímetro e volume). Padrão réplica fiel Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_03_DIA_05_18_09_2026.html",
    bookletLabel: "Abrir Caderno Hoje Impresso (PDF)"
  },
          ouro: {
    title: "⭐ ESSENCIAL OURO — 89 Questões (caminho rápido)",
    desc: "Essenciais de maior incidência + dia 17 de hoje COMPLETO (contratos, sanções e concordância). Terminou este bloco = hoje zerado. Depois complete o restante no Provão (filtro Pendentes). Mesmas questões, mesmo progresso. Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_ESSENCIAL_OURO_89Q.html",
    bookletLabel: "Abrir Essencial Impresso (PDF)"
  },
          w3_d4: {
    title: "📅 Semana 3 • Dia 4 — Quinta-feira (17/09/2026): Lei 14.133 Contratos & Concordância (30 Questões)",
    desc: "20 questões de Lei 14.133/2021 (Contratação Direta, Contratos, Fiscalização e Sanções) + 10 questões de Língua Portuguesa (Concordância Verbal & Nominal). Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_03_DIA_04_17_09_2026.html",
    bookletLabel: "Abrir Caderno Hoje Impresso (PDF)"
  },
          resgatao: {
    title: "📅 Provão de Resgate — Dias 11 + 14 + 15 + 16 + 17 (137 Questões — completo)",
    desc: "Todas as suas pendências em uma prova só: PT Sintaxe 361-380 (20) + PT Período 401-420 (20) + Admin Extinção 424-440 (17) + Matemática 441-460 (20) + Lei 14.133 461-480 (20) + Redes 481-490 (10) + Dia 17 Contratos/Concordância 491-520 (30). Faça em 4 sessões (~35Q): o app salva o progresso. Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_PROVAO_RESGATE_137Q.html",
    bookletLabel: "Abrir Provão Impresso (PDF)"
  },
          reforco_port: {
    title: "📅 Reforço — Português Dia 11 + Dia 14 mesclados (40 Questões)",
    desc: "20 questões de Sintaxe da Oração dia 11 (IDs 361-380: sujeito, transitividade, complemento x adjunto, SE, aposto, vocativo) + 20 questões de Período Composto dia 14 (IDs 401-420: coordenação, substantivas, adjetivas, adverbiais e SE). Mescladas para fazer agora. Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_REFORCO_PORTUGUES_SINTAXE_PERIODO_40Q.html",
    bookletLabel: "Abrir Caderno Reforço Mesclado (PDF)"
  },
          w3_d3: {
    title: "📅 Semana 3 • Dia 3 — Quarta-feira (16/09/2026): Lei 14.133 Licitações & Redes/Internet (30 Questões)",
    desc: "20 questões de Lei 14.133/2021 (Princípios Art. 5º, Agentes, Planejamento/ETP, Modalidades e Critérios) + 10 questões de Informática (Internet, Intranet, Navegadores Chrome/Edge/Firefox, Busca Avançada e Protocolos). Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_03_DIA_03_16_09_2026.html",
    bookletLabel: "Abrir Caderno Hoje Impresso (PDF)"
  },
          w3_d2: {
    title: "📅 Semana 3 • Dia 2 — Terça-feira (15/09/2026): Extinção de Atos & Matemática/Medidas (40 Questões)",
    desc: "20 questões de Direito Administrativo (Extinção, Invalidação e Convalidação dos Atos: Anulação, Revogação, Cassação, Caducidade, Convalidação FO-CO, Vinculação e Discricionariedade) + 20 questões de Matemática & RLM (Sistema Monetário Brasileiro, Trocos, Juros e Descontos, Sistema de Medidas: comprimento, superfície, volume, capacidade, massa e tempo). Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_03_DIA_02_15_09_2026.html",
    bookletLabel: "Abrir Caderno Hoje Impresso (PDF)"
  },
  w3_d1: {
    title: "📅 Semana 3 • Dia 1 — Segunda-feira (14/09/2026): Atos Administrativos & Período Composto (40 Questões)",
    desc: "20 questões de Direito Administrativo (Atos Administrativos: requisitos COMFIFOR, atributos PATI, mérito, classificação e espécies) + 20 questões de Língua Portuguesa (Período Composto: Coordenação e Subordinação, orações substantivas, adjetivas, adverbiais e conectivos). Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_03_DIA_01_14_09_2026.html",
    bookletLabel: "Abrir Caderno Dia 1 (PDF)"
  },
  w2_d5: {
    title: "📅 Semana 2 • Dia 5 — Sexta-feira (11/09/2026): Técnica Legislativa LC 95/98 & Sintaxe da Oração (40 Questões)",
    desc: "20 questões de Conhecimentos Específicos (Técnica Legislativa, LC 95/1998, Articulação, Alteração e Consolidação de Leis) + 20 questões de Língua Portuguesa (Sintaxe da Oração, Termos Essenciais, Integrantes e Acessórios, Transitividade e Pontuação). Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_02_DIA_05_11_09_2026.html",
    bookletLabel: "Abrir Caderno Dia 5 (PDF)"
  },
  w2_d4: {
    title: "📅 Semana 2 • Dia 4 — Quinta-feira (10/09/2026): Sessões, Representação Partidária & Matemática/RLM (40 Questões)",
    desc: "20 questões de Conhecimentos Específicos (Sessões Plenárias, Ordem do Dia, Partidos Políticos, Quociente Eleitoral e Partidário) + 20 questões de Matemática & RLM (Razão, Proporção, Regra de Três, Porcentagem e Juros Simples). Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_02_DIA_04_10_09_2026.html",
    bookletLabel: "Abrir Caderno Dia 4 (PDF)"
  },
  w2_d3: {
    title: "📅 Semana 2 • Dia 3 — Quarta-feira (09/09/2026): Processo Legislativo & Pacote Office (40 Questões)",
    desc: "20 questões de Conhecimentos Específicos (Processo Legislativo, Espécies Normativas CF art. 59, Iniciativa, Tramitação, Emendas, Substitutivos e Vetos) + 20 questões de Informática (MS Word, Excel fórmulas, PowerPoint e Google Workspace). Padrão Oficial Banca INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_02_DIA_03_09_09_2026.html",
    bookletLabel: "Abrir Caderno Dia 3 (PDF)"
  },
  w2_d2: {
    title: "📅 Semana 2 • Dia 2 — Terça-feira (08/09/2026): Funções da Câmara & Crase/Regência (40 Questões)",
    desc: "20 questões de Técnico Legislativo (Funções do Poder Legislativo, Controle e Fiscalização) + 20 questões de Português (Uso do Sinal Indicativo de Crase, Sinais de Pontuação e Regência). Padrão Oficial INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_02_DIA_02_08_09_2026.html",
    bookletLabel: "Abrir Caderno Dia 2 (PDF)"
  },
  w2_d1: {
    title: "📅 Semana 2 • Dia 1 — Segunda-feira (07/09/2026): Organização do Estado & Formação de Palavras (40 Questões)",
    desc: "20 questões de D. Constitucional (CF/88 Arts. 18 a 31: Competências, Municípios e Controle) + 20 de Português (Estrutura e Processos de Formação de Palavras). Padrão Oficial INBRASP.",
    bookletUrl: "provas/CADERNO_QUESTOES_SEMANA_02_DIA_01_07_09_2026.html",
    bookletLabel: "Abrir Caderno Dia 1 (PDF)"
  },
  dia6: {
    title: "📅 Semana 1 • Dia 6 — Sábado (05/09/2026): SIMULADO 01 OFICIAL (40 Questões)",
    desc: "Prova Completa 40Q no Padrão Oficial da Banca INBRASP (10 Português + 5 Informática + 5 RLM + 20 Específicas). Treino de cronometragem de 3 horas.",
    bookletUrl: "provas/PROVA_OFICIAL_SIMULADO_01_INBRASP.html",
    bookletLabel: "Abrir Prova Simulado 01 (PDF)"
  },
  dia5: {
    title: "📅 Semana 1 • Dia 5 — Sexta-feira (04/09/2026): D. Administrativo, Python & Lei Orgânica (40 Questões)",
    desc: "15 questões de D. Administrativo (Poderes & Atributos PATI) + 15 de Informática (Algoritmos, Fluxogramas & Python) + 10 de Lei Orgânica de Meruoca (Arts. 16 ao 30).",
    bookletUrl: "provas/CADERNO_QUESTOES_DIA_05_04_09_2026.html",
    bookletLabel: "Abrir Caderno Dia 5 (PDF)"
  },
  dia4: {
    title: "📅 Semana 1 • Dia 4 — Quinta-feira (03/09/2026): Português, Constitucional & Lei Orgânica (40 Questões)",
    desc: "15 questões de Português (Fonologia, Acentuação e Crase) + 15 de Constitucional (Direitos Sociais Arts. 6º ao 11) + 10 de Lei Orgânica de Meruoca (Arts. 1º ao 15).",
    bookletUrl: "provas/CADERNO_QUESTOES_DIA_04_03_09_2026.html",
    bookletLabel: "Abrir Caderno Dia 4 (PDF)"
  },
  dia3: {
    title: "📅 Semana 1 • Dia 3 — Quarta-feira (02/09/2026): D. Administrativo & Informática (30 Questões)",
    desc: "15 questões de Direito Administrativo (Princípios LIMPE e Organização) + 15 questões de Informática (Windows 11, Linux, Hardware e Backup).",
    bookletUrl: "provas/CENTRAL_DE_PROVAS.html",
    bookletLabel: "Abrir Central de Provas"
  },
  dia2: {
    title: "📅 Semana 1 • Dia 2 — Terça-feira (01/09/2026): D. Constitucional & Português (30 Questões)",
    desc: "15 questões de Direito Constitucional (Art. 5º e Remédios) + 15 questões de Português (Tipos e Gêneros Textuais).",
    bookletUrl: "provas/CENTRAL_DE_PROVAS.html",
    bookletLabel: "Abrir Central de Provas"
  },
  all: {
    title: "📚 Todas as Questões do Banco de Provas (585 Questões)",
    desc: "Simulado geral contendo todas as 490 questões ativas (Semanas 1 e 2 completas + Semana 3 Dias 1, 2 e 3) para treino de alta performance.",
    bookletUrl: "provas/CENTRAL_DE_PROVAS.html",
    bookletLabel: "Abrir Central de Provas & Editais"
  }
};

function selectQuizDay(dayKey) {
  if (!QUIZ_DAYS_CONFIG[dayKey]) {
    dayKey = 'w4_d1';
  }
  appState.quizCategoryFilter = dayKey;
  
  // Sincronizar classes ativas nos botões das abas
  document.querySelectorAll('.day-tab-btn').forEach(btn => {
    const onclickStr = btn.getAttribute('onclick') || '';
    btn.classList.toggle('active', onclickStr.includes("'" + dayKey + "'"));
  });

  const cfg = QUIZ_DAYS_CONFIG[dayKey] || QUIZ_DAYS_CONFIG.all;
  const titleEl = document.getElementById('quizDayTitle');
  const descEl = document.getElementById('quizDayDesc');
  const bookletBtn = document.getElementById('btnOpenDayBooklet');
  if (titleEl) titleEl.innerText = cfg.title;
  if (descEl) descEl.innerText = cfg.desc;
  if (bookletBtn && cfg.bookletUrl) {
    bookletBtn.href = cfg.bookletUrl;
    bookletBtn.innerHTML = `<i class="fas fa-print"></i> ${cfg.bookletLabel || 'Abrir Caderno Impresso (PDF)'}`;
  }

  saveState();
  renderQuiz();
}

function resetQuizAnswers() {
  if (confirm("Deseja realmente limpar todas as respostas do bloco selecionado e recomeçar do zero?")) {
    const filterKey = appState.quizCategoryFilter || 'w2_d3';
    if (appState.quizShuffledOrder) {
      delete appState.quizShuffledOrder[`${filterKey}_random`];
      delete appState.quizShuffledOrder[`${filterKey}_interleaved`];
    }
    
    const baseQuestions = getFilteredBaseQuestions(filterKey);
    baseQuestions.forEach(q => {
      const existing = appState.quizAnswers[q.id];
      if (existing && existing.confirmed) {
        const dayId = getQuestionDayKey(q);
        if (appState.dayQuestions[dayId]) {
          appState.dayQuestions[dayId].done = Math.max(0, (appState.dayQuestions[dayId].done || 0) - 1);
          if (existing.isCorrect) {
            appState.dayQuestions[dayId].correct = Math.max(0, (appState.dayQuestions[dayId].correct || 0) - 1);
          }
        }
      }
      delete appState.quizAnswers[q.id];
    });

    saveState();
    renderQuiz();
    renderDaysForWeek(appState.currentWeek);
    showToast("Bloco reiniciado com nova ordem!");
  }
}

function addQuizErrorToBook(qId) {
  const q = QUIZ_QUESTIONS_DATA.find(item => item.id === qId);
  if (!q) return;

  const userAns = appState.quizAnswers[qId];
  const userLetter = userAns && userAns.selected !== null ? ['A', 'B', 'C', 'D'][userAns.selected] : '?';
  const correctLetter = ['A', 'B', 'C', 'D'][q.correctAnswer];

  const newError = {
    id: 'err_quiz_' + qId + '_' + Date.now(),
    date: new Date().toLocaleDateString('pt-BR'),
    disciplina: q.discipline,
    assunto: `Questão ${qId} — ${q.topic}`,
    tipo: 'duvida',
    conceito: `Gabarito correto: ${correctLetter}. ${q.commentary}`,
    pegadinha: `Marquei alternativa ${userLetter}. A alternativa correta é a ${correctLetter}: ${q.options[q.correctAnswer]}`,
    revisado: false
  };

  const exists = appState.cadernoErros.some(e => e.id && e.id.startsWith('err_quiz_' + qId + '_'));
  if (!exists) {
    appState.cadernoErros.unshift(newError);
    saveState();
    renderCadernoErros();
    showToast(`Questão ${qId} enviada para o Caderno de Erros!`);
  } else {
    showToast(`A Questão ${qId} já consta registrada no seu Caderno de Erros.`);
  }
}

// =========================================================================
// MÓDULO SEMANAS & DIAS
// =========================================================================
function renderWeekPills() {
  const container = document.getElementById('weekPillsContainer');
  if (!container) return;

  container.innerHTML = WEEKS_DATA.map(w => `
    <button class="week-pill-btn ${w.weekNumber === appState.currentWeek ? 'active' : ''}" onclick="selectWeek(${w.weekNumber})">
      <span>Semana ${w.weekNumber}</span>
      <span class="pill-badge" id="weekBadge_${w.weekNumber}">0%</span>
    </button>
  `).join('');
  
  updateWeekBadges();
}

function selectWeek(weekNum) {
  appState.currentWeek = weekNum;
  renderWeekPills();
  renderDaysForWeek(weekNum);
  saveState();
}

function updateWeekBadges() {
  WEEKS_DATA.forEach(w => {
    let totalTasks = 0;
    let doneTasks = 0;
    w.days.forEach(d => {
      d.blocks.forEach((b, bIdx) => {
        b.tasks.forEach((t, tIdx) => {
          totalTasks++;
          const taskId = `${d.id}_b${bIdx}_t${tIdx}`;
          if (appState.checkedTasks[taskId]) doneTasks++;
        });
      });
    });
    const pct = totalTasks > 0 ? Math.round((doneTasks / totalTasks) * 100) : 0;
    const badge = document.getElementById(`weekBadge_${w.weekNumber}`);
    if (badge) badge.innerText = `${pct}%`;
  });
}

function renderDaysForWeek(weekNum) {
  const week = WEEKS_DATA.find(w => w.weekNumber === weekNum);
  const container = document.getElementById('daysContainer');
  const titleElem = document.getElementById('currentWeekTitle');
  const focusElem = document.getElementById('currentWeekFocus');

  if (!week || !container) return;

  if (titleElem) titleElem.innerText = week.title;
  if (focusElem) focusElem.innerText = week.focus;

  container.innerHTML = week.days.map((day, dIdx) => {
    let dayTotalTasks = 0;
    let dayDoneTasks = 0;

    day.blocks.forEach((b, bIdx) => {
      b.tasks.forEach((t, tIdx) => {
        dayTotalTasks++;
        const taskId = `${day.id}_b${bIdx}_t${tIdx}`;
        if (appState.checkedTasks[taskId]) dayDoneTasks++;
      });
    });

    const isDone = dayTotalTasks > 0 && dayDoneTasks === dayTotalTasks;
    const todayStr = "15/09/2026";
    const isToday = (day.date === todayStr);
    const hasTodayInWeek = week.days.some(d => d.date === todayStr);
    const shouldOpen = isToday || (!hasTodayInWeek && dIdx === 0);

    const questionsDone = (appState.dayQuestions[day.id] && appState.dayQuestions[day.id].done) || 0;
    const questionsCorrect = (appState.dayQuestions[day.id] && appState.dayQuestions[day.id].correct) || 0;

    return `
      <div class="day-card ${isDone ? 'completed' : ''} ${isToday ? 'today' : ''} ${shouldOpen ? 'open' : ''}" id="card_${day.id}">
        <div class="day-header" onclick="toggleDayAccordion('${day.id}')">
          <div class="day-header-left">
            <span class="day-tag">${day.dayLabel}</span>
            <div class="day-title-box">
              <h3>${day.date}</h3>
              <span>${day.blocks.map(b => b.subject.split('—')[0]).join(' • ')}</span>
            </div>
          </div>
          <div class="day-header-right">
            <span class="day-progress-text" id="prog_${day.id}">${dayDoneTasks}/${dayTotalTasks} tarefas</span>
            <i class="fas fa-chevron-down day-chevron"></i>
          </div>
        </div>
        <div class="day-body">
          <div class="study-blocks-grid">
            ${day.blocks.map((block, bIdx) => `
              <div class="study-block">
                <div>
                  <div class="block-header">
                    <span class="block-badge">${block.badge}</span>
                  </div>
                  <h4 class="block-subject">${block.subject}</h4>
                  <p class="block-details">${block.details}</p>
                </div>
                <div class="block-checklist">
                  ${block.tasks.map((task, tIdx) => {
                    const taskId = `${day.id}_b${bIdx}_t${tIdx}`;
                    const isChecked = !!appState.checkedTasks[taskId];
                    return `
                      <label class="custom-checkbox">
                        <input type="checkbox" ${isChecked ? 'checked' : ''} onchange="toggleTask('${day.id}', '${taskId}')">
                        <span class="checkmark"></span>
                        <span class="label-text">${task}</span>
                      </label>
                    `;
                  }).join('')}
                </div>
              </div>
            `).join('')}
          </div>

          <div class="day-questions-box">
            <div>
              <strong><i class="fas fa-bullseye" style="color: var(--primary); margin-right: 6px;"></i> Registro de Questões do Dia</strong>
              <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 2px;">Meta sugerida: ${day.targetQuestions} questões</div>
            </div>
            <div class="q-inputs">
              <div class="q-field">
                <label>Resolvidas:</label>
                <input type="number" min="0" value="${questionsDone}" onchange="updateDayQuestions('${day.id}', this.value, null)">
              </div>
              <div class="q-field">
                <label>Acertos:</label>
                <input type="number" min="0" value="${questionsCorrect}" onchange="updateDayQuestions('${day.id}', null, this.value)">
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function toggleDayAccordion(dayId) {
  const card = document.getElementById(`card_${dayId}`);
  if (card) {
    card.classList.toggle('open');
  }
}

function toggleTask(dayId, taskId) {
  if (appState.checkedTasks[taskId]) {
    delete appState.checkedTasks[taskId];
  } else {
    appState.checkedTasks[taskId] = true;
  }
  saveState();
  updateWeekBadges();
  renderDaysForWeek(appState.currentWeek);
}

function updateDayQuestions(dayId, done, correct) {
  if (!appState.dayQuestions[dayId]) {
    appState.dayQuestions[dayId] = { done: 0, correct: 0 };
  }
  if (done !== null) appState.dayQuestions[dayId].done = parseInt(done) || 0;
  if (correct !== null) appState.dayQuestions[dayId].correct = parseInt(correct) || 0;
  saveState();
}

// =========================================================================
// MÉTRICAS GLOBAIS
// =========================================================================
function updateGlobalMetrics() {
  let totalTasks = 0;
  let doneTasks = 0;

  WEEKS_DATA.forEach(w => {
    w.days.forEach(d => {
      d.blocks.forEach((b, bIdx) => {
        b.tasks.forEach((t, tIdx) => {
          totalTasks++;
          const taskId = `${d.id}_b${bIdx}_t${tIdx}`;
          if (appState.checkedTasks[taskId]) doneTasks++;
        });
      });
    });
  });

  const progressPct = totalTasks > 0 ? Math.round((doneTasks / totalTasks) * 100) : 0;
  
  let totalQuestionsResolved = 0;
  let totalQuestionsCorrect = 0;
  Object.values(appState.dayQuestions).forEach(q => {
    totalQuestionsResolved += (q.done || 0);
    totalQuestionsCorrect += (q.correct || 0);
  });

  let simCount = 0;
  let simSum = 0;
  appState.simulados.forEach(s => {
    if (s.acertos > 0) {
      simCount++;
      simSum += (s.acertos / s.total) * 100;
    }
  });
  const avgSim = simCount > 0 ? Math.round(simSum / simCount) : 0;

  const globalProgElem = document.getElementById('metricGlobalProgress');
  const globalProgBar = document.getElementById('metricGlobalProgressBar');
  const questDoneElem = document.getElementById('metricQuestionsDone');
  const questAccElem = document.getElementById('metricQuestionsAccuracy');
  const simAvgElem = document.getElementById('metricSimuladoAvg');
  const errorsCountElem = document.getElementById('metricErrorsCount');
  const sidebarErrorBadge = document.getElementById('sidebarErrorBadge');
  const fcMasteredElem = document.getElementById('metricFlashcardsMastered');

  if (globalProgElem) globalProgElem.innerText = `${progressPct}%`;
  if (globalProgBar) globalProgBar.style.width = `${progressPct}%`;
  if (questDoneElem) questDoneElem.innerText = `${totalQuestionsResolved}`;
  if (questAccElem) {
    const accPct = totalQuestionsResolved > 0 ? Math.round((totalQuestionsCorrect / totalQuestionsResolved) * 100) : 0;
    questAccElem.innerText = `${accPct}% de acertos`;
  }
  if (simAvgElem) simAvgElem.innerText = `${avgSim}%`;
  if (errorsCountElem) errorsCountElem.innerText = `${appState.cadernoErros.length}`;
  if (sidebarErrorBadge) sidebarErrorBadge.innerText = `${appState.cadernoErros.length}`;
  if (fcMasteredElem) fcMasteredElem.innerText = `${Object.keys(appState.masteredFlashcards).length} / ${FLASHCARDS_DATA.length}`;
}

// =========================================================================
// CADERNO DE ERROS
// =========================================================================
function setupErrorForm() {
  const form = document.getElementById('errorForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const disciplina = document.getElementById('errDisciplina').value;
    const assunto = document.getElementById('errAssunto').value;
    const tipo = document.getElementById('errTipo').value;
    const conceito = document.getElementById('errConceito').value;
    const pegadinha = document.getElementById('errPegadinha').value;

    const newError = {
      id: 'err_' + Date.now(),
      date: new Date().toLocaleDateString('pt-BR'),
      disciplina,
      assunto,
      tipo,
      conceito,
      pegadinha,
      revisado: false
    };

    appState.cadernoErros.unshift(newError);
    saveState();
    renderCadernoErros();
    form.reset();
    showToast("Erro adicionado com sucesso ao Caderno!");
  });
}

function renderCadernoErros(filterTipo = 'all') {
  const container = document.getElementById('errorListContainer');
  if (!container) return;

  let list = appState.cadernoErros;
  if (filterTipo !== 'all') {
    list = list.filter(e => e.tipo === filterTipo);
  }

  if (list.length === 0) {
    container.innerHTML = `
      <div style="text-align: center; padding: 40px 20px; color: var(--text-muted);">
        <i class="fas fa-book-open" style="font-size: 2.5rem; margin-bottom: 12px; opacity: 0.5;"></i>
        <p>Nenhum erro registrado ainda. Quando errar uma questão no Banco de Questões ou Simulado, envie para cá!</p>
      </div>
    `;
    return;
  }

  const typeLabels = {
    'nao-sabia': { label: '🔴 Não sabia', class: 'tag-nao-sabia' },
    'esqueci': { label: '🟠 Esqueci', class: 'tag-esqueci' },
    'duvida': { label: '🟡 Dúvida', class: 'tag-duvida' },
    'interpretacao': { label: '🔵 Interpretação', class: 'tag-interpretacao' },
    'distracao': { label: '⚫ Distração', class: 'tag-distracao' }
  };

  container.innerHTML = list.map(err => {
    const typeInfo = typeLabels[err.tipo] || { label: err.tipo, class: '' };
    return `
      <div class="error-item" id="${err.id}">
        <div class="error-item-header">
          <span class="error-meta">${err.disciplina} • ${err.assunto}</span>
          <span class="error-tag ${typeInfo.class}">${typeInfo.label}</span>
        </div>
        <div class="error-concept">
          <strong>Conceito Correto:</strong> ${err.conceito}
          ${err.pegadinha ? `<div style="margin-top: 6px; font-size: 0.8rem; color: var(--warning);">⚠️ <strong>Pegadinha / Alerta:</strong> ${err.pegadinha}</div>` : ''}
        </div>
        <div class="error-item-footer">
          <span style="font-size: 0.75rem; color: var(--text-muted);"><i class="far fa-calendar-alt"></i> ${err.date}</span>
          <div style="display: flex; gap: 8px;">
            <button class="btn btn-secondary" style="padding: 4px 10px; font-size: 0.75rem;" onclick="toggleRevisado('${err.id}')">
              ${err.revisado ? '<i class="fas fa-check-double" style="color: var(--success);"></i> Revisado' : '<i class="far fa-clock"></i> Pendente'}
            </button>
            <button class="btn btn-danger" style="padding: 4px 10px; font-size: 0.75rem;" onclick="deleteError('${err.id}')">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function filterErrors(tipo) {
  renderCadernoErros(tipo);
}

function toggleRevisado(errId) {
  const item = appState.cadernoErros.find(e => e.id === errId);
  if (item) {
    item.revisado = !item.revisado;
    saveState();
    renderCadernoErros();
  }
}

function deleteError(errId) {
  if (confirm("Deseja realmente remover este registro de erro?")) {
    appState.cadernoErros = appState.cadernoErros.filter(e => e.id !== errId);
    saveState();
    renderCadernoErros();
    showToast("Registro excluído.");
  }
}

// =========================================================================
// MÓDULO SIMULADOS
// =========================================================================
function renderSimulados() {
  const tbody = document.getElementById('simuladosTableBody');
  if (!tbody) return;

  tbody.innerHTML = appState.simulados.map((s, idx) => {
    const pct = s.acertos > 0 ? Math.round((s.acertos / s.total) * 100) : 0;
    let badgeColor = 'var(--text-muted)';
    if (pct >= 90) badgeColor = 'var(--success)';
    else if (pct >= 80) badgeColor = 'var(--primary)';
    else if (pct >= 70) badgeColor = 'var(--warning)';
    else if (pct > 0) badgeColor = 'var(--danger)';

    return `
      <tr>
        <td><strong>Simulado ${s.num}</strong></td>
        <td>${s.date}</td>
        <td>
          <input type="number" min="0" max="40" value="${s.acertos}" style="width: 60px; padding: 4px 8px; border: 1px solid var(--border); border-radius: 4px; font-weight: 700; background: var(--bg-card); color: var(--text-main);" onchange="updateSimuladoScore(${idx}, this.value)">
          / 40
        </td>
        <td>
          <span style="font-weight: 800; color: ${badgeColor};">${pct}%</span>
        </td>
        <td>
          <input type="text" value="${s.tempo}" style="width: 70px; padding: 4px 8px; border: 1px solid var(--border); border-radius: 4px; background: var(--bg-card); color: var(--text-main);" onchange="updateSimuladoTempo(${idx}, this.value)">
        </td>
      </tr>
    `;
  }).join('');
}

function updateSimuladoScore(index, acertos) {
  appState.simulados[index].acertos = parseInt(acertos) || 0;
  saveState();
  renderSimulados();
}

function updateSimuladoTempo(index, tempo) {
  appState.simulados[index].tempo = tempo;
  saveState();
}

// =========================================================================
// TABELA DE DIAGNÓSTICO FINAL
// =========================================================================
function renderDiagnostico() {
  const tbody = document.getElementById('diagnosticoTableBody');
  if (!tbody) return;

  const labels = {
    portugues: "Língua Portuguesa",
    informatica: "Informática",
    matematica: "Matemática / RLM",
    constitucional: "Direito Constitucional",
    administrativo: "Direito Administrativo",
    especificos: "Conhecimentos Específicos",
    legislacao: "Legislação Municipal (LO + RI)"
  };

  tbody.innerHTML = Object.keys(appState.diagnostico).map(key => {
    const item = appState.diagnostico[key];
    const pct = item.total > 0 ? Math.round((item.acertos / item.total) * 100) : 0;
    
    let statusText = "Pendente";
    let statusClass = "tag-distracao";
    if (pct >= 90) { statusText = "🟢 Domínio (≥90%)"; statusClass = "tag-nao-sabia"; }
    else if (pct >= 80) { statusText = "🔵 Forte (80-89%)"; statusClass = "tag-interpretacao"; }
    else if (pct >= 70) { statusText = "🟡 Atenção (70-79%)"; statusClass = "tag-duvida"; }
    else if (item.acertos > 0) { statusText = "🔴 Prioridade (<70%)"; statusClass = "tag-nao-sabia"; }

    return `
      <tr>
        <td><strong>${labels[key]}</strong></td>
        <td>
          <input type="number" min="0" value="${item.acertos}" style="width: 60px; padding: 4px; border: 1px solid var(--border); border-radius: 4px; background: var(--bg-card); color: var(--text-main);" onchange="updateDiag('${key}', 'acertos', this.value)">
        </td>
        <td>
          <input type="number" min="1" value="${item.total}" style="width: 60px; padding: 4px; border: 1px solid var(--border); border-radius: 4px; background: var(--bg-card); color: var(--text-main);" onchange="updateDiag('${key}', 'total', this.value)">
        </td>
        <td><strong>${pct}%</strong></td>
        <td><span class="error-tag ${statusClass}">${statusText}</span></td>
      </tr>
    `;
  }).join('');
}

function updateDiag(key, field, val) {
  appState.diagnostico[key][field] = parseInt(val) || 0;
  saveState();
  renderDiagnostico();
}

// =========================================================================
// TIMER / POMODORO
// =========================================================================
let timerInterval = null;
let timerSeconds = 70 * 60;
let isTimerRunning = false;

function setupTimer() {
  updateTimerDisplay();
}

function updateTimerDisplay() {
  const display = document.getElementById('timerDisplay');
  if (!display) return;
  const mins = Math.floor(timerSeconds / 60);
  const secs = timerSeconds % 60;
  display.innerText = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}

function startTimer() {
  if (isTimerRunning) return;
  isTimerRunning = true;
  timerInterval = setInterval(() => {
    if (timerSeconds > 0) {
      timerSeconds--;
      updateTimerDisplay();
    } else {
      clearInterval(timerInterval);
      isTimerRunning = false;
      showToast("⏰ Tempo esgotado! Excelente bloco de estudo concluído.");
    }
  }, 1000);
}

function pauseTimer() {
  clearInterval(timerInterval);
  isTimerRunning = false;
}

function resetTimer(minutes = 70) {
  pauseTimer();
  timerSeconds = minutes * 60;
  updateTimerDisplay();
}

// Toast
function showToast(msg) {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerText = msg;
  container.appendChild(toast);
  setTimeout(() => {
    toast.remove();
  }, 3500);
}

// Backup
function exportBackup() {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(appState, null, 2));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", `estudos_meruoca_backup_${new Date().toISOString().slice(0,10)}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
  showToast("Backup exportado com sucesso!");
}

function importBackup() {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = '.json';
  input.onchange = e => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.readAsText(file, 'UTF-8');
    reader.onload = readerEvent => {
      try {
        const content = JSON.parse(readerEvent.target.result);
        appState = content;
        saveState();
        location.reload();
      } catch (err) {
        alert("Arquivo de backup inválido!");
      }
    };
  };
  input.click();
}

// =========================================================================
// EDITAL VERTICALIZADO & CONTEÚDO PROGRAMÁTICO OFICIAL (EDITAL 001/2026)
// =========================================================================
let currentEditalRole = 'tecnico';

const EDITAL_PROGRAMATICO = {
  tecnico: [
    {
      id: "lp_tecnico",
      nome: "Língua Portuguesa (Nível Superior)",
      icone: "fa-book",
      peso: "10 Questões | Peso 2.5 (25 Pontos)",
      tipo: "geral",
      topicos: [
        { id: "lp-1", nome: "Compreensão e Interpretação de Textos", desc: "Situação comunicativa, pressuposição, inferência, ambiguidade, ironia, figurativização, polissemia, intertextualidade e linguagem não-verbal.", tags: ["Interpretação", "INBRASP"] },
        { id: "lp-2", nome: "Tipos e Gêneros Textuais", desc: "Narrativo, descritivo, expositivo, argumentativo, instrucional, propaganda, editorial, cartaz, anúncio, artigo de opinião, artigo de divulgação científica, ofício e carta.", tags: ["Gêneros Textuais"] },
        { id: "lp-3", nome: "Estrutura Textual & Coesão e Coerência", desc: "Progressão temática, parágrafo, frase, oração, período, enunciado, pontuação e conectivos coesivos.", tags: ["Coesão & Coerência"] },
        { id: "lp-4", nome: "Variedade Linguística & Adequação", desc: "Variedade linguística, formalidade vs informalidade, formas de tratamento, propriedade lexical e adequação comunicativa.", tags: ["Adequação"] },
        { id: "lp-5", nome: "Ortografia Oficial, Acentuação & Crase", desc: "Novo Acordo Ortográfico, regras de acentuação (oxítonas, paroxítonas, proparoxítonas e hiatos) e emprego do sinal indicativo de crase.", tags: ["Altíssima Incidência"] },
        { id: "lp-6", nome: "Morfologia & Formação de Palavras", desc: "Processos de derivação (prefixal, sufixal, parassintética) e composição; sentido e emprego das 10 classes de palavras; flexão nominal e verbal.", tags: ["Morfologia"] },
        { id: "lp-7", nome: "Sintaxe da Oração e do Período", desc: "Termos da oração (essenciais, integrantes e acessórios); processos de coordenação e subordinação de orações.", tags: ["Sintaxe"] },
        { id: "lp-8", nome: "Regência e Concordância (Nominal e Verbal)", desc: "Regência nominal e verbal de casos clássicos; concordância com sujeito composto, partitivo e verbo haver impessoal (transitivo direto).", tags: ["Altíssima Incidência"] },
        { id: "lp-9", nome: "Colocação Pronominal", desc: "Padrões gerais de próclise, mesóclise e ênclise no português padrão e casos proibitivos.", tags: ["Padrão Culto"] },
        { id: "lp-10", nome: "Semântica, Estilística & Reescrita", desc: "Sentido e emprego dos vocábulos, campos semânticos, sinônimos, figuras de linguagem; reescrita de frases (substituição, deslocamento, paralelismo sintático).", tags: ["Semântica"] }
      ]
    },
    {
      id: "inf_tecnico",
      nome: "Noções de Informática (Nível Superior)",
      icone: "fa-desktop",
      peso: "Conhecimentos Gerais (Peso 2.5)",
      tipo: "geral",
      topicos: [
        { id: "inf-1", nome: "Algoritmos e Programação de Computadores", desc: "Fundamentos, construção e análise de algoritmos, pseudocódigos, fluxogramas, conceitos de programação estruturada (Python, JavaScript, etc.).", tags: ["Diferencial do Edital"] },
        { id: "inf-2", nome: "Sistemas Operacionais Modernos", desc: "Fundamentos e operação, gerenciamento de arquivos/pastas, procedimentos de backup e recuperação (disaster recovery), Ubuntu Linux e Windows 11.", tags: ["Linux & Win 11"] },
        { id: "inf-3", nome: "Dispositivos de Entrada e Saída (Hardware)", desc: "Conceitos de arquitetura de computadores, funcionamento, tipos e instalação de periféricos.", tags: ["Hardware"] },
        { id: "inf-4", nome: "Aplicativos para Escritório (Office & Workspace)", desc: "Edição de textos, planilhas eletrônicas (fórmulas, funções e referências no Excel/Calc), apresentações e bancos de dados (Microsoft Office e Google Workspace).", tags: ["Office & Workspace"] },
        { id: "inf-5", nome: "Importação e Exportação de Dados", desc: "Formatos de documentos (PDF, CSV, XLSX, XML, JSON), técnicas de conversão e transferência entre plataformas.", tags: ["Dados"] },
        { id: "inf-6", nome: "Redes de Computadores & Internet/Intranet", desc: "Fundamentos, modelos de rede (LAN, WAN), endereçamento IP, protocolos essenciais (TCP/IP, HTTP, HTTPS, DNS, DHCP).", tags: ["Redes"] },
        { id: "inf-7", nome: "Navegadores & Serviços de Internet", desc: "Microsoft Edge, Mozilla Firefox e Google Chrome: recursos de navegação, histórico, modo anônimo, extensões e pesquisas avançadas.", tags: ["Navegadores"] },
        { id: "inf-8", nome: "Correio Eletrônico & Ferramentas de Comunicação", desc: "Email do Windows, Thunderbird, protocolos (SMTP, POP3, IMAP); soluções corporativas e mensageria (WhatsApp, Telegram, Skype, Discord, Teams).", tags: ["Comunicação"] },
        { id: "inf-9", nome: "Computação em Nuvem (Cloud Computing)", desc: "Fundamentos de nuvem, tipos de oferta de serviço (IaaS, PaaS, SaaS), modelos de implementação e provedoras (Google, Amazon AWS, Microsoft Azure).", tags: ["Cloud"] },
        { id: "inf-10", nome: "Segurança da Informação & Malwares", desc: "Princípios de segurança (confidencialidade, integridade, disponibilidade, autenticidade), malwares (vírus, worms, trojans, ransomware, phishing), antivírus e firewall.", tags: ["Altíssima Incidência"] },
        { id: "inf-11", nome: "Ambientes Corporativos & Domínio", desc: "Serviços de rede, autenticação e autorização, conceito de domínio de rede e compartilhamento seguro de pastas e recursos.", tags: ["Corporativo"] }
      ]
    },
    {
      id: "mat_tecnico",
      nome: "Matemática e Raciocínio Lógico (Nível Superior)",
      icone: "fa-calculator",
      peso: "Conhecimentos Gerais (Peso 2.5)",
      tipo: "geral",
      topicos: [
        { id: "mat-1", nome: "Raciocínio Lógico Proposicional", desc: "Proposições lógicas, conectivos (conjunção, disjunção, condicional, bicondicional), tabela-verdade, negações lógicas (Leis de De Morgan) e equivalências.", tags: ["RLM Clássico"] },
        { id: "mat-2", nome: "Teoria dos Conjuntos & Diagramas", desc: "Relações de pertinência, inclusão, união, intersecção, diferença de conjuntos e resolução de problemas práticos via diagramas de Venn.", tags: ["Conjuntos"] },
        { id: "mat-3", nome: "Razão, Proporção & Regra de Três", desc: "Grandezas direta e inversamente proporcionais, divisão proporcional, regra de três simples e composta aplicada a rotinas públicas.", tags: ["Proporcionalidade"] },
        { id: "mat-4", nome: "Porcentagem & Juros Simples", desc: "Cálculo de variações percentuais, aumentos e descontos sucessivos, juros simples e determinação de montante.", tags: ["Matemática Financeira"] },
        { id: "mat-5", nome: "Geometria Plana e Espacial", desc: "Cálculo de perímetros, áreas de figuras planas (triângulos, quadriláteros, círculos) e noções de volume.", tags: ["Geometria"] },
        { id: "mat-6", nome: "Sistemas Lineares & Álgebra Básica", desc: "Equações de primeiro e segundo graus, resolução de sistemas lineares de duas ou mais variáveis.", tags: ["Álgebra"] },
        { id: "mat-7", nome: "Progressões (PA e PG)", desc: "Identificação de progressão aritmética e geométrica, termo geral, razão e soma dos termos.", tags: ["Sequências"] },
        { id: "mat-8", nome: "Análise Combinatória & Probabilidade", desc: "Princípio fundamental da contagem, fatorial, permutações, arranjos, combinações e probabilidade em eventos simples e compostos.", tags: ["Contagem"] },
        { id: "mat-9", nome: "Estatística Descritiva", desc: "Interpretação de dados, gráficos e tabelas; medidas de tendência central: média aritmética simples e ponderada, moda e mediana.", tags: ["Estatística"] },
        { id: "mat-10", nome: "Trigonometria & Sequências Lógicas", desc: "Relações trigonométricas no triângulo retângulo (seno, cosseno, tangente) e identificação de padrões lógicos sequenciais.", tags: ["Lógica"] }
      ]
    },
    {
      id: "dir_geral_tecnico",
      nome: "Noções de D. Administrativo e Constitucional (Gerais)",
      icone: "fa-scale-balanced",
      peso: "Conhecimentos Gerais (Peso 2.5)",
      tipo: "geral",
      topicos: [
        { id: "dg-1", nome: "Princípios da Administração Pública (Art. 37 CF)", desc: "Princípios expressos (LIMPE: Legalidade, Impessoalidade, Moralidade, Publicidade, Eficiência) e princípios implícitos da administração.", tags: ["LIMPE - Art. 37"] },
        { id: "dg-2", nome: "Poderes Administrativos", desc: "Poder vinculado, discricionário, hierárquico, disciplinar, regulamentar e de polícia (características, autoexecutoriedade, discricionariedade e limites).", tags: ["Poderes"] },
        { id: "dg-3", nome: "Atos Administrativos", desc: "Conceito, requisitos/elementos de validade (COMFIFOR), atributos do ato (PATI: presunção, autoexecutoriedade, tipicidade, imperatividade), espécies e invalidação.", tags: ["Atos Adm"] },
        { id: "dg-4", nome: "Licitações e Contratos Administrativos", desc: "Noções fundamentais da Lei nº 14.133/2021: princípios, fases do procedimento, modalidades e hipóteses de contratação direta.", tags: ["Lei 14.133/2021"] },
        { id: "dg-5", nome: "Serviços Públicos & Órgãos Públicos", desc: "Conceito e princípios dos serviços públicos, descentralização vs desconcentração, administração direta e indireta.", tags: ["Organização"] },
        { id: "dg-6", nome: "Servidores Públicos & Improbidade", desc: "Regimes funcionais (estatutário e trabalhista), cargo, emprego e função pública; noções de processo administrativo e improbidade.", tags: ["Servidores"] },
        { id: "dg-7", nome: "CF/88: Princípios & Direitos Fundamentais (Arts. 1º ao 5º)", desc: "Princípios fundamentais (Arts. 1º ao 4º) e direitos e deveres individuais e coletivos (Art. 5º: vida, liberdade, igualdade, segurança, propriedade e remédios constitucionais).", tags: ["CF Arts. 1º a 5º"] },
        { id: "dg-8", nome: "CF/88: Direitos Sociais, Nacionalidade & Políticos (Arts. 6º ao 16)", desc: "Direitos sociais dos trabalhadores (Arts. 6º ao 11), nacionalidade originária e derivada (Arts. 12-13), e direitos políticos/partidos (Arts. 14-16).", tags: ["CF Arts. 6º a 16"] },
        { id: "dg-9", nome: "CF/88: Organização, Municípios & Servidores (Arts. 18-19, 29-31, 37-41)", desc: "Organização político-administrativa, preceitos específicos sobre os Municípios (autonomia, subsídios, fiscalização da Câmara) e regime dos servidores públicos.", tags: ["CF Arts. 29-31 e 37-41"] }
      ]
    },
    {
      id: "especificas_tecnico",
      nome: "Conhecimentos Específicos: Técnico Legislativo",
      icone: "fa-gavel",
      peso: "20 Questões | Peso 2.5 (50 PONTOS — 50% DE TODA A PROVA)",
      tipo: "especifica",
      topicos: [
        { id: "esp-1", nome: "CF/88 & O Poder Legislativo Constitucional", desc: "Princípios e objetivos da República; organização do Estado; funções típicas (legislar e fiscalizar) e atípicas (administrar e julgar); processo legislativo constitucional; espécies normativas (Art. 59 CF); competência legislativa municipal (Art. 30 CF); controle de constitucionalidade.", tags: ["CF/88", "Processo Legislativo", "50% da Prova"] },
        { id: "esp-2", nome: "Direito Administrativo Aplicado & Responsabilidade", desc: "Administração direta e indireta; atos administrativos (elementos, atributos, cassação, anulação, revogação e convalidação); poderes administrativos; serviços públicos; responsabilidade civil objetiva do Estado (Art. 37, §6º da CF); controle interno e externo.", tags: ["D. Administrativo", "Controle Externo"] },
        { id: "esp-3", nome: "Nova Lei de Licitações (Lei nº 14.133/2021)", desc: "Princípios da licitação; modalidades (pregão, concorrência, concurso, leilão, diálogo competitivo); rito procedimental e inversão de fases; contratação direta (dispensa e inexigibilidade); contratos administrativos e Sistema de Registro de Preços (SRP).", tags: ["Lei 14.133/2021", "Altíssima Incidência"] },
        { id: "esp-4", nome: "Lei de Improbidade Administrativa (Lei nº 8.429/1992)", desc: "Atualizações trazidas pela Lei 14.230/2021: exigência de dolo específico; atos de enriquecimento ilícito (Art. 9º), prejuízo ao erário (Art. 10) e atentado aos princípios (Art. 11); prazos de prescrição unificados em 8 anos.", tags: ["Lei 8.429/92", "Improbidade"] },
        { id: "esp-5", nome: "Lei Orgânica do Município de Meruoca", desc: "Organização dos poderes locais; competências privativas e comuns da Câmara e do Prefeito; prazos de sanção e veto (15 dias úteis) e derrubada de veto (30 dias); quóruns qualificados (2/3 e maioria absoluta); processo legislativo municipal.", tags: ["Legislação de Meruoca", "Obrigatório"] },
        { id: "esp-6", nome: "Regimento Interno da Câmara de Meruoca", desc: "Mesa Diretora (eleição, competências do Presidente); sessões legislativas (ordinárias, extraordinárias, solenes e secretas); comissões permanentes e temporárias (CPIs); proposições legislativas, substitutivos, emendas e rito de votação.", tags: ["Regimento Interno", "Rotina Parlamentar"] },
        { id: "esp-7", nome: "Técnica Legislativa & Lei Complementar nº 95/1998", desc: "Elaboração, redação, alteração e consolidação das leis; estrutura padrão das normas (epígrafe, ementa, preâmbulo, artigos, parágrafos, incisos, alíneas e fecho); regras de revogação e contagem de prazos de vigência.", tags: ["LC 95/1998", "Técnica Legislativa"] },
        { id: "esp-8", nome: "Redação Oficial & Atos Parlamentares", desc: "Linguagem normativa (clareza, concisão e impessoalidade); elaboração de projetos de lei, decretos legislativos, resoluções, pareceres técnicos e jurídicos; atos administrativos e correspondências oficiais (ofícios, cartas e memorandos).", tags: ["Redação Oficial"] },
        { id: "esp-9", nome: "Gestão Pública, Governança & Organização", desc: "Planejamento estratégico no setor público; organização administrativa da Câmara Municipal; gestão de processos de trabalho legislativos; gestão de pessoas no setor público; governança pública e compliance; avaliação de resultados.", tags: ["Gestão Pública", "Governança"] },
        { id: "esp-10", nome: "Gestão Documental & Arquivística", desc: "Ciclo vital dos documentos (teoria das três idades: arquivo corrente, intermediário e permanente); métodos de arquivamento (alfabético, numérico, ideográfico/por assunto); tabela de temporalidade; protocolo, rastreabilidade e GED.", tags: ["Arquivologia", "Protocolo"] },
        { id: "esp-11", nome: "Orçamento Público (PPA, LDO e LOA)", desc: "Conceitos e princípios orçamentários (anualidade, universalidade, unidade, exclusividade); Plano Plurianual (PPA); Lei de Diretrizes Orçamentárias (LDO); Lei Orçamentária Anual (LOA); créditos adicionais; fiscalização contábil, orçamentária e financeira.", tags: ["Orçamento Público", "PPA/LDO/LOA"] },
        { id: "esp-12", nome: "Lei de Responsabilidade Fiscal (LC nº 101/2000)", desc: "Limites de gastos com pessoal para o Poder Legislativo Municipal; vedações no final de mandato e Restos a Pagar (Art. 42); Relatório de Gestão Fiscal (RGF); mecanismos de transparência e controle da gestão fiscal.", tags: ["LRF / LC 101", "Fiscalização"] },
        { id: "esp-13", nome: "Ciência Política & Políticas Públicas", desc: "Estado, governo e sociedade; sistemas de governo e formas de Estado; democracia representativa e participativa; partidos e representação parlamentar; processo decisório e agenda legislativa; ciclo das políticas públicas e controle social.", tags: ["Políticas Públicas", "Ciência Política"] },
        { id: "esp-14", nome: "Transparência, Ética & Proteção de Dados (LAI & LGPD)", desc: "Lei de Acesso à Informação (Lei nº 12.527/2011: transparência ativa e passiva); Código de Ética do Servidor Público e conflito de interesses; Lei Geral de Proteção de Dados (Lei nº 13.709/2018 - LGPD); segurança da informação no setor público.", tags: ["LAI & LGPD", "Ética no Serviço"] }
      ]
    }
  ],
  agente: [
    {
      id: "lp_agente",
      nome: "Língua Portuguesa (Nível Médio)",
      icone: "fa-book",
      peso: "10 Questões | Peso 2.5 (25 Pontos)",
      tipo: "geral",
      topicos: [
        { id: "ag-lp-1", nome: "Compreensão e Interpretação de Textos", desc: "Identificação da ideia principal, informações explícitas e implícitas, inferências e linguagem não-verbal.", tags: ["Interpretação"] },
        { id: "ag-lp-2", nome: "Ortografia, Acentuação & Crase", desc: "Regras do Acordo Ortográfico, divisão silábica, acentuação gráfica e emprego do sinal de crase.", tags: ["Ortografia"] },
        { id: "ag-lp-3", nome: "Classes de Palavras & Flexão", desc: "Identificação e sentido de substantivos, adjetivos, pronomes, verbos, conjunções e preposições.", tags: ["Morfologia"] },
        { id: "ag-lp-4", nome: "Sintaxe, Concordância & Regência", desc: "Termos fundamentais da oração, concordância nominal e verbal, regência verbal e nominal.", tags: ["Sintaxe"] }
      ]
    },
    {
      id: "gerais_agente",
      nome: "Noções Gerais: Informática, RLM, Constitucional e Administrativo",
      icone: "fa-layer-group",
      peso: "10 Questões | Peso 2.5 (25 Pontos)",
      tipo: "geral",
      topicos: [
        { id: "ag-ger-1", nome: "Noções de Informática (Word & Excel)", desc: "Edição de textos, formatação de parágrafos, tabelas, fórmulas básicas e planilhas eletrônicas no Word e Excel.", tags: ["Informática"] },
        { id: "ag-ger-2", nome: "Matemática e Raciocínio Lógico", desc: "Conjuntos numéricos, operações fundamentais, regra de três simples, porcentagem, medidas e problemas lógicos.", tags: ["Matemática"] },
        { id: "ag-ger-3", nome: "Constituição Federal (Arts. 1º a 16, 29 a 31, 37 a 41)", desc: "Princípios fundamentais, direitos e garantias fundamentais, regras dos municípios e princípios da administração pública.", tags: ["CF/88"] },
        { id: "ag-ger-4", nome: "Noções de Direito Administrativo", desc: "Princípios (LIMPE), poderes administrativos, atos administrativos (requisitos e atributos), licitações e contratos.", tags: ["D. Administrativo"] }
      ]
    },
    {
      id: "especificas_agente",
      nome: "Conhecimentos Específicos: Agente Administrativo",
      icone: "fa-folder-open",
      peso: "20 Questões | Peso 2.5 (50 PONTOS — 50% DA PROVA)",
      tipo: "especifica",
      topicos: [
        { id: "ag-esp-1", nome: "Redação Oficial & Correspondências", desc: "Estrutura e redação de ofícios, comunicações internas, cartas, requerimentos; protocolo, expedição e distribuição de correspondência.", tags: ["Redação Oficial"] },
        { id: "ag-esp-2", nome: "Rotinas Administrativas, Arquivo & Protocolo", desc: "Noções de controle de materiais, organização e métodos de arquivo, técnicas de protocolo e rastreabilidade documental, racionalização do trabalho.", tags: ["Arquivo & Protocolo"] },
        { id: "ag-esp-3", nome: "Atendimento ao Público & Qualidade", desc: "Noções básicas de atendimento ao público, acolhimento, escuta ativa, clareza, resolutividade e excelência na prestação de serviço.", tags: ["Atendimento"] },
        { id: "ag-esp-4", nome: "Relações Humanas, Ética & Motivação", desc: "Ética profissional, relações interpessoais, trabalho em equipe, motivação, comunicação no ambiente de trabalho e etiqueta profissional.", tags: ["Relações Humanas"] },
        { id: "ag-esp-5", nome: "Higiene e Segurança no Trabalho", desc: "Conceitos básicos, importância das condições seguras de trabalho, prevenção de acidentes e qualidade de vida no trabalho (QVT).", tags: ["Segurança do Trabalho"] },
        { id: "ag-esp-6", nome: "Técnicas Administrativas & Funções da Gestão", desc: "Fundamentos da administração (planejamento, organização, direção e controle - PODC), técnicas organizacionais e recebimento/transmissão de informações.", tags: ["Administração"] }
      ]
    }
  ]
};

function initEditalVerticalizado() {
  if (!appState.editalChecks) {
    appState.editalChecks = {};
  }
  renderEditalProgramatico();
}

function switchEditalRole(role) {
  currentEditalRole = role;
  const btnTecnico = document.getElementById('btnRoleTecnico');
  const btnAgente = document.getElementById('btnRoleAgente');
  
  if (btnTecnico && btnAgente) {
    btnTecnico.classList.toggle('active', role === 'tecnico');
    btnAgente.classList.toggle('active', role === 'agente');
  }
  
  renderEditalProgramatico();
}

function renderEditalProgramatico() {
  const container = document.getElementById('editalDisciplinesContainer');
  if (!container) return;

  const disciplines = EDITAL_PROGRAMATICO[currentEditalRole] || EDITAL_PROGRAMATICO.tecnico;
  
  container.innerHTML = disciplines.map(disc => {
    const isEspec = disc.tipo === 'especifica';
    const badgeClass = isEspec ? 'badge-peso-especifica' : 'badge-peso-geral';

    return `
      <div class="discipline-card" id="disc_card_${disc.id}">
        <div class="discipline-card-header" onclick="toggleDiscipline('${disc.id}')">
          <div class="discipline-card-title">
            <i class="fas ${disc.icone}" style="color: ${isEspec ? '#dc2626' : 'var(--primary)'}; font-size: 1.2rem;"></i>
            <span>${disc.nome}</span>
          </div>
          <div class="discipline-card-badges">
            <span class="badge-discipline-peso ${badgeClass}">${disc.peso}</span>
            <i class="fas fa-chevron-down" id="chevron_${disc.id}" style="color: var(--text-muted); transition: transform 0.2s;"></i>
          </div>
        </div>

        <div class="topics-container" id="topics_${disc.id}">
          ${disc.topicos.map(topic => {
            const checks = appState.editalChecks[topic.id] || { teoria: false, questoes: false, revisao: false };
            return `
              <div class="topic-item" data-topic-id="${topic.id}" data-search="${topic.nome.toLowerCase()} ${topic.desc.toLowerCase()} ${(topic.tags||[]).join(' ').toLowerCase()}">
                <div class="topic-info">
                  <div class="topic-name">${topic.nome}</div>
                  <div class="topic-details">${topic.desc}</div>
                  ${topic.tags && topic.tags.length ? `
                    <div class="topic-tags">
                      ${topic.tags.map(t => `<span class="topic-tag ${t.includes('Altíssima') || t.includes('50%') || t.includes('Obrigatório') ? 'highlight' : ''}">${t}</span>`).join('')}
                    </div>
                  ` : ''}
                </div>

                <div class="topic-checks">
                  <button type="button" class="topic-check-btn ${checks.teoria ? 'checked-teoria' : ''}" onclick="toggleTopicCheck('${topic.id}', 'teoria')">
                    <i class="fas ${checks.teoria ? 'fa-check-circle' : 'fa-circle'}"></i> Teoria
                  </button>
                  <button type="button" class="topic-check-btn ${checks.questoes ? 'checked-questoes' : ''}" onclick="toggleTopicCheck('${topic.id}', 'questoes')">
                    <i class="fas ${checks.questoes ? 'fa-check-circle' : 'fa-circle'}"></i> Questões
                  </button>
                  <button type="button" class="topic-check-btn ${checks.revisao ? 'checked-revisao' : ''}" onclick="toggleTopicCheck('${topic.id}', 'revisao')">
                    <i class="fas ${checks.revisao ? 'fa-check-circle' : 'fa-circle'}"></i> Revisão
                  </button>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>
    `;
  }).join('');

  updateEditalProgress();
}

function toggleDiscipline(discId) {
  const topicsDiv = document.getElementById(`topics_${discId}`);
  const chevron = document.getElementById(`chevron_${discId}`);
  if (!topicsDiv) return;

  if (topicsDiv.style.display === 'none') {
    topicsDiv.style.display = 'block';
    if (chevron) chevron.style.transform = 'rotate(0deg)';
  } else {
    topicsDiv.style.display = 'none';
    if (chevron) chevron.style.transform = 'rotate(-90deg)';
  }
}

function expandAllDisciplines() {
  const disciplines = EDITAL_PROGRAMATICO[currentEditalRole] || EDITAL_PROGRAMATICO.tecnico;
  disciplines.forEach(disc => {
    const topicsDiv = document.getElementById(`topics_${disc.id}`);
    const chevron = document.getElementById(`chevron_${disc.id}`);
    if (topicsDiv) topicsDiv.style.display = 'block';
    if (chevron) chevron.style.transform = 'rotate(0deg)';
  });
}

function collapseAllDisciplines() {
  const disciplines = EDITAL_PROGRAMATICO[currentEditalRole] || EDITAL_PROGRAMATICO.tecnico;
  disciplines.forEach(disc => {
    const topicsDiv = document.getElementById(`topics_${disc.id}`);
    const chevron = document.getElementById(`chevron_${disc.id}`);
    if (topicsDiv) topicsDiv.style.display = 'none';
    if (chevron) chevron.style.transform = 'rotate(-90deg)';
  });
}

function toggleTopicCheck(topicId, type) {
  if (!appState.editalChecks) appState.editalChecks = {};
  if (!appState.editalChecks[topicId]) {
    appState.editalChecks[topicId] = { teoria: false, questoes: false, revisao: false };
  }

  appState.editalChecks[topicId][type] = !appState.editalChecks[topicId][type];
  saveState();
  renderEditalProgramatico();
}

function updateEditalProgress() {
  const disciplines = EDITAL_PROGRAMATICO[currentEditalRole] || EDITAL_PROGRAMATICO.tecnico;
  let totalTopics = 0;
  let completedTopics = 0;

  disciplines.forEach(disc => {
    disc.topicos.forEach(topic => {
      totalTopics++;
      const checks = appState.editalChecks[topic.id];
      // Tópico é considerado concluído/dominado se tiver Teoria OU Questões assinaladas
      if (checks && (checks.teoria || checks.questoes)) {
        completedTopics++;
      }
    });
  });

  const pct = totalTopics > 0 ? Math.round((completedTopics / totalTopics) * 100) : 0;
  
  const countEl = document.getElementById('editalProgressCount');
  const pctEl = document.getElementById('editalProgressPercent');
  const barEl = document.getElementById('editalProgressBar');

  if (countEl) countEl.innerText = `${completedTopics} de ${totalTopics} tópicos dominados`;
  if (pctEl) pctEl.innerText = `${pct}%`;
  if (barEl) barEl.style.width = `${pct}%`;
}

function filterEditalTopics() {
  const input = document.getElementById('editalSearchInput');
  if (!input) return;
  const q = input.value.toLowerCase().trim();

  const items = document.querySelectorAll('.topic-item');
  items.forEach(item => {
    const searchData = item.getAttribute('data-search') || '';
    if (!q || searchData.includes(q)) {
      item.style.display = 'flex';
    } else {
      item.style.display = 'none';
    }
  });

  // Também oculta cartões de disciplinas que não têm tópicos visíveis
  const disciplines = EDITAL_PROGRAMATICO[currentEditalRole] || EDITAL_PROGRAMATICO.tecnico;
  disciplines.forEach(disc => {
    const card = document.getElementById(`disc_card_${disc.id}`);
    const topicsDiv = document.getElementById(`topics_${disc.id}`);
    if (!card || !topicsDiv) return;

    if (!q) {
      card.style.display = 'block';
    } else {
      const visibleItems = topicsDiv.querySelectorAll('.topic-item:not([style*="display: none"])');
      card.style.display = visibleItems.length > 0 ? 'block' : 'none';
      if (visibleItems.length > 0) {
        topicsDiv.style.display = 'block';
      }
    }
  });
}

// =========================================
// FILTRO E BUSCA DA ABA MACETES DE PORTUGUÊS
// =========================================
let currentMacetesFilter = 'all';

function filterMacetes(type) {
  currentMacetesFilter = type;
  const btnOuro = document.getElementById('btnFilterOuro');
  const btnAll = document.getElementById('btnFilterAll');
  if (btnOuro && btnAll) {
    btnOuro.classList.toggle('active', type === 'ouro');
    btnAll.classList.toggle('active', type === 'all');
  }

  const cards = document.querySelectorAll('#tab-macetes .summary-cards-grid .summary-card');
  const searchInput = document.getElementById('macetesSearchInput');
  const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

  cards.forEach(card => {
    const isOuro = card.classList.contains('ouro-card');
    const text = card.textContent.toLowerCase();

    let matchFilter = (type === 'all') || (type === 'ouro' && isOuro);
    let matchSearch = !query || text.includes(query);

    card.style.display = (matchFilter && matchSearch) ? 'flex' : 'none';
  });
}

function searchMacetes(val) {
  const query = (val || '').toLowerCase().trim();
  const cards = document.querySelectorAll('#tab-macetes .summary-cards-grid .summary-card');

  cards.forEach(card => {
    const isOuro = card.classList.contains('ouro-card');
    const text = card.textContent.toLowerCase();

    let matchFilter = (currentMacetesFilter === 'all') || (currentMacetesFilter === 'ouro' && isOuro);
    let matchSearch = !query || text.includes(query);

    card.style.display = (matchFilter && matchSearch) ? 'flex' : 'none';
  });
}


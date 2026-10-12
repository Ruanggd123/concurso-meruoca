import json

QUESTOES_S4_D2 = [
  # =========================================================================
  # REGIMENTO INTERNO — COMISSOES, PROPOSICOES E PLENARIO (ANGULOS NOVOS)
  # QUESTOES 595 A 604 (10 QUESTOES)
  # =========================================================================
  {
    "id": 595,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Moções Parlamentares",
    "question": "As moções são proposições por meio das quais a Câmara se manifesta sobre fatos ou pessoas. É CORRETO afirmar que as moções podem expressar:",
    "options": [
      "Congratulação, apelo, repúdio ou pesar, conforme o sentimento do Plenário sobre o fato.",
      "Aprovação de leis ordinárias sem necessidade de sanção do Prefeito.",
      "Nomeação de servidores para cargos em comissão da Câmara.",
      "Julgamento definitivo de crimes praticados por autoridades municipais."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Moção = manifestação (congratula, apela, repudia, lamenta). Não aprova lei, não nomeia servidor, não julga crimes."
  },
  {
    "id": 596,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Espécies: Lei, Resolução e Decreto Legislativo",
    "question": "No âmbito municipal, distinguem-se projeto de lei, projeto de resolução e projeto de decreto legislativo porque:",
    "options": [
      "Os três têm o mesmo objeto e diferem apenas no nome da capa.",
      "O projeto de lei vai à sanção; a resolução regula a Câmara; o decreto trata de matéria exclusiva do Plenário.",
      "A resolução depende de sanção do Prefeito e o decreto legislativo depende do Governador.",
      "O projeto de lei é votado em turno único secreto e os demais em aclamação."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Lei = norma geral (vai à sanção); resolução = matéria interna/administrativa da Câmara (promulgada pelo Presidente); decreto legislativo = competência exclusiva do Plenário com efeito externo (contas, títulos, sustação)."
  },
  {
    "id": 597,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Parecer Contrário e Arquivamento",
    "question": "Quando a Comissão de Constituição e Justiça emite parecer pela inconstitucionalidade de um projeto, a consequência regimental típica é que:",
    "options": [
      "O projeto é automaticamente promulgado como lei.",
      "O parecer é ignorado e a tramitação segue inalterada em qualquer caso.",
      "O projeto pode ser arquivado, salvo recurso de parte dos vereadores para o Plenário decidir.",
      "O Prefeito fica obrigado a sancionar o projeto imediatamente."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Parecer terminativo pela inconstitucionalidade leva ao arquivamento, com recurso ao Plenário (em regra, 1/10 dos membros). CCJ não promulga nem obriga sanção."
  },
  {
    "id": 598,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Votação por Destaque",
    "question": "A votação por destaque, admitida nos regimentos, consiste em:",
    "options": [
      "Votar separadamente parte da proposição ou emenda, a requerimento aprovado, sem prejuízo do restante do texto.",
      "Votar todas as matérias do ano em uma única sessão de dezembro.",
      "Impedir qualquer vereador de votar nas matérias orçamentárias.",
      "Substituir a votação pela decisão individual do Presidente."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Destaque = fatiar a votação (trecho/emenda) mediante requerimento. Não concentra o ano, não exclui votantes, não transfere ao Presidente."
  },
  {
    "id": 599,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Questão de Ordem",
    "question": "A questão de ordem é o instrumento pelo qual o vereador suscita dúvida sobre a aplicação do Regimento durante os trabalhos. Sobre ela, é CORRETO afirmar que:",
    "options": [
      "É decidida de imediato pelo Presidente, cabendo recurso ao Plenário contra a decisão.",
      "Só pode ser formulada pelo Prefeito, nunca por vereadores.",
      "Suspende todos os mandatos até julgamento pelo Tribunal de Contas.",
      "Serve para discutir o mérito de projetos ainda não apresentados."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Questão de ordem = dúvida regimental decidida na hora pelo Presidente, com recurso ao Plenário. É prerrogativa de vereador, não suspende mandatos nem discute mérito futuro."
  },
  {
    "id": 600,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Audiências Públicas das Comissões",
    "question": "As comissões da Câmara podem realizar audiências públicas com entidades da sociedade civil. Essa atribuição tem por finalidade:",
    "options": [
      "Julgar processos criminais contra cidadãos do Município.",
      "Instruir matéria em tramitação, colhendo subsídios e opiniões sobre o tema.",
      "Arrecadar tributos municipais diretamente dos contribuintes.",
      "Nomear os membros da Mesa Diretora para a legislatura seguinte."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Audiência pública = instrução democrática da matéria (CF, Art. 58, § 2º, II, por simetria). Comissões não julgam crimes, não arrecadam, não elegem Mesa."
  },
  {
    "id": 601,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Líderes e Blocos Parlamentares",
    "question": "Os líderes partidários e de blocos parlamentares exercem, entre outras funções regimentais:",
    "options": [
      "Executar o orçamento da Câmara sem prestar contas.",
      "Vetar projetos de lei aprovados pelo Plenário.",
      "Indicar os membros das comissões pelas respectivas bancadas e orientar a votação.",
      "Presidir todas as sessões no lugar do Presidente eleito."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Líder indica comissão, orienta bancada, fala pela liderança e pede verificações. Executar orçamento, vetar e presidir no lugar do eleito extrapolam a função."
  },
  {
    "id": 602,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Discussão Global e Parcelada",
    "question": "A discussão das proposições em Plenário pode ser global ou parcelada. Assinale a alternativa CORRETA:",
    "options": [
      "A discussão parcelada divide o texto em partes a requerimento, votando-se cada uma separadamente.",
      "A discussão global é proibida em qualquer hipótese nos regimentos.",
      "A discussão parcelada dispensa a votação posterior de cada parte.",
      "Toda discussão exige quórum de dois terços para ser iniciada."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Parcelada = fatiar discussão/votação por requerimento; global = texto inteiro de uma vez (regra). Quórum de 2/3 para iniciar discussão inexiste como regra."
  },
  {
    "id": 603,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Comissões de Representação",
    "question": "As comissões de representação da Câmara Municipal destinam-se a:",
    "options": [
      "Representar a Câmara em atos externos e solenidades, sendo temporárias e designadas pelo Presidente.",
      "Julgar as contas anuais do Prefeito em substituição ao Plenário.",
      "Legislar sobre matéria tributária sem passar pelas comissões permanentes.",
      "Substituir a Mesa Diretora durante todo o mandato."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Representação = temporária, externa, designada (ex.: representar a Câmara em evento). Não julga contas, não legisla, não substitui a Mesa."
  },
  {
    "id": 604,
    "category": "legislacao",
    "day": "w4_d2",
    "discipline": "Regimento Interno",
    "topic": "Urgência na Tramitação",
    "question": "O regime de urgência na tramitação de proposições caracteriza-se por:",
    "options": [
      "Acelerar os prazos regimentais das comissões e do Plenário, sem suprimir o direito ao debate e às emendas.",
      "Eliminar todas as formalidades, inclusive a votação em Plenário.",
      "Permitir a aprovação por decisão individual de qualquer vereador.",
      "Dispensar a sanção do Prefeito nas leis aprovadas sob urgência."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Urgência encurta prazos, não elimina debate, emendas, votação nem sanção. Decisão individual e dispensa de sanção violam o processo legislativo."
  },

  # =========================================================================
  # RLM — ARGUMENTACAO, CATEGORICAS E NEGACOES (INEDITO NO BANCO)
  # QUESTOES 605 A 612 (8 QUESTOES)
  # =========================================================================
  {
    "id": 605,
    "category": "matematica",
    "day": "w4_d2",
    "discipline": "Matemática / RLM",
    "topic": "Silogismo Válido (Modus Ponens)",
    "question": "Considere as premissas: 'Se chove, a sessão é adiada' e 'Choveu'. A conclusão logicamente válida é:",
    "options": [
      "A sessão foi adiada.",
      "A sessão não foi adiada.",
      "Não choveu na cidade vizinha.",
      "A sessão será adiada amanhã."
    ],
    "correctAnswer": 0,
    "commentary": "Gabarito: A. Modus ponens: P → Q; P; logo Q. Afirmada a condição (choveu), segue-se o consequente (adiada). Negar ou projetar no tempo extrapola as premissas."
  },
  {
    "id": 606,
    "category": "matematica",
    "day": "w4_d2",
    "discipline": "Matemática / RLM",
    "topic": "Falácia da Afirmação do Consequente",
    "question": "Premissas: 'Se o projeto é aprovado, o Prefeito o sanciona' e 'O Prefeito sancionou o projeto'. Sobre a conclusão 'logo, o projeto foi aprovado', é CORRETO afirmar que:",
    "options": [
      "É válida, pois toda sanção pressupõe aprovação anterior.",
      "É inválida: afirmar o consequente não garante o antecedente (falácia formal).",
      "É válida, pois sanção e aprovação são proposições equivalentes.",
      "É inválida, pois o Prefeito jamais sanciona projetos."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Afirmar Q em P → Q nada conclui sobre P (o Prefeito poderia sancionar por outro fundamento na hipótese lógica). Validade formal independe do conteúdo ser plausível — aí está a pegadinha."
  },
  {
    "id": 607,
    "category": "matematica",
    "day": "w4_d2",
    "discipline": "Matemática / RLM",
    "topic": "Proposições Categóricas: Todo e Nenhum",
    "question": "Premissas: 'Todo vereador é eleitor' e 'Nenhum eleitor é estrangeiro'. A conclusão válida é:",
    "options": [
      "Algum vereador é estrangeiro.",
      "Todo estrangeiro é vereador.",
      "Nenhum vereador é estrangeiro.",
      "Algum eleitor não é vereador."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. Se todo V está em E, e nada de E está em S, então nada de V está em S. As demais invertem os termos ou criam relação inexistente entre eles."
  },
  {
    "id": 608,
    "category": "matematica",
    "day": "w4_d2",
    "discipline": "Matemática / RLM",
    "topic": "Proposições Categóricas: Algum",
    "question": "Premissas: 'Alguns vereadores são advogados' e 'Todos os advogados possuem OAB'. Conclui-se validamente que:",
    "options": [
      "Todos os vereadores são advogados.",
      "Nenhum vereador possui OAB.",
      "Todos os advogados são vereadores.",
      "Alguns vereadores possuem OAB."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. A parte dos vereadores que é advogada herda a propriedade do grupo (OAB). 'Alguns' não autoriza 'todos' em nenhum dos sentidos; inversões de sujeito e predicado são falácias."
  },
  {
    "id": 609,
    "category": "matematica",
    "day": "w4_d2",
    "discipline": "Matemática / RLM",
    "topic": "Equivalência: Contrapositiva",
    "question": "A proposição 'Se o projeto é aprovado, o Prefeito o sanciona' é logicamente equivalente a:",
    "options": [
      "Se o projeto é aprovado, o Prefeito não o sanciona.",
      "Se o Prefeito não sanciona o projeto, então ele não foi aprovado.",
      "Se o Prefeito sanciona o projeto, então ele foi aprovado.",
      "O projeto é aprovado se e somente se o Prefeito o sanciona."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. Contrapositiva: P → Q ≡ ~Q → ~P. Nega as duas partes e inverte a ordem. A recíproca (C) e a bicondicional (D) não são equivalentes; A nega só o consequente."
  },
  {
    "id": 610,
    "category": "matematica",
    "day": "w4_d2",
    "discipline": "Matemática / RLM",
    "topic": "De Morgan: Negação da Conjunção",
    "question": "A negação lógica de 'O edital foi publicado e o prazo foi aberto' é:",
    "options": [
      "O edital foi publicado ou o prazo foi aberto.",
      "O edital não foi publicado ou o prazo não foi aberto.",
      "O edital não foi publicado e o prazo não foi aberto.",
      "Se o edital foi publicado, então o prazo foi aberto."
    ],
    "correctAnswer": 1,
    "commentary": "Gabarito: B. De Morgan: ~(P ∧ Q) ≡ ~P ∨ ~Q — nega as duas partes e troca E por OU. Manter o E (C) ou trocar só uma parte são os erros clássicos."
  },
  {
    "id": 611,
    "category": "matematica",
    "day": "w4_d2",
    "discipline": "Matemática / RLM",
    "topic": "De Morgan: Negação da Disjunção",
    "question": "É falso que 'choveu ou fez frio'. Logo, é verdade que:",
    "options": [
      "Choveu e fez frio.",
      "Não choveu ou não fez frio.",
      "Não choveu e não fez frio.",
      "Se choveu, então fez frio."
    ],
    "correctAnswer": 2,
    "commentary": "Gabarito: C. De Morgan: ~(P ∨ Q) ≡ ~P ∧ ~Q. Negar o OU gera E com as duas partes negadas. 'É falso que' = negação da proposição inteira."
  },
  {
    "id": 612,
    "category": "matematica",
    "day": "w4_d2",
    "discipline": "Matemática / RLM",
    "topic": "Diagrama de Venn com Três Conjuntos",
    "question": "Dos 120 servidores da Câmara, 70 fizeram curso X, 60 fizeram Y e 50 fizeram Z. Fizeram X e Y 30; X e Z 25; Y e Z 20; os três cursos 10. Quantos não fizeram nenhum curso?",
    "options": [
      "15 servidores.",
      "10 servidores.",
      "5 servidores.",
      "Nenhum servidor."
    ],
    "correctAnswer": 3,
    "commentary": "Gabarito: D. Inclusão-exclusão: 70+60+50−30−25−20+10 = 115 fizeram ao menos um; 120−115 = 5. Some tudo, subtraia as duplas, some a tripla e tire do total."
  }
]

print(f"[OK] Total de questões S4/D2 geradas: {len(QUESTOES_S4_D2)}")
